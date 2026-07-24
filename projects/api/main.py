from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.services import smart_search,get_ranked_jobs_by_location_and_keyword_hybrid_score,initialize_vectors,refresh_vectors

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    initialize_vectors()

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.get("/jobs/search")
def jobs_search(keyword: str,location: str):
    return {"jobs":get_ranked_jobs_by_location_and_keyword_hybrid_score(keyword,location)}

@app.post("/jobs/refresh")
def refresh():
     refresh_vectors()
     return {"message":"Vectors refreshed successfully."}

@app.get("/jobs/smart-search")
def jobs_by_query(query:str):
     return smart_search(query)