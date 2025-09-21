# Union Types Research

This directory contains comprehensive research materials on union types in type theory and programming languages.

## Contents

### [Bibliography](bibliography.md)
Comprehensive academic bibliography covering:
- **Historical Development**: Early foundations from Hoare's discriminators to modern systems
- **Typed Assembly Language**: Union types in low-level programming contexts
- **Gradual Typing**: Integration with dynamic-static typing systems
- **Flow-Sensitive Systems**: Occurrence typing and type refinement
- **Pattern Matching**: Algebraic data types and exhaustive analysis
- **Modern Implementations**: TypeScript, Flow, Rust, Scala 3

### [Implementations](implementations.md)
Catalog of source code implementations including:
- **Production Languages**: TypeScript, Flow, Rust enums, Scala 3, OCaml variants
- **Research Prototypes**: Typed Racket, Whiley, gradual typing systems
- **Academic Implementations**: Research type checkers, verification systems
- **Language Libraries**: Runtime validation, functional programming abstractions
- **Development Tools**: IDEs, build systems, testing frameworks

## Key Theoretical Properties

1. **Flow-Sensitive Typing**: Type refinement through control flow analysis
2. **Occurrence Typing**: Revolutionary approach enabling practical union types
3. **Pattern Matching**: Exhaustive case analysis and completeness checking
4. **Gradual Integration**: Sound interoperability between typed and untyped code

## Practical Applications

1. **Error Handling**: `Result<T, E>` types, optional values
2. **State Machines**: Finite state representation with type safety
3. **API Design**: Flexible parameter and return types
4. **Data Modeling**: Discriminated unions, variant types

## Research Directions

- **Performance**: Efficient union type checking and inference
- **Advanced Inference**: Principal typing for complex union systems
- **Verification**: Union type correctness and safety proofs
- **Concurrent Systems**: Union types in session types and concurrent calculi

## Implementation Strategies

1. **Tagged Unions**: Runtime type discrimination (Rust enums)
2. **Flow-Sensitive Analysis**: Type refinement through control flow (TypeScript, Flow)
3. **Pattern Matching**: Exhaustive case analysis (functional languages)
4. **Type Guards**: Runtime type checking integration (TypeScript)

## Historical Timeline

- **1965**: Hoare introduces "record class discriminators"
- **1974**: Reynolds formalizes union types in type structure theory
- **1988**: Typed assembly language applications
- **2006-2007**: Gradual typing foundations (Siek, Taha)
- **2008**: Tobin-Hochstadt introduces occurrence typing in Typed Scheme
- **2012**: TypeScript brings union types to mainstream JavaScript
- **2015**: Rust 1.0 with algebraic data types as tagged unions
- **2021**: Scala 3 introduces native union type support

## Language Comparison

| Language | Union Syntax | Key Features | Status |
|----------|--------------|--------------|---------|
| TypeScript | `A \| B` | Discriminated unions, type guards | Production |
| Flow | `A \| B` | Flow-sensitive refinement | Production |
| Rust | `enum` | Zero-cost tagged unions | Production |
| Scala 3 | `A \| B` | DOT calculus based | Production |
| OCaml | Polymorphic variants | Row polymorphism | Production |
| Haskell | ADTs | Algebraic data types | Production |

*Part of the Lambda Calculus Research Repository*