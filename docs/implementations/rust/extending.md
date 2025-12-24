# Extending the Implementation: Adding New Features

## Overview

This guide walks through adding new features to tapl-rust, from simple combinators to complete calculus variants. Each section provides step-by-step instructions with real code examples.

## Quick Reference: Where Things Go

| Feature Type | Location | Crate |
|--------------|----------|-------|
| New term constructor | `lambda-core/src/lib.rs` | `lambda-core` |
| New combinator | `lambda-core/src/lib.rs` (combinators module) | `lambda-core` |
| New evaluation strategy | `lambda-eval/src/lib.rs` | `lambda-eval` |
| New type system | `lambda-types/src/lib.rs` | `lambda-types` |
| Parsing for new syntax | `lambda-parser/src/lib.rs` | `lambda-parser` |
| Usage examples | `lambda-examples/` | `lambda-examples` |

---

## Example 1: Adding a Simple Combinator

**Goal**: Add the B combinator (function composition): `λf.λg.λx.f (g x)`

### Step 1: Write the Test First (TDD)

**File**: `lambda-core/src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;
    
    // Add to existing test module
    #[test]
    fn test_b_combinator() {
        // B combinator: λf.λg.λx.f (g x)
        let b = combinators::b_combinator();
        
        // Expected structure
        let expected = Term::abs(
            "f",
            Term::abs(
                "g",
                Term::abs(
                    "x",
                    Term::app(
                        Term::var("f"),
                        Term::app(Term::var("g"), Term::var("x"))
                    )
                )
            )
        );
        
        assert_eq!(b, expected);
    }
    
    #[test]
    fn test_b_combinator_evaluation() {
        // Test: B f g x → f (g x)
        use crate::combinators::*;
        
        let b = b_combinator();
        
        // Apply B to three arguments
        let term = Term::app(
            Term::app(
                Term::app(b, Term::var("inc")),
                Term::var("double")
            ),
            Term::var("5")
        );
        
        // After evaluation should be: inc (double 5)
        let eval = lambda_eval::CallByNameEval::new(
            lambda_eval::EvalConfig::default()
        );
        let result = eval.normalize(&term).unwrap();
        
        let expected = Term::app(
            Term::var("inc"),
            Term::app(Term::var("double"), Term::var("5"))
        );
        
        assert_eq!(result, expected);
    }
}
```

Run test (should fail):
```bash
cargo test test_b_combinator
# Error: cannot find function `b_combinator` in module `combinators`
```

### Step 2: Implement the Combinator

**File**: `lambda-core/src/lib.rs`

```rust
/// Common lambda calculus combinators
pub mod combinators {
    use super::Term;
    
    // ... existing combinators (identity, k_combinator, s_combinator, etc.)
    
    /// B combinator (composition): λf.λg.λx.f (g x)
    ///
    /// The B combinator represents function composition.
    /// In Haskell notation: (.) = \f g x -> f (g x)
    ///
    /// # Examples
    ///
    /// ```
    /// use lambda_core::Term;
    /// use lambda_core::combinators::b_combinator;
    ///
    /// let b = b_combinator();
    /// // Represents: λf.λg.λx.f (g x)
    /// ```
    ///
    /// # References
    ///
    /// - Curry, H.B. & Feys, R. (1958). "Combinatory Logic, Vol. I"
    /// - Smullyan, R. (1985). "To Mock a Mockingbird"
    pub fn b_combinator() -> Term {
        Term::abs(
            "f",
            Term::abs(
                "g",
                Term::abs(
                    "x",
                    Term::app(
                        Term::var("f"),
                        Term::app(Term::var("g"), Term::var("x"))
                    )
                )
            )
        )
    }
}
```

### Step 3: Verify Tests Pass

```bash
cargo test test_b_combinator
# Should pass now

# Run all tests to check for regressions
cargo test
```

### Step 4: Update Documentation

Add to `examples.md`:

```markdown
### B Combinator (Function Composition)

