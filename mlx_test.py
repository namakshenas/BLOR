from mlx_lm import load, generate, sample_utils
from benchmarks.b04.assistant import assistant_query
from benchmarks.b04.user import user_query

QUERY = [
    {"role": "assistant", "content": assistant_query},
    {"role": "user", "content": user_query},
]

# model, tokenizer = load("mlx-community/VibeThinker-1.5B-mlx-4bit")
# model, tokenizer = load("mlx-community/Qwen3-30B-A3B-Instruct-2507-4bit")
# model, tokenizer = load("mlx-community/Qwen3-30B-A3B-Thinking-2507-4bit")
model, tokenizer = load("mlx-community/Qwen3-Next-80B-A3B-Thinking-8bit")

prompt = tokenizer.apply_chat_template(
    QUERY, add_generation_prompt=True
)

text = generate(
    model, 
    tokenizer, 
    prompt=prompt, 
    verbose=True,
    max_tokens=16*1024,
    sampler = sample_utils.make_sampler(temp=0.4, top_p=0.95),
    logits_processors = sample_utils.make_logits_processors(
        repetition_penalty=1.1
    )
)

# model saved here: # Check the cache directory
# ls -lh ~/.cache/huggingface/hub/

# # Or search for your specific model
# ls ~/.cache/huggingface/hub/ | grep VibeThinker

# or
# model, tokenizer = load("~/.cache/huggingface/hub/models--mlx-community--VibeThinker-1.5B-mlx-4bit/...")
