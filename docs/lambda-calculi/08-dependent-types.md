# Dependent Types

Types that depend on values, enabling precise specification of program behavior and forming the foundation for advanced type systems used in theorem proving and verified programming.

## Overview

Dependent Types extend type systems with:
- **Value Dependencies**: Types can depend on runtime values
- **Precise Specifications**: Express exact program properties in types
- **Curry-Howard Correspondence**: Types as propositions, terms as proofs
- **Verification**: Static guarantees about program correctness
- **Expressiveness**: Capture invariants impossible in simple type systems

## Core Dependent Type Formers

### Dependent Function Types (Π-types)
```
Formation: Γ ⊢ A : Type    Γ, x:A ⊢ B : Type
          ─────────────────────────────────
          Γ ⊢ Π x:A. B : Type

Introduction: Γ, x:A ⊢ b : B
             ─────────────────
             Γ ⊢ λx.b : Π x:A. B

Elimination: Γ ⊢ f : Π x:A. B    Γ ⊢ a : A
            ─────────────────────────────
            Γ ⊢ f a : B[a/x]
```

### Dependent Pair Types (Σ-types)
```
Formation: Γ ⊢ A : Type    Γ, x:A ⊢ B : Type
          ─────────────────────────────────
          Γ ⊢ Σ x:A. B : Type

Introduction: Γ ⊢ a : A    Γ ⊢ b : B[a/x]
             ─────────────────────────────
             Γ ⊢ (a, b) : Σ x:A. B

Elimination: Γ ⊢ p : Σ x:A. B
            ─────────────────
            Γ ⊢ π₁ p : A

            Γ ⊢ p : Σ x:A. B
            ─────────────────────
            Γ ⊢ π₂ p : B[π₁ p/x]
```

## Key Properties

- **Type Safety**: Well-typed programs satisfy their specifications
- **Decidable Type Checking**: Algorithms exist for verification
- **Expressiveness**: Can encode sophisticated program properties
- **Computational Content**: Proofs carry algorithmic information
- **Normalization**: Strong normalization for consistency

## Historical Development

- **de Bruijn (1968)**: Automath system with dependent types
- **Martin-Löf (1975)**: Intuitionistic type theory
- **Constable et al. (1986)**: NuPRL proof development system
- **Coquand-Huet (1985)**: Calculus of Constructions
- **Dybjer (1990s)**: Inductive families and pattern matching
- **Brady (2013)**: Idris practical dependent programming

## Examples and Applications

### Length-Indexed Vectors
```
Vec : Nat → Type → Type

nil : ∀A. Vec 0 A
cons : ∀A. ∀n. A → Vec n A → Vec (succ n) A

append : ∀A. ∀n. ∀m. Vec n A → Vec m A → Vec (n + m) A
append nil ys = ys
append (cons x xs) ys = cons x (append xs ys)

-- Type ensures length correctness at compile time
```

### Matrix Operations with Dimension Safety
```
Matrix : Nat → Nat → Type → Type

mult : ∀A. ∀n. ∀m. ∀p. Matrix n m A → Matrix m p A → Matrix n p A
-- Type prevents dimension mismatches in matrix multiplication
```

### Sorted Lists
```
Sorted : List Nat → Type
Sorted nil = Unit
Sorted (cons x nil) = Unit
Sorted (cons x (cons y ys)) = (x ≤ y) × Sorted (cons y ys)

insert : ∀xs. Nat → List Nat → Sorted xs →
         Σ ys:List Nat. Sorted ys
-- Insertion preserves sortedness
```

### Database Schemas
```
Schema : Type
Record : Schema → Type

Person : Schema
Person = [("name", String), ("age", Nat), ("email", String)]

john : Record Person
john = [("name", "John"), ("age", 30), ("email", "john@example.com")]

-- Type ensures records match schema structure
```

## Advanced Features

### Equality Types
```
Eq : ∀A:Type. A → A → Type

refl : ∀A. ∀x:A. Eq A x x

subst : ∀A. ∀P:A→Type. ∀x,y:A. Eq A x y → P x → P y
-- Leibniz equality with substitution principle
```

### Quotient Types
```
Quotient : ∀A:Type. (A → A → Type) → Type
-- Types with custom equality relations

Rational = Quotient (Int × Int) (λ(a,b) (c,d). a*d = b*c)
-- Rational numbers as equivalence classes
```

### Inductive Families
```
-- Well-typed expressions parameterized by result type
Expr : Type → Type where
  Val : ∀A. A → Expr A
  Add : Expr Nat → Expr Nat → Expr Nat
  If  : ∀A. Expr Bool → Expr A → Expr A → Expr A

eval : ∀A. Expr A → A
eval (Val x) = x
eval (Add e1 e2) = eval e1 + eval e2
eval (If c t e) = if eval c then eval t else eval e
```

