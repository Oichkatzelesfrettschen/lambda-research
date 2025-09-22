# Lambda Calculus Research Repository

A comprehensive collection of academic papers, implementations, and educational resources covering the major variants of lambda calculus and type theory.

## Structure

This repository is organized into the following major categories:

### Core Lambda Calculi
- **01-untyped-lambda-calculus/** - The original lambda calculus by Church
- **02-simply-typed-lambda-calculus/** - Basic typed lambda calculus with function types
- **03-system-f-polymorphic/** - Polymorphic lambda calculus (System F)

### Foundational Concepts
- **08-dependent-types/** - Types depending on values
- **26-proof-theory/** - Formal study of mathematical proofs
- **27-domain-theory/** - Mathematical semantics for computation

### Advanced Type Systems
- **04-calculus-of-constructions/** - Higher-order dependent types
- **05-martin-lof-type-theory/** - Constructive type theory
- **06-linear-lambda-calculus/** - Resource-aware computation
- **07-session-types/** - Communication protocol types
- **09-substructural-types/** - Affine, relevant, and ordered types
- **10-concurrent-variants/** - Pi-calculus, actor models
- **11-quantum-variants/** - Quantum lambda calculi
- **12-pure-type-systems/** - Barendregt's lambda cube and generalizations
- **13-combinatory-logic/** - Combinatorial basis for lambda calculus
- **14-intersection-types/** - Types for characterizing normalization properties
- **15-union-types/** - Discriminated unions and sum types
- **16-gradual-typing/** - Dynamic-static typing integration
- **17-effect-systems/** - Computational effects and algebraic effects
- **18-categorical-semantics/** - Category theory foundations for lambda calculus
- **19-modal-types/** - Modal logic integration with types
- **20-refinement-types/** - Types with logical predicates and SMT integration
- **21-probabilistic-types/** - Probabilistic programming and uncertainty quantification
- **22-quantum-lambda-calculus/** - Quantum computation and quantum types
- **23-advanced-lambda-variants/** - Specialized lambda calculus extensions
- **24-tensor-lambda-calculus/** - Tensor lambda calculus
- **25-geometric-algebra-lambda-calculus/** - Geometric algebra lambda calculus
- **29-homotopy-type-theory/** - Univalent foundations for mathematics
- **30-cubical-type-theory/** - Constructive HoTT with explicit paths
- **31-directed-type-theory/** - Asymmetric transformations and higher categories

### Operational Semantics and Implementation
- **28-abstract-machines/** - Execution models for functional languages

## Folder Organization

Each category contains:
- **papers/** - Academic papers, whitepapers, and journal articles
- **implementations/** - Source code for interpreters, compilers, and libraries
- **tutorials/** - Educational materials and textbooks
- **historical/** - Foundational and historically significant works

## Usage

Browse the folders to find comprehensive resources on each lambda calculus variant. Each folder contains bibliographies and curated collections of the most important works in that area.

## Papers Archive

The **papers-archive/** directory contains a systematic collection of open access lambda calculus research papers, organized for research and educational purposes. This includes:

- **Historical papers** (pre-1980): Church's original lambda calculus, Curry-Feys combinatory logic, Scott's domain theory
- **Classical works** (1980-2000): Girard's System F and Linear Logic, Martin-Löf type theory, polymorphism foundations
- **Modern developments** (2000-2020): Homotopy type theory, practical dependent types, session types
- **Recent research** (2020+): Quantum lambda calculi, probabilistic types, AI applications

### Features

- **Automated Downloads**: Scripts to download open access papers from arXiv, author homepages, and institutional repositories
- **Metadata Management**: BibTeX bibliography, author index, topic classification, and citation tracking
- **Search Capabilities**: Full-text search across titles, authors, abstracts, and topic tags
- **Copyright Compliance**: Only downloads legally available papers (open access, public domain, author permission)

### Usage

```bash
cd papers-archive/

# Download high priority papers
make download-high

# Search for papers
make search QUERY="linear logic"
make search-author AUTHOR="Girard"

# Generate indices and cross-references
make generate-indices

# Verify URL accessibility
make verify

# Get status report
make status
```

See [papers-archive/README.md](/papers-archive/README.md) for detailed documentation.

## Contributing

This repository aims to be a comprehensive academic resource. Sources are organized by theoretical importance, practical impact, and educational value.