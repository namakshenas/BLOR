from llama_cpp import Llama

llm = Llama(
    model_path="models/Qwen3-4B-Thinking-2507-Q4_K_M.gguf",
    n_gpu_layers=-1, # Use all GPU (Metal acceleration)
    n_ctx=65536,
    n_batch=512,
    verbose=False
)