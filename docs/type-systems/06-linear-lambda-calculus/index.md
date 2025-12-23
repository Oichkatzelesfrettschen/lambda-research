# Linear Lambda Calculus

A resource-aware type system where variables must be used exactly once, enabling precise control over computational resources and supporting applications in concurrency, quantum computing, and memory management.

## Overview

Linear Lambda Calculus extends lambda calculus with:
- **Linear types**: Resources that must be used exactly once
- **Resource tracking**: Variables cannot be duplicated or discarded freely
- **Substructural logic**: Based on linear logic principles
- **Controlled sharing**: Explicit operators for duplication and deletion
- **Resource safety**: Prevents resource leaks and double-free errors

## Syntax and Typing

```
Types: A, B ::= α | A ⊸ B | A ⊗ B | A ⊕ B | A & B | !A | 1 | 0 | ⊤ | ⊥

Terms: M, N ::= x | λx.M | M N | ⟨M,N⟩ | let ⟨x,y⟩ = M in N |
               inl(M) | inr(M) | case M of {inl(x) → N; inr(y) → P} |
               !M | let !x = M in N | derelict(M) |
               * | abort(M)

Linear Context: Γ ::= ∅ | Γ, x:A    (each variable used exactly once)
Unrestricted Context: Δ ::= ∅ | Δ, x:!A    (can be used any number of times)
```

## Typing Rules

### Linear Function Types (⊸)
```
Γ, x:A ⊢ M : B
─────────────────                    (⊸-Intro)
Γ ⊢ λx.M : A ⊸ B

Γ₁ ⊢ M : A ⊸ B    Γ₂ ⊢ N : A
─────────────────────────────        (⊸-Elim)
Γ₁, Γ₂ ⊢ M N : B
```

### Multiplicative Conjunction (⊗)
```
Γ₁ ⊢ M : A    Γ₂ ⊢ N : B
─────────────────────────             (⊗-Intro)
Γ₁, Γ₂ ⊢ ⟨M,N⟩ : A ⊗ B

Γ₁ ⊢ M : A ⊗ B    Γ₂, x:A, y:B ⊢ N : C
─────────────────────────────────────    (⊗-Elim)
Γ₁, Γ₂ ⊢ let ⟨x,y⟩ = M in N : C
```

### Exponential Modality (!)
```
Δ ⊢ M : A
─────────────                        (!-Intro)
Δ ⊢ !M : !A

Γ₁ ⊢ M : !A    Γ₂, x:A ⊢ N : B
─────────────────────────────        (!-Elim)
Γ₁, Γ₂ ⊢ let !x = M in N : B

Δ, x:!A ⊢ M : B
─────────────────                    (Dereliction)
Δ, x:!A ⊢ M : B

Δ ⊢ M : B
─────────────────                    (Weakening)
Δ, x:!A ⊢ M : B

Δ, x:!A, y:!A ⊢ M : B
─────────────────────                (Contraction)
Δ, z:!A ⊢ M[z/x][z/y] : B
```

## Key Properties

- **Resource Safety**: No double-use or unused resources
- **Confluence**: Church-Rosser property holds
- **Strong Normalization**: All well-typed terms terminate
- **Decidable Type Checking**: Linear resource tracking is decidable
- **Cut Elimination**: Corresponds to normalization
- **Resource Bounds**: Precise control over space and time usage

## Historical Development

- **Girard (1987)**: Linear logic foundation
- **Abramsky (1993)**: Computational interpretations
- **Wadler (1993)**: Linear types for functional programming
- **Benton (1995)**: Mixed linear/non-linear systems
- **Walker (2005)**: Linear types in low-level programming

## Linear Logic Correspondence

| Linear Logic | Programming Interpretation |
|--------------|---------------------------|
| A ⊸ B        | Linear function type      |
| A ⊗ B        | Pair consumed linearly    |
| A ⊕ B        | Linear sum type           |
| A & B        | Non-deterministic choice  |
| !A           | Unrestricted use allowed  |
| 1            | Unit type                 |
| ⊥            | Linear continuation       |

