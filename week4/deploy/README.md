# Mistral-7B Technical Documentation Model Deployment

This repository contains the deployment code for a fine-tuned Mistral-7B model specialized in technical documentation generation. The deployment utilizes vLLM for efficient inference and FastAPI for serving.

## System Architecture

### Components
1. **Base Model**: mistralai/mistral-7b-v0.1
2. **Fine-tuned Adapter**: goaiguru/mistral-technical-docs (LoRA weights)
3. **Serving Infrastructure**: 
   - vLLM for optimized inference
   - FastAPI for HTTP endpoints
   - Uvicorn as ASGI server

### Key Technologies

#### vLLM
vLLM (Very Light Large Language Model) is an open-source library for LLM inference that offers:
- PagedAttention for efficient memory management
- Continuous batching for higher throughput
- Optimized CUDA kernels for faster inference
- Dynamic memory allocation
- Supports various model architectures including Mistral

#### FastAPI
FastAPI is a modern web framework that provides:
- High performance (built on Starlette)
- Automatic API documentation (Swagger/OpenAPI)
- Type checking and validation
- Async support
- Easy deployment and scaling

## Setup Instructions

### Prerequisites
- Python 3.10+
- CUDA-compatible GPU with at least 16GB VRAM
- 32GB+ system RAM recommended

### Installation

1. Create and activate virtual environment:
```bash
python -m venv vllm-env
source vllm-env/bin/activate  # On Windows: vllm-env\Scripts\activate
```

2. Install dependencies:
```bash
pip install vllm fastapi uvicorn torch transformers peft
```

3. Clone repository and navigate to directory:
```bash
git clone <repository-url>
cd <repository-directory>
```

### Deployment

1. Start the server:
```bash
python server.py
```

The server will:
- Load the base Mistral model
- Load and merge LoRA weights
- Initialize vLLM engine
- Start FastAPI server on port 8000

## API Usage

### Generate Endpoint

**Endpoint**: `/generate`
**Method**: POST
**Content-Type**: application/json

Request body:
```json
{
    "prompts": [
        "Write technical documentation for a Python function that implements merge sort."
    ]
}
```

Example curl command:
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["Write technical documentation for a Python function that implements merge sort."]}'
```

Response format:
```json
{
    "responses": [
        {
            "generated_text": "...",
            "num_tokens": 256
        }
    ]
}
```

## Performance Optimization

### vLLM Configuration
The deployment uses these optimized settings:
```python
llm = LLM(
    model=merged_model_path,
    tensor_parallel_size=1,  # Adjust based on GPU count
    gpu_memory_utilization=0.90,
    max_num_batched_tokens=32768,
    max_model_len=32768,
    trust_remote_code=True
)
```

Key parameters:
- `tensor_parallel_size`: Number of GPUs for tensor parallelism
- `gpu_memory_utilization`: GPU memory usage threshold
- `max_num_batched_tokens`: Maximum tokens in a batch
- `max_model_len`: Maximum sequence length

### Generation Parameters
```python
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=256
)
```

## Troubleshooting

Common issues and solutions:

1. **Out of Memory (OOM)**
   - Reduce `max_num_batched_tokens`
   - Lower `gpu_memory_utilization`
   - Decrease batch size in requests

2. **Slow First Request**
   - Normal behavior due to model loading and merging
   - Subsequent requests will be faster

3. **CUDA Issues**
   - Ensure CUDA toolkit matches PyTorch version
   - Verify GPU drivers are up to date

## Monitoring and Maintenance

### Logs
The server provides detailed logs for:
- Model loading progress
- Merge operations
- Request processing
- Error messages

### Performance Metrics
Monitor:
- GPU memory usage (nvidia-smi)
- Request latency
- Throughput
- Token generation speed

## Security Considerations

1. **API Security**
   - Add authentication if needed
   - Implement rate limiting
   - Set up CORS policies

2. **Model Security**
   - Validate input lengths
   - Implement prompt filtering if needed
   - Monitor for abuse patterns

## Future Improvements

Potential enhancements:
1. Add authentication
2. Implement request queueing
3. Add health checks
4. Set up monitoring dashboards
5. Add request logging
6. Implement caching for common prompts
7. Add model result validation
8. Set up load balancing for multiple GPUs

## License
MIT

## Contributing
Please send PR for any issue
