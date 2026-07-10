import requests 
import time
from bs4 import BeautifulSoup
from database.db import create_jobs_table, insert_job
from api.services import refresh_vectors


url="https://realpython.github.io/fake-jobs/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

items=soup.find(id="ResultsContainer")
job_cards=items.find_all("div",class_="card")

create_jobs_table()
job_list=[]
for in_job in job_cards:
	title=in_job.find("h2",class_="title").text.strip()
	company=in_job.find("h3",class_="company").text.strip()
	location=in_job.find("p",class_="location").text.strip()
	link=in_job.find("a",string="Apply",class_="card-footer-item")["href"]

	response2=requests.get(link)
	time.sleep(0.5)
	soup2=BeautifulSoup(response2.text,"html.parser")
	content_container=soup2.find("div",class_="content")
	description_tag=content_container.find("p",id=False)
	description=description_tag.text.strip()

	job_list.append({"title":title,
			 "company":company,
			 "location":location,
			 "link":link,
			 "description":description})
	
print(job_list)
insert_job(job_list)

refresh_vectors()