## Resource Management Examples

### Linear File Handling
```
File : Type
read : File ⊸ (Data ⊗ File)
write : File ⊸ Data ⊸ File
close : File ⊸ 1

safe_file_ops : File ⊸ Data ⊸ 1
safe_file_ops = λf.λd.
  let ⟨data, f'⟩ = read f in
  let f'' = write f' d in
  close f''
```

### Memory Management
```
Ptr : Type → Type
alloc : !A → (Ptr A ⊗ A)
free : ∀A. Ptr A ⊸ 1
deref : ∀A. Ptr A ⊸ (A ⊗ Ptr A)

safe_memory : !Int → 1
safe_memory = λn.
  let ⟨ptr, val⟩ = alloc n in
  let ⟨_, ptr'⟩ = deref ptr in
  free ptr'
```

## Extensions and Variants

### Affine Types
- Variables used **at most once** (weaker than linear)
- Allows discarding but not duplication
- Useful for resource cleanup without strict usage requirements

### Relevant Types
- Variables used **at least once** (relevant logic)
- Prevents unused variables but allows duplication
- Useful for ensuring all inputs are considered

### Ordered Types
- Variables used in **specific order** (non-commutative)
- Models sequential resource access
- Applications in hardware and protocol verification

### Session Types
- Linear types for communication protocols
- Ensures proper protocol adherence
- Prevents communication errors and deadlocks

## Applications

### Systems Programming
- Memory safety without garbage collection
- Resource management (files, sockets, locks)
- Prevention of use-after-free and double-free bugs

### Concurrency
- Safe sharing of mutable state
- Protocol verification for message passing
- Deadlock prevention through resource ordering

### Quantum Computing
- Quantum states cannot be cloned (no-cloning theorem)
- Linear types naturally model quantum resources
- Ensures measurement occurs exactly once

### Compiler Optimizations
- Alias analysis and memory optimization
- Resource usage verification
- Safe parallelization of linear computations

## Implementation Strategies

### Type Checking
```
Algorithm: Linear Type Checking
Input: Context Γ, Term M, Type A
Output: Success/Failure + Resource usage

check(Γ, x, A):
  if x:A ∈ Γ then return (Γ \ {x:A}, Success)
  else return (Γ, Failure)

check(Γ, λx.M, A ⊸ B):
  (Γ', result) = check(Γ ∪ {x:A}, M, B)
  if x:A ∈ Γ' then return (Γ, Failure)  // x not used
  else return (Γ' \ {x:A}, Success)
```

### Runtime Systems
- Reference counting for linear resources
- Unique ownership tracking
- Automatic resource cleanup

## Theoretical Foundations

### Cut Elimination
```
Cut Rule in Linear Logic:
Γ ⊢ M : A    Δ, x:A ⊢ N : B
─────────────────────────────  (Cut)
Γ, Δ ⊢ N[M/x] : B

Elimination preserves linearity and reduces proof complexity.
```

### Categorical Semantics
- Models in symmetric monoidal closed categories
- Linear continuations and control operators
- Relationship to classical logic through double negation

## Resources

- **Papers**: See [papers/bibliography.md](papers/bibliography.md) for linear logic foundations
- **Implementations**: Linear type checkers and compilers (Rust, Clean, ATS)
- **Tutorials**: Resource-aware programming examples
- **Applications**: Systems programming and quantum computing case studies

## Related Systems

- [Substructural Types](../09-substructural-types/index.md) - General framework for resource logics
- [Session Types](../07-session-types/index.md) - Communication protocol types
- [Quantum Variants](../../advanced/11-quantum-variants/index.md) - Quantum resource management
- [Simply Typed Lambda Calculus](../../foundation/02-simply-typed-lambda-calculus/index.md) - Non-linear foundation

---

*Linear Lambda Calculus provides a foundation for resource-aware computation, enabling safe and efficient resource management while maintaining the expressiveness of functional programming.*