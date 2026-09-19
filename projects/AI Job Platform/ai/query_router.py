from database.db import get_all_locations
from database.db import get_all_jobs

jobs = get_all_jobs()

def extract_location(query):
    query = query.lower()

    locations = get_all_locations()

    for location in locations:
        if location.lower() in query:
            return location

    return None

def understand_query(query):
    location = extract_location(query)
    semantic_query = extract_semantic_query(query,location)

    return {
        "location": location,
        "semantic_query": semantic_query
    }

def classify_query(query):
	query=query.lower()

	if "where" in query:
		return "structured"

	if "mention" in query:
		return "structured"

	if "similar" in query:
		return "semantic"

	if "best" in query:
		return "generative"

	if "recommend" in query:
		return "generative"

	return "semantic"

def extract_semantic_query(query, location):
    query = query.lower()

    if location:
        query = query.replace(location.lower(), "")

    removable_words = [
        "find",
        "show",
        "me",
        "jobs",
        "job",
        "which",
        "are",
        "is",
        "located",
        "in"
    ]

    words = query.split()

    words = [
        word
        for word in words
        if word not in removable_words
    ]

    return " ".join(words).strip(" .,?!")

queries = [
    "Which jobs are in Adamburgh, AA?",
    "Find jobs in Alberttown, AE.",
    "Show me jobs in Amyborough, AA.",
    "Find Python backend jobs in Adamburgh, AA.",
    "Find Python backend jobs."
]

for query in queries:
    result = understand_query(query)

    print("\nQuery:", query)
    print("Location:", result["location"])
    print("Semantic Query:", result["semantic_query"])