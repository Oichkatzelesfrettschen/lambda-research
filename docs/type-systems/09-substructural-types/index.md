# Substructural Types

Type systems based on substructural logics that restrict or control the structural rules of weakening, contraction, and exchange, enabling fine-grained resource management and novel computational interpretations.

## Overview

Substructural Types encompass:
- **Linear Types**: Resources used exactly once (no weakening or contraction)
- **Affine Types**: Resources used at most once (weakening but no contraction)
- **Relevant Types**: Resources used at least once (contraction but no weakening)
- **Ordered Types**: Resources used in order (no exchange)
- **Mixed Systems**: Combining multiple substructural disciplines

## Structural Rules and Their Restrictions

### Classical Structural Rules
In classical logic and standard type systems:

```
Weakening:     Γ ⊢ M : A
              ─────────────
              Γ, x:B ⊢ M : A

Contraction:   Γ, x:A, y:A ⊢ M : B
              ─────────────────────
              Γ, z:A ⊢ M[z/x][z/y] : B

Exchange:      Γ, x:A, y:B, Δ ⊢ M : C
              ─────────────────────────
              Γ, y:B, x:A, Δ ⊢ M : C
```

### Substructural Restrictions

| Logic Type | Weakening | Contraction | Exchange | Interpretation |
|------------|-----------|-------------|----------|----------------|
| Classical  | ✓         | ✓           | ✓        | Unlimited use  |
| Linear     | ✗         | ✗           | ✓        | Exactly once   |
| Affine     | ✓         | ✗           | ✓        | At most once   |
| Relevant   | ✗         | ✓           | ✓        | At least once  |
| Ordered    | ✗         | ✗           | ✗        | Ordered use    |

## Linear Types (No Weakening, No Contraction)

### Type System
```
Types: A, B ::= α | A ⊸ B | A ⊗ B | A ⊕ B | A & B | !A | 1 | 0

Contexts: Γ, Δ ::= ∅ | Γ, x:A

Typing: Γ ⊢ M : A where each variable in Γ used exactly once
```

### Key Connectives
```
Linear Implication (⊸):
Γ, x:A ⊢ M : B
─────────────────    (⊸-Intro)
Γ ⊢ λx.M : A ⊸ B

Multiplicative Conjunction (⊗):
Γ₁ ⊢ M : A    Γ₂ ⊢ N : B
─────────────────────────    (⊗-Intro)
Γ₁, Γ₂ ⊢ ⟨M,N⟩ : A ⊗ B

Exponential (!):
Δ ⊢ M : A
─────────────    (!-Intro, where all variables in Δ marked with !)
Δ ⊢ !M : !A
```

## Affine Types (Weakening, No Contraction)

### Characteristics
- Variables can be **discarded** (weakening allowed)
- Variables **cannot be duplicated** (no contraction)
- Useful for **resource cleanup** without strict usage requirements

### Example: Affine File Handling
```
File : Affine Type
read : File ⊸ Data ⊗ File
close : File ⊸ 1

-- Can discard file without closing (weakening)
-- But cannot duplicate file handle (no contraction)
safe_read : File ⊸ Data
safe_read f = let ⟨d, f'⟩ = read f in d  -- f' discarded safely
```

## Relevant Types (No Weakening, Contraction)

### Characteristics
- Variables **must be used** (no weakening)
- Variables **can be duplicated** (contraction allowed)
- Ensures **all inputs are considered**

### Example: Relevant Security Types
```
Secret : Relevant Type
use_secret : Secret → Secret → Result

-- All secrets must be used (no discarding)
-- But secrets can be duplicated for multiple uses
process_secrets : Secret ⊸ Secret ⊸ Result
process_secrets s1 s2 = use_secret s1 s1  -- s1 duplicated, s2 unused: ERROR
```

## Ordered Types (No Weakening, No Contraction, No Exchange)

### Characteristics
- Variables used **exactly once** in **specific order**
- Models **sequential processing** and **protocol adherence**
- Useful for **hardware interfaces** and **lock ordering**

### Example: Lock Ordering
```
Lock : Nat → Ordered Type  -- Locks with priority levels

acquire : Lock n → Computation (Lock n)
release : Lock n → Computation 1

-- Must acquire and release locks in priority order
deadlock_free : Lock 1 ⊸ Lock 2 ⊸ Computation 1
deadlock_free l1 l2 =
  do l1' ← acquire l1      -- Must acquire lower priority first
     l2' ← acquire l2      -- Then higher priority
     release l2'           -- Release in reverse order
     release l1'
```

## Mixed Substructural Systems

### Bunched Types
Combination of additive (classical) and multiplicative (linear) contexts:

```
Γ; Δ ⊢ M : A
where Γ allows weakening/contraction, Δ is linear

Additive Implication:
Γ, x:A; Δ ⊢ M : B
─────────────────────    (→-Intro)
Γ; Δ ⊢ λx.M : A → B

Multiplicative Implication:
Γ; Δ, x:A ⊢ M : B
─────────────────────    (⊸-Intro)
Γ; Δ ⊢ λx.M : A ⊸ B
```

### Coeffect Systems
Types annotated with resource usage information:

```
A<span>@</span>r where r tracks resource usage

x:A<span>@</span>1, y:B<span>@</span>1 ⊢ ⟨x,y⟩ : (A ⊗ B)<span>@</span>1    -- Each resource used once
x:A<span>@</span>2 ⊢ ⟨x,x⟩ : (A ⊗ A)<span>@</span>2            -- Resource used twice
```

