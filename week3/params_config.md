# Comprehensive ML Training Guide: Understanding Parameters & Configurations

## Model Architecture Parameters

### Base Architecture Selection

```python
model_type = "bert"  # or "gpt", "t5", etc.
```

- **What it is**: Defines the fundamental architecture of your model
- **Why it matters**: Different architectures are better suited for different tasks
  - BERT: Good for understanding context in both directions (bidirectional)
  - GPT: Excellent for text generation and completing sequences
  - T5: Versatile for many text-to-text tasks
- **How to choose**:
  - For classification/understanding: Consider BERT
  - For generation: Consider GPT
  - For versatile tasks: Consider T5
- **Impact on training**: Affects memory usage, training speed, and model capabilities

### Hidden Layer Configuration

```python
config = {
    "num_hidden_layers": 12,
    "hidden_size": 768,
    "intermediate_size": 3072
}
```

- **num_hidden_layers**:
  - **What**: Number of transformer blocks in your model
  - **Impact**: More layers = deeper understanding but harder to train
  - **Trade-off**: Deeper models can learn more complex patterns but require more compute and are prone to overfitting
- **hidden_size**:

  - **What**: Dimension of the hidden states (representations)
  - **Impact**: Larger size = more capacity but more memory usage
  - **Rule of thumb**: Start with standard sizes (768 for base models, 1024 for large) and adjust based on your dataset size

- **intermediate_size**:
  - **What**: Size of feed-forward networks in transformer blocks
  - **Impact**: Affects model's processing capacity
  - **Usually**: 4x the hidden_size

## Training Process Parameters

### Optimization Settings

```python
optimizer_config = {
    "optimizer": {
        "type": "AdamW",
        "learning_rate": 5e-5,
        "weight_decay": 0.01,
        "beta1": 0.9,
        "beta2": 0.999,
        "epsilon": 1e-8
    }
}
```

- **Learning Rate**:

  - **What**: Step size for weight updates
  - **Impact**: Critical for training success
  - **Too high**: Training becomes unstable
  - **Too low**: Training takes too long
  - **Best practice**: Start with 5e-5 for fine-tuning, 1e-4 for training from scratch

- **Weight Decay**:
  - **What**: L2 regularization strength
  - **Purpose**: Prevents overfitting by penalizing large weights
  - **When to adjust**: Increase if seeing overfitting, decrease if underfitting
  - **Typical values**: 0.01 for fine-tuning, 0.1 for training from scratch

### Batch Processing

```python
training_config = {
    "per_device_train_batch_size": 16,
    "gradient_accumulation_steps": 4,
    "max_grad_norm": 1.0
}
```

- **Batch Size**:

  - **What**: Number of examples processed together
  - **Impact**: Affects training stability and memory usage
  - **Larger batches**:
    - More stable gradient updates
    - Better GPU utilization
    - Might require larger learning rate
  - **Smaller batches**:
    - More updates per epoch
    - Better regularization
    - More memory efficient

- **Gradient Accumulation**:
  - **What**: Accumulating gradients over multiple forward/backward passes
  - **Why use it**: To simulate larger batch sizes when memory is limited
  - **Example**: batch_size=16 with gradient_accumulation=4 simulates batch_size=64
  - **When to use**: When you want larger effective batch sizes but have limited GPU memory

## Memory Management

### Mixed Precision Training

```python
mixed_precision_config = {
    "fp16": {
        "enabled": True,
        "loss_scale": "dynamic",
        "initial_scale_power": 16
    }
}
```

- **What it does**: Uses both 16-bit and 32-bit floating-point precision
- **Benefits**:
  - Reduces memory usage (almost 2x)
  - Speeds up training on modern GPUs
  - Allows larger batch sizes
- **When to use**: Almost always on modern NVIDIA GPUs
- **Cautions**:
  - Monitor for training instability
  - May need to adjust loss scaling
  - Not all operations support FP16

### Gradient Checkpointing

```python
model_config = {
    "gradient_checkpointing": True
}
```

