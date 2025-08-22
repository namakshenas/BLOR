from model_conf import llm
import gc
from queries.assistant import assistant_query
from queries.user import user_query

QUERY = [
    {"role": "system", "content": assistant_query},
    {"role": "user", "content": user_query},
]

response = llm.create_chat_completion(
    messages=QUERY,
    max_tokens=32768,
    temperature=0.3,
    top_p=0.8,   
    repeat_penalty=1.1,
    stream=True,
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
