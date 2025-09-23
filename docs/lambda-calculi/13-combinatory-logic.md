# Combinatory Logic

A variable-free foundation for computation based on function composition, providing an alternative to lambda calculus through combinatorial completeness and offering insights into the nature of computation and logic.

## Overview

Combinatory Logic provides:
- **Variable-Free Computation**: No variable binding or substitution
- **Combinatorial Completeness**: Every computable function expressible
- **Foundational Alternative**: Different perspective on computation theory
- **Historical Significance**: Predates lambda calculus as computation model
- **Practical Applications**: Implementation strategies and optimization techniques

## Basic Combinators

### Fundamental Combinators

#### S-Combinator (Substitution)
```
S : (A → B → C) → (A → B) → A → C
S x y z = x z (y z)

-- Distributes application over two arguments
-- S f g x applies f to x and (g x)
```

#### K-Combinator (Constant)
```
K : A → B → A
K x y = x

-- Returns first argument, ignoring second
-- Represents constant functions
```

#### I-Combinator (Identity)
```
I : A → A
I x = x

-- Identity function
-- Note: I can be derived as S K K
```

### Combinatorial Completeness

The S and K combinators alone are sufficient to express any computable function:

#### Theorem (S-K Completeness)
Every lambda term can be translated to a combination of S and K combinators.

#### Translation Algorithm
```
T[x] = x                                    -- Variable
T[M N] = T[M] T[N]                         -- Application
T[λx.M] = abstract(x, T[M])                -- Abstraction

where abstract(x, M) is defined as:
abstract(x, x) = I
abstract(x, M) = K M                       (if x ∉ FV(M))
abstract(x, M N) = S (abstract(x, M)) (abstract(x, N))
```

#### Example Translation
```
λx.λy.x  ≡  λx.(λy.x)
         ≡  abstract(x, abstract(y, x))
         ≡  abstract(x, K x)
         ≡  S (abstract(x, K)) (abstract(x, x))
         ≡  S (K K) I
         ≡  S (K K) (S K K)
```

## Extended Combinator Sets

### B-C-K-W System
More natural combinators for many translations:

#### B-Combinator (Composition)
```
B : (B → C) → (A → B) → A → C
B f g x = f (g x)

-- Function composition
-- B ≡ S (K S) K
```

#### C-Combinator (Flip)
```
C : (A → B → C) → B → A → C
C f x y = f y x

-- Argument permutation
-- C ≡ S (S (K (S (K S) K)) S) (K K)
```

#### W-Combinator (Duplication)
```
W : (A → A → B) → A → B
W f x = f x x

-- Argument duplication
-- W ≡ S S (S K)
```

### Practical Combinators

#### Y-Combinator (Fixed Point)
```
Y : (A → A) → A
Y f = f (Y f)

-- Fixed-point combinator for recursion
-- Y ≡ S (K (S I I)) (S (S (K S) K) (K (S I I)))
```

#### Θ-Combinator (Turing's Fixed Point)
```
Θ : (A → A) → A
Θ = (λx.λf.f (x x f)) (λx.λf.f (x x f))

-- Alternative fixed-point combinator
```

## Computational Examples

### Church Numerals in Combinatory Logic
```
-- Church numerals
0 = K I = K (S K K)
1 = I = S K K
2 = S B (S K K) = S (S (K S) K) (S K K)
3 = S B 2 = ...

-- Successor function
SUCC = S B (S K K)
-- where B is composition combinator

-- Addition
ADD = S (S (K S) K)
```

### Boolean Logic
```
-- Boolean values
TRUE = K = λx.λy.x
FALSE = K I = λx.λy.y = S K

-- Boolean operations
AND = S S (K K) = λx.λy.x y FALSE
OR = S I (K TRUE) = λx.λy.x TRUE y
NOT = S (S I (K FALSE)) (K TRUE) = λx.x FALSE TRUE
```

### List Operations
```
-- Pair construction and projection
PAIR = S (S K (S (K K) I)) (K I)
FIRST = S K K = I
SECOND = S K (K I)

-- List operations using pairs
NIL = K
CONS = PAIR
HEAD = FIRST
TAIL = SECOND
NULL? = S (K FALSE) (K TRUE)
```

## Advanced Combinatorial Systems

### Illative Combinatory Logic
Extension with types and logical operators:

