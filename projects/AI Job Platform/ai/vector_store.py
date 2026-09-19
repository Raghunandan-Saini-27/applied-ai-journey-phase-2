import faiss
import os
import json

INDEX_PATH="ai/job_index.faiss"
IDS_PATH = "ai/job_ids.json"

def save_index(index,job_ids):
	faiss.write_index(index,INDEX_PATH)

	with open(IDS_PATH,"w") as file:
		json.dump(job_ids,file)

def load_index():
	if not os.path.exists(INDEX_PATH):
		return None,None

	index = faiss.read_index(INDEX_PATH)

	with open(IDS_PATH,"r") as file:
		job_ids=json.load(file)

	return index,job_ids