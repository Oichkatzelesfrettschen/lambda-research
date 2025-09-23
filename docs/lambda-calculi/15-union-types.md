# Union Types Research

This directory contains comprehensive research materials on union types in type theory and programming languages.

## Contents

### [Bibliography](../../15-union-types/papers/bibliography.md)
Comprehensive academic bibliography covering:
- **Historical Development**: Early foundations from Hoare's discriminators to modern systems
- **Typed Assembly Language**: Union types in low-level programming contexts
- **Gradual Typing**: Integration with dynamic-static typing systems
- **Flow-Sensitive Systems**: Occurrence typing and type refinement
- **Pattern Matching**: Algebraic data types and exhaustive analysis
- **Modern Implementations**: TypeScript, Flow, Rust, Scala 3

## Union Types: Implementation Catalog

### Production Language Implementations

#### TypeScript
- **Repository**: https://github.com/microsoft/TypeScript
- **Language**: TypeScript (self-hosting)
- **Union Support**: Full `A | B` syntax with discriminated unions
- **Key Features**:
  - Discriminated unions with literal types
  - Type guards for union narrowing
  - Control flow analysis
  - Exhaustiveness checking
  - Tagged union patterns
- **Type Checker**: Built-in TypeScript compiler (tsc)
- **Performance**: Optimized for large codebases with complex unions
- **Documentation**: https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html

#### Flow
- **Repository**: https://github.com/facebook/flow
- **Language**: OCaml
- **Union Support**: Disjoint unions, refined unions
- **Key Features**:
  - Flow-sensitive union refinement
  - Exact and inexact union types
  - Disjoint union enforcement
  - Pattern matching support
  - Incremental union analysis
- **Type Checker**: Flow static type checker
- **Performance**: Optimized for large JavaScript codebases
- **Documentation**: https://flow.org/en/docs/types/unions/

#### Rust (Enums as Tagged Unions)
- **Repository**: https://github.com/rust-lang/rust
- **Language**: Rust
- **Union Support**: Algebraic data types via `enum`
- **Key Features**:
  - Memory-efficient tagged unions
  - Exhaustive pattern matching
  - Zero-cost abstractions
  - Compile-time safety guarantees
  - Option and Result standard types
- **Type Checker**: rustc compiler
- **Performance**: Zero-cost runtime representation
- **Documentation**: https://doc.rust-lang.org/book/ch06-00-enums-and-pattern-matching.html

#### Scala 3
- **Repository**: https://github.com/lampepfl/dotty
- **Language**: Scala
- **Union Support**: Native `A | B` union types
- **Key Features**:
  - DOT calculus based unions
  - Pattern matching with union types
  - Type-level computation
  - Seamless Java interop
  - Match types for union analysis
- **Type Checker**: Dotty compiler
- **Performance**: Compile-time union resolution
- **Documentation**: https://docs.scala-lang.org/scala3/reference/new-types/union-types.html

#### OCaml (Polymorphic Variants)
- **Repository**: https://github.com/ocaml/ocaml
- **Language**: OCaml
- **Union Support**: Polymorphic variants as flexible unions
- **Key Features**:
  - Row polymorphism
  - Flexible union composition
  - Structural subtyping
  - Pattern matching support
  - No prior declaration required
- **Type Checker**: OCaml compiler
- **Performance**: Efficient runtime representation
- **Documentation**: https://dev.realworldocaml.org/variants.html

#### Haskell (Sum Types)
- **Repository**: https://github.com/ghc/ghc
- **Language**: Haskell
- **Union Support**: Algebraic data types, GADTs
- **Key Features**:
  - Algebraic data type definitions
  - Pattern matching with guards
  - Type family computations
  - GADT extensions
  - Deriving mechanisms
- **Type Checker**: GHC compiler
- **Performance**: Lazy evaluation with efficient representations
- **Documentation**: https://wiki.haskell.org/Algebraic_data_type

### Research Type Checkers and Prototypes

#### Ezno (TypeScript Alternative)
- **Repository**: https://github.com/kaleidawave/ezno
- **Language**: Rust
- **Purpose**: Fast TypeScript type checker with enhanced union support
- **Union Features**:
  - TypeScript-compatible union syntax
  - Advanced union inference
  - Performance optimizations
  - Extended union type analysis
- **Status**: Active development
- **Performance**: Targets superior speed to tsc
- **License**: MIT

#### tyty (Rust-based TypeScript Checker)
- **Language**: Rust
- **Purpose**: High-performance TypeScript type checker
- **Union Features**:
  - Native union type support
  - Rust implementation for speed
  - TypeScript compatibility
- **Status**: Development phase
- **Focus**: Performance optimization

#### Typed Racket
- **Repository**: https://github.com/racket/typed-racket
- **Language**: Racket
- **Union Support**: Occurrence typing with unions
- **Key Features**:
  - Occurrence typing (flow-sensitive)
  - Union refinement through predicates
  - Gradual typing integration
  - Advanced control flow analysis