## Applications and Examples

### Memory Management
```
-- Affine types for safe memory management
Ptr : Type → Affine Type
malloc : Size → Ptr A
free : Ptr A ⊸ 1
deref : Ptr A ⊸ A ⊗ Ptr A

-- Use-after-free prevented by type system
safe_malloc : Size → A → 1
safe_malloc size value =
  let ptr = malloc size in
  let ⟨_, ptr'⟩ = deref ptr in
  free ptr'  -- ptr cannot be used again
```

### Protocol Verification
```
-- Ordered types for network protocol states
Protocol : State → Ordered Type

handshake : Protocol Initial ⊸ Protocol Connected
send_data : Protocol Connected ⊸ Data ⊸ Protocol Connected
disconnect : Protocol Connected ⊸ Protocol Closed

-- Protocol must follow exact sequence
correct_session : Protocol Initial ⊸ Data ⊸ Protocol Closed
correct_session p data =
  let p' = handshake p in      -- Must handshake first
  let p'' = send_data p' data in   -- Then send data
  disconnect p''               -- Finally disconnect
```

### Concurrent Programming
```
-- Linear types for channel communication
Channel : Type → Linear Type
send : Channel A ⊸ A ⊸ 1
recv : Channel A ⊸ A

-- Prevents double-send or double-receive
one_shot_channel : A → A
one_shot_channel value =
  let ch = new_channel in
  let _ = send ch value in  -- Channel consumed
  recv ch                  -- Error: ch already used
```

## Advanced Features

### Polymorphic Substructural Types
```
∀ρ. A@ρ  -- Polymorphic over resource annotations
id : ∀A. ∀ρ. A@ρ → A@ρ
```

### Subtyping Relations
```
Linear <: Affine <: Unrestricted
A<span>@</span>1 <: A<span>@</span>*  -- Linear resources can be used unrestrictedly
```

### Effect Systems Integration
```
Computation : Effect → Type → Type
pure : A → Computation ∅ A
linear_op : A ⊸ Computation {linear} B
```

## Theoretical Foundations

### Categorical Semantics
- **Symmetric Monoidal Categories**: Model multiplicative structure
- **Cartesian Categories**: Model additive structure
- **Linear Categories**: Combine both structures appropriately

### Proof Theory Correspondence
```
Substructural Logic ↔ Resource-Aware Computation
Cut Elimination ↔ Normalization
Proof Nets ↔ Computation Graphs
```

### Game Semantics
- **Linear Games**: Players have limited resources
- **Strategies**: Resource-conscious winning conditions
- **Composition**: Resource tracking through game composition

## Implementation Considerations

### Type Checking Algorithms
```
Algorithm: Substructural Type Checking
Input: Context Γ, Term M, Type A, Structural Rules S
Output: Success/Failure + Resource usage tracking

check_substructural(Γ, M, A, S):
  case M of
    x → if x:B ∈ Γ and B <: A then (Γ \ {x:B}, Success)
        else Failure
    λx.N → check_function(Γ, x, N, A, S)
    M N → check_application(Γ, M, N, A, S)
```

### Runtime Systems
- **Reference Counting**: Track linear resource usage
- **Ownership Transfer**: Move semantics for affine types
- **Protocol Monitoring**: Runtime verification of ordered usage

### Optimization Opportunities
- **In-Place Updates**: Safe for linear data
- **Parallel Execution**: Disjoint resource usage
- **Memory Reuse**: Immediate deallocation for affine types

## Research Directions

### Gradual Substructural Typing
```
-- Mixing typed and untyped code
A<span>@</span>? -- Unknown resource annotation
cast : A<span>@</span>r → A<span>@</span>s  -- Runtime check for resource compatibility
```

### Dependent Substructural Types
```
Vec : Nat → Type → Resource → Type
append : ∀n m. Vec n A<span>@</span>r → Vec m A<span>@</span>r → Vec (n+m) A<span>@</span>r
```

### Quantum Resource Types
```
Qubit : Quantum Type  -- Cannot be cloned or deleted
measure : Qubit ⊸ Bool  -- Measurement consumes qubit
```

## Tools and Languages

### Languages with Substructural Types
- **Rust**: Ownership system (affine types)
- **Clean**: Uniqueness types (linear-like)
- **ATS**: Linear types with theorem proving
- **Granule**: Graded modal types

### Research Implementations
- **Linear/Concurrent ML**: Academic language experiments
- **Vault**: Adoption and focus for systems programming
- **Cyclone**: Safe C with region types

## Resources

- **Papers**: See [papers/bibliography.md](papers/bibliography.md) for substructural logic foundations
- **Implementations**: Substructural type checkers and compilers
- **Tutorials**: Resource-aware programming examples
- **Applications**: Systems programming and protocol verification

## Related Systems

- [Linear Lambda Calculus](../06-linear-lambda-calculus/index.md) - Pure linear types
- [Session Types](../07-session-types/index.md) - Protocol-specific linear types
- [Quantum Variants](../../advanced/11-quantum-variants/index.md) - Quantum resource management
- [Modal Types](../19-modal-types/index.md) - General modal type theory

---

*Substructural Types provide fine-grained control over resource usage, enabling safe and efficient programming patterns while preventing common errors like memory leaks, use-after-free, and protocol violations.*

## Syntax

TODO: Add Syntax content.


## Properties

TODO: Add Properties content.
