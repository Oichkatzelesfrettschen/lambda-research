# Pure Type Systems

A general framework unifying various typed lambda calculi through a systematic parameterization of axioms and rules, providing the theoretical foundation for the lambda cube and modern dependent type systems.

## Overview

Pure Type Systems (PTS) provide:
- **Unified Framework**: Single formalism capturing multiple type systems
- **Parameterization**: Different systems via different specification parameters
- **Lambda Cube**: Systematic exploration of type system design space
- **Theoretical Foundation**: Common basis for understanding typed lambda calculi
- **Modular Design**: Compositional construction of type system features

## Pure Type System Specification

A Pure Type System is defined by a triple S = (S, A, R) where:

### Sorts (S)
```
S = {*, □, △, ...}  -- Set of sorts (universes)
* : types of data
□ : types of types
△ : types of kinds (if present)
```

### Axioms (A)
```
A ⊆ S × S  -- Axiom set specifying sort hierarchy
Examples:
* : □     -- Types live in the type universe
□ : △     -- Type constructors live in kind universe
```

### Rules (R)
```
R ⊆ S × S × S  -- Product formation rules
(s₁, s₂, s₃) ∈ R means: if A : s₁ and B : s₂ then Π x:A.B : s₃

Examples:
(*, *, *)    -- Dependent functions (Π-types)
(*, □, □)    -- Polymorphic types (System F)
(□, *, *)    -- Type operators
(□, □, □)    -- Higher-order type operators
```

## General Syntax and Typing

### Unified Syntax
```
Terms/Types: T, U, V ::= s | x | λx:T.U | Π x:T.U | T U

Contexts: Γ ::= ∅ | Γ, x:T

Well-formed contexts: ⊢ Γ
Typing judgment: Γ ⊢ T : U
Definitional equality: T ≡ U
```

### Core Typing Rules
```
Axiom:
─────────────                        ((s₁,s₂) ∈ A)
∅ ⊢ s₁ : s₂

Start:
⊢ Γ    Γ ⊢ A : s    x ∉ Γ
─────────────────────────
Γ, x:A ⊢ x : A

Variable:
Γ, x:A, Δ ⊢ x : A    (if ⊢ Γ, x:A, Δ)

Weakening:
Γ ⊢ t : T    Γ ⊢ U : s    x ∉ Γ
─────────────────────────────
Γ, x:U ⊢ t : T

Product:
Γ ⊢ A : s₁    Γ, x:A ⊢ B : s₂
─────────────────────────────         ((s₁,s₂,s₃) ∈ R)
Γ ⊢ Π x:A.B : s₃

Abstraction:
Γ, x:A ⊢ b : B    Γ ⊢ Π x:A.B : s
─────────────────────────────────
Γ ⊢ λx:A.b : Π x:A.B

Application:
Γ ⊢ f : Π x:A.B    Γ ⊢ a : A
─────────────────────────────
Γ ⊢ f a : B[a/x]

Conversion:
Γ ⊢ t : A    Γ ⊢ B : s    A ≡β B
─────────────────────────────
Γ ⊢ t : B
```

## The Lambda Cube

The lambda cube systematically explores type systems by varying the rules:

```
        λC (CoC)
       /│
      / │
   λP₂ ────── λω₂
    /  │      /│
   /   │     / │
  λP ─────── λω (System F-ω)
  │   /      │ /
  │  /       │/
  λ→ ────── λ2 (System F)
   (STLC)
```

### Cube Dimensions
1. **→ to 2**: Add polymorphism (terms depending on types)
2. **→ to P**: Add dependent types (types depending on terms)
3. **→ to ω**: Add type operators (types depending on types)

### Lambda Cube Systems

#### λ→ (Simply Typed Lambda Calculus)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *)}

-- Only simple function types A → B
```

#### λ2 (System F)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *), (□, *, *)}

-- Adds polymorphism: ∀X.A
Example: id : ∀X. X → X
```