```
Type Combinators:
∈ : A → Type → Prop               -- Membership
⊆ : Type → Type → Prop            -- Subtyping
∀ : (A → Prop) → Prop             -- Universal quantification
∃ : (A → Prop) → Prop             -- Existential quantification

Logical Combinators:
⊃ : Prop → Prop → Prop            -- Implication
∧ : Prop → Prop → Prop            -- Conjunction
∨ : Prop → Prop → Prop            -- Disjunction
¬ : Prop → Prop                   -- Negation
```

### Categorical Combinators
Combinators corresponding to categorical operations:

```
-- Cartesian closed category combinators
eval : (A → B) × A → B
curry : (A × B → C) → (A → B → C)
uncurry : (A → B → C) → (A × B → C)

-- Product and coproduct combinators
fst : A × B → A
snd : A × B → B
inl : A → A + B
inr : B → A + B
```

## Reduction Strategies

### Weak Reduction
```
-- Only reduce at the root
(S f g) x →w f x (g x)
(K x) y →w x

-- Weak normal form exists for all combinatorial terms
```

### Strong Reduction
```
-- Reduce anywhere in the term
S (K x) y z →s K x z (y z) →s x (y z)

-- Not all terms have strong normal form
```

### Optimal Reduction
```
-- Share common subexpressions
-- Corresponds to graph reduction
-- Achieves optimal asymptotic complexity
```

## Implementation Techniques

### Graph Reduction
```
-- Represent combinatorial terms as graphs
data Node = App Node Node | Combinator Comb | Variable Var

-- Reduction as graph rewriting
reduce_graph : Graph → Graph
reduce_graph graph =
  case find_redex(graph) of
    Some(S, f, g, x) → rewrite(graph, f x (g x))
    Some(K, x, y) → rewrite(graph, x)
    None → graph
```

### Abstract Machine
```
-- Stack-based combinator machine
data Instruction = Push Combinator | Apply
data State = State { stack :: [Value], code :: [Instruction] }

execute : State → State
execute (State (f:x:stack) [Apply]) =
  State (apply_combinator(f, x):stack) []
execute (State stack (Push c:code)) =
  State (c:stack) code
```

### Compilation to Combinators
```
-- Compile lambda terms to combinators
compile : LambdaTerm → CombinatorTerm
compile (Var x) = x
compile (App f x) = App (compile f) (compile x)
compile (Lam x body) = abstract x (compile body)

-- Bracket abstraction algorithm
abstract : Variable → CombinatorTerm → CombinatorTerm
abstract x x = I
abstract x t = K t  (if x ∉ free_vars(t))
abstract x (App u v) = App (App S (abstract x u)) (abstract x v)
```

## Theoretical Properties

### Church-Rosser Property
```
-- Combinatory logic satisfies confluence
∀M. M →* N₁ ∧ M →* N₂ ⟹ ∃P. N₁ →* P ∧ N₂ →* P
```

### Standardization
```
-- Standard reduction sequences exist
standard : Term → [ReductionStep]
standard term = leftmost_outermost_reduction(term)
```

### Complexity Analysis
```
-- Complexity of combinator reduction
optimal_reduction_complexity : Term → Nat
worst_case_complexity : Term → Nat

-- Exponential blowup possible with naive reduction
-- Optimal reduction achieves better bounds
```

## Relation to Lambda Calculus

### Correspondence Theorem
```
-- Bijection between lambda terms and combinatory terms
to_combinators : LambdaTerm → CombinatorTerm
to_lambda : CombinatorTerm → LambdaTerm

-- Preservation of reduction
M →β N ⟺ to_combinators(M) →c to_combinators(N)
```

### Advantages of Combinators
- No variable binding complications
- Simpler substitution-free reduction
- Direct implementation on hardware
- Clear separation of logic and variables

### Advantages of Lambda Calculus
- More natural for human reasoning
- Direct correspondence to mathematical functions
- Easier type system integration
- Better abstraction mechanisms

## Applications

### Programming Language Implementation
```
-- Functional language compilation target
compile_to_combinators : FunctionalProgram → CombinatorCode
-- Lazy evaluation via graph reduction
-- Memory management through reference counting
```

### Hardware Implementation
```
-- Direct implementation in silicon
-- Combinator reduction engines
-- Parallel combinator machines
-- FPGA implementations
```

### Automated Theorem Proving
```
-- Resolution-based theorem proving
-- Combinatory logic as proof system
-- Automated proof search
-- Proof verification
```

### Compiler Optimization
```
-- Intermediate representation
-- Dead code elimination
-- Common subexpression elimination
-- Loop optimization
```

## Historical Development

