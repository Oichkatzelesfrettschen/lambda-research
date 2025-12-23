# System F (Polymorphic Lambda Calculus)

The second-order polymorphic lambda calculus, introducing parametric polymorphism through type abstraction and universal quantification over types.

## Overview

System F extends simply typed lambda calculus with:
- **Type variables**: `X`, `Y`, `Z` ranging over all types
- **Universal quantification**: `∀X.τ` for polymorphic types
- **Type abstraction**: `ΛX.M` for polymorphic terms
- **Type application**: `M[τ]` for type instantiation
- **Parametric polymorphism**: Types parameterized by other types

## Syntax and Typing

```
Types: σ, τ ::= X | σ → τ | ∀X.τ

Terms: M, N ::= x | λx:σ.M | M N | ΛX.M | M[τ]

Typing: Γ; Δ ⊢ M : σ
  where Γ is term context, Δ is type context
```

## Typing Rules

```
Γ; Δ, X ⊢ M : τ
─────────────────────                    (Type Abstraction)
Γ; Δ ⊢ ΛX.M : ∀X.τ

Γ; Δ ⊢ M : ∀X.τ    Δ ⊢ σ
─────────────────────────                (Type Application)
Γ; Δ ⊢ M[σ] : τ[σ/X]

Γ, x:σ; Δ ⊢ x : σ                        (Variable)

Γ, x:σ; Δ ⊢ M : τ
─────────────────────                     (Abstraction)
Γ; Δ ⊢ λx:σ.M : σ → τ

Γ; Δ ⊢ M : σ → τ    Γ; Δ ⊢ N : σ
─────────────────────────────             (Application)
Γ; Δ ⊢ M N : τ
```

## Key Properties

- **Strong Normalization**: All well-typed terms terminate
- **Parametricity**: Types determine behavior abstractly
- **Type Preservation**: Types preserved under reduction
- **Decidable Type Checking**: Though inference is undecidable
- **Impredicativity**: Types can quantify over themselves

## Historical Development

- **Girard (1971)**: System F as proof system for second-order logic
- **Reynolds (1974)**: Polymorphic lambda calculus independently
- **Girard (1972)**: Representation theorem for data types
- **Reynolds (1983)**: Parametricity and relational interpretations
- **Wadler (1989)**: Theorems for free from parametricity

## Important Theorems

- **Strong Normalization**: All System F terms normalize
- **Representation Theorem**: All finite data types encodable
- **Parametricity**: Free theorems from polymorphic types
- **Undecidability**: Type inference is undecidable
- **Expressive Power**: Captures second-order arithmetic

## Encodings and Examples

### Church Numerals
```
Nat = ∀X.(X → X) → X → X
zero = ΛX.λf:X→X.λx:X.x
succ = λn:Nat.ΛX.λf:X→X.λx:X.f (n[X] f x)
```

### Polymorphic Identity
```
id = ΛX.λx:X.x : ∀X.X → X
```

### List Type
```
List = λX.∀Y.(X → Y → Y) → Y → Y
nil = ΛX.ΛY.λc:X→Y→Y.λn:Y.n
cons = ΛX.λh:X.λt:List X.ΛY.λc:X→Y→Y.λn:Y.c h (t[Y] c n)
```

## Extensions and Variants

- **System F-omega**: Higher-order polymorphism with type operators
- **System F-sub**: Subtyping extensions
- **Bounded Quantification**: `∀X<:τ.σ` with type bounds
- **Higher-Rank Types**: Polymorphism in arbitrary positions
- **Existential Types**: `∃X.τ` for abstract data types

## Applications

- Foundation of ML-style polymorphism
- Generic programming languages (Haskell, ML)
- Proof assistants and theorem provers
- Abstract data type implementations
- Compiler intermediate representations

## Computational Complexity

- **Type Checking**: Decidable in polynomial time
- **Type Inference**: Undecidable in general
- **Strong Normalization**: Bounds on reduction length
- **Space Complexity**: Polynomial in input size

## Resources

- **Papers**: See [papers/bibliography.md](papers/bibliography.md) for foundational works
- **Implementations**: Type checkers and interpreters in various languages
- **Tutorials**: Step-by-step examples of polymorphic programming
- **Historical**: Development from proof theory to programming languages

## Related Systems

- [Simply Typed Lambda Calculus](../02-simply-typed-lambda-calculus/index.md) - Monomorphic foundation
- [Calculus of Constructions](../04-calculus-of-constructions/index.md) - Dependent types extension
- [Pure Type Systems](../../type-systems/12-pure-type-systems/index.md) - Generalization framework
- [Martin-Löf Type Theory](../05-martin-lof-type-theory/index.md) - Constructive alternative

---

*System F established parametric polymorphism as a fundamental principle in type theory and programming languages, enabling generic programming while maintaining strong theoretical foundations.*