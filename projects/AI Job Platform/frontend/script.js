import { fetchJobs } from "./api.js";
import { showMessage,createJobCard,renderJobs,setButtonLoadingState } from "./ui.js";

console.log("Javascript Connected Successfully!");

const searchButton = document.getElementById("search-btn");

const searchBox = document.getElementById("search-box");

const results=document.getElementById("results");

const DEFAULT_BUTTON_TEXT="Search";

const SEARCHING_BUTTON_TEXT = "Searching...";

let isSearching = false;


searchButton.addEventListener("click",function()
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

function cleanSearchQuery(search_value)					//Cleans the query
{
	search_value=search_value.trim().toLowerCase();

	return search_value;
}

async function searchJobs()								//Main Controller
{
	if(isSearching)
	{
		return ;
	}

	const rawQuery=searchBox.value;

	const cleanQuery=cleanSearchQuery(rawQuery);

	if(cleanQuery==="")
	{
		return showMessage("Please enter a valid query.")
	}

	isSearching = true;

	setButtonLoadingState(searchButton,true,SEARCHING_BUTTON_TEXT);

	showMessage("Searching...");
	
	try{
		const jobs=await fetchJobs(cleanQuery);

		renderJobs(jobs);
	}
	catch(error)
	{
		console.error(error)

		showMessage("Couldn't connect to the server.")
	}
	finally
	{
		isSearching = false;

		setButtonLoadingState(searchButton,false,DEFAULT_BUTTON_TEXT)
	}
}
