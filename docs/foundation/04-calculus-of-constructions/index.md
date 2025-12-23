# Calculus of Constructions

The most expressive corner of the lambda cube, combining dependent types with polymorphism to create a unified framework for both computation and logical reasoning.

## Overview

The Calculus of Constructions (CoC) unifies:
- **Dependent types**: Types depending on values (Π-types)
- **Polymorphism**: Types depending on types (System F)
- **Type operators**: Types depending on type operators
- **Higher-order logic**: Propositions as types, proofs as terms
- **Impredicativity**: Types can quantify over all types including themselves

## Syntax and Typing

```
Sorts: s ::= * | □

Types/Terms: A, B, M, N ::= s | x | λx:A.B | Π x:A.B | M N

Typing: Γ ⊢ M : A
```

Note: The same syntax is used for types and terms (unified syntax).

## Typing Rules

```
─────────────                            (Axiom)
∅ ⊢ * : □

Γ ⊢ A : s    x ∉ Γ
─────────────────                        (Start)
Γ, x:A ⊢ x : A

Γ ⊢ A : s    Γ, x:A ⊢ B : t
─────────────────────────                (Product)
Γ ⊢ Π x:A.B : t
  where (s,t) ∈ {(*,*), (*,□), (□,*), (□,□)}

Γ, x:A ⊢ b : B    Γ ⊢ Π x:A.B : s
─────────────────────────────             (Abstraction)
Γ ⊢ λx:A.b : Π x:A.B

Γ ⊢ f : Π x:A.B    Γ ⊢ a : A
─────────────────────────────             (Application)
Γ ⊢ f a : B[a/x]

Γ ⊢ a : A    Γ ⊢ B : s    A ≡β B
─────────────────────────────             (Conversion)
Γ ⊢ a : B
```

## Key Properties

- **Strong Normalization**: All well-typed terms terminate
- **Confluence**: Church-Rosser property holds
- **Consistency**: No proof of contradiction
- **Subject Reduction**: Types preserved under reduction
- **Decidable Type Checking**: Algorithms exist for verification
- **Expressive Power**: Encodes higher-order logic

## Historical Development

- **de Bruijn (1970s)**: Automath project, dependent types
- **Martin-Löf (1975)**: Intuitionistic type theory
- **Girard (1972)**: System F and higher-order logic
- **Coquand-Huet (1985)**: Calculus of Constructions proper
- **Barendregt (1991)**: Lambda cube classification

## Important Theorems

- **Strong Normalization**: Girard-Tait method proof
- **Consistency**: No term of type ∀X:*.X
- **Representability**: All recursive functions encodable
- **Decidability**: Type checking is decidable
- **Expressivity**: Equivalent to higher-order logic

## Lambda Cube Position

CoC occupies the (1,1,1) corner of the lambda cube:
- **λ→**: Simply typed lambda calculus
- **λ2**: System F (polymorphism)
- **λP**: LF (dependent types)
- **λω**: System F-omega (type operators)
- **λC**: CoC (all three dimensions)

## Encodings and Examples

### Dependent Function Types
```
Vector : Nat → * → *
Vector = λn:Nat.λA:*.Vec A n  -- length-indexed vectors

append : Π n:Nat.Π m:Nat.Π A:*.
         Vector n A → Vector m A → Vector (plus n m) A
```

### Polymorphic Identity with Dependent Types
```
dep_id : Π A:*.A → A
dep_id = λA:*.λx:A.x
```

### Propositions as Types
```
And : * → * → *
And = λP:*.λQ:*.Π R:*.(P → Q → R) → R

and_intro : Π P:*.Π Q:*.P → Q → And P Q
and_intro = λP:*.λQ:*.λp:P.λq:Q.λR:*.λf:P→Q→R.f p q
```

### Natural Numbers
```
Nat : *
Nat = Π X:*.(X → X) → X → X

zero : Nat
zero = λX:*.λs:X→X.λz:X.z

succ : Nat → Nat
succ = λn:Nat.λX:*.λs:X→X.λz:X.s (n X s z)
```

## Extensions and Variants

- **Calculus of Inductive Constructions**: Add inductive types
- **Extended Calculus of Constructions**: Universe hierarchies
- **Calculus of Constructions with Definitions**: Let expressions
- **Observational Type Theory**: Proof-relevant equality
- **Homotopy Type Theory**: Univalent foundations

## Applications

- **Proof Assistants**: Coq, Lean, Agda kernels
- **Dependent Programming**: Verified software development
- **Mathematical Formalization**: Computer-checked proofs
- **Type-Driven Development**: Precise specifications
- **Certified Compilation**: Verified compiler correctness

## Computational Interpretation

- **Curry-Howard Correspondence**: Propositions as types, proofs as programs
- **Extraction**: Extract computational content from proofs
- **Evaluation Strategy**: Call-by-name for consistency
- **Termination**: Strong normalization ensures consistency

## Resources

- **Papers**: See [papers/bibliography.md](papers/bibliography.md) for foundational works
- **Implementations**: CoC implementations and proof assistants
- **Tutorials**: Dependent type programming examples
- **Historical**: Development from lambda calculus to modern proof assistants

## Related Systems

- [System F](../03-system-f-polymorphic/index.md) - Polymorphic foundation
- [Martin-Löf Type Theory](../05-martin-lof-type-theory/index.md) - Constructive alternative
- [Pure Type Systems](../../type-systems/12-pure-type-systems/index.md) - General framework
- [Dependent Types](../../type-systems/08-dependent-types/index.md) - Core concept exploration

---

*The Calculus of Constructions represents the theoretical pinnacle of typed lambda calculi, providing a foundation for modern proof assistants and dependently typed programming languages.*