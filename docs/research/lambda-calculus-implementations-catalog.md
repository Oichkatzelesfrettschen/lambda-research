# Lambda Calculus Variants Implementation Catalog

A comprehensive catalog of source code implementations for major lambda calculus variants, organized by theoretical framework and practical application.

## 1. Untyped Lambda Calculus

### Academic/Research Implementations

**sgillespie/lambda-calculator**
- **Description**: A simple implementation of the Untyped Lambda Calculus designed as an educational resource
- **Repository**: https://github.com/sgillespie/lambda-calculator
- **Language**: Haskell
- **Institution**: Independent research
- **Key Features**: Simple implementation focused on educational clarity
- **Academic Relevance**: Educational tool for learning functional programming language implementation

**KTStephano/Untyped-Lambda-Calculus-Interpreter**
- **Description**: A simple interactive interpreter for the untyped lambda calculus
- **Repository**: https://github.com/KTStephano/Untyped-Lambda-Calculus-Interpreter
- **Language**: Not specified
- **Institution**: Independent research
- **Key Features**: Interactive interpreter interface
- **Academic Relevance**: Practical exploration of untyped lambda calculus evaluation

### Educational Resources

**Types and Programming Languages (Pierce) Implementations**
- **Description**: Rust implementations of exercises from Benjamin Pierce's seminal textbook
- **Repository**: https://github.com/lazear/types-and-programming-languages
- **Language**: Rust
- **Institution**: Based on UPenn textbook
- **Key Features**: arith (numeric operations), lambda (chapters 5-7 implementation)
- **Academic Relevance**: Standard reference implementations for academic study

**OCaml TAPL Implementations**
- **Description**: Implementation in different programming languages of exercises from Pierce's textbook
- **Repository**: https://github.com/dannywillems/types-and-programming-languages-pierce-implementation
- **Language**: Multiple languages (OCaml primary)
- **Institution**: Academic exercise solutions
- **Key Features**: Multiple language implementations with detailed explanations
- **Academic Relevance**: Cross-language comparison of implementation approaches

### Modern GitHub Projects

**JelleZijlstra/lambda (Untyped Variant)**
- **Description**: Almost pure untyped lambda calculus with integers, print statements, and let-in
- **Repository**: https://github.com/JelleZijlstra/lambda
- **Language**: OCaml
- **Institution**: Independent research
- **Key Features**: Practical extensions for usability, interpreter and compiler to JavaScript
- **Academic Relevance**: Bridge between pure theory and practical implementation

**FlorianCassayre/TypedUntypedLambdaCalculus**
- **Description**: Proof of concept interpreter implemented within the Scala type system
- **Repository**: https://github.com/FlorianCassayre/TypedUntypedLambdaCalculus
- **Language**: Scala
- **Institution**: Independent research
- **Key Features**: Meta-level implementation using host language type system
- **Academic Relevance**: Novel approach to embedding lambda calculus in typed host language

**lambda-11235/lambda-calc**
- **Description**: Interpreter for untyped lambda calculus with lazy evaluation
- **Repository**: https://github.com/lambda-11235/lambda-calc
- **Language**: Not specified
- **Institution**: Independent research
- **Key Features**: Lazy evaluation semantics
- **Academic Relevance**: Exploration of different evaluation strategies

## 2. Simply Typed Lambda Calculus (STLC)

### Academic/Research Implementations

**Software Foundations STLC**
- **Description**: Simply typed lambda-calculus formalization in Coq
- **Repository**: https://softwarefoundations.cis.upenn.edu/plf-current/Stlc.html
- **Language**: Coq
- **Institution**: University of Pennsylvania
- **Key Features**: 100% formalized and machine-checked implementation
- **Academic Relevance**: Gold standard for formal verification of STLC properties

**hubbards/stlc-coq**
- **Description**: Simply typed lambda calculus formalization in Coq
- **Repository**: https://github.com/hubbards/stlc-coq
- **Language**: Coq
- **Institution**: Independent research
- **Key Features**: Formal proof development
- **Academic Relevance**: Formal verification of type safety properties

**caotic123/Formalized-STLC**
- **Description**: Formalization using dependent type theory to prove structural properties
- **Repository**: https://github.com/caotic123/Formalized-STLC
- **Language**: Dependent type theory
- **Institution**: Independent research
- **Key Features**: Structural property proofs
- **Academic Relevance**: Advanced formal verification techniques

### Production Systems

**hubbards/stlc-haskell**
- **Description**: Simply typed lambda calculus implementation in Haskell
- **Repository**: https://github.com/hubbards/stlc-haskell
- **Language**: Haskell
- **Institution**: Independent research
- **Key Features**: Functional programming approach
- **Academic Relevance**: Practical implementation in a typed functional language

