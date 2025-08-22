from model_conf import llm
import gc
from queries.sample_2.assistant import assistant_query
from queries.sample_2.user import user_query

QUERY = [
    {"role": "system", "content": assistant_query},
    {"role": "user", "content": user_query},
]

response = llm.create_chat_completion(
    messages=QUERY,
    max_tokens=32768, 
    repeat_penalty=1.1,
    stream=True,
    temperature=0.2,
    top_p=0.95, 
    top_k=40, 
    min_p=0.05,
    frequency_penalty=0.0,
    presence_penalty=0.0,
)

for chunk in response:
    if "choices" in chunk and len(chunk["choices"]) > 0:
        delta = chunk["choices"][0].get("delta", {})
        if "content" in delta:
            print(delta["content"], end="", flush=True)

print()

# Cleanup
del llm
gc.collect()
