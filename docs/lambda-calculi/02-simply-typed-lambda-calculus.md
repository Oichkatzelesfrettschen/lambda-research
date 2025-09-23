# Simply Typed Lambda Calculus

The foundational typed functional language, extending the untyped lambda calculus with a simple type system to ensure type safety and strong normalization.

## Overview

Simply Typed Lambda Calculus (STLC) adds types to lambda calculus:
- **Base types**: `o` (booleans), `ι` (individuals), etc.
- **Function types**: `σ → τ` (functions from σ to τ)
- **Type safety**: Well-typed terms don't get stuck
- **Strong normalization**: All well-typed terms terminate

## Syntax and Typing

```
Types: σ, τ ::= o | ι | σ → τ

Terms: M, N ::= x | λx:σ.M | M N | c

Typing: Γ ⊢ M : σ
```

## Typing Rules

```
Γ, x:σ ⊢ x : σ                           (Variable)

Γ, x:σ ⊢ M : τ
─────────────────                         (Abstraction)
Γ ⊢ λx:σ.M : σ → τ

Γ ⊢ M : σ → τ    Γ ⊢ N : σ
─────────────────────────────             (Application)
Γ ⊢ M N : τ
```

## Key Properties

- **Type Safety**: Progress and preservation theorems
- **Strong Normalization**: All well-typed terms terminate
- **Decidable Type Checking**: Algorithm W (Hindley-Milner)
- **Canonical Forms**: Normal forms have predictable structure

## Historical Development

- **Church (1940)**: Original typed lambda calculus
- **Curry (1958)**: Type assignment systems
- **Hindley (1969)**: Principal type theorem
- **Milner (1978)**: Algorithm W and ML

## Important Theorems

- **Church-Rosser**: Confluence holds for typed terms
- **Strong Normalization**: All reduction sequences terminate
- **Principal Types**: Most general type assignment
- **Decidability**: Type checking and inference algorithms

## Extensions and Variants

- **Product Types**: `σ × τ` for pairs
- **Sum Types**: `σ + τ` for unions
- **Unit Type**: `1` for the empty tuple
- **Void Type**: `0` for the empty type

## Applications

- Foundation for functional programming languages
- Basis for type inference algorithms
- Proof assistant kernels
- Programming language theory

## Resources

- **Papers**: See [bibliography.md](../../02-simply-typed-lambda-calculus/papers/bibliography.md) for 30+ key papers
- **Implementations**: Type checkers and interpreters
- **Tutorials**: Step-by-step type checking examples
- **Historical**: Development from Church to modern systems

## Related Systems

- [Untyped Lambda Calculus](/../01-untyped-lambda-calculus/) - Untyped foundation
- [System F](/../03-system-f-polymorphic/) - Polymorphic extension
- [Martin-Löf Type Theory](/../05-martin-lof-type-theory/) - Dependent types

---

*Simply Typed Lambda Calculus established the foundations of type safety and remains the core of most functional programming languages.*