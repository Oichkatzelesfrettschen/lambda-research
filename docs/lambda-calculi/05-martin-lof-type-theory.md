# Martin-Löf Type Theory

A constructive type theory serving as both a programming language and a foundation for mathematics, emphasizing computational content and intuitionistic logic.

## Overview

Martin-Löf Type Theory (MLTT) provides:
- **Constructive mathematics**: All proofs have computational content
- **Dependent types**: Types depending on values (Π and Σ types)
- **Inductive types**: Built-in support for natural numbers, lists, trees
- **Identity types**: Propositional equality with computational content
- **Universe hierarchy**: Types of types with predicative stratification
- **Intuitionistic logic**: Constructive proofs and excluded middle rejection

## Syntax and Core Types

```
Types: A, B ::= U_i | Π x:A.B | Σ x:A.B | A + B | A × B |
               N | Id_A(a,b) | 0 | 1

Terms: a, b ::= x | λx.a | app(f,a) | pair(a,b) | fst(p) | snd(p) |
               inl(a) | inr(b) | case(c,f,g) | 0 | succ(n) |
               rec_N(n,f,g) | refl_a | J(P,d,p)

Contexts: Γ ::= ∅ | Γ, x:A
```

## Formation Rules (Selected)

### Dependent Function Types (Π-types)
```
Γ ⊢ A : U_i    Γ, x:A ⊢ B : U_i
────────────────────────────────    (Π-formation)
Γ ⊢ Π x:A.B : U_i

Γ, x:A ⊢ b : B
─────────────────────────────      (Π-introduction)
Γ ⊢ λx.b : Π x:A.B

Γ ⊢ f : Π x:A.B    Γ ⊢ a : A
─────────────────────────────      (Π-elimination)
Γ ⊢ app(f,a) : B[a/x]

app(λx.b, a) = b[a/x]              (Π-computation)
```

### Dependent Pair Types (Σ-types)
```
Γ ⊢ A : U_i    Γ, x:A ⊢ B : U_i
────────────────────────────────    (Σ-formation)
Γ ⊢ Σ x:A.B : U_i

Γ ⊢ a : A    Γ ⊢ b : B[a/x]
─────────────────────────────      (Σ-introduction)
Γ ⊢ pair(a,b) : Σ x:A.B

Γ ⊢ p : Σ x:A.B
─────────────────────────────      (Σ-elimination)
Γ ⊢ fst(p) : A

Γ ⊢ p : Σ x:A.B
─────────────────────────────
Γ ⊢ snd(p) : B[fst(p)/x]
```

## Key Properties

- **Canonical Forms**: Each type has canonical inhabitants
- **Decidable Type Checking**: Algorithmic type checking exists
- **Strong Normalization**: All well-typed terms normalize
- **Consistency**: No proof of contradiction constructively
- **Computational Content**: All proofs compute to canonical forms
- **Predicativity**: Universe hierarchy prevents paradoxes

## Historical Development

- **Martin-Löf (1972)**: First version with one universe
- **Martin-Löf (1975)**: Revised with universe hierarchy
- **Martin-Löf (1984)**: Intuitionistic type theory
- **Constable et al. (1986)**: NuPRL implementation
- **Dybjer (1995)**: Inductive families
- **Altenkirch et al. (1995)**: Containers and polynomial functors

## Core Type Formers

### Natural Numbers
```
Formation: Γ ⊢ N : U_0
Introduction: Γ ⊢ 0 : N    Γ ⊢ succ(n) : N
Elimination: Γ ⊢ rec_N(n, c, f) : C[n/x]
  where Γ, x:N ⊢ C : U_i
        Γ ⊢ c : C[0/x]
        Γ ⊢ f : Π x:N.C → C[succ(x)/x]
```

### Identity Types
```
Formation: Γ ⊢ A : U_i    Γ ⊢ a,b : A
          ─────────────────────────
          Γ ⊢ Id_A(a,b) : U_i

Introduction: Γ ⊢ a : A
             ─────────────
             Γ ⊢ refl_a : Id_A(a,a)

Elimination: J-eliminator for path induction
```

### Finite Types
```
Empty Type: 0 : U_0    (no introduction rules)
Unit Type:  1 : U_0    with constructor * : 1
```

## Constructive Mathematics

### Function Extensionality
```
funext : Π f,g : Π x:A.B. (Π x:A. Id_B(f(x), g(x))) → Id(f,g)
```

### Univalence (HoTT Extension)
```
ua : Π A,B : U. (A ≃ B) → Id_U(A,B)
```

### Propositions as Types
- Logical conjunction: Σ-types `Σ x:A.B`
- Logical disjunction: Sum types `A + B`
- Logical implication: Π-types `A → B`
- Existential quantification: Σ-types `Σ x:A.P(x)`
- Universal quantification: Π-types `Π x:A.P(x)`

## Extensions and Variants

- **Intensional vs Extensional**: Different identity type behaviors
- **Inductive-Recursive Types**: Simultaneous type and function definition
- **Quotient Types**: Types with custom equality relations
- **Higher Inductive Types**: Types with higher-dimensional structure
- **Cubical Type Theory**: Computational univalence
- **Observational Type Theory**: Proof-relevant equality

## Applications

- **Proof Assistants**: Agda, Coq (CIC), Lean foundations
- **Verified Programming**: Certified software development
- **Mathematical Formalization**: Computer-checked mathematics
- **Type-Driven Development**: Precise specifications guide implementation
- **Foundations of Mathematics**: Alternative to set theory

## Computational Interpretation

- **Curry-Howard-de Bruijn**: Propositions-types-programs correspondence
- **Extraction**: Programs from constructive proofs
- **Normalization**: Reduction to canonical forms
- **Decidability**: Effective procedures for type checking

## Comparison with Classical Logic

| Classical Logic | Constructive Logic (MLTT) |
|-----------------|---------------------------|
| Excluded Middle | Not provable              |
| Proof by Contradiction | Not always valid    |
| Existence Proofs | Must provide witness      |
| Double Negation | Not eliminable           |
| Choice Principle | Not assumed              |

## Resources

- **Papers**: See [papers/bibliography.md](../../05-martin-lof-type-theory/papers/bibliography.md) for foundational works
- **Implementations**: Agda, Coq, NuPRL, and other proof assistants
- **Tutorials**: Constructive mathematics and dependent type programming
- **Historical**: Development from intuitionistic logic to modern type theory

## Related Systems

- [Calculus of Constructions](/../04-calculus-of-constructions/) - Impredicative variant
- [Dependent Types](/../08-dependent-types/) - Core concept exploration
- [Pure Type Systems](/../12-pure-type-systems/) - General framework
- [Homotopy Type Theory](/../29-homotopy-type-theory/) - Higher-dimensional extension

---

*Martin-Löf Type Theory established constructive type theory as a foundation for both mathematics and computation, emphasizing that all proofs must have computational content.*