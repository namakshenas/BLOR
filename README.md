## Battle-testing LLM models on scientific local-reasoning [llama.cpp]

To install llama.cpp locally:

```python
pip install llama-cpp-python
```

To install llama.cpp in apple silicon:

```python
pip install 'llama-cpp-python[metal]'
```

Download your desired model from `huggingface` with `.gguf` format and add it to models dir. For example:

```bash
wget https://huggingface.co/unsloth/Qwen3-4B-Thinking-2507-GGUF/resolve/main/Qwen3-4B-Thinking-2507-Q4_K_M.gguf
```

To test with fastapi:
```bash
pip install fastapi[standard]
```

then:
```bash
fastapi dev llama_cpp_fastapi.py
```

```bash
curl -N http://127.0.0.1:8000/streamllm
```