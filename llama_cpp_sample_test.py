from model_conf import llm
import gc
from queries.bench_3.assistant import assistant_query
from queries.bench_3.user import user_query

QUERY = [
    {"role": "system", "content": assistant_query},
    {"role": "user", "content": user_query},
]

try:
    response = llm.create_chat_completion(
        messages=QUERY,
        max_tokens=1024*32,
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

    # Add timeout and explicit completion checking
    for chunk in response:
        try:
            if "choices" in chunk and len(chunk["choices"]) > 0:
                choice = chunk["choices"][0]
                delta = choice.get("delta", {})
                    
                if "content" in delta:
                    print(delta["content"], end="", flush=True)
                    
        except Exception as chunk_error:
            print(f"\nError processing chunk: {chunk_error}")
            break

except Exception as e:
    print(f"\nError during completion: {e}")

finally:
    print("\n")
    
    # Cleanup and memory management
    try:
        if 'response' in locals():
            # Close the stream if it has a close method
            if hasattr(response, 'close'):
                response.close()
        
        if 'llm' in locals():
            del llm
            
        collected = gc.collect(generation=2)
        print(f"Garbage collector: collected {collected} objects.")
        
    except Exception as cleanup_error:
        print(f"Cleanup error: {cleanup_error}")
    
    finally:
        gc.disable()