**trackoor/STLC**
- **Description**: STLC formalized in Coq with REPL in Haskell
- **Repository**: https://github.com/trackoor/STLC
- **Language**: Coq, Haskell
- **Institution**: Independent research
- **Key Features**: Formal verification with practical interface
- **Academic Relevance**: Bridge between theory and practice

### Educational Resources

**STLC with de Bruijn Indices in Lean**
- **Description**: Project to formalize STLC with de Bruijn indices
- **Repository**: https://elifuskuplu.github.io/Stlc_deBruijn/
- **Language**: Lean
- **Institution**: Independent research
- **Key Features**: De Bruijn index representation
- **Academic Relevance**: Modern proof assistant implementation

## 3. System F (Polymorphic Lambda Calculus)

### Academic/Research Implementations

**Lysxia/system-F**
- **Description**: Formalization of polymorphic lambda calculus with parametricity theorem
- **Repository**: https://github.com/Lysxia/system-F
- **Language**: Dependently-typed (likely Agda/Coq)
- **Institution**: Independent research
- **Key Features**: Dependently-typed representation, Reynolds parametricity proof
- **Academic Relevance**: Advanced formalization of polymorphism theory

**sstucki/system-f-agda**
- **Description**: Formalization extended with iso-recursive types
- **Repository**: https://github.com/sstucki/system-f-agda
- **Language**: Agda
- **Institution**: Independent research
- **Key Features**: Iso-recursive types, general recursion
- **Academic Relevance**: Extension of basic System F with practical type features

### Educational Resources

**System F-ω Typechecker Zoo**
- **Description**: Minimal implementation from Typechecker Zoo project
- **Repository**: https://sdiehl.github.io/typechecker-zoo/implementations/system-f-omega/system-f-omega.html
- **Language**: Rust
- **Institution**: Educational project by Stephen Diehl
- **Key Features**: Higher-kinded types, kind system
- **Academic Relevance**: Simplified educational implementation

**TAPL System F Implementations**
- **Description**: System F implementation from Pierce exercises
- **Repository**: https://github.com/lazear/types-and-programming-languages
- **Language**: Rust
- **Institution**: Based on TAPL textbook
- **Key Features**: Parametric polymorphism, bidirectional type checking
- **Academic Relevance**: Standard textbook implementation

### Modern GitHub Projects

**Hirrolot/system-f-omega (GitHub Gist)**
- **Description**: Minimalistic OCaml implementation of higher-order polymorphism
- **Repository**: https://gist.github.com/Hirrolot/505901460f131da1f0cd8b118e46a7bc
- **Language**: OCaml
- **Institution**: Independent research
- **Key Features**: Bidirectional typing, no existential types
- **Academic Relevance**: Concise implementation focusing on core features

## 4. Calculus of Constructions (CoC)

### Academic/Research Implementations

**rocq-archive/coq-in-coq**
- **Description**: Formalization of the Calculus of Constructions in Coq
- **Repository**: https://github.com/coq-contribs/coq-in-coq
- **Language**: Coq
- **Institution**: Rocq project contributors
- **Key Features**: Stand-alone proof-checker, significant CIC fragment
- **Academic Relevance**: Self-hosting formalization, foundational research

**anfelor/coc-lean**
- **Description**: Calculus of constructions implementation in Lean
- **Repository**: https://github.com/anfelor/coc-lean
- **Language**: Lean
- **Institution**: Independent research
- **Key Features**: De Bruijn variables, type checker with error reporting, correctness proofs
- **Academic Relevance**: Modern proof assistant implementation

### Educational Resources

**CoC Typechecker Zoo**
- **Description**: Educational implementation from Typechecker Zoo
- **Repository**: https://github.com/sdiehl/typechecker-zoo
- **Language**: Rust
- **Institution**: Educational project by Stephen Diehl
- **Key Features**: Lambda cube pinnacle, unified framework
- **Academic Relevance**: Simplified educational implementation

**Cornell CS 6120 CoC Implementation**
- **Description**: Course project implementing Calculus of Constructions
- **Repository**: https://www.cs.cornell.edu/courses/cs6120/2022sp/blog/coc/
- **Language**: Various
- **Institution**: Cornell University
- **Key Features**: Educational blog post with implementation
- **Academic Relevance**: Course-level educational resource

### Modern GitHub Projects

**VictorTaelin/calculus-of-constructions**
- **Description**: Minimal, fast, robust implementation in JavaScript
- **Repository**: https://github.com/VictorTaelin/calculus-of-constructions
- **Language**: JavaScript
- **Institution**: Independent research
- **Key Features**: Minimalistic design, web-based implementation
- **Academic Relevance**: Accessible implementation for broader audience

