import {API_BASE_URL,SMART_SEARCH_ENDPOINT} from "./config.js";

export async function fetchJobs(query)					//Fetches job from the backend
{
	const url=`${API_BASE_URL}${SMART_SEARCH_ENDPOINT}?query=${query}`;
	
	const response=await fetch(url);

	if(!response.ok)
		{
			throw new Error(`HTTP ${response.status}`);
		}

	const jobs=await response.json();	

	return jobs;
}