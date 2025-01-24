# Week 2: Retrieval Augmented Generation (RAG)

## Research Papers

1. [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511)
   - Authors: Meta AI Research
   - Year: 2023
   - Key topics: Self-reflective retrieval, Adaptive RAG systems, Response quality improvement

2. [ReAct Meets RAG: Neurally-Guided Retrieval of Relevant Information](https://arxiv.org/abs/2312.12343)
   - Authors: Google Research
   - Year: 2023
   - Key topics: Dynamic information retrieval, Reasoning-action framework integration

3. [Precise Zero-Shot Dense Retrieval without Relevance Labels](https://arxiv.org/abs/2312.02210)
   - Authors: Microsoft Research
   - Year: 2023
   - Key topics: Zero-shot dense retrieval, Embedding optimization

4. [Chain-of-Note: Enhancing Robustness in Retrieval-Augmented Language Models](https://arxiv.org/abs/2311.09210)
   - Authors: Microsoft Research
   - Year: 2023
   - Key topics: Information extraction, Note-taking mechanisms, Retrieval robustness

## Current Trends

### Vector Databases and Embeddings
- Progress in embedding models
- Vector database optimizations
- [Chroma DB Documentation](https://docs.trychroma.com/)
- [FAISS: Facebook AI Similarity Search](https://github.com/facebookresearch/faiss)

### Advanced RAG Architectures
- Hybrid search strategies
- Multi-step retrieval
- Query expansion techniques
- [LlamaIndex Advanced RAG](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/)

### Context Processing
- Recursive retrieval
- Dynamic context window management
- Semantic chunking strategies
- [LangChain Context Window Management](https://python.langchain.com/docs/modules/data_connection/)

### Evaluation and Optimization
- RAG evaluation metrics
- Auto-tuning systems
- [RAGAS: RAG Assessment Framework](https://github.com/explodinggradients/ragas)
- [LangSmith Evaluation Platform](https://www.langchain.com/langsmith)

## Advanced RAG Techniques

### Hybrid Search Methods
- BM25 + Dense Retrieval
- Cross-encoders for re-ranking
- [Sentence Transformers Documentation](https://www.sbert.net/)

### Query Transformation
- Query expansion
- Query decomposition
- Hypothetical document embeddings
- [HyDE: Hypothetical Document Embeddings](https://arxiv.org/abs/2212.10496)

### Multi-Vector Retrieval
- Parent-child chunking
- Hierarchical retrieval
- [LlamaIndex Multi-Vector Retrieval](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/)

### Contextual Compression
- Document compression
- Adaptive chunking
- [LangChain Context Compression](https://python.langchain.com/docs/modules/data_connection/contextual_compression/)

## Additional Resources

### Tutorials
1. [LangChain RAG Overview](https://python.langchain.com/docs/use_cases/question_answering/)
2. [LlamaIndex RAG Guide](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)
3. [Anthropic's RAG Best Practices](https://docs.anthropic.com/claude/docs/retrieval-augmented-generation-rag)

### Tools
1. [ChromaDB](https://www.trychroma.com/)
2. [FAISS](https://github.com/facebookresearch/faiss)
3. [Weaviate](https://weaviate.io/)
4. [LangChain](https://github.com/langchain-ai/langchain)

### Videos
1. [Building RAG Applications with LangChain](https://www.youtube.com/watch?v=LhnCsygAvzY)
2. [Advanced RAG Techniques](https://www.youtube.com/watch?v=TRjq7t2Ms5U)
3. [Stanford Seminar - Retrieval Augmented Generation](https://www.youtube.com/watch?v=QK2tGQWxTFc)

## Practice Project: Enhanced Documentation Assistant

### Basic RAG Implementation:
- Vector database integration
- Basic document retrieval
- Context injection
- Similarity search

### Advanced Features:
1. Hybrid Search
   - Combine semantic and keyword search
   - Re-ranking with cross-encoders

2. Smart Retrieval
   - Query expansion
   - Multi-step retrieval
   - Recursive document fetching

3. Context Optimization
   - Adaptive chunking
   - Context compression
   - Parent-child relationships

4. Evaluation
   - Answer relevance metrics
   - Context quality assessment
   - Response consistency checking

## Homework Assignment
Enhance the Documentation Assistant with:
1. Implementation of at least one advanced RAG technique
2. Comparative analysis with basic RAG
3. Performance metrics and evaluation
4. Documentation of findings and challenges