## Type Theory Foundations

### Universe Hierarchies
```
Type₀ : Type₁
Type₁ : Type₂
...
Typeᵢ : Typeᵢ₊₁

-- Prevents Russell's paradox while maintaining expressiveness
```

### Computational vs Propositional
```
-- Computational equality (definitional)
2 + 2 ≡ 4    -- Reduces by computation

-- Propositional equality (by proof)
commutative : ∀x,y. x + y = y + x
-- Requires proof, doesn't reduce automatically
```

### Pattern Matching and Elimination
```
case : ∀P:Nat→Type. P 0 → (∀n. P n → P (succ n)) → ∀n. P n
-- Structural recursion with dependent return type
```

## Programming with Dependent Types

### Verification Workflow
1. **Specify**: Write precise types expressing desired properties
2. **Implement**: Write programs satisfying the specifications
3. **Verify**: Type checker confirms correctness automatically
4. **Extract**: Obtain verified executable code

### Example: Verified Quicksort
```
quicksort : ∀xs:List Nat. Σ ys:List Nat.
           (Sorted ys × Permutation xs ys)
quicksort [] = ([], (sorted_nil, perm_nil))
quicksort (x::xs) =
  let (smaller, pf1) = filter (≤ x) xs in
  let (larger, pf2) = filter (> x) xs in
  let (sorted_smaller, pf3) = quicksort smaller in
  let (sorted_larger, pf4) = quicksort larger in
  (sorted_smaller ++ [x] ++ sorted_larger,
   combine_proofs pf1 pf2 pf3 pf4)
```

## Challenges and Solutions

### Type Inference
- **Problem**: Dependent types make inference undecidable
- **Solutions**:
  - Bidirectional type checking
  - Type annotations and holes
  - Constraint solving
  - Unification modulo theories

### Proof Burden
- **Problem**: Complex proofs required for simple programs
- **Solutions**:
  - Proof automation and tactics
  - Reflection and proof by computation
  - Standard library of common proofs
  - Proof irrelevance for computational parts

### Performance
- **Problem**: Proof terms increase runtime overhead
- **Solutions**:
  - Proof erasure during compilation
  - Separate computational and logical content
  - Optimizations for proof-irrelevant code

## Implementation Strategies

### Elaboration
```
Surface Language → Core Language
∀n. Vec n Nat → Π n:Nat. Vec n Nat
-- Elaborate implicit arguments and syntactic sugar
```

### Type Checking Algorithm
```
Algorithm: Bidirectional Type Checking
check(Γ, e, A):   -- Check e has type A in context Γ
infer(Γ, e):      -- Infer type of e in context Γ
equal(A, B):      -- Check definitional equality of types A and B
```

### Proof Erasure
```
Runtime Code = erase_proofs(Verified_Code)
-- Remove proof terms, keep computational content
```

## Applications

### Verified Systems Programming
- Operating system kernels with memory safety
- Network protocol implementations
- Cryptographic algorithm verification

### Mathematical Formalization
- Formal proofs of mathematical theorems
- Computer-checked mathematics
- Educational proof assistants

### Language Design
- Type-safe embedded domain-specific languages
- Safe API design with rich specifications
- Protocol verification and generation

### Scientific Computing
- Correct-by-construction numerical algorithms
- Dimension analysis in physical simulations
- Verified machine learning implementations

## Tools and Languages

### Practical Languages
- **Agda**: Pure functional with dependent types
- **Idris**: Practical programming with dependent types
- **Coq**: Proof assistant with extraction
- **Lean**: Modern theorem prover with tactics

### Research Systems
- **Twelf**: Logical framework for metatheory
- **Dafny**: Verification-aware imperative language
- **F\***: Functional programming aimed at program verification
- **Liquid Haskell**: Refinement types for Haskell

## Resources

- **Papers**: See [papers/bibliography.md](/papers/bibliography.md) for foundational dependent type research
- **Implementations**: Dependent type checkers and proof assistants
- **Tutorials**: Programming with dependent types and verification
- **Examples**: Verified algorithms and data structures

## Related Systems

- [Martin-Löf Type Theory](/../05-martin-lof-type-theory/) - Constructive foundation
- [Calculus of Constructions](/../04-calculus-of-constructions/) - Impredicative variant
- [Pure Type Systems](/../12-pure-type-systems/) - General framework
- [Refinement Types](/../20-refinement-types/) - Lightweight verification approach

---

*Dependent Types enable precise specification and verification of program properties, bridging the gap between programming and mathematical proof while maintaining computational content.*