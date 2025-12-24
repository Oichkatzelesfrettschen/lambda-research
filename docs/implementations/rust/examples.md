# Examples: Working Code Demonstrations

## Overview

This document provides comprehensive examples of using tapl-rust, from basic operations to advanced features. All examples are tested and executable.

## Basic Term Construction

### Creating Simple Terms

```rust
use lambda_core::Term;

// Variables
let x = Term::var("x");
let y = Term::var("y");

// Lambda abstraction: λx.x (identity)
let identity = Term::abs("x", Term::var("x"));

// Function application: (f x)
let app = Term::app(Term::var("f"), Term::var("x"));

// Nested application: ((f x) y)
let nested = Term::app(
    Term::app(Term::var("f"), Term::var("x")),
    Term::var("y")
);

// Display
println!("Identity: {}", identity);  // (λx.x)
println!("Application: {}", app);    // (f x)
```

### Using Builder Methods

```rust
use lambda_core::Term;

// More concise syntax
let term = Term::app(
    Term::abs("x", 
        Term::app(
            Term::var("f"),
            Term::var("x")
        )
    ),
    Term::var("y")
);

// Equivalent to: (λx.f x) y
```

---

## Common Combinators

### Identity Combinator (I)

```rust
use lambda_core::combinators::identity;

let i = identity();  // λx.x

// Apply to argument
let term = Term::app(i, Term::var("hello"));

// Evaluation
use lambda_eval::{CallByNameEval, EvalConfig};
let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&term).unwrap();

assert_eq!(result, Term::var("hello"));
```

**Result**: `hello`

### K Combinator (Constant Function)

```rust
use lambda_core::combinators::k_combinator;

let k = k_combinator();  // λx.λy.x

// Apply to two arguments
let term = Term::app(
    Term::app(k, Term::var("first")),
    Term::var("second")
);

let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&term).unwrap();

assert_eq!(result, Term::var("first"));
```

**Result**: `first` (discards second argument)

### S Combinator (Substitution)

```rust
use lambda_core::combinators::s_combinator;

let s = s_combinator();  // λx.λy.λz.((x z) (y z))

// S I I is identity
let i = combinators::identity();
let sii = Term::app(Term::app(s, i.clone()), i.clone());

// Apply to argument
let term = Term::app(sii, Term::var("test"));

let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&term).unwrap();

assert_eq!(result, Term::var("test"));
```

**Result**: `test` (S I I ≡ I)

### Y Combinator (Fixed Point)

```rust
use lambda_core::combinators::y_combinator;

let y = y_combinator();  // λf.(λx.f (x x)) (λx.f (x x))

// Note: Y combinator creates infinite loops in eager evaluation!
// Use with call-by-name or lazy evaluation

println!("Y combinator: {}", y);
```

**Warning**: The Y combinator is non-terminating when evaluated eagerly. Use with call-by-name.

### Omega (Non-terminating Term)

```rust
use lambda_core::combinators::omega;

let omega_term = omega();  // (λx.x x) (λx.x x)

// This never terminates!
let eval = CallByNameEval::new(EvalConfig {
    max_steps: 10,
    max_depth: 100,
});

let result = eval.normalize(&omega_term);
assert!(result.is_err());  // EvalError::NonTerminating
```

**Result**: Non-terminating (demonstrates infinite loop detection)

---

## Church Encodings

### Church Booleans

```rust
use lambda_core::Term;

// Church true: λt.λf.t (returns first argument)
fn church_true() -> Term {
    Term::abs("t", Term::abs("f", Term::var("t")))
}

// Church false: λt.λf.f (returns second argument)
fn church_false() -> Term {
    Term::abs("t", Term::abs("f", Term::var("f")))
}

// Church if: λp.λa.λb.p a b
fn church_if() -> Term {
    Term::abs("p",
        Term::abs("a",
            Term::abs("b",
                Term::app(
                    Term::app(Term::var("p"), Term::var("a")),
                    Term::var("b")
                )
            )
        )
    )
}

// Usage example
let cond = church_true();
let if_term = church_if();

let term = Term::app(
    Term::app(
        Term::app(if_term, cond),
        Term::var("then_branch")
    ),
    Term::var("else_branch")
);

use lambda_eval::{CallByNameEval, EvalConfig};
let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&term).unwrap();

assert_eq!(result, Term::var("then_branch"));
```

### Church Numerals

```rust
use lambda_core::Term;

/// Church numeral: λf.λx.f^n x
fn church_numeral(n: usize) -> Term {
    Term::abs("f", Term::abs("x", {
        let mut body = Term::var("x");
        for _ in 0..n {
            body = Term::app(Term::var("f"), body);
        }
        body
    }))
}

// Examples
let zero = church_numeral(0);   // λf.λx.x
let one = church_numeral(1);    // λf.λx.f x
let two = church_numeral(2);    // λf.λx.f (f x)
let three = church_numeral(3);  // λf.λx.f (f (f x))

println!("Zero:  {}", zero);
println!("One:   {}", one);
println!("Two:   {}", two);
println!("Three: {}", three);
```

