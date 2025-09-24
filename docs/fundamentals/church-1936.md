# Church (1936): An Unsolvable Problem of Elementary Number Theory

**The paper that invented lambda calculus**

---

## Why This Paper Matters

This is where it all began. In 1936, Alonzo Church was trying to solve the **Entscheidungsproblem** (German for "decision problem") - the question of whether there exists an algorithm that can determine if any given mathematical statement is true or false.

Church's answer was revolutionary: **No, such an algorithm cannot exist.** To prove this, he invented lambda calculus as a way to represent all possible computations.

---

## What You'll Learn

- **Lambda notation**: How to write functions using `λ`
- **Church numerals**: Representing numbers using pure functions
- **Undecidability**: Why some problems have no algorithmic solution
- **Historical context**: The birth of theoretical computer science

---

## Before You Read

**Prerequisites**: Basic logic, comfort with mathematical notation, high school algebra

**Difficulty**: 🟡 Intermediate - The paper is from 1936, so the writing style is formal and mathematical. Don't worry if you don't understand everything on the first reading.

**Time needed**: 2-3 hours for careful reading

---

## The Paper

<!-- PDF Viewer for Church (1936) Paper -->
<div class="pdf-viewer-container">
  <div class="pdf-controls">
    <h4>[PDF] Church (1936) - An Unsolvable Problem</h4>
    <div class="pdf-actions">
      <a href="/lambda-research/papers/essential/1936_church_unsolvable_problem_oa.pdf"
         target="_blank" class="btn-download">
        Download PDF
      </a>
      <a href="https://mozilla.github.io/pdf.js/web/viewer.html?file=https://oichkatzelesfrettschen.github.io/lambda-research/papers/essential/1936_church_unsolvable_problem_oa.pdf"
         target="_blank" class="btn-external">
        Open PDF Viewer
      </a>
    </div>
  </div>

  <div class="pdf-embed">
    <iframe src="https://mozilla.github.io/pdf.js/web/viewer.html?file=https://oichkatzelesfrettschen.github.io/lambda-research/papers/essential/1936_church_unsolvable_problem_oa.pdf"
            width="100%"
            height="600px"
            frameborder="0">
      <p>Your browser doesn't support embedded PDFs.
         <a href="/lambda-research/papers/essential/1936_church_unsolvable_problem_oa.pdf">Download the PDF</a> instead.
      </p>
    </iframe>
  </div>

  <div class="pdf-fallback">
    <details>
      <summary>[MOBILE] PDF not loading?</summary>
      <p>Some mobile browsers have issues with embedded PDFs. Try:</p>
      <ul>
        <li><a href="/lambda-research/papers/essential/1936_church_unsolvable_problem_oa.pdf">Direct download link</a></li>
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

@media (max-width: 768px) {
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

### Lambda Notation
Church introduces the notation `λx.E` to mean "a function that takes input `x` and returns `E`".

**Modern equivalents**:
- JavaScript: `x => E`
- Python: `lambda x: E`
- Haskell: `\x -> E`

### Church Numerals
Church shows how to represent numbers using only functions:
- `0 = λf.λx.x` (apply function f zero times)
- `1 = λf.λx.f x` (apply function f once)
- `2 = λf.λx.f(f x)` (apply function f twice)

This was mind-blowing in 1936 - you can do arithmetic with pure functions!

### The Undecidability Result
Church proves that no algorithm can solve the Entscheidungsproblem by:
1. Showing how to encode any computation as lambda calculus
2. Constructing a self-referential statement that breaks any supposed decision algorithm
3. This is the same idea behind the halting problem

---

## Historical Context

**1930s Mathematics**: Hilbert's program sought to formalize all mathematics. Church, Gödel, and Turing showed this was impossible.

**What was new**: The idea that computation itself could be studied mathematically.

**Impact**: Led to the development of programming languages, type theory, and theoretical computer science.

---

## Common Confusions

**"Why use λ instead of f(x)?"** Lambda calculus is about functions as first-class objects. `λx.x+1` IS the function, not just its application to some value.

**"What's the big deal about undecidability?"** It means there are fundamental limits to what computers can do - some problems have no algorithmic solution.

**"Is this just historical?"** No! Lambda calculus is the foundation of functional programming and modern type theory.

---

## Discussion Questions

1. How does Church's encoding of numbers relate to modern programming concepts?
2. What are the philosophical implications of undecidability?
3. How might computation look different if Church had made different choices?

---

## What's Next?

After reading this paper, you should:

1. **Try the exercises**: Work through some lambda calculus reductions by hand
2. **Move to Girard (1989)**: For a more modern, readable introduction to the practical side
3. **Explore implementations**: Build your own lambda calculus interpreter

---

## Additional Resources

- **Wikipedia**: [Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus) - Good overview with examples
- **Interactive Tutorial**: [Lambda Calculus for Beginners](https://crypto.stanford.edu/~blynn/lambda/) - Try lambda calculus in your browser
- **Modern Treatment**: Pierce's "Types and Programming Languages" Chapter 5

---

## Questions or Stuck?

Having trouble with the paper? Found an error? Want to discuss concepts?

[Open the repository](https://github.com/Oichkatzelesfrettschen/lambda-research) - we're here to help!

---

*Next: [Girard (1989) - Proofs and Types](girard-1989.md) - A more accessible introduction to the practical applications of lambda calculus.*
