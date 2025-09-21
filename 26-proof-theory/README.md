# Proof Theory

Proof theory is a major branch of mathematical logic that treats proofs themselves as formal mathematical objects, facilitating their analysis using mathematical techniques. Its development is deeply intertwined with the foundations of computer science, particularly in programming language theory, type systems, and automated reasoning.

## Core Concepts

*   **Formal Systems:** Proof theory studies formal systems for representing proofs, such as **Natural Deduction** and **Sequent Calculus**, both introduced by Gerhard Gentzen. These systems provide a rigorous foundation for studying the structure of proofs and are fundamental to the design of logic programming languages and theorem provers.

*   **Curry-Howard Correspondence:** This profound discovery reveals a direct correspondence between proofs in constructive logic and programs in typed lambda calculus. 
    *   Propositions correspond to Types.
    *   Proofs correspond to Programs.
    *   Proof normalization corresponds to Program evaluation.
    This isomorphism establishes a deep link between proof theory and programming language theory, allowing insights from one field to be applied to the other.

*   **Consistency and Foundations:** A primary goal of early proof theory, initiated by David Hilbert, was to provide a finitary proof of the consistency of mathematics. While Gödel's incompleteness theorems showed the limitations of this goal, the effort spurred the development of formal axiomatic systems and a deeper understanding of the limits of computation.

## Relevance to Lambda Calculus

Proof theory is not just related to lambda calculus; it is a parallel field that is in many ways equivalent. The Curry-Howard correspondence means that the study of type systems for lambda calculus *is* the study of proof systems. 

*   **Simply Typed Lambda Calculus** corresponds to basic propositional logic.
*   **System F (Polymorphic Lambda Calculus)** corresponds to second-order logic.
*   **The Calculus of Constructions** corresponds to higher-order logic.
*   **Linear Logic** (and thus linear lambda calculus) arose from a direct analysis of the structural rules of sequent calculus.

Understanding proof theory provides a deeper understanding of the design and properties of type systems.
