# Girard (1989): Proofs and Types

**The bridge between logic and computation**

---

## Why This Paper Matters

Jean-Yves Girard's "Proofs and Types" is one of the most accessible introductions to the **Curry-Howard correspondence** - the profound connection between mathematical proofs and computer programs.

Written in 1989, this paper explains how:
- **Types correspond to propositions** (logical statements)
- **Programs correspond to proofs** (logical derivations)
- **Program execution corresponds to proof simplification**

---

## What You'll Learn

- **The Curry-Howard isomorphism**: How types and logic mirror each other
- **System F**: The second-order lambda calculus with polymorphism
- **Linear logic basics**: How to reason about computational resources
- **Practical applications**: Why this matters for modern programming

---

## Before You Read

**Prerequisites**: Church (1936) or basic lambda calculus, elementary logic

**Difficulty**: [EASY] Beginner-friendly - Girard writes clearly for newcomers

**Time needed**: 3-4 hours for careful reading

---

## The Paper

<!-- PDF Viewer for Girard (1989) Paper -->
<div class="pdf-viewer-container">
  <div class="pdf-controls">
    <h4>[PDF] Girard (1989) - Proofs and Types</h4>
    <div class="pdf-actions">
      <a href="/lambda-research/papers/essential/1989_girard_proofs_types_oa.pdf"
         target="_blank" class="btn-download">
        Download PDF
      </a>
      <a href="https://mozilla.github.io/pdf.js/web/viewer.html?file=https://oichkatzelesfrettschen.github.io/lambda-research/papers/essential/1989_girard_proofs_types_oa.pdf"
         target="_blank" class="btn-external">
        Open PDF Viewer
      </a>
    </div>
  </div>

  <div class="pdf-embed">
    <iframe src="https://mozilla.github.io/pdf.js/web/viewer.html?file=https://oichkatzelesfrettschen.github.io/lambda-research/papers/essential/1989_girard_proofs_types_oa.pdf"
            width="100%"
            height="600px"
            frameborder="0">
      <p>Your browser doesn't support embedded PDFs.
         <a href="/lambda-research/papers/essential/1989_girard_proofs_types_oa.pdf">Download the PDF</a> instead.
      </p>
    </iframe>
  </div>

  <div class="pdf-fallback">
    <details>
      <summary>[MOBILE] PDF not loading?</summary>
      <p>Some mobile browsers have issues with embedded PDFs. Try:</p>
      <ul>
        <li><a href="/lambda-research/papers/essential/1989_girard_proofs_types_oa.pdf">Direct download link</a></li>
        <li>Opening in your device's PDF app</li>
        <li>Using a desktop browser</li>
      </ul>
    </details>
  </div>
</div>

<style>
.pdf-viewer-container {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 1rem 0;
  background: #f9f9f9;
}

.pdf-controls {
  background: #f0f0f0;
  padding: 1rem;
  border-bottom: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.pdf-controls h4 {
  margin: 0;
  font-size: 1.1em;
  color: #333;
}

.pdf-actions {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.pdf-actions a {
  background: #007acc;
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.9em;
  transition: background 0.2s;
}

.pdf-actions a:hover {
  background: #005999;
}

.pdf-fallback {
  padding: 1rem;
  background: #fff;
  border-top: 1px solid #ddd;
}

.pdf-fallback summary {
  cursor: pointer;
  font-weight: bold;
  color: #666;
}

.pdf-fallback ul {
  margin: 0.5rem 0 0 1rem;
}

<span>@</span>media (max-width: 768px) {
  .pdf-controls {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }
  .pdf-actions {
    justify-content: center;
  }
  .pdf-embed iframe {
    height: 400px;
  }
}
</style>

---

## Key Concepts Explained

### The Curry-Howard Correspondence

Girard shows the beautiful connection between:

| **Logic** | **Computation** |
|-----------|-----------------|
| Proposition A | Type A |
| Proof of A | Program of type A |
| A implies B | Function type A → B |
| Proof simplification | Program execution |

### System F (Second-Order Lambda Calculus)

Girard introduces **polymorphic types**:
- `∀X. X → X` is the type of the identity function for any type X
- This enables generic programming before languages had generics
- Strong normalization: all System F programs terminate

### Linear Logic Preview

Girard hints at his later invention of linear logic:
- Traditional logic allows unlimited use of assumptions
- Linear logic tracks how many times each assumption is used
- This leads to better resource management in programming

---

## Historical Context

**Late 1980s Computing**: Object-oriented programming was dominant. Girard showed that functional programming had deeper mathematical foundations.

**What was revolutionary**: The idea that there's a fundamental correspondence between mathematical reasoning and computation.

**Impact**: Led to modern dependently typed languages and proof assistants.

---

## Practical Examples

### In Haskell
```haskell
-- The type forall a. a -> a corresponds to the logical proposition ∀X. X ⊃ X
identity :: forall a. a -> a
identity x = x

-- This is a proof that "for any proposition X, X implies X"
```

### In Rust
```rust
// Generic functions are proofs of universal statements
fn identity<T>(x: T) -> T {
    x  // This code IS the proof
}
```

---

## Common Confusions

**"How can code be a proof?"** In constructive logic, to prove "there exists an X such that P(X)" you must construct a specific X. Programs are these constructions.

**"Why does this matter practically?"** Modern type systems prevent bugs by ensuring your program's logic is sound. Types catch logical errors at compile time.

**"Is this just theoretical?"** No! Modern languages like Haskell, Rust, and F# use these ideas extensively.

---

## Discussion Questions

1. How does the Curry-Howard correspondence change how you think about types?
2. What are the implications of "programs as proofs" for software verification?
3. How might programming languages evolve if more programmers understood this connection?

---

## What's Next?

After reading this paper, you should:

1. **Try dependent types**: Explore Agda or Idris where the correspondence is even clearer
2. **Study System F**: Understand polymorphism from a theoretical perspective
3. **Explore proof assistants**: Try Coq or Lean to see proofs-as-programs in action

---

## Additional Resources

- **Girard's Linear Logic Paper**: The follow-up that revolutionized resource-aware computation
- **Wadler's "Propositions as Types"**: Excellent modern explanation of Curry-Howard
- **Agda Tutorial**: See the correspondence in action with dependent types

---

## Questions or Stuck?

Having trouble with the paper? Want to discuss the philosophical implications?

[Open the repository](https://github.com/Oichkatzelesfrettschen/lambda-research) - we're here to help!

---

*Next: Move to [Advanced Topics](../advanced/index.md) for dependent types and linear logic, or try the [Implementations](../implementations/index.md) to see these ideas in working code.*
