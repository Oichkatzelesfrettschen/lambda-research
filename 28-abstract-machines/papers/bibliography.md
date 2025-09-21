# Foundational Papers on Abstract Machines

This bibliography lists the key papers that introduced the most influential abstract machines for the lambda calculus.

## Key Papers

*   **Landin, P. J. (1964). *The mechanical evaluation of expressions*.**
    *   **Contribution:** This seminal paper introduced the **SECD machine**, one of the first abstract machines for evaluating lambda calculus expressions. It laid the groundwork for the implementation of functional programming languages.

*   **Krivine, J.-L. (1986). *A call-by-name lambda-calculus machine*.**
    *   **Contribution:** Introduced the **Krivine machine**, an elegant and efficient abstract machine for call-by-name evaluation. It has been influential in the development of lazy functional languages.

*   **Felleisen, M., & Friedman, D. P. (1986). *Control operators, the SECD machine, and the lambda-calculus*.**
    *   **Contribution:** This paper explores the relationship between control operators (like call/cc) and the SECD machine, leading to the development of the **CEK machine**, which makes the continuation explicit.

*   **Johnsson, T. (1984). *Efficient compilation of lazy evaluation*.**
    *   **Contribution:** This paper introduced the **G-machine**, a graph-reduction-based abstract machine designed for the efficient compilation of lazy functional languages like Haskell. This was a major breakthrough in making lazy evaluation practical.

*   **Ager, M. S., Biernacki, D., Danvy, O., & Midtgaard, J. (2003). *A Functional Correspondence between Evaluators and Abstract Machines*.**
    *   **Contribution:** This paper (and others by the same authors) establishes a formal correspondence between interpreters (evaluators) and abstract machines. It shows how to derive an abstract machine from an evaluator through a series of program transformations, providing a deep understanding of the relationship between these two implementation techniques.
