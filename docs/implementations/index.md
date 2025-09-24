# Lambda Calculus Implementations

**Learn by building: working code you can run and modify**

---

## Why Implement Lambda Calculus?

Building your own lambda calculus interpreter is one of the best ways to truly understand how computation works. You'll see how:

- **Variables and binding** work in practice
- **Function application** is actually implemented
- **Type checking** prevents runtime errors
- **Evaluation strategies** affect performance

---

## Our Implementation Collection

### [PYTHON] Python: Untyped Lambda Calculus
**Perfect for beginners** - Python's simplicity lets you focus on the core concepts.

- **Features**: Variables, abstraction, application, beta reduction
- **Highlights**: Church numerals, combinators, normalization
- **Time to understand**: 2-3 hours
- **Prerequisites**: Basic Python knowledge

[EXPLORE] Explore Implementation](untyped-lambda-python.md)

```python
# Example: Identity function
identity = Abstraction("x", Variable("x"))
result = apply(identity, Variable("y"))  # Returns Variable("y")
```

---

### [HASKELL] Haskell: Simply Typed Lambda Calculus
**Next step up** - Adds types for safety and explores Haskell's lambda calculus roots.

- **Features**: Type checking, base types (Int, Bool), function types
- **Highlights**: Type inference, type errors, strong normalization
- **Time to understand**: 3-4 hours
- **Prerequisites**: Basic Haskell or functional programming

[EXPLORE] Explore Implementation](simply-typed-haskell.md)

```haskell
-- Example: Typed identity function
identity :: forall a. a -> a
identity x = x
```

---

## Learning Path

### [START] Start Here: Python Untyped
1. **Read the code** - Start with [untyped-lambda-python.md](untyped-lambda-python.md)
2. **Run examples** - Try the Church numeral examples
3. **Modify it** - Add new combinators or change evaluation order
4. **Understand substitution** - This is the trickiest part!

### [NEXT] Then Try: Haskell Typed
1. **Compare with Python** - See how types change everything
2. **Break it intentionally** - Try type errors to understand the checker
3. **Extend it** - Add new base types or operations
4. **Explore inference** - How does Haskell figure out types?

---

## Extension Ideas

### Easy Extensions (Weekend Projects)
- **Add new base types**: Strings, lists, or booleans
- **Better error messages**: Show where substitution fails
- **Pretty printing**: Make lambda terms readable
- **REPL**: Interactive interpreter for experimentation

### Medium Extensions (Week-long Projects)
- **Let bindings**: Add `let x = M in N` syntax
- **Recursion**: Implement fixed-point combinators
- **Pattern matching**: Simple patterns like `case` expressions
- **Module system**: Separate namespaces for definitions

### Advanced Extensions (Month-long Projects)
- **Type inference**: Hindley-Milner algorithm implementation
- **Dependent types**: Simple dependent function types
- **Linear types**: Track resource usage like Rust
- **Effects**: Model IO, exceptions, or state

---

## Implementation Resources

### Other Languages to Try
Once you understand the basics, try implementing in:

- **OCaml**: Pattern matching makes ASTs elegant
- **Rust**: Ownership types teach you about binding and scope
- **JavaScript**: Web-based interpreters for interactive learning
- **C++**: Understanding memory management in interpreters

### Helpful Libraries
- **Parsing**: Use parser combinators (Parsec, nom, etc.)
- **Pretty printing**: Libraries for formatting output nicely
- **Testing**: Property-based testing for language implementations

---

## Real-World Connections

### Production Languages
See how these ideas appear in real systems:
- **JavaScript closures**: Basically lambda calculus
- **Haskell**: Direct implementation of typed lambda calculus
- **Lisp/Scheme**: Untyped lambda calculus with extra features
- **ML/OCaml**: Practical typed functional programming

### Advanced Systems
More complex implementations to study:
- **GHC**: Haskell compiler (millions of lines, very advanced)
- **OCaml compiler**: Smaller, more readable implementation
- **Racket**: Lisp with amazing macro system
- **Idris**: Dependent types for practical programming

---

## Getting Help

### When You're Stuck
1. **Read the papers** - [Fundamentals](../fundamentals/index.md) explain the theory
2. **Check existing code** - Both implementations have detailed comments
3. **Try simpler examples** - Start with identity function, work up
4. **Ask questions** - Use GitHub issues for this repository

### Common Pitfalls
- **Variable capture**: Make sure bound variables don't clash
- **Substitution bugs**: The hardest part to get right
- **Infinite loops**: Some lambda terms never terminate
- **Type errors**: In typed versions, understand when and why they occur

---

## Beyond These Examples

### Academic Implementations
- **Mini-ML**: Standard teaching implementation
- **System F**: Polymorphic types (very advanced)
- **Calculus of Constructions**: Full dependent types

### Production-Ready
- **Write your own language**: Start with lambda calculus, add features
- **Contribute to existing languages**: Many are open source
- **Build DSLs**: Domain-specific languages for specific problems

---

*Ready to build? Start with [Python Untyped Lambda Calculus](untyped-lambda-python.md) and see computation come to life in code you wrote yourself.*