# Lambda Calculus Research Repository - Comprehensive Index

**[← Back to Indices](README.md)** | **Other Views**: [By Author](by-author.md) · [Chronological](chronological.md) · [By Topic](by-topic.md) · [By Citation](by-citation.md) · [Access Type](access-type.md) · [Statistics](statistics.md)

---

## Repository Structure Overview

This repository organizes academic citations on lambda calculus variants into systematic categories with bibliographies, external implementations, and educational resources.

## Core Lambda Calculi

### 01-untyped-lambda-calculus/
**Church's original lambda calculus (1936)**
- **papers/bibliography.md**: 25 foundational papers from Church (1936) to modern developments
- Key topics: Church-Rosser theorem, denotational semantics, complexity theory
- Notable papers: Church (1941), Scott (1970), Barendregt (1984)

### 02-simply-typed-lambda-calculus/
**Typed lambda calculus with function types only**
- **papers/bibliography.md**: 40 citations covering type inference, decidability, and performance analysis
- Implementations: see external projects referenced in the Implementations Catalog
- Key topics: Hindley-Milner inference, Curry-Howard correspondence, complexity, evaluation strategies
- Notable papers: Church (1940), Hindley (1969), Milner (1978), Plotkin (1975), Ariola & Felleisen (1997)
  

### 03-system-f-polymorphic/
**Second-order polymorphic lambda calculus**
- **papers/bibliography.md**: 32 papers on parametric polymorphism
- Key topics: System F, parametricity, strong normalization
- Notable papers: Girard (1972), Reynolds (1974), Wadler (1989)

## Advanced Type Systems

### 04-calculus-of-constructions/
**Higher-order dependent types (lambda cube vertex)**
- **papers/bibliography.md**: 34 papers from Coquand-Huet foundations
- Key topics: Dependent types, lambda cube, inductive constructions
- Notable papers: Coquand & Huet (1988), Barendregt (1991)

### 05-martin-lof-type-theory/
**Constructive type theory with dependent types**
- **papers/bibliography.md**: 35+ papers spanning 55 years (1970-2025)
- Key topics: Constructive mathematics, identity types, universes
- Notable papers: Martin-Löf (1975, 1984), HoTT Book (2013)

### 29-homotopy-type-theory/
**Univalent foundations for mathematics**
- **papers/bibliography.md**: 20+ foundational papers from Voevodsky, Awodey, and the HoTT Book
- Key topics: Types as spaces, identity types as paths, Univalence Axiom, Higher Inductive Types
- Notable papers: HoTT Book (2013), Voevodsky (2010), Awodey & Warren (2009)

### 30-cubical-type-theory/
**Constructive HoTT with explicit paths**
- **papers/bibliography.md**: 15+ foundational papers from Cohen, Huber, and Mörtberg
- Key topics: Cubes, interval type, constructive univalence, path composition
- Notable papers: Cohen et al. (2018), Huber (2016), Mörtberg & Nordvall Forsberg (2018)

### 31-directed-type-theory/
**Asymmetric transformations and higher categories**
- **papers/bibliography.md**: 10+ foundational papers from Sterling, Harper, and North
- Key topics: Directed paths, higher categories, variance, homomorphism types
- Notable papers: Sterling & Harper (2020), North (2018), Altenkirch & Neumann (2021)

## Substructural Type Systems

### 06-linear-lambda-calculus/
**Resource-aware computation**
- **papers/bibliography.md**: 40 papers from Girard's Linear Logic (1987)
- Key topics: Linear logic, resource semantics, quantum computation
- Notable papers: Girard (1987), Abramsky (1993)

### 07-session-types/
**Communication protocol types**
- **papers/bibliography.md**: 27 papers spanning 32 years (1993-2025)
- Key topics: Structured communication, multiparty protocols
- Notable papers: Honda (1993), Gay & Vasconcelos (2010)

## Foundational Concepts

### 08-dependent-types/
**General dependent type theory**
- **papers/bibliography.md**: 37 papers covering implementation and theory
- Key topics: AUTOMATH, proof assistants, homotopy type theory
- Notable papers: de Bruijn (1970), Voevodsky (2006)

### 26-proof-theory/
**Formal study of mathematical proofs**
- **papers/bibliography.md**: 25+ foundational papers from Gödel, Gentzen, and Howard
- Key topics: Natural deduction, sequent calculus, Curry-Howard correspondence, consistency
- Notable papers: Gödel (1931), Gentzen (1935), Howard (1980)

### 27-domain-theory/
**Mathematical semantics for computation**
- **papers/bibliography.md**: 20+ foundational papers from Scott and Strachey
- Key topics: CPOs, continuous functions, fixed-point semantics, D_infinity models
- Notable papers: Scott (1972), Scott & Strachey (1971)

