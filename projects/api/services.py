from database.db import get_all_jobs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

vectorizer=None
job_vectors=None
job_cache=None


def clean_text(text):
    text=text.strip().lower()
    text=re.sub(r"[^a-zA-Z0-9 ]", "",text)
    text = re.sub(r"\s+", " ", text)
    return text


def score_job(job,keywords):
    title = clean_text(job["title"])
    company = clean_text(job["company"])
    location = clean_text(job["location"])
    rule_score = 0
    for word in keywords:
        if word in title:
            rule_score += 2

        if word in company:
            rule_score += 1
        
        if word in location:
            rule_score +=1

    return rule_score

def initialize_vectors():
    jobs=get_all_jobs()
    jobs_text=[]
    for job in jobs:
        raw_text=f"{job['title']} {job['company']} {job['location']} {job['description']}"
        cleaned_text=clean_text(raw_text)
        jobs_text.append(cleaned_text)

    MAX_FEATURES=500
    global vectorizer,job_vectors,job_cache
    vectorizer=TfidfVectorizer(stop_words="english",max_features=MAX_FEATURES,min_df=1,max_df=3)
    vectorizer.fit(jobs_text)

    job_vectors=vectorizer.transform(jobs_text)
    job_cache=jobs

def refresh_vectors():
    initialize_vectors()

def get_jobs_by_location(location: str):
    global job_cache
    job_copy=[job.copy() for job in job_cache]
    location=clean_text(location)
    result=[]

    if not location:
        return result
    
    for job in job_copy:
            if location in clean_text(job["location"]):
                result.append(job)

    return result[:10]

def get_ranked_jobs_by_keyword(keyword: str):
    global job_cache
    job_copy=[job.copy() for job in job_cache]
    keyword=clean_text(keyword).split()
    result = []
    
    if not keyword:
        return result
        
    for job in job_copy:
        score = score_job(job, keyword)

        if score > 0:
            job["score"] = score
            result.append(job)

    result.sort(key=lambda x: x["score"], reverse=True)

    return result[:10]

def get_ranked_jobs_by_keyword_hybrid_score(keyword:str):
    global vectorizer, job_vectors, job_cache

    keyword=clean_text(keyword)
    keywords=keyword.split()
    if not keywords :
        return []
    
    if vectorizer is None or job_vectors is None:
        return []
    
    query_vec=vectorizer.transform([keyword])

    similarity=cosine_similarity(query_vec,job_vectors)

    result=[]
    for i,job in enumerate(job_cache):
        ml_score=similarity[0][i]
        rule_score=score_job(job,keywords)
        final_score=(0.5*rule_score)+ml_score
           
        if final_score>0:
            job_copy=job.copy()
            job_copy['score']=float(final_score)
            result.append(job_copy)

    result.sort(key=lambda x:x['score'],reverse=True)

    return result[:10]

def get_ranked_jobs_by_location_and_keyword_hybrid_score(keyword:str,location:str):
    global job_cache,job_vectors

    keyword=clean_text(keyword)
    keywords=keyword.split()

    location=clean_text(location)
    if not location:
        return job_cache[:10]

    if vectorizer is None or job_vectors is None:
        return []
    
    filtered_jobs=[]
    filtered_indices=[]
    for i,job in enumerate(job_cache):
        if location in clean_text(job["location"]) :
            filtered_jobs.append(job)
            filtered_indices.append(i)

    result=[]
    query_vec=vectorizer.transform([keyword])
    similarity=cosine_similarity(query_vec,job_vectors)

    for idx,job in zip(filtered_indices,filtered_jobs):
        ml_score=similarity[0][idx]
        rule_score=score_job(job,keywords)
        final_score=ml_score+(rule_score*0.5)

        if final_score>0:
            job_copy=job.copy()
            job_copy["score"]=float(final_score)
            result.append(job_copy)
    result.sort(key=lambda x: x["score"], reverse=True)

    return result[:10]

def parse_query(query:str):
    query=clean_text(query)
    KNOWN_LOCATIONS=["aa","ap","ae"]
    keywords=[]
    location=None

    words=query.split()
    for word in words:
        if word in KNOWN_LOCATIONS:
            location=word

        else:
            keywords.append(word)

    parsed_query={"keywords":keywords,
                  "location":location}

    return parsed_query

def smart_search(query:str):
    parsed=parse_query(query)
    keywords=parsed["keywords"]
    location=parsed["location"]
    keywords=" ".join(keywords)
    
    if location is not None :
        if keywords!="":
            result=get_ranked_jobs_by_location_and_keyword_hybrid_score(keywords,location)
            return result
        
        else :
            result=get_jobs_by_location(location)
            return result
            

    else :
        if keywords!="":
            result=get_ranked_jobs_by_keyword_hybrid_score(keywords)
            return result
        
        else :
            return {"error":"Please enter a valid query."}