- **Research Significance**: First practical occurrence typing
- **Performance**: Production-ready Scheme variant
- **Documentation**: https://docs.racket-lang.org/ts-guide/

#### Whiley
- **Repository**: https://github.com/Whiley/WhileyCompiler
- **Language**: Java
- **Union Support**: Native union types with verification
- **Key Features**:
  - Extended static checking
  - Union type verification
  - Automated theorem proving
  - Pre/post condition checking
- **Research Focus**: Verification-oriented programming
- **Status**: Research language implementation

### Academic Research Implementations

#### gradual-intersection-types (Gradual Union Support)
- **Repository**: GitHub topic: intersection-types (includes union work)
- **Language**: Haskell
- **Purpose**: Gradual typing with union and intersection types
- **Features**:
  - Gradual union type inference
  - Dynamic-static interoperability
  - Type soundness preservation
- **Research Focus**: Gradual typing theory
- **Status**: Research prototype

#### transform-json-types
- **Repository**: https://github.com/transform-it/transform-json-types
- **Language**: Multiple target languages
- **Purpose**: Generate union types across languages
- **Features**:
  - TypeScript union generation
  - Flow union types
  - Rust enum generation
  - Scala case class variants
- **Use Case**: Cross-language type generation
- **Status**: Production utility

#### Contracts for Union Types
- **Repository**: Various research implementations
- **Language**: TypeScript, Racket
- **Purpose**: Contract-based union type verification
- **Features**:
  - Runtime union type checking
  - Higher-order contracts
  - Gradual verification
- **Research Focus**: Contract programming
- **Status**: Experimental implementations

### Language-Specific Union Type Libraries

#### TypeScript Ecosystem

##### io-ts
- **Repository**: https://github.com/gcanti/io-ts
- **Purpose**: Runtime type checking for TypeScript
- **Union Features**:
  - Union type validation
  - Runtime type decoding
  - Functional programming approach
- **Status**: Production ready
- **Performance**: Optimized validation

##### zod
- **Repository**: https://github.com/colinhacks/zod
- **Purpose**: TypeScript-first schema declaration and validation
- **Union Features**:
  - Union schema definition
  - Discriminated union support
  - Runtime type safety
- **Status**: Widely adopted
- **Performance**: Efficient validation

##### fp-ts
- **Repository**: https://github.com/gcanti/fp-ts
- **Purpose**: Functional programming for TypeScript
- **Union Features**:
  - Either type (union of success/error)
  - Option type (union with undefined)
  - TaskEither for async unions
- **Status**: Mature library
- **Approach**: Category theory based

#### Rust Ecosystem

##### serde
- **Repository**: https://github.com/serde-rs/serde
- **Purpose**: Serialization framework
- **Union Features**:
  - Enum serialization/deserialization
  - Tagged and untagged variants
  - External tagging strategies
- **Status**: De facto standard
- **Performance**: Zero-cost serialization

##### thiserror
- **Repository**: https://github.com/dtolnay/thiserror
- **Purpose**: Error handling with enums
- **Union Features**:
  - Error enum derivation
  - Custom error union types
  - Display implementation generation
- **Status**: Widely used
- **Integration**: Standard error handling

#### Scala Ecosystem

##### Shapeless
- **Repository**: https://github.com/milessabin/shapeless
- **Purpose**: Generic programming library
- **Union Features**:
  - Coproduct types (union representation)
  - Generic derivation for unions
  - Type-level computation
- **Status**: Mature (Scala 2)
- **Research**: Advanced type-level programming

##### Cats
- **Repository**: https://github.com/typelevel/cats
- **Purpose**: Functional programming abstractions
- **Union Features**:
  - Either type for error handling
  - Validated type for accumulating errors
  - EitherT transformer
- **Status**: Standard Scala FP library
- **Performance**: Optimized abstractions

### Minimal and Educational Implementations

#### Typechecker Zoo
- **Repository**: https://github.com/sdiehl/typechecker-zoo
- **Language**: Rust
- **Purpose**: Educational type checker implementations
- **Union Support**: Foundation for union type extensions
- **Features**:
  - Sum type implementation examples
  - Pattern matching algorithms
  - Type inference foundations
- **Educational Value**: Learning resource
- **License**: MIT

#### Union Type Implementations in Various Languages

##### JavaScript/Node.js
- **Libraries**: Various runtime union checking libraries
- **Features**: Dynamic union validation, type guards
- **Use Case**: Runtime type safety for JavaScript
- **Performance**: Runtime overhead for safety

##### Python (Union Support)
- **Built-in**: `Union` from `typing` module (Python 3.5+)
- **Syntax**: `X | Y` union syntax (Python 3.10+)
- **Libraries**: `pydantic` for runtime validation
- **Features**: Type hints, runtime checking
- **Status**: Growing adoption

