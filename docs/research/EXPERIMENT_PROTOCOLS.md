# Novel Experiment Protocols: Unified Spandrel Synthesis

## Experiment 1: Latent Normalization Prediction (LNP)
*   **Data**: 10,000,000 synthetic lambda terms (`src/data/shards/*.parquet`).
*   **Architecture**: Encoder-Decoder Transformer with injected Triton Tensor Contraction layers.
*   **Methodology**:
    1.  Encode lambda terms into high-dimensional vector space.
    2.  Predict the normal form (or step count to normalization) without explicit reduction.
    3.  Verify predictions against the Rust-based `lambda-eval` reference.
*   **Optimization**: Use SM89 Tensor Cores for the encoder bottleneck.

## Experiment 2: Type Inference via Substructural Encoders
*   **Data**: Theorem prover traces and Linear Lambda Calculus terms.
*   **Methodology**:
    1.  Apply custom Triton kernels to simulate resource-bounded reduction (Linear/Affine).
    2.  Fling calculations through a decoder to synthesize valid type signatures.
*   **Expected Results**: Improved type inference accuracy for substructural systems where standard unification is NP-hard.

## Experiment 3: Ray Tracing for Proof Search Visualization
*   **Hardware**: SM89 Ray Tracing cores.
*   **Methodology**: Map Proof-Search trees into 3D acceleration structures (BVH).
*   **Goal**: Use RT cores to traverse proving paths at speed, treating proof search as a geometric intersection problem.