## Implementation Resources

### implementations/catalog.md
**Comprehensive source code catalog**
- 8 major lambda calculus variants covered
- Categories: Academic/Research, Production Systems, Educational Resources
- Languages: Haskell, Rust, OCaml, Coq, Lean, Agda, others
- Institutions: UPenn, INRIA, Microsoft Research, Cornell

## Operational Semantics and Implementation

### 28-abstract-machines/
**Execution models for functional languages**
- **papers/bibliography.md**: 15+ foundational papers on SECD, Krivine, CEK, G-machine
- Key topics: Operational semantics, evaluation strategies, garbage collection
- Notable papers: Landin (1964), Krivine (1986), Johnsson (1984)

## Advanced Type Features

### 13-combinatory-logic/
**Combinatorial basis for lambda calculus**
- **papers/bibliography.md**: 25 papers from Schönfinkel (1924) to modern developments
- Key topics: SKI combinators, illative combinatory logic, implementation techniques
- Notable papers: Schönfinkel (1924), Curry & Feys (1958), Turner (1979)

### 14-intersection-types/
**Types for characterizing normalization properties**
- **bibliography.md**: 40+ papers from Coppo-Dezani (1978) to modern developments
- **implementations.md**: TypeScript, Flow, Scala 3, research prototypes
- Key topics: Strong normalization, principal types, strict systems, BCD framework
- Notable papers: Coppo & Dezani (1978), Barendregt et al. (1983), van Bakel (1992)

### 15-union-types/
**Discriminated unions and sum types**
- **bibliography.md**: 35+ papers from Hoare (1965) to contemporary systems
- **implementations.md**: TypeScript, Flow, Rust, Scala 3, OCaml variants
- Key topics: Flow-sensitive typing, occurrence typing, pattern matching, gradual typing
- Notable papers: Tobin-Hochstadt & Felleisen (2008), gradual typing literature

## Extended Categories (Folder Structure)

### 09-substructural-types/
**Affine, relevant, and ordered lambda calculi**
- **papers/bibliography.md**: 37 papers from foundational substructural logic to modern applications
- Key topics: Resource awareness, structural rules, separation logic, bunched implications
- Notable papers: Girard (1987), Wadler (1990), O'Hearn & Pym (1999), Rust ownership types

### 10-concurrent-variants/
*Prepared for: Pi-calculus, actor models, process calculi*

### 11-quantum-variants/
*Prepared for: Quantum lambda calculi, measurement types*

### 12-pure-type-systems/
**Lambda cube generalizations and PTS framework**
- **papers/bibliography.md**: 32 papers from AUTOMATH foundations to cubical type theory
- Key topics: Lambda cube, dependent polymorphism, homotopy type theory, univalent foundations
- Notable papers: Barendregt (1991), Voevodsky (2006), Cohen et al. (2018), HoTT Book (2013)

### 16-gradual-typing/
**Dynamic-static typing integration**
- **papers/bibliography.md**: 30 papers from Siek & Taha (2006) to modern developments
- Key topics: Blame calculus, type soundness, space efficiency, parametricity
- Notable papers: Siek & Taha (2006), Wadler & Findler (2009), TypeScript/Flow implementations

### 17-effect-systems/
**Computational effects and algebraic effects**
- **papers/bibliography.md**: 40 papers from Gifford & Lucassen (1986) to OCaml 5.0
- Key topics: Region-based memory management, algebraic effects, monad transformers
- Notable papers: Lucassen & Gifford (1988), Plotkin & Pretnar (2009), Leijen (2017)

### 18-categorical-semantics/
**Category theory foundations for lambda calculus**
- **papers/bibliography.md**: 40 papers from Eilenberg & Mac Lane (1945) to HoTT developments
- Key topics: Cartesian closed categories, topos theory, homotopy type theory
- Notable papers: Lambek (1980), Seely (1987), Awodey & Warren (2009)

### 19-modal-types/
**Modal logic integration with types**
- **papers/bibliography.md**: 40 papers from Lewis (1918) to modern modal dependent types
- Key topics: Staged computation, temporal reasoning, necessity modality
- Notable papers: Davies & Pfenning (2001), Taha & Sheard (2000), Sterling & Harper (2021)

### 20-refinement-types/
**Types with logical predicates and SMT integration**
- **papers/bibliography.md**: 30 papers from Freeman & Pfenning (1991) to modern developments
- Key topics: Liquid types, F* verification, Dafny contracts, SMT solving
- Notable papers: Rondon et al. (2008), Vazou et al. (2014), Swamy et al. (2016)

### 21-probabilistic-types/
**Probabilistic programming and uncertainty quantification**
- **papers/bibliography.md**: 36 papers from early probabilistic logic to modern ML integration
- Key topics: Church encoding, Bayesian inference, differential privacy, quantum probability
- Notable papers: Ramsey & Pfeffer (2002), Goodman et al. (2008), Bingham et al. (2019)

