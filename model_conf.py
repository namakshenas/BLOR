from llama_cpp import Llama

llm = Llama(
    # model_path="models/Phi-4-reasoning-plus-Q4_K_M.gguf",
    # model_path="models/gemma-3-270m-it-Q4_K_M.gguf",
    model_path="models/Qwen3-4B-Thinking-2507-Q4_K_M.gguf",
    n_gpu_layers=-1, # -1 for Use all GPU (Metal acceleration)
    # n_ctx=131072,
    # n_ctx=65536,
    n_ctx=1024*32,
    n_batch=512,
    verbose=False,
    use_mmap=True,        # Memory-mapped files for efficiency
    use_mlock=False,      # Set True if you have enough RAM
    logits_all=False,     # Don't need all logits for chat
    f16_kv=True,
    n_threads=12,
    # chat_format="chatml",  # or try "phi-3", "openchat", or "auto" --- corresponds to the --jinja functionality in the CLI version
)