from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from model_conf import llm
import gc
from benchmarks.b04.assistant import assistant_query
from benchmarks.b04.user import user_query

print(f"LLM imported: {llm}")  # Debug line

app = FastAPI()

QUERY = [
    {"role": "assistant", "content": assistant_query},
    {"role": "user", "content": user_query},
]

def generate_stream():
    try:
        response = llm.create_chat_completion(
            messages=QUERY,
            max_tokens=1024*16,
            repeat_penalty=1.2,
            stream=True,
            temperature=0.2,
            top_p=0.95,
            top_k=40,
            min_p=0.05,  
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["<|im_end|>", "</thinking>", "<|endofthinking|>", "\n\nHuman:", "\n\nAssistant:"]
        )

        for chunk in response:
            try:
                if "choices" in chunk and len(chunk["choices"]) > 0:
                    choice = chunk["choices"][0]
                    delta = choice.get("delta", {})
                        
                    if "content" in delta:
                        print(delta["content"], end="", flush=True)
                        yield delta["content"]
                        
            except Exception as chunk_error:
                yield f"\nError processing chunk: {chunk_error}"
                break

    except Exception as e:
        yield f"\nError during completion: {e}"

    finally:
        try:
            if response and hasattr(response, 'close'):
                response.close()
                
            collected = gc.collect(generation=2)
            
        except Exception as cleanup_error:
            yield f"Cleanup error: {cleanup_error}"

@app.get("/streamllm")
async def stream_response():
    return StreamingResponse(generate_stream(), media_type="text/plain")