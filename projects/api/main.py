from fastapi import FastAPI
from database.db import get_all_jobs,search_jobs_by_location,search_jobs_by_title
from api.services import smart_search,get_ranked_jobs_by_keyword,get_ranked_jobs_by_location_and_keyword_hybrid_score,get_ranked_jobs_by_keyword_hybrid_score,initialize_vectors,refresh_vectors

app=FastAPI()

@app.on_event("startup")
def startup_event():
    initialize_vectors()

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.get("/jobs")
def jobs(page: int=1,limit: int=10):
	# Prevent negative pages
    if page < 1:
        page = 1
        
    offset = (page - 1) * limit
    
    # Only fetch what is needed
    job_titles = get_all_jobs(limit, offset)
    
    return {"jobs": job_titles}

@app.get("/jobs/search")
def jobs_search(keyword: str,location: str):
    return {"jobs":get_ranked_jobs_by_location_and_keyword_hybrid_score(keyword,location)}

@app.get("/jobs/location")
def jobs_search_by_location(location: str):
    return {"jobs": search_jobs_by_location(location)}

@app.get("/jobs/ranked")
def ranked_jobs(keyword : str):
    return get_ranked_jobs_by_keyword(keyword)

@app.get("/jobs/ranked-ml")
def ranked_ml_jobs(keyword:str):
     return get_ranked_jobs_by_keyword_hybrid_score(keyword)

@app.post("/jobs/refresh")
def refresh():
     refresh_vectors()
     return {"message":"Vectors refreshed successfully."}

@app.get("/jobs/smart-search")
def jobs_by_query(query:str):
     return smart_search(query)