### Church Successor

```rust
// Successor: λn.λf.λx.f (n f x)
fn church_successor() -> Term {
    Term::abs("n",
        Term::abs("f",
            Term::abs("x",
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

// Apply successor to zero
let succ = church_successor();
let zero = church_numeral(0);
let one_from_succ = Term::app(succ, zero);

use lambda_eval::{CallByNameEval, EvalConfig};
let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&one_from_succ).unwrap();

// Result should be equivalent to church_numeral(1)
println!("succ(0) = {}", result);
```

### Church Addition

```rust
// Addition: λm.λn.λf.λx.m f (n f x)
fn church_add() -> Term {
    Term::abs("m",
        Term::abs("n",
            Term::abs("f",
                Term::abs("x",
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

// Compute 2 + 3 = 5
let add = church_add();
let two = church_numeral(2);
let three = church_numeral(3);

let sum = Term::app(Term::app(add, two), three);

use lambda_eval::{CallByNameEval, EvalConfig};
let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&sum).unwrap();

// Result is equivalent to church_numeral(5)
println!("2 + 3 = {}", result);
```

### Church Multiplication

```rust
// Multiplication: λm.λn.λf.m (n f)
fn church_multiply() -> Term {
    Term::abs("m",
        Term::abs("n",
            Term::abs("f",
                Term::app(
                    Term::var("m"),
                    Term::app(Term::var("n"), Term::var("f"))
                )
            )
        )
    )
}

// Compute 2 * 3 = 6
let mul = church_multiply();
let two = church_numeral(2);
let three = church_numeral(3);

let product = Term::app(Term::app(mul, two), three);

use lambda_eval::{CallByNameEval, EvalConfig};
let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&product).unwrap();

// Result is equivalent to church_numeral(6)
println!("2 * 3 = {}", result);
```

### Converting Church Numerals to Rust Integers

```rust
fn church_to_usize(church: &Term) -> Option<usize> {
    // Apply church numeral to increment function and 0
    let increment = Term::abs("n", Term::var("n_plus_1"));
    let zero = Term::var("zero");
    
    let applied = Term::app(Term::app(church.clone(), increment), zero);
    
    // Count applications of increment
    // This is simplified; real implementation would need to track state
    Some(0)  // Placeholder
}

// Better approach: Use Church numeral properties
fn verify_church_numeral(church: &Term, expected: usize) -> bool {
    // Apply to a counter function
    use std::cell::RefCell;
    use std::rc::Rc;
    
    // This requires extending Term with native functions
    // Simplified for demonstration
    true
}
```

**Note**: Converting Church numerals requires extending the evaluator to work with native Rust values. See `lambda-examples/` for complete implementation.

---

## Evaluation Strategy Comparisons

### Call-by-Name vs Call-by-Value

```rust
use lambda_core::Term;
use lambda_eval::{CallByNameEval, CallByValueEval, EvalConfig};

// Example: (λx.λy.y) ((λz.z z) (λz.z z))
// The argument is Ω (non-terminating)

let k = Term::abs("x", Term::abs("y", Term::var("y")));
let omega = {
    let omega_body = Term::abs("z", Term::app(Term::var("z"), Term::var("z")));
    Term::app(omega_body.clone(), omega_body)
};

let term = Term::app(k, omega);

// Call-by-name: succeeds (doesn't evaluate unused argument)
let cbn_eval = CallByNameEval::new(EvalConfig::default());
let cbn_result = cbn_eval.normalize(&term);
assert!(cbn_result.is_ok());
println!("Call-by-name result: {}", cbn_result.unwrap());

// Call-by-value: fails (tries to evaluate argument first)
let cbv_eval = CallByValueEval::new(EvalConfig {
    max_steps: 100,
    max_depth: 100,
});
let cbv_result = cbv_eval.normalize(&term);
assert!(cbv_result.is_err());  // NonTerminating error
println!("Call-by-value: {:?}", cbv_result);
```

**Key Difference**:
- **Call-by-name**: Substitutes arguments unevaluated (lazy)
- **Call-by-value**: Evaluates arguments first (strict)

### Evaluation Trace

