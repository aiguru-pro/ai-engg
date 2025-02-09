# AI Engineering Tools & Technologies Reference Guide

## 1. Large Language Models (LLMs)

### Foundation Models

#### OpenAI Models
- **GPT-4o**
  - Best for: Enterprise-grade applications requiring high reliability
  - Key features: Strong reasoning, consistent outputs
  - Cost: Higher pricing tier

- **OpenAI o3-mini (Released Jan 2025)**
  - Best for: Cost-effective STEM and reasoning tasks
  - Key features: 
    - Function calling, structured outputs
    - Three reasoning effort levels (low, medium, high)
    - Strong performance in math, coding, and science
    - 24% faster than o1-mini
    - Matches o1's performance in STEM with medium reasoning
  - Use cases: Technical domains requiring precision and speed

#### Anthropic Models
- **Claude 3.5 Sonnet (Released Jun 2024)**
  - Best for: Complex reasoning and coding tasks
  - Key features:
    - 2x faster than Claude 3 Opus
    - 200K token context window
    - Strong vision capabilities
    - Advanced tool use and coding abilities
    - 64% success rate on agentic coding tasks
  - Cost: $3/M input tokens, $15/M output tokens

#### DeepSeek Models
- **DeepSeek-R1**
  - Best for: Advanced reasoning and STEM tasks
  - Architecture: 671B parameters (37B activated)
  - Key features:
    - Strong performance in math (AIME, MATH-500)
    - Advanced coding capabilities
    - 128K context window
  - Variants: DeepSeek-R1-Zero (RL-only model), DeepSeek-R1 (full model)
  
- **DeepSeek-R1-Distill Series**
  - Variants: 1.5B to 70B parameter models
  - Based on: Qwen and Llama architectures
  - Performance: Competitive with larger models on specific tasks

#### Meta Models
- **Llama 3 Family**
  - **Llama 3.1**
    - 8B: Light-weight, ultra-fast model
    - 405B: Flagship foundation model
  
  - **Llama 3.2**
    - 1B/3B: Efficient, on-device models
    - 11B/90B: Multimodal capabilities
  
  - **Llama 3.3**
    - 70B: High performance at reduced cost
    - Comparable to 405B model performance

### Model Hosting/Inference
- **vLLM**
  - Use for: High-throughput inference
  - Key feature: PagedAttention for memory management

- **Text Generation Inference (TGI)**
  - Use for: Production deployment
  - Key feature: Optimized for Hugging Face models

## 2. Embedding Models & Vector Search

### Embedding Models
- **Cohere Embed v3**
  - Best for: Enterprise-grade semantic search and RAG
  - Key features:
    - Multimodal capabilities
    - Robust to noisy data
    - Optimized for retrieval tasks
  - Use cases: Semantic search, RAG, clustering, classification

- **OpenAI text-embedding-ada-002**
  - Best for: High-quality text embeddings
  - Key features: Strong semantic understanding

### Vector Databases
- **Chroma**
  - Best for: Development and prototyping
  - Key features: Python native, easy setup

- **Pinecone**
  - Best for: Managed vector search
  - Key features: Real-time updates, managed service

- **Weaviate**
  - Best for: Production deployments
  - Key features: GraphQL API, multi-modal support

## 3. Fine-tuning & Training

### Frameworks
- **Hugging Face Transformers**
  - Best for: Complete ML workflow
  - Key features: Model hub, training utilities

- **PEFT**
  - Best for: Resource-efficient fine-tuning
  - Features: LoRA, QLoRA, Prefix tuning

### Training Optimization
- **DeepSpeed**
  - Best for: Distributed training
  - Features: ZeRO optimization, pipeline parallelism

- **bitsandbytes**
  - Best for: Model quantization
  - Features: 4-bit, 8-bit quantization

## 4. Deployment & Monitoring

### Platforms
- **AWS SageMaker**
  - Best for: Enterprise ML deployment
  - Features: Complete ML lifecycle

- **Hugging Face Inference Endpoints**
  - Best for: Quick model deployment
  - Features: Easy scaling, versioning

### Monitoring & Observability
- **Weights & Biases**
  - Best for: Experiment tracking
  - Features: Visualization, collaboration

- **MLflow**
  - Best for: Model lifecycle management
  - Features: Model registry, tracking

### Evaluation
- **OpenAI evals**
  - Best for: LLM evaluation
  - Features: Automated testing

- **RAGAS**
  - Best for: RAG evaluation
  - Features: Context relevance, faithfulness metrics