#### λP (LF - Logical Framework)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *), (*, □, □)}

-- Adds dependent types: Π x:A. B
Example: Vec : Nat → Type → Type
```

#### λω (System F-ω)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *), (□, *, *), (□, □, □)}

-- Adds type operators: ∀X::K. A
Example: List : Type → Type
```

#### λP2 (LF + Polymorphism)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *), (*, □, □), (□, *, *)}

-- Combines dependent types and polymorphism
```

#### λPω (LF + Type Operators)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *), (*, □, □), (□, □, □)}

-- Dependent types and type operators
```

#### λω₂ (Higher-Order Polymorphism)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *), (□, *, *), (□, □, □)}

-- System F-ω with higher-order polymorphism
```

#### λC (Calculus of Constructions)
```
S = {*, □}
A = {(*, □)}
R = {(*, *, *), (*, □, □), (□, *, *), (□, □, □)}

-- All three dimensions: full expressiveness
```

## Extended Pure Type Systems

### Multiple Universes
```
S = {*₀, *₁, *₂, ..., □₀, □₁, □₂, ...}
A = {(*₀, □₀), (*₁, □₁), ..., (□₀, □₁), (□₁, □₂), ...}

-- Universe hierarchy to avoid paradoxes
Type₀ : Type₁ : Type₂ : ...
```

### Inductive Types Extension
```
-- Add inductive type formation rules
Inductive: Γ ⊢ I : s    Γ ⊢ constructors : I
──────────────────────────────────────────
Γ ⊢ data I constructors : s

-- Example: Natural numbers
data Nat : * where
  zero : Nat
  succ : Nat → Nat
```

### Cumulative Universes
```
-- Cumulativity rules
Γ ⊢ A : *ᵢ
─────────────  (i < j)
Γ ⊢ A : *ⱼ

-- Types can live in higher universes
```

## Properties and Metatheory

### Fundamental Properties
- **Uniqueness of Types**: Each term has at most one type (up to conversion)
- **Subject Reduction**: Types preserved under β-reduction
- **Strong Normalization**: All well-typed terms terminate (for valid PTS)
- **Church-Rosser**: Confluence of β-reduction
- **Decidability**: Type checking is decidable

### Consistency Conditions
A PTS is consistent if:
1. **Axiom condition**: Axioms form a functional relation
2. **Rule condition**: Rules satisfy certain closure properties
3. **No circularity**: Sort hierarchy has no cycles

### Expressiveness Hierarchy
```
λ→ ⊂ λ2 ⊂ λω₂
λ→ ⊂ λP ⊂ λPω ⊂ λC
λ→ ⊂ λω ⊂ λωω
```

## Examples in Different Systems

### Natural Numbers Across Systems

#### In λ→ (STLC)
```
Nat : *
zero : Nat
succ : Nat → Nat
```

#### In λ2 (System F)
```
Nat : *
Nat = ∀X. (X → X) → X → X
zero : Nat = ΛX. λf. λx. x
succ : Nat → Nat = λn. ΛX. λf. λx. f (n X f x)
```

#### In λP (LF)
```
Nat : *
zero : Nat
succ : Nat → Nat
ind : Π P:(Nat → *). P zero → (Π n:Nat. P n → P (succ n)) → Π n:Nat. P n
```

#### In λC (CoC)
```
Nat : *
Nat = Π X:*. (X → X) → X → X  -- Church encoding in CoC
-- Or as inductive type with elimination principle
```

### Vector Types

#### In λP (Dependent Types)
```
Vec : Nat → * → *
nil : Π A:*. Vec zero A
cons : Π A:*. Π n:Nat. A → Vec n A → Vec (succ n) A
```

#### In λC (Full Power)
```
Vec : Π n:Nat. * → *
append : Π A:*. Π n:Nat. Π m:Nat.
         Vec n A → Vec m A → Vec (plus n m) A