- **What it does**: Trades computation for memory by recomputing activations during backward pass
- **When to use**:
  - Training large models
  - When running out of memory
  - Can't reduce batch size further
- **Trade-off**: Training becomes ~20-30% slower but uses much less memory

## Data Processing

### Sequence Length Management

```python
data_config = {
    "max_seq_length": 512,
    "padding": "max_length",
    "truncation": True
}
```

- **max_seq_length**:
  - **What**: Maximum number of tokens in a sequence
  - **Impact**: Directly affects memory usage
  - **How to choose**:
    - Check your data distribution
    - Consider model architecture limits
    - Balance between coverage and memory
- **padding/truncation**:
  - **What**: How to handle sequences of different lengths
  - **Strategies**:
    - "max_length": Pad/truncate to max_seq_length
    - "longest": Pad to longest in batch
    - Dynamic padding: Most memory efficient
  - **Trade-offs**: Memory usage vs processing efficiency

## Advanced Training Features

### Learning Rate Scheduling

```python
lr_config = {
    "scheduler": "cosine",
    "num_warmup_steps": 500,
    "num_training_steps": 50000
}
```

- **Scheduler Types**:
  - **Linear**: Simple, predictable decay
  - **Cosine**: Smooth decay with potential restarts
  - **Polynomial**: Flexible decay pattern
- **Warmup**:
  - **Purpose**: Gradually increase learning rate to prevent early instability
  - **When to use**: Almost always for transformer models
  - **How much**:
    - By steps: Usually 500-1000 steps
    - By ratio: Usually 10% of training

### Distributed Training

```python
distributed_config = {
    "strategy": "ddp",
    "find_unused_parameters": False,
    "sync_batch_norm": True
}
```

- **What it enables**: Training across multiple GPUs/machines
- **Different strategies**:
  - **DDP (DistributedDataParallel)**:
    - Most common for multi-GPU training
    - Each GPU has its own process
    - Synchronizes gradients across processes
  - **DeepSpeed**:
    - Advanced optimizations
    - Better memory efficiency
    - More complex setup
- **Best practices**:
  - Ensure proper batch size scaling
  - Monitor GPU utilization
  - Check for proper synchronization

## Evaluation and Checkpointing

### Evaluation Strategy

```python
eval_config = {
    "evaluation_strategy": "steps",
    "eval_steps": 500,
    "metric_for_best_model": "loss",
    "save_total_limit": 2
}
```

- **When to evaluate**:

  - **By steps**: Regular intervals during training
  - **By epoch**: End of each epoch
  - Trade-off: Monitoring granularity vs training speed

- **What to save**:
  - Best models based on metric
  - Regular checkpoints for resuming
  - Balance between storage and safety

## Monitoring and Debugging

### Logging Configuration

```python
logging_config = {
    "logging_steps": 10,
    "logging_dir": "./logs",
    "report_to": ["wandb", "tensorboard"]
}
```

- **What to log**:

  - Training/validation metrics
  - Learning rates
  - GPU memory usage
  - Gradient norms

- **How often to log**:
  - More frequent early in training
  - Can reduce frequency later
  - Balance between insight and overhead

## Best Practices and Common Issues

### Memory Issues

- **Symptoms**:
  - CUDA out of memory
  - Gradients becoming NaN
- **Solutions**:
  1. Reduce batch size
  2. Enable gradient checkpointing
  3. Use mixed precision
  4. Reduce sequence length

### Training Instability

- **Symptoms**:
  - Loss not decreasing
  - Validation metrics fluctuating
- **Solutions**:
  1. Reduce learning rate
  2. Increase warmup steps
  3. Check gradient clipping
  4. Monitor gradient norms

### Performance Optimization

- **For speed**:

  1. Increase batch size
  2. Use mixed precision
  3. Optimize data loading
  4. Use gradient accumulation wisely

- **For memory**:
  1. Enable gradient checkpointing
  2. Use mixed precision
  3. Implement gradient accumulation
  4. Monitor memory usage

Remember: These parameters often interact with each other. Changes to one might require adjustments to others for optimal performance.
