# Unified Spandrel Synthesis: Research & Experimental Plan

## 1. Executive Objective
Transition from theoretical documentation to a high-performance neuro-symbolic synthesis engine. We will implement a Transformer-based model for generating well-typed lambda terms (System F / Calculus of Constructions) optimized for SM89 (Ada Lovelace) hardware using CUDA 12.

## 2. Core Research Papers
| Paper | Methodology to Extract |
|-------|------------------------|
| **DeepCoder (Balog et al.)** | Attribute-based program search and DSL embedding. |
| **Program Synthesis with Refinement Types (Polikarpova)** | Integration of type-checking into the search heuristic. |
| **Neural Lambda Calculus (Lamb et al.)** | Differentiable reduction rules for end-to-end training. |
| **Triton: An Intermediate Language for Deep Learning** | Kernel optimization strategies for GPUs. |

## 3. Experimental Parameters
### Dataset Scale
- **Training Set**: 10M generated valid lambda terms across 31 variants.
- **Format**: Parquet (storage) -> TFRecords (streaming ingestion).
- **Synthetics**: Random term generation with exhaustive type-checking validation.

### Model Architecture
- **Backbone**: Decoder-only Transformer (Custom implementation).
- **Features**: SM89-optimized Attention (utilizing FlashAttention-2 or custom kernels).
- **Output**: Linearized lambda terms (De Bruijn indices).

### Hyperparameter Ranges
- **Learning Rate**: 1e-4 to 5e-3 (Cosine annealing).
- **Batch Size**: 1024 - 4096 (optimized for 24GB+ VRAM).
- **Precision**: FP16 / BF16 (using Tensor Cores).

## 4. Benchmarks & Profiling
### Performance Metrics
- **Throughput**: FLOPS achieved in training loop.
- **Latency**: End-to-end synthesis time (ms).
- **Utilization**: % SM utilization during custom kernel execution.

### Tools
- **nvprof / Nsight Compute**: Profiling CUDA kernels for warp divergence.
- **perf**: CPU bottleneck analysis.
- **Weights & Biases**: Experiment tracking and validation curves.

## 5. Kernel Optimization Plan
- **Shared Memory**: Implement manual tiling for tensor contraction in "Tensor Lambda Calculus" nodes.
- **Warp Alignment**: Ensure De Bruijn index lookups avoid bank conflicts.
- **AutoGPU Adjust**: Dynamic batch size adjustment based on VRAM availability.

## 6. Convergence Criteria
- **Validation Accuracy**: > 95% well-typed term generation.
- **Type-Check Latency**: < 5ms per synthesized term.
- **Loss Threshold**: < 0.01 cross-entropy on validation set.
