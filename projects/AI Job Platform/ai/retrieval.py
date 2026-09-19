from database.db import get_all_jobs
from ai.embeddings import embed_query
from ai.chroma_store import get_collection

def retrieve_jobs(query,top_k=20):
	collection=get_collection()
	query_embedding=embed_query(query)
	results=collection.query(query_embeddings=query_embedding.tolist(),n_results=top_k)

	jobs=get_all_jobs()
	jobs_by_id={job["id"]:job for job in jobs}
	final_results=[]

	for job_id,distance in zip(results["ids"][0],results["distances"][0]):
		job=jobs_by_id.get(int(job_id))
		if job is None:
			continue

		final_results.append({"job":job,"score":float(distance)})

	return final_results