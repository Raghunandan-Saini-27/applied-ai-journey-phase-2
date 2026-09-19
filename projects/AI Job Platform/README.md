# 💼 AI Job Intelligence Platform

## 🚀 Overview

This project simulates a real-world data pipeline:

* Scraping → Database → API → Client

* AI-powered backend system that collects, stores, and serves job listings through APIs.

* Now includes a rule-based recommendation engine for ranking job listings.

🔥 Feature: Semantic Job Search

* The platform now supports machine learning–based job ranking using TF-IDF and cosine similarity.

🔥 Improvements

* Text normalization using regex cleaning

* Stopwords removal for better relevance

* Vocabulary control using max_features

* Noise reduction using min_df

* Consistent preprocessing across all ranking systems

* Dynamic Vector Updates

🔥 Feature

* Added ability to refresh vector representations when job data changes

* Introduced system-level update mechanism for ML pipeline

* Filtering + Ranking

* Features:

* Location-based filtering

* Hybrid keyword ranking

* Combined structured + semantic search


## 🧠 Result

* More accurate job matching

* Cleaner and faster vector processing

* Improved semantic search quality


---

## ⚙️ Features

### 🔍 Job Data Collection

* Web scraping using `requests` + `BeautifulSoup`
* Multi-page scraping support
* Clean extraction of:

  * Title
  * Company
  * Location
  * Link

### 🗄️ Database

* SQLite database
* Structured schema
* Duplicate prevention using `UNIQUE` constraint

### ⚡ API (FastAPI)

* `GET /jobs` → Paginated job listings
* `GET /jobs/search?keyword=` → Search by job title
* `GET /jobs/location?location=` → Filter by location

### 📄 Pagination

* Efficient data loading using:

  * `limit`
  * `offset`

---

## 🧠 Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy (basic usage)
* BeautifulSoup (scraping)
* Docker (planned)

---

## 📂 Project Structure

```
project/
│── api/
│── database/
│── scraper/
│── main.py
│── database.db
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run API

```
uvicorn main:app --reload
```

### 3. Access API

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Future Improvements

* Add filtering (salary, role)
* Add caching (Redis)
* Deploy on cloud (Render / AWS)
* Add AI features (job recommendations, RAG)

---

## 📌 Learning Goals

* Backend engineering fundamentals
* API design
* Data pipeline building
* Real-world system thinking

---
