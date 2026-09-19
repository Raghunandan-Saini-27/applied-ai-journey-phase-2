export function showMessage(message)					//Displays Messages
{
	results.innerHTML=`<p class=message>${message}<p>`;
}

export function createJobCard(job)						//Creates JobCard
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

export function renderJobs(jobs)						//Renders the job for displaying on webpage
{
	results.innerHTML = "";

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
		}
}

export function setButtonLoadingState(button,disabled,text)
{
	button.disabled=disabled;

	button.textContent=text;

}