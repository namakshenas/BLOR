# Battle-testing LLM models on scientific local-reasoning [llama.cpp]

## Installation

### Standard Installation

For most systems, install the Python bindings for llama.cpp:

```bash
pip install llama-cpp-python
```

### Apple Silicon Installation

If you're using a Mac with Apple Silicon (M1/M2/M3 chips), install with Metal support for GPU acceleration:

```bash
pip install 'llama-cpp-python[metal]'
```

> **Note:** The Metal backend provides significant performance improvements on Apple Silicon by utilizing the GPU.

## Model Setup

### Download a Model

Models for llama.cpp use the `.gguf` format. You can download them from Hugging Face. First, create a models directory:

```bash
mkdir models
cd models
```

Then download your desired model. For example, to download the Qwen3-4B model:

```bash
wget https://huggingface.co/unsloth/Qwen3-4B-Thinking-2507-GGUF/resolve/main/Qwen3-4B-Thinking-2507-Q4_K_M.gguf
```

> **Model Notes:**
> - `.gguf` files are quantized models that balance performance and quality
> - `Q4_K_M` indicates 4-bit quantization with medium quality
> - Smaller quantized models use less RAM but may have slightly reduced quality

## Testing with FastAPI

### Install FastAPI

To test your setup with a web API, install FastAPI with all standard dependencies:

```bash
pip install fastapi[standard]
```

### Run the Server

Start the FastAPI development server with your llama.cpp application:

```bash
fastapi dev llama_cpp_fastapi.py
```

> **Note:** Make sure you have a file named `llama_cpp_fastapi.py` that sets up the FastAPI endpoints for your llama.cpp model.

### Test the API

Once the server is running, you can test the streaming endpoint:

```bash
curl -N http://127.0.0.1:8000/streamllm
```

The `-N` flag disables buffering, which is important for streaming responses.

## Next Steps

- Experiment with different model sizes and quantization levels
- Explore the llama.cpp documentation for advanced configuration options
- Consider setting up proper logging and error handling for production use
- Look into model-specific chat templates and prompt formats

## Troubleshooting

- **Installation Issues:** If you encounter compilation errors, ensure you have the necessary build tools installed
- **Memory Issues:** Larger models require more RAM. Consider using more heavily quantized versions if you run out of memory
- **Performance:** Monitor CPU/GPU usage and adjust thread counts as needed for optimal performance