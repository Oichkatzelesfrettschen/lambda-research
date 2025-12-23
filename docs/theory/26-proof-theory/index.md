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


## Overview

Proof theory focuses on the formal structure of proofs and their reduction properties. In the context of lambda calculus, this is primarily expressed through the **Curry-Howard Correspondence**, which establishes a bijection between natural deduction proofs and lambda terms. The primary research goal in this domain is often **Cut-Elimination** (or normalization), which guarantees that every proof can be reduced to a canonical, non-redundant form. This property is crucial for ensuring the consistency of the underlying logic and the termination of programs in the corresponding type system.

## Syntax

Proof-theoretic syntax typically uses **Sequent Calculus** or **Natural Deduction**. A typical sequent in intuitionistic logic is represented as:

\[ \Gamma \vdash A \]

Where:
- \(\Gamma\) is a set of assumptions (the context).
- \(\vdash\) is the entailment symbol.
- \(A\) is the formula being proved.

Under the Curry-Howard correspondence, this maps to:

\[ x_1:A_1, ..., x_n:A_n \vdash M : A \]

where \(M\) is a lambda term representing the proof.

## Resources

*   **Standardize Bibliography:** See [papers/bibliography.md](papers/bibliography.md) for 25+ foundational papers from Gödel, Gentzen, and Howard.
*   **Implementations:** Modern proof assistants like **Coq**, **Lean**, and **Agda** are practical implementations of higher-order proof theory.
*   **Further Reading:** 
    *   *Proofs and Types* by Jean-Yves Girard.
    *   *Structural Proof Theory* by Negri and von Plato.
    *   *Basic Proof Theory* by Troelstra and Schwichtenberg.