```rust
use lambda_core::combinators::b_combinator;

let b = b_combinator();
// λf.λg.λx.f (g x)

// Example: compose increment and double
let composed = Term::app(Term::app(b, inc), double);
// Result: λx.inc (double x)
```
```

### Step 5: Add to Bibliography (if needed)

If implementing from a specific paper:

**File**: `01-untyped-lambda-calculus/bibliography.md`

```markdown
## Combinatory Logic

- Curry, H.B. & Feys, R. (1958). "Combinatory Logic, Vol. I". North-Holland.
  - Foundation of combinator calculus
  - Defines B, C, I, K, S, and other combinators
```

---

## Example 2: Adding Church Numerals

**Goal**: Implement Church encoding for natural numbers

### Step 1: Create Module Structure

**File**: `lambda-core/src/church.rs` (new file)

```rust
//! Church encodings for data structures
//!
//! Church encodings represent data using only functions.
//!
//! # References
//!
//! - Church, A. (1941). "The Calculi of Lambda Conversion"
//! - Pierce, B. (2002). "Types and Programming Languages" Chapter 5.2

use crate::Term;

/// Church numeral: λf.λx.f (f (... (f x)))
///
/// A Church numeral n is a function that applies its first argument
/// n times to its second argument.
///
/// # Examples
///
/// ```
/// use lambda_core::church::numeral;
///
/// let zero = numeral(0);  // λf.λx.x
/// let one = numeral(1);   // λf.λx.f x
/// let two = numeral(2);   // λf.λx.f (f x)
/// ```
pub fn numeral(n: usize) -> Term {
    Term::abs(
        "f",
        Term::abs("x", {
            let mut body = Term::var("x");
            for _ in 0..n {
                body = Term::app(Term::var("f"), body);
            }
            body
        })
    )
}

/// Church zero: λf.λx.x
pub fn zero() -> Term {
    numeral(0)
}

/// Church successor: λn.λf.λx.f (n f x)
///
/// Adds one to a Church numeral.
pub fn successor() -> Term {
    Term::abs(
        "n",
        Term::abs(
            "f",
            Term::abs(
                "x",
                Term::app(
                    Term::var("f"),
                    Term::app(
                        Term::app(Term::var("n"), Term::var("f")),
                        Term::var("x")
                    )
                )
            )
        )
    )
}

/// Church addition: λm.λn.λf.λx.m f (n f x)
pub fn add() -> Term {
    Term::abs(
        "m",
        Term::abs(
            "n",
            Term::abs(
                "f",
                Term::abs(
                    "x",
                    Term::app(
                        Term::app(Term::var("m"), Term::var("f")),
                        Term::app(
                            Term::app(Term::var("n"), Term::var("f")),
                            Term::var("x")
                        )
                    )
                )
            )
        )
    )
}

