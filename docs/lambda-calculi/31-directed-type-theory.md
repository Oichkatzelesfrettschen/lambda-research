# Directed Type Theory

Directed Type Theory (DTT) is a modern development in type theory that extends traditional type theory by incorporating an asymmetric notion of transformation or "directed paths" between elements of a type. Unlike symmetric type theories like Homotopy Type Theory (HoTT), where paths are invertible (like in topology), DTT focuses on non-invertible transformations, making it suitable for modeling phenomena with inherent directionality, such as computation, causality, and categorical structures.

## Core Concepts

*   **Directed Paths/Morphisms:** In DTT, the fundamental notion of equality is replaced or augmented by a concept of a "directed path" or "morphism" from one term to another. This reflects the idea that a transformation might go in one direction but not necessarily be reversible.

*   **Higher Categories:** DTT provides a synthetic framework for reasoning about **higher categories**. Just as HoTT interprets types as spaces and identity types as paths, DTT interprets types as higher categories and directed paths as higher morphisms within those categories.

*   **Variance:** DTT explicitly handles variance (covariant and contravariant dependencies) at a foundational level, which is crucial for modeling categorical structures and programming language features like subtyping.

*   **Homomorphism Type:** Instead of just an identity type, DTT often introduces a "homomorphism type" that captures the concept of a morphism from category theory or a directed path from directed homotopy theory. This type is distinct from the symmetric identity type.

*   **Directed Univalence:** Similar to the Univalence Axiom in HoTT, there are proposals for "directed univalence" principles in DTT, which would equate equivalent directed structures with identical ones.

## Relevance to Lambda Calculus and Category Theory

DTT offers a powerful new perspective on the foundations of mathematics and computer science, particularly in areas where directionality is important:

*   **Synthetic Category Theory:** DTT provides a language for doing synthetic category theory, allowing mathematicians to reason about categories, functors, and natural transformations directly within the type theory, without relying on set-theoretic encodings.

*   **Programming Language Semantics:** It has potential applications in programming language semantics, especially for languages with effects, concurrency, or resource management, where transformations are often directed and not easily reversible.

*   **Modeling Computation:** The directed nature of DTT makes it a natural fit for modeling computational processes, which inherently proceed in a specific direction.

*   **Extension of HoTT:** DTT can be seen as an extension of HoTT, providing tools to reason about structures that are not necessarily invertible, thus broadening the scope of univalent foundations.