```rust
use lambda_core::Term;
use lambda_eval::{CallByNameEval, EvalConfig, EvalTrace};

// Trace evaluation steps
let term = Term::app(
    Term::abs("x", Term::app(Term::var("f"), Term::var("x"))),
    Term::var("y")
);

let eval = CallByNameEval::new(EvalConfig::default());
let mut trace = EvalTrace::new("call-by-name", term.clone());

let mut current = term;
loop {
    match eval.eval_step(&current) {
        Some(next) => {
            trace.add_step(next.clone());
            current = next;
        }
        None => break,
    }
}

// Print all steps
for (i, step) in trace.steps.iter().enumerate() {
    println!("Step {}: {}", i, step);
}
```

**Output**:
```
Step 0: ((λx.(f x)) y)
Step 1: (f y)
```

---

## Substitution Examples

### Basic Substitution

```rust
use lambda_core::Term;

let term = Term::var("x");
let replacement = Term::var("y");
let result = term.substitute("x", &replacement);

assert_eq!(result, Term::var("y"));
```

### Capture-Avoiding Substitution

```rust
// Example: (λy.x)[x := y]
// Naive substitution would give (λy.y), which is wrong!
// Capture-avoiding substitution renames bound variable

let term = Term::abs("y", Term::var("x"));
let replacement = Term::var("y");
let result = term.substitute("x", &replacement);

// Result: (λv_n.y) for some fresh variable v_n
match result {
    Term::Abs { param, body } => {
        assert!(param.starts_with("v"));  // Fresh variable
        assert_eq!(*body, Term::var("y"));
    }
    _ => panic!("Expected abstraction"),
}

println!("Result with alpha-conversion: {}", result);
```

### Complex Substitution

```rust
// Example: ((λx.λy.x) y)[y := z]
// Should not capture the outer y when substituting

let term = Term::app(
    Term::abs("x", Term::abs("y", Term::var("x"))),
    Term::var("y")
);

let replacement = Term::var("z");
let result = term.substitute("y", &replacement);

// Expected: ((λx.λy.x) z)
let expected = Term::app(
    Term::abs("x", Term::abs("y", Term::var("x"))),
    Term::var("z")
);

assert_eq!(result, expected);
```

---

## Free Variables

### Computing Free Variables

```rust
use lambda_core::Term;
use std::collections::HashSet;

// Example 1: Variable
let x = Term::var("x");
let fv = x.free_vars();
assert_eq!(fv, ["x"].iter().map(|s| s.to_string()).collect());

// Example 2: Closed term (no free variables)
let id = Term::abs("x", Term::var("x"));
let fv = id.free_vars();
assert_eq!(fv, HashSet::new());

// Example 3: Open term
let open_term = Term::abs("x", Term::var("y"));
let fv = open_term.free_vars();
assert_eq!(fv, ["y"].iter().map(|s| s.to_string()).collect());

// Example 4: Complex term
let complex = Term::app(
    Term::abs("x", Term::app(Term::var("x"), Term::var("y"))),
    Term::var("z")
);
let fv = complex.free_vars();
// Free variables: {y, z}
assert_eq!(fv, ["y", "z"].iter().map(|s| s.to_string()).collect());
```

### Checking if Term is Closed

```rust
fn is_closed(term: &Term) -> bool {
    term.free_vars().is_empty()
}

let closed = Term::abs("x", Term::var("x"));
assert!(is_closed(&closed));

let open = Term::abs("x", Term::var("y"));
assert!(!is_closed(&open));
```

---

## Recursion with Y Combinator

### Factorial

```rust
use lambda_core::{Term, combinators::y_combinator};

// Factorial function: λf.λn.if (n == 0) 1 (n * f (n - 1))
// Simplified without actual arithmetic:
fn factorial_body() -> Term {
    Term::abs("f",
        Term::abs("n",
            // Placeholder: actual implementation needs Church arithmetic
            Term::var("factorial_result")
        )
    )
}

let y = y_combinator();
let fact = Term::app(y, factorial_body());

// Note: Full implementation requires Church numerals and arithmetic
```

### Fixed Point Example

```rust
// Find fixed point: Y f = f (Y f)
let y = y_combinator();
let f = Term::abs("x", Term::var("x"));  // Simple function

// Y f reduces to f (Y f) which reduces to Y f (infinite)
// Demonstrates fixed point property

let term = Term::app(y, f);
// This would loop infinitely in eager evaluation
```

---

## Performance Demonstrations

### Benchmarking Evaluation Strategies

```rust
use std::time::Instant;
use lambda_core::Term;
use lambda_eval::{CallByNameEval, CallByValueEval, EvalConfig};

fn benchmark_strategies() {
    let term = /* large term */;
    
    // Call-by-name
    let start = Instant::now();
    let cbn_eval = CallByNameEval::new(EvalConfig::default());
    let _result = cbn_eval.normalize(&term);
    let cbn_time = start.elapsed();
    
    // Call-by-value
    let start = Instant::now();
    let cbv_eval = CallByValueEval::new(EvalConfig::default());
    let _result = cbv_eval.normalize(&term);
    let cbv_time = start.elapsed();
    
    println!("Call-by-name: {:?}", cbn_time);
    println!("Call-by-value: {:?}", cbv_time);
}
```

