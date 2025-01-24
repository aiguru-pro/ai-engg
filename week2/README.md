# Week 2: Retrieval Augmented Generation (RAG)

## Research Papers

# Research Papers on Retrieval-Augmented Generation (RAG)

## 1. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)](https://arxiv.org/abs/2005.11401)
- **Authors:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, et al.
- **Summary:** 
  This foundational paper introduces the RAG framework, combining pre-trained sequence-to-sequence models with a retrieval component to enhance performance on knowledge-intensive tasks. The authors demonstrate that RAG models outperform traditional architectures in open-domain question answering and other applications.

---

## 2. [Retrieval-Augmented Generation for AI-Generated Content: A Survey (2024)](https://arxiv.org/abs/2402.19473)
- **Authors:** Penghao Zhao, Hailin Zhang, Qinhan Yu, et al.
- **Summary:** 
  This survey provides a comprehensive review of existing efforts that integrate RAG techniques into AI-generated content scenarios. It classifies RAG foundations, discusses enhancement methods, and explores practical applications across different modalities and tasks.

---

## 3. [A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions (2024)](https://arxiv.org/abs/2410.12837)
- **Authors:** Shailja Gupta, Rajesh Ranjan, Surya Narayan Singh
- **Summary:** 
  This paper presents a detailed study of RAG, tracing its evolution from foundational concepts to the current state of the art. It explores the basic architecture of RAG, significant technological advancements, applications across various domains, and discusses ongoing challenges and future research directions.
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
1. [LangChain RAG Overview](https://python.langchain.com/docs/concepts/rag/)
2. [LlamaIndex RAG Guide](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)
3. [Anthropic's Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)

### Tools
1. [ChromaDB](https://www.trychroma.com/)
2. [FAISS](https://github.com/facebookresearch/faiss)
3. [Weaviate](https://weaviate.io/)
4. [LangChain](https://github.com/langchain-ai/langchain)

# Videos on Retrieval-Augmented Generation (RAG)

## 1. [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M)
- **Published:** Approximately 1.4 years ago
- **Summary:** This video provides an overview of RAG, explaining how large language models can be enhanced by integrating retrieval mechanisms to access up-to-date and trustworthy information. It discusses the benefits of combining retrieval with generation to improve the accuracy and reliability of AI outputs.

## 2. [How to use Retrieval Augmented Generation (RAG)](https://www.youtube.com/watch?v=oVtlp72f9NQ)
- **Published:** About 3 months ago
- **Summary:** This video delves into the practical applications of RAG, demonstrating how to implement retrieval-augmented generation in AI applications. It covers the components, benefits, and steps involved in a basic RAG workflow, providing a hands-on approach to understanding and utilizing RAG in real-world scenarios.

## 3. [For dummies: Retrieval Augmented Generation (RAG)](https://www.youtube.com/watch?v=_U7j6BgLNto)
- **Published:** Date not specified
- **Summary:** Aimed at beginners, this video breaks down the basic RAG pipeline and showcases it in action through a hands-on example. It's designed to help those new to the concept grasp the fundamentals of RAG and see its practical implementation.

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
