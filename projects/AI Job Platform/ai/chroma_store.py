import chromadb

from ai.embeddings import (
    get_data,
    embed_documents,
    embed_query
)

def get_collection():
    client = chromadb.PersistentClient(
        path="data/chroma"
    )

    return client.get_or_create_collection(
        name="jobs"
    )

def create_vector_database():
	collection=get_collection()

	jobs,jobs_text=get_data()

	embeddings=embed_documents(jobs_text)

	ids=[str(job["id"]) for job in jobs]

	collection.add(ids=ids,
	embeddings=embeddings.tolist(),
	documents=jobs_text,
	metadatas=[{"title":job["title"],
				"company":job["company"],
				"location":job["location"]}
				for job in jobs])

	return collection

def search_job_vdb(query, n_results=5):

    collection = get_collection()

    query_embedding = embed_query(query)

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_results
    )

    return results