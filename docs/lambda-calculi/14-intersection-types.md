# Intersection Types Research

This directory contains comprehensive research materials on intersection types in type theory and programming languages.

## Contents

### [Bibliography](14-intersection-types/bibliography.md)
Comprehensive academic bibliography covering:
- **Foundational Works (1978-1983)**: Coppo-Dezani original work, BCD system development
- **Principal Type Inference**: Kfoury-Tiuryn contributions, decidability results
- **Strict Intersection Types**: van Bakel's system and theoretical developments
- **Semantic Characterizations**: Ronchi della Rocca's compositional work
- **Modern Developments**: TypeScript, Flow, and contemporary implementations
- **Connections to Other Systems**: Polymorphism, subtyping, higher-order systems

### [Implementations](14-intersection-types/implementations.md)
Catalog of source code implementations including:
- **Production Languages**: TypeScript, Flow, Scala 3
- **Research Type Checkers**: Ezno, tyty, academic prototypes
- **Library Implementations**: Type guards, contracts, utilities
- **Historical Implementations**: BCD system, van Bakel's strict system
- **Development Tools**: IDEs, build systems, testing frameworks

## Key Theoretical Properties

1. **Strong Normalization**: Intersection types characterize strongly normalizing lambda terms
2. **Principal Types**: Finite-rank restrictions have principal typings and decidable inference
3. **Compositional Analysis**: Semantic characterization of evaluation properties
4. **Strict Systems**: Syntax-directed systems maintaining BCD properties

## Practical Applications

1. **Programming Languages**: TypeScript `A & B`, Flow intersections, Scala 3 intersections
2. **Type Inference**: Bidirectional type checking with intersection constraints
3. **API Design**: Combining interfaces and extending object types
4. **Component Systems**: React props composition, mixin patterns

## Research Directions

- **Performance**: Efficient intersection type checking algorithms
- **Extensions**: Probabilistic and control operator intersections
- **Implementation**: Mainstream programming language adoption
- **Theory**: Advanced semantic foundations and proof techniques

## Historical Timeline

- **1978**: Coppo-Dezani introduce intersection types for lambda calculus
- **1980**: Extension to basic functionality theory
- **1983**: BCD filter lambda model and completeness
- **1988**: van Bakel's strict intersection type system
- **1992**: Kfoury-Tiuryn principal type inference results
- **2012**: TypeScript introduces intersection types to mainstream programming
- **2024**: Modern bidirectional higher-rank polymorphism with intersections

*Part of the Lambda Calculus Research Repository*