### Timeline
- **Schönfinkel (1924)**: Invented combinatory logic
- **Curry (1930)**: Developed theory further
- **Church (1936)**: Lambda calculus as alternative
- **Turner (1979)**: SASL implementation using combinators
- **Hughes (1982)**: Super-combinators for efficiency
- **Peyton Jones (1987)**: Graph reduction techniques

### Influence on Computer Science
- Foundation for functional programming
- Graph reduction implementation techniques
- Understanding of computation without variables
- Insights into the nature of abstraction

## Modern Developments

### Super-combinators
```
-- Optimized combinators for specific patterns
super_comb : [Variable] → CombinatorTerm → SuperCombinator
-- Reduce interpretation overhead
-- Better memory locality
-- Specialized reduction rules
```

### Interaction Nets
```
-- Graphical representation of combinators
-- Parallel reduction strategies
-- Optimal sharing of computations
-- Connection to linear logic
```

### Categorical Semantics
```
-- Combinators as morphisms in cartesian closed categories
-- Categorical compilation techniques
-- Connection to type theory
-- Higher-order categorical structures
```

## Variants and Extensions

### Linear Combinatory Logic
```
-- Resource-aware combinators
L : A ⊸ (A ⊸ B) ⊸ B    -- Linear application
D : A ⊸ A ⊗ A           -- Duplication (controlled)
W : A ⊸ 1               -- Weakening (controlled)
```

### Modal Combinatory Logic
```
-- Modal operators as combinators
□ : A → □A              -- Necessity
◇ : A → ◇A              -- Possibility
-- Distributed computing applications
```

### Quantum Combinatory Logic
```
-- Quantum combinators
H : Qubit → Qubit       -- Hadamard
CNOT : Qubit → Qubit → Qubit ⊗ Qubit
-- Quantum circuit compilation
```

## Implementation Examples

### Simple Combinator Interpreter
```haskell
data Combinator = S | K | I | B | C | W
data Term = Comb Combinator | App Term Term

reduce :: Term → Term
reduce (App (App (App (Comb S) f) g) x) =
  App (App f x) (App g x)
reduce (App (App (Comb K) x) y) = x
reduce (App (Comb I) x) = x
reduce (App f x) = App (reduce f) (reduce x)
reduce t = t
```

### Graph Reduction Engine
```c
typedef struct node {
  enum { APP, COMB } tag;
  union {
    struct { struct node *fun, *arg; } app;
    combinator_t comb;
  };
} node_t;

node_t* reduce(node_t* term) {
  // Implement graph reduction with sharing
  // Handle cycles and memory management
  // Optimize common patterns
}
```

## Performance Considerations

### Reduction Strategies
- **Call-by-need**: Lazy evaluation with sharing
- **Call-by-value**: Strict evaluation order
- **Optimal reduction**: Sharing all common subexpressions

### Memory Management
- **Reference counting**: Simple but handles cycles poorly
- **Garbage collection**: Better for complex sharing patterns
- **Linear types**: Static memory management

### Optimization Techniques
- **Super-combinators**: Reduce interpretation overhead
- **Strictness analysis**: Identify eager evaluation opportunities
- **Fusion**: Eliminate intermediate data structures

## Tools and Systems

### Historical Systems
- **SASL**: Early functional language using combinators
- **Miranda**: Lazy functional language
- **Orwell**: Combinator-based implementation

### Modern Tools
- **GHC**: Haskell compiler with combinator techniques
- **Clean**: Functional language with graph reduction
- **Interaction Nets**: Optimal reduction implementations

### Research Tools
- **Combinatory Logic Workbench**: Interactive theorem proving
- **Graph Reduction Simulators**: Performance analysis
- **Optimal Lambda Machines**: Research implementations

## Resources

- **Papers**: See [papers/bibliography.md](../../13-combinatory-logic/papers/bibliography.md) for combinatory logic foundations
- **Implementations**: Combinator interpreters and compilers
- **Tutorials**: Variable-free programming and reduction techniques
- **Historical**: Development from Schönfinkel to modern applications

## Related Systems

- [Untyped Lambda Calculus](/../01-untyped-lambda-calculus/) - Alternative computational foundation
- [Simply Typed Lambda Calculus](/../02-simply-typed-lambda-calculus/) - Typed variant comparison
- [Linear Lambda Calculus](/../06-linear-lambda-calculus/) - Resource-aware alternatives
- [Pure Type Systems](/../12-pure-type-systems/) - Type system frameworks

---

*Combinatory Logic provides a variable-free foundation for computation that offers unique insights into the nature of abstraction and function application, while serving as a practical compilation target for functional programming languages.*