**SabrinaJewson/CoC**
- **Description**: Toy implementation with Lean/Coq-like language features
- **Repository**: https://github.com/SabrinaJewson/CoC
- **Language**: Rust
- **Institution**: Independent research
- **Key Features**: Basic theorem proving capabilities
- **Academic Relevance**: Learning-focused implementation

## 5. Martin-Löf Type Theory (MLTT)

### Academic/Research Implementations

**sconybeare/mltt**
- **Description**: Implementation of Martin-Löf Type Theory in Haskell
- **Repository**: https://github.com/sconybeare/mltt
- **Language**: Haskell
- **Institution**: Independent research
- **Key Features**: Pure MLTT implementation
- **Academic Relevance**: Direct implementation of Martin-Löf's type theory

**jozefg/nbe-for-mltt**
- **Description**: Normalization by Evaluation for Martin-Löf Type Theory
- **Repository**: https://github.com/jozefg/nbe-for-mltt
- **Language**: Unknown (likely Haskell/OCaml)
- **Institution**: Independent research
- **Key Features**: Dependent products/sums, natural numbers, cumulative hierarchy, eta for pi/sigma
- **Academic Relevance**: Advanced normalization techniques, semantic type checker

### Educational Resources

**michaelt/martin-lof**
- **Description**: Collection of Per Martin-Löf's foundational papers
- **Repository**: https://github.com/michaelt/martin-lof
- **Language**: Papers (LaTeX/PDF)
- **Institution**: Academic paper collection
- **Key Features**: Original theoretical foundations, searchable versions
- **Academic Relevance**: Primary sources for MLTT theory

### Production Systems

**Agda Implementation**
- **Description**: Dependently typed programming language based on MLTT
- **Repository**: https://github.com/agda/agda
- **Language**: Haskell
- **Institution**: International academic collaboration
- **Key Features**: Interactive theorem prover, powerful pattern matching
- **Academic Relevance**: Production-quality MLTT-based system

**Lean Mathematical Library (Mathlib)**
- **Description**: Extensive mathematical formalization in Lean
- **Repository**: Lean Prover Community
- **Language**: Lean
- **Institution**: International mathematics community
- **Key Features**: Typeclass organization, mathematical structures
- **Academic Relevance**: Large-scale formalization of mathematics

## 6. Linear Lambda Calculus

### Academic/Research Implementations

**dfeltey/linear-lambda-caclulus**
- **Description**: Racket implementation with interleaved typechecking and macro expansion
- **Repository**: https://github.com/dfeltey/linear-lambda-caclulus
- **Language**: Racket
- **Institution**: Independent research
- **Key Features**: STLC extended with booleans, products, and linear types
- **Academic Relevance**: Syntactic type soundness proofs, algorithmic typing equivalence

**aerabi/llc**
- **Description**: Linear Lambda Calculus with formal proofs in Coq
- **Repository**: https://github.com/aerabi/llc
- **Language**: Coq
- **Institution**: Independent research
- **Key Features**: Syntax, type system, small-step semantics, preservation and progress proofs
- **Academic Relevance**: Complete formal verification of linear type system

**dportin/linear**
- **Description**: Formalization of simply-typed lambda calculus with linear types
- **Repository**: https://github.com/dportin/linear
- **Language**: Unknown
- **Institution**: Independent research
- **Key Features**: Syntactic type soundness proof, nondeterministic/algorithmic typing equivalence
- **Academic Relevance**: Formal verification of linear type systems

### Modern GitHub Projects

**noamz/linlam**
- **Description**: Library for experimental linear lambda calculus
- **Repository**: https://github.com/noamz/linlam
- **Language**: Unknown
- **Institution**: Independent research
- **Key Features**: Experimental features for linear types
- **Academic Relevance**: Research platform for linear type experiments

**na0214/linear-lambda-calculus**
- **Description**: Implementation of Linear Lambda Calculus
- **Repository**: https://github.com/na0214/linear-lambda-calculus
- **Language**: Unknown
- **Institution**: Independent research
- **Key Features**: Basic linear lambda calculus implementation
- **Academic Relevance**: Educational/research implementation

## 7. Session Types

### Academic/Research Implementations

**session-pi/session-pi**
- **Description**: Session-typed pi-calculus interpreter
- **Repository**: https://github.com/session-pi/session-pi
- **Language**: Unknown
- **Institution**: Independent research
- **Key Features**: Practical implementation of session types in pi-calculus
- **Academic Relevance**: Experimental platform for session type research

### Production Systems