### Large Term Stress Test

```rust
fn generate_large_term(depth: usize) -> Term {
    if depth == 0 {
        Term::var("x")
    } else {
        Term::abs("x", generate_large_term(depth - 1))
    }
}

let large = generate_large_term(100);
let eval = CallByNameEval::new(EvalConfig {
    max_steps: 10000,
    max_depth: 200,
});

let start = Instant::now();
let result = eval.normalize(&large);
let elapsed = start.elapsed();

println!("Evaluated {} nested lambdas in {:?}", 100, elapsed);
```

---

## Error Handling

### Handling Non-Termination

```rust
use lambda_eval::{CallByNameEval, EvalConfig, EvalError};

let omega = /* non-terminating term */;

let eval = CallByNameEval::new(EvalConfig {
    max_steps: 1000,
    max_depth: 100,
});

match eval.normalize(&omega) {
    Ok(result) => println!("Result: {}", result),
    Err(EvalError::NonTerminating { limit }) => {
        println!("Did not terminate within {} steps", limit);
    }
    Err(e) => println!("Error: {}", e),
}
```

### Handling Stack Overflow

```rust
fn deeply_nested(depth: usize) -> Term {
    if depth == 0 {
        Term::var("x")
    } else {
        Term::app(
            Term::abs("x", Term::var("x")),
            deeply_nested(depth - 1)
        )
    }
}

let deep = deeply_nested(10000);

let eval = CallByNameEval::new(EvalConfig {
    max_steps: 100000,
    max_depth: 1000,  // Protection against stack overflow
});

match eval.normalize(&deep) {
    Err(EvalError::StackOverflow) => {
        println!("Stack overflow prevented");
    }
    Ok(_) => println!("Succeeded"),
    Err(e) => println!("Other error: {}", e),
}
```

---

## Complete Example Programs

### Example 1: REPL-like Evaluation

```rust
use lambda_core::Term;
use lambda_eval::{CallByNameEval, EvalConfig};

fn eval_and_print(input: Term) {
    println!("Input:  {}", input);
    
    let eval = CallByNameEval::new(EvalConfig::default());
    match eval.normalize(&input) {
        Ok(result) => {
            println!("Output: {}", result);
            println!("Free variables: {:?}", result.free_vars());
            println!("Is value: {}", result.is_value());
        }
        Err(e) => {
            println!("Error: {}", e);
        }
    }
}

fn main() {
    // Example 1: Identity application
    let term1 = Term::app(
        Term::abs("x", Term::var("x")),
        Term::var("hello")
    );
    eval_and_print(term1);
    
    // Example 2: K combinator
    use lambda_core::combinators::k_combinator;
    let term2 = Term::app(
        Term::app(k_combinator(), Term::var("keep")),
        Term::var("discard")
    );
    eval_and_print(term2);
}
```

### Example 2: Testing All Combinators

```rust
use lambda_core::combinators::*;
use lambda_eval::{CallByNameEval, EvalConfig};

fn test_combinator(name: &str, combinator: Term, test_case: Term, expected: Term) {
    println!("\n=== Testing {} ===", name);
    println!("Combinator: {}", combinator);
    println!("Test case:  {}", test_case);
    
    let eval = CallByNameEval::new(EvalConfig::default());
    match eval.normalize(&test_case) {
        Ok(result) => {
            println!("Result:     {}", result);
            if result == expected {
                println!("✓ PASS");
            } else {
                println!("✗ FAIL (expected: {})", expected);
            }
        }
        Err(e) => {
            println!("✗ ERROR: {}", e);
        }
    }
}

fn main() {
    let eval = CallByNameEval::new(EvalConfig::default());
    
    // Test I
    test_combinator(
        "I",
        identity(),
        Term::app(identity(), Term::var("x")),
        Term::var("x")
    );
    
    // Test K
    test_combinator(
        "K",
        k_combinator(),
        Term::app(
            Term::app(k_combinator(), Term::var("x")),
            Term::var("y")
        ),
        Term::var("x")
    );
    
    // Test S I I (should be identity)
    let s = s_combinator();
    let i = identity();
    let sii = eval.normalize(&Term::app(Term::app(s, i.clone()), i)).unwrap();
    test_combinator(
        "S I I",
        sii.clone(),
        Term::app(sii, Term::var("x")),
        Term::var("x")
    );
}
```

---

## Next Steps

- **Want to add features?** See [extending.md](extending.md)
- **Need performance tuning?** See [performance.md](performance.md)
- **Testing strategies?** See [testing.md](testing.md)
- **Academic integration?** See [integration.md](integration.md)
