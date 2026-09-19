def precision_at_k(retrieved_ids,relevant_ids,k=5):
	retrieved_ids=retrieved_ids[:k]

	relevant_retrieved=0

	for job_id in retrieved_ids:
		if job_id in relevant_ids:
			relevant_retrieved+=1

	return relevant_retrieved/k

def recall_at_k(retrieved_ids,relevant_ids,k):
	retrieved_ids=retrieved_ids[:k]

	relevant_retrieved=0

	for job_id in retrieved_ids:
		if job_id in relevant_ids:
			relevant_retrieved+=1
			
	return relevant_retrieved/len(relevant_ids)