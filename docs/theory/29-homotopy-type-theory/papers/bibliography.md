# Foundational Papers and Books on Homotopy Type Theory

This bibliography lists the key works that established Homotopy Type Theory as a new field of mathematics.


The Book

*   **The Univalent Foundations Program (2013). *Homotopy Type Theory: Univalent Foundations of Mathematics*.**
    *   **Contribution:** This book, often referred to as **"The HoTT Book"**, is the foundational text and comprehensive reference for the field. It was written collaboratively by a large group of researchers and provides a complete introduction to HoTT and the Univalent Foundations program. It is freely available online.


Key Papers

*   **Voevodsky, V. (2010). *The Equivalence Axiom and Univalent Models of Type Theory*.**
    *   **Contribution:** This paper, along with other talks and notes by Voevodsky, introduced the **Univalence Axiom**, a central and powerful axiom that equates isomorphism with identity. This was a key conceptual breakthrough that led to the development of HoTT.

*   **Awodey, S., & Warren, M. (2009). *Homotopy theoretic models of identity types*.**
    *   **Contribution:** This paper, along with Warren's PhD thesis, was one of the first to explicitly explore the connection between the identity types of Martin-Löf type theory and the path spaces of homotopy theory. Steve Awodey is credited with coining the term "Homotopy Type Theory".

*   **Hofmann, M., & Streicher, T. (1998). *The groupoid interpretation of type theory*.**
    *   **Contribution:** This paper provided a crucial early insight by showing that type theory could be modeled in the category of groupoids. This was a precursor to the more general idea of interpreting types as spaces and was an important step towards HoTT.

*   **Shulman, M., Lumsdaine, P. L., & Bauer, A. (2011). *Higher Inductive Types: A tour of the menagerie*.**
    *   **Contribution:** This paper (and related work by the authors) introduced **Higher Inductive Types (HITs)**, a powerful mechanism for defining types that have a specified topological shape. HITs are, along with the Univalence Axiom, a key ingredient of HoTT.


---

## Implementation Status

*Last updated: 2024-12-24*

### ⏳ Not Yet Implemented

No papers from this bibliography are currently implemented.

### 📊 Implementation Statistics

**Repository-wide metrics** (as of 2024-12-24):

- Total Rust LOC: 5,179
- Total test count: 38
- Average test coverage: 45%
- Quality score: 6.5/10
- Build status: ✅ Passing
- Clippy warnings: 5 (all in church-unsolvable-1936, low severity)

**Implementation focus areas**:

1. ✅ **Untyped Lambda Calculus** (Church 1936, 1941) - Complete
2. ✅ **Evaluation Strategies** (Pierce TAPL Ch. 5) - Complete but untested
3. 🔄 **Type Systems** (Pierce TAPL Ch. 9+) - Planned
4. 🔄 **Polymorphism** (System F) - Planned
5. 🔄 **Dependent Types** - Planned

### 🔗 Reference

- Implementation audit: `admin/implementation-status.json`
- Rust implementations: `sources/rust-implementations/`
- Academic papers: `papers-archive/`
- Documentation: See project README and individual crate documentation
