from configs.config_arm64 import llm
import gc
from benchmarks.b01.assistant import assistant_query
from benchmarks.b01.user import user_query

QUERY = [
    {"role": "assistant", "content": assistant_query},
    {"role": "user", "content": user_query},
]

def stream_final_answer(response):
    """Generator that yields only the final answer content, skipping thinking."""
    thinking_ended = False
    buffer = ""
    
    for chunk in response:
        try:
            if "choices" in chunk and len(chunk["choices"]) > 0:
                choice = chunk["choices"][0]
                delta = choice.get("delta", {})
                    
                if "content" in delta:
                    content = delta["content"]
                    
                    if not thinking_ended:
                        buffer += content
                        # Check if thinking has ended
                        if "</think>" in buffer:
                            thinking_ended = True
                            # Yield only the content after </think>
                            remaining = buffer.split("</think>")[-1]
                            if remaining.strip():
                                yield remaining
                    else:
                        # We're past the thinking phase, yield immediately
                        yield content
                        
        except Exception as chunk_error:
            print(f"\nError processing chunk: {chunk_error}")
            break

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

    # Stream only the final answer content
    for content_chunk in stream_final_answer(response):
        print(content_chunk, end="", flush=True)

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