### 22-quantum-lambda-calculus/
**Quantum computation and quantum types**
- **papers/bibliography.md**: 40 papers from quantum foundations to modern quantum languages
- Key topics: Quantum superposition types, measurement effects, no-cloning, entanglement
- Notable papers: van Tonder (2004), Selinger & Valiron (2006), Green et al. (2013)

### 23-advanced-lambda-variants/
**Specialized lambda calculus extensions**
- **papers/bibliography.md**: 35 papers covering higher-rank polymorphism, constraint systems, fixpoints
- Key topics: System F extensions, constraint-based inference, recursive types, algebraic effects
- Notable papers: Dunfield & Krishnaswami (2013), Plotkin & Pretnar (2009), Leijen (2017)

## Bibliography Statistics

### Total Academic Coverage
- **700+ citations** across all categories
- **Time span**: 1918-2025 (107 years of research)
- **Venues**: POPL, ICFP, TLCA, TCS, Journal of ACM, ACM Computing Surveys, LICS, ESOP, PLDI, and more
- **Contributors**: Church, Curry, Martin-Löf, Girard, Reynolds, Coquand, Coppo, Dezani, Tobin-Hochstadt, Lewis, Kripke, Davies, Pfenning, Plotkin, Abramsky, Voevodsky, and hundreds more

### Research Quality Standards
- Focus on first-party academic sources
- Emphasis on highly-cited, foundational works
- Comprehensive coverage from historical foundations to cutting-edge developments
- Full bibliographic citations with venue information

## Key Theoretical Connections

### Lambda Cube Framework
```
Simply Typed LC -----> System F (polymorphism)
      |                    |
      |                    |
      v                    v
 Dependent Types ----> Calculus of Constructions
```

### Curry-Howard Correspondence
- Propositions ↔ Types
- Proofs ↔ Programs
- Proof normalization ↔ Program evaluation

### Substructural Hierarchy
```
Classical Logic
     |
Intuitionistic Logic
     |
Linear Logic -----> Affine Logic
     |                 |
Relevant Logic    Ordered Logic
```

## Educational Pathways

### Beginner Track
1. **Untyped Lambda Calculus** - Core computational model
2. **Simply Typed Lambda Calculus** - Basic type safety
3. **System F** - Parametric polymorphism

### Advanced Theory Track
1. **Martin-Löf Type Theory** - Constructive foundations
2. **Calculus of Constructions** - Higher-order dependent types
3. **Homotopy Type Theory** - Modern foundations

### Systems Track
1. **Linear Lambda Calculus** - Resource management
2. **Session Types** - Communication protocols
3. **Implementation Catalog** - Practical systems

## Modern Applications (2020-2025)

### AI and Theorem Proving
- Lean Copilot: LLM integration with theorem provers
- AlphaProof: AI systems proving IMO-level theorems
- Automated proof synthesis and verification

### Programming Language Design
- Rust: Linear types for memory safety
- Idris 2: Quantitative types for resource awareness
- Cubical Agda: Computational univalence

### Mathematical Formalization
- Mathlib: Extensive Lean mathematics library
- Formal verification of fundamental theorems
- Computer-checked mathematical proofs

## Research Institutions and Communities

### Primary Academic Centers
- **University of Pennsylvania**: Software Foundations, TAPL
- **INRIA**: Coq development, type theory research
- **Microsoft Research**: Lean theorem prover
- **Imperial College London**: Session types, multiparty protocols
- **Chalmers University**: Agda development

### Active Research Areas
- Homotopy type theory and univalent foundations
- Quantum lambda calculi and quantum programming
- Session types for distributed systems
- AI-assisted theorem proving and verification
- Cubical type theory and computational mathematics

## Usage Guidelines

### For Researchers
- Each bibliography provides comprehensive starting points for literature review
- Implementation catalog offers practical validation of theoretical concepts
- Cross-references enable exploration of theoretical connections

### For Educators
- Progressive complexity from untyped through dependent types
- Historical development shows evolution of ideas
- Implementation examples provide hands-on learning opportunities

### For Practitioners
- Session types for protocol verification
- Linear types for resource management
- Dependent types for program correctness

---

*This index represents the most comprehensive academic resource on lambda calculus variants available, suitable for research, education, and practical application across the full spectrum of type theory and programming language design.*

**Last Updated**: September 2025
**Total Citations**: 700+
**Implementation Projects**: 75+
**Research Institutions**: 35+
**Type System Categories**: 23+
**Papers Archive**: 10 PDFs downloaded from open access sources
**Cross-Reference System**: Complete theoretical connection mapping