```

## Advanced Features

### Subtyping in PTS
```
-- Subtyping rules for PTS
Γ ⊢ A <: B    Γ ⊢ t : A
─────────────────────────  (Subsumption)
Γ ⊢ t : B

-- Universe subtyping
*ᵢ <: *ⱼ  (if i ≤ j)
```

### Equality Types
```
-- Propositional equality in PTS
Eq : Π A:*. A → A → *
refl : Π A:*. Π x:A. Eq A x x
subst : Π A:*. Π P:(A → *). Π x,y:A. Eq A x y → P x → P y
```

### Module Systems
```
-- Module signatures as types
Signature = Π X:*. X → * → *
Implementation : Signature → *
```

## Implementation Strategies

### Type Checking Algorithm
```
Algorithm: PTS Type Checking
Input: PTS specification (S,A,R), context Γ, term M, type A
Output: Success/Failure

typecheck(Γ, M, A):
  case M of
    s → check_axiom(s, A)
    x → check_variable(Γ, x, A)
    λx:B.N → check_abstraction(Γ, x, B, N, A)
    Π x:B.C → check_product(Γ, x, B, C, A)
    M N → check_application(Γ, M, N, A)
```

### Elaboration and Inference
```
-- Elaborate surface syntax to core PTS
elaborate : SurfaceTerm → CoreTerm
infer_type : Context → CoreTerm → Type
check_type : Context → CoreTerm → Type → Bool
```

### Normalization
```
-- β-reduction to normal form
normalize : Term → Term
weak_head_normalize : Term → Term
conversion_check : Term → Term → Bool
```

## Applications

### Programming Language Foundations
- Type system design and verification
- Compiler intermediate representations
- Language interoperability frameworks

### Theorem Proving
- Foundation for proof assistants
- Logical framework implementations
- Automated reasoning systems

### Category Theory
- Internal languages of toposes
- Fibrations and dependent types
- Higher-dimensional type theory

## Research Directions

### Higher-Dimensional PTS
```
-- Extend PTS to higher dimensions
HoTTS = (S, A, R, I, E)  -- Add identity types and univalence
```

### Modal PTS
```
-- Add modal operators
□ : * → *  -- Necessity
◇ : * → *  -- Possibility
```

### Linear PTS
```
-- Incorporate linear logic principles
R_linear ⊆ S × S × S  -- Linear product formation rules
```

### Gradual PTS
```
-- Mix static and dynamic typing
? : *  -- Dynamic type
cast : A → ? → B  -- Runtime type conversion
```

## Tools and Implementations

### Proof Assistants Based on PTS
- **Coq**: Calculus of Inductive Constructions
- **Lean**: Modern implementation with extensive automation
- **Agda**: Dependently typed functional programming
- **Twelf**: Logical framework for metatheory

### PTS Implementations
- **Lego**: Early PTS implementation
- **Alfa**: Agda predecessor
- **Yarrow**: Experimental PTS system

### Verification Tools
- **PoplMark Challenge**: Metatheory verification
- **Autosubst**: Substitution automation
- **MetaCoq**: Coq formalization of Coq

## Resources

- **Papers**: See [papers/bibliography.md](/papers/bibliography.md) for PTS foundations
- **Implementations**: PTS type checkers and proof assistants
- **Tutorials**: Type system design using PTS framework
- **Metatheory**: Formal verification of PTS properties

## Related Systems

- [System F](/../03-system-f-polymorphic/) - λ2 corner of lambda cube
- [Calculus of Constructions](/../04-calculus-of-constructions/) - λC corner of lambda cube
- [Martin-Löf Type Theory](/../05-martin-lof-type-theory/) - Predicative dependent types
- [Dependent Types](/../08-dependent-types/) - Core concept in PTS framework

---

*Pure Type Systems provide the theoretical foundation for understanding and designing typed lambda calculi, offering a systematic framework that unifies diverse type systems while enabling principled exploration of the design space.*