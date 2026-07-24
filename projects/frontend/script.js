console.log("Javascript Connected Successfully!");

const button = document.getElementById("search-btn");

const searchBox = document.getElementById("search-box");

const results=document.getElementById("results");

button.addEventListener("click",function()
{
	console.log(searchBox.value);
	searchJobs();
});

searchBox.addEventListener("keydown",function(event)
{
	if(event.key==="Enter")
	{
		event.preventDefault();
		searchJobs();
	}
});

async function searchJobs() 
{
	const query=searchBox.value;

	const url=`http://127.0.0.1:8000/jobs/smart-search?query=${query}`;

	showMessage("Searching...");
	
	const response=await fetch(url);

	const jobs= await response.json()

	showMessage("")

	if(jobs.length===0)
	{
		showMessage("No Results found! Try another keyword.")
	}

	else{
	
	for (const job of jobs)
	{
		const jobCard=createJobCard(job);

		results.appendChild(jobCard);
	}

	console.log(jobs)
	
	console.log(results)
}
}

function showMessage(message)
{
	results.innerHTML=`<p class=message>${message}<p>`;
}

function createJobCard(job)
{
	const card=document.createElement("div");

	card.className="job-card";

	const subcard=document.createElement("div");

	subcard.className="job-header";

	const job_title=document.createElement("h3");

	const apply_button=document.createElement("button");

	apply_button.addEventListener("click",function()
		{
			window.open(job.link, "_blank")
		}
	)

	const job_company=document.createElement("p");

	const job_location=document.createElement("p");

	const job_description=document.createElement("p");

	job_title.textContent=job.title;

	apply_button.textContent="Apply";

	job_company.textContent=job.company;

	job_location.textContent=job.location;

	job_description.textContent=job.description;

	subcard.appendChild(job_title);

	subcard.appendChild(apply_button);

	card.appendChild(subcard);

	card.appendChild(job_company);

	card.appendChild(job_location);

	card.appendChild(job_description);

	return card;
}