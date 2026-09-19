from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_jobs(query, retrieved_jobs):

    keywords = query.lower().split()

    reranked = []

    keyword_score = 0
    title_score = 0

    for result in retrieved_jobs:

        job = result["job"]
        title = job["title"].lower()
        description = job["description"].lower()
        
        retrieval_score = result["score"]

        for word in keywords:
            if word in title and word in description:
               print(job["title"])
               keyword_score+=0.25

            if word in job["title"]:
                title_score+=0.75

        final_score=keyword_score+title_score+retrieval_score

        reranked.append({
            "job": job,
            "retrieval_score": retrieval_score,
            "keyword_score": keyword_score,
            "title_score": title_score,
            "final_score": final_score
        })

    reranked.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return reranked

def rerank(query, candidates, top_k=5):

    pairs = []

    for candidate in candidates:

        job = candidate["job"]

        job_text = f"""
        Title: {job["title"]}
        Company: {job["company"]}
        Location: {job["location"]}
        Description: {job["description"]}
        """

        pairs.append(
            (query, job_text)
        )

    scores = model.predict(pairs)

    reranked = []

    for candidate, score in zip(candidates, scores):

        candidate_copy = candidate.copy()

        candidate_copy["rerank_score"] = float(score)

        reranked.append(candidate_copy)

    reranked.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked[:top_k]
