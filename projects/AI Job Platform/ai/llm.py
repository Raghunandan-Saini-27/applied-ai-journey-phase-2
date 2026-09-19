from ai.retrieval import retrieve_jobs
from ai.prompt import build_rag_prompt
from ai.context import build_job_context
from ai.reranker import rerank
import ollama
import time

def answer_question(query):
    start = time.perf_counter()

    results = retrieve_jobs(query, top_k=20)
    retrieval_time = time.perf_counter()

    reranked_results = rerank(
        query,
        results,
        top_k=5
    )
    rerank_time = time.perf_counter()

    context = build_job_context(reranked_results)
    prompt = build_rag_prompt(query, context)
    prompt_time = time.perf_counter()

    answer = generate_answer(prompt)
    llm_time = time.perf_counter()

    print("\n--- TIMING ---")
    print("Retrieval:", retrieval_time - start)
    print("Reranking:", rerank_time - retrieval_time)
    print("Prompt:", prompt_time - rerank_time)
    print("LLM:", llm_time - prompt_time)
    print("Total:", llm_time - start)

    return answer

def generate_answer(prompt):
    response = ollama.chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        think=False,
        options={
            "num_predict": 200
        }
    )

    print("\n--- OLLAMA METRICS ---")
    print("Prompt eval count:", response.get("prompt_eval_count"))
    print("Prompt eval duration:", response.get("prompt_eval_duration"))
    print("Eval count:", response.get("eval_count"))
    print("Eval duration:", response.get("eval_duration"))
    print("Total duration:", response.get("total_duration"))
    print("Load duration:", response.get("load_duration"))

    return response["message"]["content"]

questions=['1. Which jobs pay more than $100,000?',

'2. Which jobs mention Django?',

'3. Which Python backend jobs are available?'
]

for question in questions:
    print(f"\n{question}")
    print(answer_question(question))