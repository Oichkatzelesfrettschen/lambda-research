# Foundational Papers in Proof Theory

This bibliography includes seminal works in proof theory that have had a significant impact on logic and computer science.


Key Papers

*   **Gödel, K. (1931). *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*.** 
    *   **Contribution:** Introduced the groundbreaking incompleteness theorems, demonstrating the inherent limitations of formal systems. This paper is a cornerstone of mathematical logic and theoretical computer science.

*   **Gentzen, G. (1935). *Untersuchungen über das logische Schließen I & II*.**
    *   **Contribution:** Introduced the formal proof systems of **Natural Deduction** and **Sequent Calculus**. These systems are foundational to modern proof theory and are widely used in computer science for automated reasoning and logic programming.

*   **Church, A. (1936). *An unsolvable problem of elementary number theory*.**
    *   **Contribution:** Introduced the **Lambda Calculus**, a universal model of computation that forms the basis of functional programming. While a paper on computability, its connection to logic via the Curry-Howard correspondence makes it essential to applied proof theory.

*   **Turing, A. M. (1936). *On Computable Numbers, with an Application to the Entscheidungsproblem*.**
    *   **Contribution:** Introduced the **Turing Machine**, another universal model of computation. This paper, along with Church's, laid the formal foundations for what is computable.

*   **Howard, W. A. (1980). *The formulae-as-types notion of construction*.**
    *   **Contribution:** This paper, originally written in 1969, explicitly describes the **Curry-Howard Correspondence**, linking proofs to programs. It formally establishes the deep connection between proof theory and programming language theory.

*   **Girard, J.-Y. (1987). *Linear logic*.**
    *   **Contribution:** Introduced **Linear Logic**, a refinement of classical and intuitionistic logic that pays close attention to resources. This was achieved by analyzing the structural rules of sequent calculus and has had a major impact on the design of programming languages and resource-aware computation.


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