**Rust Session Types**
- **Description**: Various Rust libraries implementing session types
- **Repository**: Multiple repositories in Rust ecosystem
- **Language**: Rust
- **Institution**: Rust community
- **Key Features**: Compile-time protocol verification
- **Academic Relevance**: Production use of session type theory

### Educational Resources

**Academic Papers Collection**
- **Description**: Extensive literature on session types in pi-calculus
- **Sources**: Various academic venues (Acta Informatica, ScienceDirect, arXiv)
- **Institution**: International research community
- **Key Features**: Subtyping, algorithmic type checking, minimal session types
- **Academic Relevance**: Theoretical foundations and practical applications

## 8. Dependent Types

### Academic/Research Implementations

**Agda**
- **Description**: Dependently typed programming language and proof assistant
- **Repository**: https://github.com/agda/agda
- **Language**: Haskell
- **Institution**: International academic collaboration
- **Key Features**: Dependent pattern matching, universe polymorphism, interactive development
- **Academic Relevance**: Leading research platform for dependent types

**Lean Theorem Prover**
- **Description**: Modern theorem prover based on dependent type theory
- **Repository**: Lean Prover Community
- **Language**: C++, Lean
- **Institution**: Microsoft Research, academic community
- **Key Features**: Calculus of Constructions with universes, powerful automation
- **Academic Relevance**: Modern foundation for mathematics formalization

### Production Systems

**Idris**
- **Description**: General-purpose dependently typed programming language
- **Repository**: Idris community
- **Language**: Haskell
- **Institution**: Academic and industry collaboration
- **Key Features**: Practical programming with dependent types, tactics, totality checking
- **Academic Relevance**: Bridge between theory and practical programming

**Coq/Rocq**
- **Description**: Formal proof management system
- **Repository**: Coq development team
- **Language**: OCaml
- **Institution**: INRIA and international collaboration
- **Key Features**: Calculus of Inductive Constructions, tactics, extensive libraries
- **Academic Relevance**: Foundational tool for formal verification research

### Educational Resources

**Software Foundations Series**
- **Description**: Electronic textbooks on formal methods
- **Repository**: https://softwarefoundations.cis.upenn.edu/
- **Language**: Coq
- **Institution**: University of Pennsylvania
- **Key Features**: 100% formalized and machine-checked content
- **Academic Relevance**: Standard curriculum for formal methods education

**Theorem Proving in Lean**
- **Description**: Comprehensive tutorial for Lean theorem prover
- **Repository**: Lean community documentation
- **Language**: Lean
- **Institution**: Lean community
- **Key Features**: Practical introduction to dependent types and theorem proving
- **Academic Relevance**: Accessible entry point to modern dependent type theory

## Cross-Cutting Educational Resources

### Typechecker Zoo
- **Description**: Minimal implementations of major type systems
- **Repository**: https://sdiehl.github.io/typechecker-zoo/
- **Language**: Rust
- **Institution**: Stephen Diehl (educational project)
- **Key Features**: Algorithm W, System F, System F-ω, CoC implementations
- **Academic Relevance**: Comprehensive educational resource for type system implementation

### Lambda Programming Language Zoo (lplzoo)
- **Description**: Fine-grain implementations of lambda calculi in Haskell
- **Repository**: https://github.com/lukeg101/lplzoo
- **Language**: Haskell
- **Institution**: Independent research
- **Key Features**: Untyped LC, STLC, System T, PCF, System F, SOL, CoC
- **Academic Relevance**: Comprehensive coverage with QuickCheck testing

### Types and Programming Languages Implementations
- **Description**: Multi-language implementations of Pierce textbook exercises
- **Repository**: Multiple repositories implementing TAPL exercises
- **Language**: Rust, OCaml, Haskell, others
- **Institution**: Based on Benjamin Pierce's textbook
- **Key Features**: Standard reference implementations across type system spectrum
- **Academic Relevance**: Canonical implementations for academic study

## Research Institutions and Communities

### Primary Academic Institutions
- **University of Pennsylvania**: Software Foundations, TAPL
- **INRIA**: Coq development, type theory research
- **Microsoft Research**: Lean development
- **Cornell University**: CS courses on type systems
- **University of Oregon**: Programming Languages Summer School

### Active Research Communities
- **Agda Community**: Dependent types and constructive mathematics
- **Lean Community**: Mathematical formalization and theorem proving
- **Rust Community**: Session types and linear types in systems programming
- **Coq Community**: Formal verification and constructive mathematics
- **Pi-Calculus Community**: Concurrency and session types research

This catalog represents the state of lambda calculus implementation research as of 2024-2025, providing a comprehensive foundation for academic study and practical implementation across the spectrum of type system complexity.