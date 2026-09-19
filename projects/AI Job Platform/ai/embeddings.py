from sentence_transformers import SentenceTransformer
from database.db import get_all_jobs

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def get_data():
    jobs=get_all_jobs()
    jobs_text=[
        build_job_text(job)
        for job in jobs
    ]
    return jobs,jobs_text

def build_job_text(job):
    text=f"""Title: {job['title']}
    Company: {job['company']} 
    Location: {job['location']} 
    Job: {job['description']}"""
    
    return text

def embed_query(query):
	return model.encode([query],normalize_embeddings=True)


def embed_documents(documents):
    return model.encode(
        documents,
        normalize_embeddings=True
    )
