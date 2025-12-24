# Foundational Papers on Cubical Type Theory

This bibliography lists key papers that introduced and developed Cubical Type Theory, focusing on its constructive approach to univalent foundations.


Key Papers

*   **Cohen, C., Coquand, T., Huber, S., & Mörtberg, A. (2018). *Cubical Type Theory: A constructive interpretation of the univalence axiom*.**
    *   **Contribution:** This paper is a landmark in the field, providing a comprehensive and constructive interpretation of the Univalence Axiom within a cubical type theory. It laid the groundwork for practical implementations of univalent mathematics.

*   **Huber, S. (2016). *A constructive model of the univalence axiom*.**
    *   **Contribution:** This work, often cited as a precursor to the more complete formulation, presented an early constructive model of the Univalence Axiom, demonstrating its feasibility within a cubical framework.

*   **Coquand, T., & Mörtberg, A. (2015). *Cubical Type Theory*.**
    *   **Contribution:** An earlier presentation of the ideas behind Cubical Type Theory, focusing on the basic definitions of cubes, paths, and connections, and how they can be used to model identity types constructively.

*   **Awodey, S., Coquand, T., & van den Berg, B. (2015). *Homotopy Type Theory and Cubical Sets*.**
    *   **Contribution:** This paper explores the connection between Homotopy Type Theory and cubical sets, providing a categorical perspective on the models of cubical type theory.

*   **Mörtberg, A., & Nordvall Forsberg, F. (2018). *Cubical Agda: A dependently typed programming language with univalence and higher inductive types*.**
    *   **Contribution:** This paper describes **Cubical Agda**, a proof assistant that implements Cubical Type Theory, making univalent mathematics and higher inductive types computationally accessible to users.


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
