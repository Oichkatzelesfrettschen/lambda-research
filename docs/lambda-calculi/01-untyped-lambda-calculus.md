# Untyped Lambda Calculus

The foundational computational model introduced by Alonzo Church in 1936, representing computation through function abstraction and application without type constraints.

## Overview

The untyped lambda calculus consists of three basic constructs:
- **Variables**: `x`, `y`, `z`, ...
- **Abstraction**: `λx.M` (function definition)
- **Application**: `M N` (function application)

## Syntax

```
M, N ::= x              (variable)
       | λx.M           (abstraction)
       | M N            (application)
```

## Key Properties

- **Church-Rosser Property**: Confluence of reduction
- **Computability**: Can express all computable functions
- **Undecidability**: No general algorithm for equality
- **Expressiveness**: Can encode numbers, booleans, data structures

## Historical Significance

Church's original lambda calculus predates and influenced:
- Turing machines (equivalent computational power)
- LISP programming language
- Functional programming paradigms
- Modern type theory foundations

## Important Results

- **Church Numerals**: Encoding of natural numbers
- **Fixed Point Combinators**: Y combinator and recursion
- **Böhm's Theorem**: Separability of lambda terms
- **Scott-Curry Theorem**: Relation to combinatory logic

## Resources

- **Papers**: See [bibliography.md](/papers/bibliography.md) for 25+ foundational papers
- **Implementations**: Available in multiple languages in `/implementations/`
- **Tutorials**: Educational materials in `/tutorials/`
- **Historical**: Original papers and development in `/historical/`

## Related Systems

- [Simply Typed Lambda Calculus](/../02-simply-typed-lambda-calculus/) - Adding type safety
- [Combinatory Logic](/../13-combinatory-logic/) - Combinator-based equivalent
- [System F](/../03-system-f-polymorphic/) - Polymorphic extension

---

*The untyped lambda calculus remains the foundational model for understanding computation, serving as the basis for all subsequent lambda calculus variants and type systems.*