##### C# (Discriminated Unions)
- **Implementation**: F# style discriminated unions
- **Libraries**: OneOf, Union types via libraries
- **Features**: Pattern matching (C# 8+), switch expressions
- **Status**: Community-driven implementations

##### Java (Sealed Classes)
- **Implementation**: Sealed classes and interfaces (Java 17+)
- **Features**: Restricted inheritance hierarchies
- **Pattern Matching**: Preview features for pattern matching
- **Status**: Recent language addition

### Performance Benchmarks and Analysis

#### TypeScript Union Performance
- **Metrics**: Type checking speed for complex unions
- **Optimizations**: Union caching, incremental checking
- **Scale**: Large codebases with extensive union usage
- **Bottlenecks**: Complex discriminated union analysis

#### Rust Enum Performance
- **Metrics**: Zero-cost abstraction validation
- **Memory**: Efficient tagged union representation
- **Pattern Matching**: Compile-time optimization
- **Performance**: Industry benchmark for union efficiency

#### Flow Union Analysis
- **Metrics**: Incremental union refinement
- **Performance**: Flow-sensitive analysis overhead
- **Optimizations**: Lazy union checking, caching
- **Scale**: Large JavaScript applications

#### Scala 3 Union Performance
- **Metrics**: Compilation time for union-heavy code
- **DOT Calculus**: Theoretical performance characteristics
- **Optimizations**: Type-level computation efficiency
- **Status**: Production readiness assessment

### Development Tools and IDE Support

#### TypeScript Tooling
- **VS Code**: Native union type support, IntelliSense
- **IntelliJ**: Advanced union type analysis
- **Language Server**: Union type completion and error reporting
- **Features**: Discriminated union exhaustiveness checking

#### Rust Tooling
- **rust-analyzer**: Enum pattern completion, exhaustiveness
- **rustc**: Compile-time union validation
- **Clippy**: Union-related linting
- **Features**: Pattern match completeness checking

#### Scala Tooling
- **Metals**: Scala 3 union type support
- **IntelliJ Scala**: Union type inference display
- **sbt**: Compilation integration
- **Features**: Union type visualization

#### OCaml Tooling
- **Merlin**: Polymorphic variant support
- **OCaml LSP**: Union type inference
- **utop**: Interactive union type exploration
- **Features**: Variant type completion

### Testing and Validation Frameworks

#### Union Type Test Patterns

##### TypeScript Testing
- **Jest**: Runtime union type validation tests
- **Vitest**: Modern union type testing
- **Type Testing**: Compile-time union type verification
- **Patterns**: Discriminated union test cases

##### Rust Testing
- **Built-in Tests**: Enum exhaustiveness validation
- **Property Testing**: Union variant property testing
- **Benchmarking**: Performance testing for union operations
- **Patterns**: Enum serialization round-trip tests

#### Property-Based Testing
- **QuickCheck**: Haskell union type property testing
- **Hypothesis**: Python union type testing
- **fast-check**: JavaScript/TypeScript property testing
- **Features**: Automatic union variant generation

### Build System Integration

#### Modern Build Tools

##### Vite (TypeScript)
- **Integration**: Fast union type checking
- **HMR**: Hot module replacement with union types
- **Performance**: esbuild-based transformation
- **Features**: Development server optimization

##### Turbo (Rust)
- **Integration**: Enum-based configuration
- **Performance**: Parallel build optimization
- **Features**: Union type aware caching

##### Mill (Scala)
- **Integration**: Scala 3 union type support
- **Performance**: Incremental compilation
- **Features**: Union type dependency tracking

### Legacy Build Integration

#### Webpack (TypeScript)
- **Plugins**: Union type aware bundling
- **Performance**: Parallel type checking
- **Features**: Union type tree shaking

#### Cargo (Rust)
- **Integration**: Native enum support
- **Features**: Cross-crate enum dependencies
- **Performance**: Incremental enum compilation

### Future Developments and Research Directions

#### Language Evolution
- **TypeScript**: Enhanced union inference, performance improvements
- **Rust**: Enum ergonomics improvements
- **Scala 3**: Union type ecosystem maturation
- **Python**: Better union type runtime support

#### Research Areas
- **Performance**: Efficient union type algorithms
- **Inference**: Advanced union type inference
- **Verification**: Union type correctness proofs
- **Gradual Typing**: Better union type gradual systems

#### Tooling Improvements
- **IDEs**: Better union type visualization
- **Debuggers**: Union variant runtime inspection
- **Profilers**: Union type performance analysis
- **Linters**: Advanced union type checking

#### Cross-Language Interop
- **WebAssembly**: Union type representation standards
- **FFI**: Foreign function interface union types
- **Protocols**: Cross-language union type protocols
- **Serialization**: Standard union type serialization

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