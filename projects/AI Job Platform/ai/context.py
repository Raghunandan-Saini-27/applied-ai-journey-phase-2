def build_job_context(results):
    context_parts = []

    for result in results:
        job = result["job"]

        text = f"""
            Job ID: {job["id"]}
            Title: {job["title"]}
            Company: {job["company"]}
            Location: {job["location"]}
            Description: {job["description"]}
            """

        context_parts.append(text.strip())

    return "\n\n".join(context_parts)