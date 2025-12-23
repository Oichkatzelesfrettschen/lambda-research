# Synergy Map: Lambda Calculus & Unified Spandrel Synthesis (USS)

## 1. Theoretical Overlaps
Our research platform maps abstract theoretical constructs to optimized computational kernels:

| Theoretical Domain | Documentation Link | USS Implementation Component | Synergy Breakthrough |
|:---|:---|:---|:---|
| **Untyped λ-Calculus** | [01-untyped](../foundation/01-untyped-lambda-calculus/index.md) | `src/data/generator.py` | Parallelized term generation at 1.6M terms/s |
| **System F** | [03-system-f](../foundation/03-system-f-polymorphic/index.md) | `src/models/transformer.py` | Type-erased representation for neuro-symbolic learning |
| **Linear Logic** | [06-linear](../type-systems/06-linear-lambda-calculus/index.md) | `src/kernels/tensor_contraction.py` | Resource-aware tensor operations mapped to SM89 hardware |
| **Tensor λ-Calculus** | [24-tensor](../advanced/24-tensor-lambda-calculus/index.md) | `src/kernels/` | Triton-accelerated contraction for multi-dimensional reasoning |

## 2. Methodology Flow
1.  **Symbolic Source**: Academic papers define the rules (Church, Girard, Barendregt).
2.  **Data Synthesis**: Parallel generators fling millions of calculations through encoders.
3.  **HPC Acceleration**: Rust and CUDA/Triton kernels exploit Tensor Cores.
4.  **Neural Inference**: Transformer decoders learn to synthesize and verify proofs.

## 3. Breakthrough: The "Spandrel" Connection
By treating the "overhead" of formal verification as a structural "spandrel," we optimize the training loop to predict type soundness as a latent feature of the encoded lambda terms.