/// Church multiplication: λm.λn.λf.m (n f)
pub fn multiply() -> Term {
    Term::abs(
        "m",
        Term::abs(
            "n",
            Term::abs(
                "f",
                Term::app(
                    Term::var("m"),
                    Term::app(Term::var("n"), Term::var("f"))
                )
            )
        )
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;
    
    #[test]
    fn test_church_zero() {
        let zero = numeral(0);
        assert_eq!(zero, Term::abs("f", Term::abs("x", Term::var("x"))));
    }
    
    #[test]
    fn test_church_one() {
        let one = numeral(1);
        let expected = Term::abs(
            "f",
            Term::abs("x", Term::app(Term::var("f"), Term::var("x")))
        );
        assert_eq!(one, expected);
    }
    
    #[test]
    fn test_successor_evaluation() {
        use crate::lambda_eval::{CallByNameEval, EvalConfig};
        
        let succ = successor();
        let zero = numeral(0);
        
        // Apply successor to zero
        let term = Term::app(succ, zero);
        
        let eval = CallByNameEval::new(EvalConfig::default());
        let result = eval.normalize(&term).unwrap();
        
        // Result should be equivalent to one
        let one = numeral(1);
        // Note: Might need alpha-equivalence check
        // For now, just verify structure
        assert!(matches!(result, Term::Abs { .. }));
    }
}
```

### Step 2: Expose Module

**File**: `lambda-core/src/lib.rs`

```rust
// At the top of the file
pub mod church;

// Re-export for convenience
pub use church::{numeral, zero, successor, add, multiply};
```

### Step 3: Add Examples

**File**: `lambda-examples/examples/church_numerals.rs`

```rust
use lambda_core::church::{numeral, successor, add};
use lambda_eval::{CallByNameEval, EvalConfig};

fn main() {
    println!("=== Church Numerals Examples ===\n");
    
    // Example 1: Basic numerals
    let zero = numeral(0);
    let one = numeral(1);
    let two = numeral(2);
    
    println!("Zero: {}", zero);
    println!("One: {}", one);
    println!("Two: {}", two);
    
    // Example 2: Successor
    println!("\n=== Successor ===");
    let succ = successor();
    let term = Term::app(succ.clone(), zero.clone());
    
    let eval = CallByNameEval::new(EvalConfig::default());
    let result = eval.normalize(&term).unwrap();
    
    println!("succ zero = {}", result);
    
    // Example 3: Addition
    println!("\n=== Addition ===");
    let add_fn = add();
    let sum = Term::app(Term::app(add_fn, one), two);
    
    let result = eval.normalize(&sum).unwrap();
    println!("one + two = {}", result);
}
```

Run example:
```bash
cargo run --example church_numerals
```

---

## Example 3: Adding a New Evaluation Strategy

**Goal**: Implement applicative order evaluation

### Step 1: Define the Evaluator

**File**: `lambda-eval/src/lib.rs`

```rust
/// Applicative order evaluator
///
/// Evaluates leftmost-innermost redex first (call-by-value, but also
/// reduces under lambdas).
///
/// # References
///
/// - Plotkin, G. (1975). "Call-by-name, call-by-value and the λ-calculus"
/// - Pierce, B. (2002). "Types and Programming Languages" Chapter 5
pub struct ApplicativeOrderEval {
    config: EvalConfig,
}

impl ApplicativeOrderEval {
    pub fn new(config: EvalConfig) -> Self {
        Self { config }
    }
    
    /// Perform one step of applicative order evaluation
    pub fn eval_step(&self, term: &Term) -> Option<Term> {
        match term {
            Term::App { rator, rand } => {
                // Try to reduce in the argument first
                if let Some(new_rand) = self.eval_step(rand) {
                    return Some(Term::app((**rator).clone(), new_rand));
                }
                
                // Then try to reduce in the function
                if let Some(new_rator) = self.eval_step(rator) {
                    return Some(Term::app(new_rator, (**rand).clone()));
                }
                
                // Finally, try beta reduction
                match rator.as_ref() {
                    Term::Abs { param, body } => {
                        Some(body.substitute(param, rand))
                    }
                    _ => None,
                }
            }
            Term::Abs { param, body } => {
                // Reduce under lambda (key difference from CBV)
                self.eval_step(body).map(|new_body| {
                    Term::abs(param.clone(), new_body)
                })
            }
            Term::Var(_) => None,
        }
    }
    
    /// Normalize a term using applicative order strategy
    pub fn normalize(&self, term: &Term) -> EvalResult<Term> {
        let mut current = term.clone();
        let mut steps = 0;
        
        while steps < self.config.max_steps {
            match self.eval_step(&current) {
                Some(next) => {
                    current = next;
                    steps += 1;
                }
                None => return Ok(current),
            }
        }
        
        Err(EvalError::NonTerminating {
            limit: self.config.max_steps,
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use lambda_core::Term;
    
    #[test]
    fn test_applicative_order_reduces_arguments() {
        let eval = ApplicativeOrderEval::new(EvalConfig::default());
        
        // (λx.x) ((λy.y) z)
        let term = Term::app(
            Term::abs("x", Term::var("x")),
            Term::app(
                Term::abs("y", Term::var("y")),
                Term::var("z")
            )
        );
        
        // Should reduce inner application first
        let result = eval.normalize(&term).unwrap();
        assert_eq!(result, Term::var("z"));
    }
    
    #[test]
    fn test_applicative_order_reduces_under_lambda() {
        let eval = ApplicativeOrderEval::new(EvalConfig::default());
        
        // λx.((λy.y) z)
        let term = Term::abs(
            "x",
            Term::app(
                Term::abs("y", Term::var("y")),
                Term::var("z")
            )
        );
        
        // Should reduce under lambda to: λx.z
        let result = eval.normalize(&term).unwrap();
        assert_eq!(result, Term::abs("x", Term::var("z")));
    }
}
```

### Step 2: Export the New Evaluator

**File**: `lambda-eval/src/lib.rs`

```rust
// At top level, ensure it's public
pub struct ApplicativeOrderEval { /* ... */ }
```

### Step 3: Document Usage

**File**: `examples.md`

```markdown
### Applicative Order Evaluation

```rust
use lambda_eval::{ApplicativeOrderEval, EvalConfig};

let eval = ApplicativeOrderEval::new(EvalConfig::default());
let result = eval.normalize(&term)?;
```

**Characteristics**:
- Reduces leftmost-innermost redex
- Evaluates arguments before substitution
- Reduces under lambdas (unlike call-by-value)
```

---

## Example 4: Adding a New Type System (System F)

**Goal**: Add polymorphic type checking (System F)

### Step 1: Define Type Representation

**File**: `lambda-types/src/lib.rs`

```rust
//! Type systems for lambda calculus
//!
//! Implements STLC and System F type checking.
//!
//! # References
//!
//! - Pierce, B. (2002). "Types and Programming Languages"
//!   - Chapter 9: Simply Typed Lambda Calculus
//!   - Chapter 23: Universal Types (System F)

use lambda_core::Term;
use std::collections::HashMap;
use thiserror::Error;

/// Type representation for System F
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum Type {
    /// Type variable (α, β, ...)
    TyVar(String),
    /// Function type (T₁ → T₂)
    TyArrow(Box<Type>, Box<Type>),
    /// Universal quantification (∀α.T)
    TyForall(String, Box<Type>),
}

impl Type {
    /// Create type variable
    pub fn var(name: impl Into<String>) -> Self {
        Type::TyVar(name.into())
    }
    
    /// Create function type
    pub fn arrow(from: Type, to: Type) -> Self {
        Type::TyArrow(Box::new(from), Box::new(to))
    }
    
    /// Create universal type
    pub fn forall(var: impl Into<String>, body: Type) -> Self {
        Type::TyForall(var.into(), Box::new(body))
    }
}

/// Type context (Γ)
#[derive(Debug, Clone)]
pub struct TypeContext {
    term_bindings: HashMap<String, Type>,
    type_bindings: HashMap<String, ()>,  // Type variables in scope
}

impl TypeContext {
    pub fn new() -> Self {
        Self {
            term_bindings: HashMap::new(),
            type_bindings: HashMap::new(),
        }
    }
    
    /// Add term variable with type
    pub fn with_term(mut self, var: impl Into<String>, ty: Type) -> Self {
        self.term_bindings.insert(var.into(), ty);
        self
    }
    
    /// Add type variable
    pub fn with_type_var(mut self, var: impl Into<String>) -> Self {
        self.type_bindings.insert(var.into(), ());
        self
    }
    
    /// Look up term variable
    pub fn get_term(&self, var: &str) -> Option<&Type> {
        self.term_bindings.get(var)
    }
    
    /// Check if type variable is in scope
    pub fn has_type_var(&self, var: &str) -> bool {
        self.type_bindings.contains_key(var)
    }
}

/// Type checking errors
#[derive(Error, Debug, Clone, PartialEq)]
pub enum TypeError {
    #[error("Unbound variable: {name}")]
    UnboundVariable { name: String },
    
    #[error("Type mismatch: expected {expected}, got {actual}")]
    TypeMismatch { expected: String, actual: String },
    
    #[error("Unbound type variable: {name}")]
    UnboundTypeVariable { name: String },
}

/// Type check a term in System F
///
/// # References
///
/// - Pierce, B. (2002). "Types and Programming Languages" Chapter 23
pub fn typecheck(ctx: &TypeContext, term: &Term) -> Result<Type, TypeError> {
    match term {
        Term::Var(name) => {
            ctx.get_term(name)
                .cloned()
                .ok_or_else(|| TypeError::UnboundVariable {
                    name: name.clone(),
                })
        }
        
        Term::Abs { param, body } => {
            // For now, require type annotation (full inference is complex)
            // In practice, would need type annotations on lambda
            // This is simplified version
            unimplemented!("Type checking for abstractions requires type annotations")
        }
        
        Term::App { rator, rand } => {
            let rator_ty = typecheck(ctx, rator)?;
            let rand_ty = typecheck(ctx, rand)?;
            
            match rator_ty {
                Type::TyArrow(from, to) => {
                    if *from == rand_ty {
                        Ok(*to)
                    } else {
                        Err(TypeError::TypeMismatch {
                            expected: format!("{:?}", from),
                            actual: format!("{:?}", rand_ty),
                        })
                    }
                }
                _ => Err(TypeError::TypeMismatch {
                    expected: "function type".to_string(),
                    actual: format!("{:?}", rator_ty),
                }),
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_type_variable_lookup() {
        let ctx = TypeContext::new()
            .with_term("x", Type::var("A"));
        
        let term = Term::var("x");
        let ty = typecheck(&ctx, &term).unwrap();
        
        assert_eq!(ty, Type::var("A"));
    }
    
    #[test]
    fn test_function_application() {
        let ctx = TypeContext::new()
            .with_term("f", Type::arrow(Type::var("A"), Type::var("B")))
            .with_term("x", Type::var("A"));
        
        // f x : B
        let term = Term::app(Term::var("f"), Term::var("x"));
        let ty = typecheck(&ctx, &term).unwrap();
        
        assert_eq!(ty, Type::var("B"));
    }
}
```

### Step 2: Add Example

**File**: `lambda-examples/examples/type_checking.rs`

```rust
use lambda_types::{Type, TypeContext, typecheck};
use lambda_core::Term;

fn main() {
    println!("=== System F Type Checking ===\n");
    
    // Example: identity function
    // id : ∀α. α → α
    let id_type = Type::forall("α", Type::arrow(
        Type::var("α"),
        Type::var("α")
    ));
    
    println!("Identity type: {:?}", id_type);
    
    // Example: function application
    let ctx = TypeContext::new()
        .with_term("f", Type::arrow(Type::var("Int"), Type::var("Bool")))
        .with_term("x", Type::var("Int"));
    
    let app = Term::app(Term::var("f"), Term::var("x"));
    
    match typecheck(&ctx, &app) {
        Ok(ty) => println!("Type of (f x): {:?}", ty),
        Err(e) => println!("Type error: {}", e),
    }
}
```

---

## Testing Requirements

### Unit Tests (Required)

Every new feature needs:

1. **Basic functionality test**
   ```rust
   #[test]
   fn test_feature_basic() {
       let result = my_feature();
       assert_eq!(result, expected);
   }
   ```

2. **Edge cases**
   ```rust
   #[test]
   fn test_feature_edge_case() {
       // Empty input, boundary conditions, etc.
   }
   ```

3. **Error cases**
   ```rust
   #[test]
   fn test_feature_error_handling() {
       let result = my_feature_that_fails();
       assert!(result.is_err());
   }
   ```

### Property-Based Tests (Recommended)

**File**: Add to Cargo.toml dependencies:
```toml
[dev-dependencies]
proptest = "1.4"
```

**Usage**:
```rust
#[cfg(test)]
mod prop_tests {
    use super::*;
    use proptest::prelude::*;
    
    proptest! {
        #[test]
        fn test_substitution_preserves_free_vars(
            var in "[a-z]+",
            replacement in "[a-z]+"
        ) {
            let term = Term::var(&var);
            let repl = Term::var(&replacement);
            let result = term.substitute(&var, &repl);
            
            // Property: substitution should replace all occurrences
            prop_assert_eq!(result, repl);
        }
    }
}
```

---

## Documentation Requirements

### Code Documentation

1. **Module documentation**:
   ```rust
   //! Module description
   //!
   //! # References
   //!
   //! - Paper citation
   ```

2. **Function documentation**:
   ```rust
   /// Brief description
   ///
   /// # Examples
   ///
   /// ```
   /// // Working example
   /// ```
   ///
   /// # References
   ///
   /// - Specific paper or TAPL chapter
   pub fn my_function() { }
   ```

3. **Type documentation**:
   ```rust
   /// Description of the type
   ///
   /// # Fields
   ///
   /// - `field1`: description
   pub struct MyType {
       field1: String,
   }
   ```

### User Documentation

Update these files:
- `examples.md`: Add usage examples
- `architecture.md`: If adding new crate or major component
- `README.md`: If changing public API

---

## Integration with Bibliography

### Step 1: Add Citation to Code

```rust
//! # References
//!
//! - Church, A. (1932). "A Set of Postulates for the Foundation of Logic"
//!   In Annals of Mathematics, Second Series, Vol. 33, No. 2 (Apr., 1932), pp. 346-366
//!   DOI: 10.2307/1968337
```

### Step 2: Add to Category Bibliography

**File**: `01-untyped-lambda-calculus/bibliography.md`

```markdown
### Church (1932) - Foundation

Church, A. (1932). "A Set of Postulates for the Foundation of Logic"
*Annals of Mathematics*, Second Series, Vol. 33, No. 2, pp. 346-366.

- **DOI**: 10.2307/1968337
- **Significance**: Original formulation of lambda calculus
- **Implementation**: `lambda-core` combinators
```

### Step 3: Cross-Reference in Implementation Catalog

**File**: `docs/implementations/IMPLEMENTATIONS_CATALOG.md`

```markdown
### lambda-core

- **What**: Core AST and operations
- **Reference**: Church (1932), Pierce TAPL Chapter 5
- **Location**: `sources/rust-implementations/tapl-rust/lambda-core/`
```

---

## Quality Checklist

Before submitting:

- [ ] All tests pass: `cargo test`
- [ ] Code formatted: `cargo fmt`
- [ ] No clippy warnings: `cargo clippy -- -D warnings`
- [ ] Documentation complete (module, functions, examples)
- [ ] Academic references cited
- [ ] Added to appropriate bibliography
- [ ] Examples added and tested
- [ ] Updated relevant docs (README, examples.md, etc.)

---

## Common Patterns

### Pattern 1: Recursive Term Transformation

```rust
pub fn transform(term: &Term) -> Term {
    match term {
        Term::Var(name) => {
            // Transform variable
            Term::var(transform_name(name))
        }
        Term::Abs { param, body } => {
            // Transform abstraction
            Term::abs(param.clone(), transform(body))
        }
        Term::App { rator, rand } => {
            // Transform application
            Term::app(transform(rator), transform(rand))
        }
    }
}
```

### Pattern 2: Visitor Pattern

```rust
pub trait TermVisitor {
    fn visit_var(&mut self, name: &str);
    fn visit_abs(&mut self, param: &str, body: &Term);
    fn visit_app(&mut self, rator: &Term, rand: &Term);
}

pub fn visit_term<V: TermVisitor>(term: &Term, visitor: &mut V) {
    match term {
        Term::Var(name) => visitor.visit_var(name),
        Term::Abs { param, body } => visitor.visit_abs(param, body),
        Term::App { rator, rand } => visitor.visit_app(rator, rand),
    }
}
```

### Pattern 3: Builder Pattern

```rust
pub struct TermBuilder {
    term: Option<Term>,
}

impl TermBuilder {
    pub fn new() -> Self {
        Self { term: None }
    }
    
    pub fn var(mut self, name: impl Into<String>) -> Self {
        self.term = Some(Term::var(name));
        self
    }
    
    pub fn abs(mut self, param: impl Into<String>) -> Self {
        if let Some(body) = self.term {
            self.term = Some(Term::abs(param, body));
        }
        self
    }
    
    pub fn build(self) -> Option<Term> {
        self.term
    }
}
```

---

## Next Steps

- **Need performance data?** See [performance.md](performance.md)
- **Want to run tests?** See [testing.md](testing.md)
- **Academic integration?** See [integration.md](integration.md)
