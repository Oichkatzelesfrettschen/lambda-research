# Testing Strategy and Coverage

## Overview

tapl-rust employs multiple testing strategies to ensure correctness, from unit tests to property-based testing. This document covers testing philosophy, infrastructure, and best practices.

## Testing Philosophy

### Three Pillars of Testing

1. **Correctness**: Tests verify implementations match theoretical specifications
2. **Robustness**: Tests check error handling and edge cases
3. **Performance**: Benchmarks ensure acceptable performance characteristics

### Academic Validation

Every test should:
- Reference the paper or theorem being tested
- Include examples from the referenced work
- Verify corner cases mentioned in academic literature

---

## Test Organization

### Test Hierarchy

```
lambda-core/
├── src/
│   └── lib.rs
│       └── #[cfg(test)] mod tests { ... }    # Unit tests
└── tests/
    ├── integration_test.rs                    # Integration tests
    └── property_tests.rs                      # Property-based tests
```

### Unit Tests

**Location**: Same file as the code being tested

```rust
// lambda-core/src/lib.rs

impl Term {
    pub fn free_vars(&self) -> HashSet<String> {
        // implementation
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;
    
    #[test]
    fn test_free_vars_var() {
        let term = Term::var("x");
        let expected = ["x"].iter().map(|s| s.to_string()).collect();
        assert_eq!(term.free_vars(), expected);
    }
    
    #[test]
    fn test_free_vars_abs_closed() {
        let term = Term::abs("x", Term::var("x"));
        assert_eq!(term.free_vars(), HashSet::new());
    }
    
    #[test]
    fn test_free_vars_abs_open() {
        let term = Term::abs("x", Term::var("y"));
        let expected = ["y"].iter().map(|s| s.to_string()).collect();
        assert_eq!(term.free_vars(), expected);
    }
}
```

### Integration Tests

**Location**: `tests/` directory (separate from source)

```rust
// tests/integration_test.rs

use lambda_core::Term;
use lambda_eval::{CallByNameEval, EvalConfig};

#[test]
fn test_identity_evaluation() {
    // From TAPL Chapter 5
    let id = Term::abs("x", Term::var("x"));
    let arg = Term::var("v");
    let term = Term::app(id, arg);
    
    let eval = CallByNameEval::new(EvalConfig::default());
    let result = eval.normalize(&term).unwrap();
    
    assert_eq!(result, Term::var("v"));
}

#[test]
fn test_k_combinator_evaluation() {
    // K x y → x
    use lambda_core::combinators::k_combinator;
    
    let k = k_combinator();
    let term = Term::app(
        Term::app(k, Term::var("first")),
        Term::var("second")
    );
    
    let eval = CallByNameEval::new(EvalConfig::default());
    let result = eval.normalize(&term).unwrap();
    
    assert_eq!(result, Term::var("first"));
}
```

---

## Test Categories

### 1. Correctness Tests

Verify implementations match specifications.

#### Substitution Correctness

```rust
#[cfg(test)]
mod substitution_tests {
    use super::*;
    
    /// Test substitution following TAPL Definition 5.3.5
    #[test]
    fn test_substitution_cases() {
        // Case 1: x[x := s] = s
        let term = Term::var("x");
        let result = term.substitute("x", &Term::var("s"));
        assert_eq!(result, Term::var("s"));
        
        // Case 2: y[x := s] = y (if x ≠ y)
        let term = Term::var("y");
        let result = term.substitute("x", &Term::var("s"));
        assert_eq!(result, Term::var("y"));
        
        // Case 3: (λy.t₁)[x := s] (with capture avoidance)
        let term = Term::abs("y", Term::var("x"));
        let result = term.substitute("x", &Term::var("y"));
        // Should alpha-convert to avoid capture
        match result {
            Term::Abs { param, body } => {
                assert!(param != "y");  // Renamed
                assert_eq!(*body, Term::var("y"));
            }
            _ => panic!("Expected abstraction"),
        }
    }
}
```

#### Evaluation Correctness

```rust
#[cfg(test)]
mod evaluation_tests {
    use super::*;
    use lambda_eval::{CallByNameEval, EvalConfig};
    
    /// Test beta reduction: (λx.body) arg → body[x := arg]
    #[test]
    fn test_beta_reduction() {
        let term = Term::app(
            Term::abs("x", Term::var("x")),
            Term::var("v")
        );
        
        let eval = CallByNameEval::new(EvalConfig::default());
        let result = eval.normalize(&term).unwrap();
        
        assert_eq!(result, Term::var("v"));
    }
    
    /// Test evaluation order: call-by-name doesn't evaluate arguments
    #[test]
    fn test_call_by_name_order() {
        // (λx.λy.y) (Ω) → λy.y
        // Ω is non-terminating, but x is unused
        let omega = {
            let w = Term::abs("z", Term::app(Term::var("z"), Term::var("z")));
            Term::app(w.clone(), w)
        };
        
        let term = Term::app(
            Term::abs("x", Term::abs("y", Term::var("y"))),
            omega
        );
        
        let eval = CallByNameEval::new(EvalConfig::default());
        let result = eval.normalize(&term).unwrap();
        
        assert_eq!(result, Term::abs("y", Term::var("y")));
    }
}
```

### 2. Edge Case Tests

Handle boundary conditions and unusual inputs.

```rust
#[cfg(test)]
mod edge_cases {
    use super::*;
    
    #[test]
    fn test_empty_free_vars() {
        let term = Term::abs("x", Term::var("x"));
        assert_eq!(term.free_vars(), HashSet::new());
    }
    
    #[test]
    fn test_deeply_nested_lambdas() {
        fn nested(depth: usize) -> Term {
            if depth == 0 {
                Term::var("x")
            } else {
                Term::abs("x", nested(depth - 1))
            }
        }
        
        let term = nested(100);
        let fv = term.free_vars();
        
        // x is bound at every level
        assert_eq!(fv, HashSet::new());
    }
    
    #[test]
    fn test_substitution_with_shadowing() {
        // (λx.(λx.x))[x := y]
        // Inner x shadows outer, shouldn't be substituted
        let term = Term::abs("x", Term::abs("x", Term::var("x")));
        let result = term.substitute("x", &Term::var("y"));
        
        assert_eq!(result, term);  // Unchanged
    }
}
```

### 3. Error Handling Tests

Verify graceful failure modes.

```rust
#[cfg(test)]
mod error_tests {
    use super::*;
    use lambda_eval::{CallByNameEval, EvalConfig, EvalError};
    
    #[test]
    fn test_non_terminating_detection() {
        let omega = {
            let w = Term::abs("x", Term::app(Term::var("x"), Term::var("x")));
            Term::app(w.clone(), w)
        };
        
        let eval = CallByNameEval::new(EvalConfig {
            max_steps: 100,
            max_depth: 100,
        });
        
        let result = eval.normalize(&omega);
        
        assert!(matches!(result, Err(EvalError::NonTerminating { .. })));
    }
    
    #[test]
    fn test_stack_overflow_protection() {
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
            max_depth: 1000,
        });
        
        let result = eval.normalize(&deep);
        
        // Should either succeed or hit depth limit, not crash
        assert!(result.is_ok() || matches!(result, Err(EvalError::StackOverflow)));
    }
}
```

### 4. Regression Tests

Prevent previously fixed bugs from reoccurring.

```rust
#[cfg(test)]
mod regression_tests {
    use super::*;
    
    /// Regression test for issue #42: incorrect alpha-conversion
    #[test]
    fn test_issue_42_alpha_conversion() {
        // Bug: (λy.x)[x := y] was incorrectly producing (λy.y)
        let term = Term::abs("y", Term::var("x"));
        let result = term.substitute("x", &Term::var("y"));
        
        // Correct: Should alpha-convert to (λv_n.y)
        match result {
            Term::Abs { param, body } => {
                assert_ne!(param, "y");  // Must be renamed
                assert_eq!(*body, Term::var("y"));
            }
            _ => panic!("Expected abstraction"),
        }
    }
}
```

---

## Property-Based Testing

### Why Property-Based Testing?

- Tests properties that hold for all inputs
- Finds edge cases you didn't think of
- Complements example-based tests

### Setup

**Cargo.toml**:
```toml
[dev-dependencies]
proptest = "1.4"
```

### Example Properties

```rust
use proptest::prelude::*;

// Generator for random terms
fn arb_term() -> impl Strategy<Value = Term> {
    let leaf = prop_oneof![
        any::<String>().prop_map(Term::var),
    ];
    
    leaf.prop_recursive(
        8,   // levels deep
        256, // max nodes
        10,  // items per collection
        |inner| {
            prop_oneof![
                // Abstraction
                (any::<String>(), inner.clone())
                    .prop_map(|(param, body)| Term::abs(param, body)),
                // Application
                (inner.clone(), inner)
                    .prop_map(|(rator, rand)| Term::app(rator, rand)),
            ]
        },
    )
}

proptest! {
    /// Property: Substitution is idempotent on closed terms
    #[test]
    fn prop_substitution_closed_idempotent(term in arb_term(), var in "[a-z]+") {
        if term.free_vars().is_empty() {
            let result = term.substitute(&var, &Term::var("replacement"));
            prop_assert_eq!(result, term);
        }
    }
    
    /// Property: Free variables are computed correctly
    #[test]
    fn prop_free_vars_subset_of_all_vars(term in arb_term()) {
        fn all_vars(term: &Term) -> HashSet<String> {
            match term {
                Term::Var(name) => {
                    let mut set = HashSet::new();
                    set.insert(name.clone());
                    set
                }
                Term::Abs { param, body } => {
                    let mut vars = all_vars(body);
                    vars.insert(param.clone());
                    vars
                }
                Term::App { rator, rand } => {
                    let mut vars = all_vars(rator);
                    vars.extend(all_vars(rand));
                    vars
                }
            }
        }
        
        let free = term.free_vars();
        let all = all_vars(&term);
        
        prop_assert!(free.is_subset(&all));
    }
    
    /// Property: Evaluation always terminates or hits limit
    #[test]
    fn prop_evaluation_terminates_or_limits(term in arb_term()) {
        let eval = CallByNameEval::new(EvalConfig {
            max_steps: 1000,
            max_depth: 100,
        });
        
        let result = eval.normalize(&term);
        
        // Should either succeed or hit a known limit
        prop_assert!(
            result.is_ok() || 
            matches!(result, Err(EvalError::NonTerminating { .. })) ||
            matches!(result, Err(EvalError::StackOverflow))
        );
    }
}
```

---

## Test Coverage

### Measuring Coverage

```bash
# Install tarpaulin
cargo install cargo-tarpaulin

# Generate coverage report
cargo tarpaulin --out Html --output-dir coverage

# View report
xdg-open coverage/index.html  # Linux
open coverage/index.html      # macOS
```

### Coverage Goals

| Component | Target | Current |
|-----------|--------|---------|
| lambda-core | 90%+ | ~85% |
| lambda-eval | 85%+ | ~80% |
| lambda-types | 90%+ | TBD |
| lambda-parser | 80%+ | TBD |

### Improving Coverage

**Identify uncovered lines**:
```bash
cargo tarpaulin --out Html --output-dir coverage --verbose
```

**Add tests for uncovered code**:
```rust
#[test]
fn test_previously_uncovered_branch() {
    // Test the specific branch shown by coverage tool
}
```

---

## Benchmarking

### Using Criterion

**Setup** (`Cargo.toml`):
```toml
[dev-dependencies]
criterion = { version = "0.5", features = ["html_reports"] }

[[bench]]
name = "evaluation"
harness = false
```

**Benchmark file** (`benches/evaluation.rs`):
```rust
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use lambda_core::Term;
use lambda_eval::{CallByNameEval, EvalConfig};

fn benchmark_identity(c: &mut Criterion) {
    let term = Term::app(
        Term::abs("x", Term::var("x")),
        Term::var("v")
    );
    
    let eval = CallByNameEval::new(EvalConfig::default());
    
    c.bench_function("identity evaluation", |b| {
        b.iter(|| {
            eval.normalize(black_box(&term))
        })
    });
}

fn benchmark_church_numerals(c: &mut Criterion) {
    fn church_numeral(n: usize) -> Term {
        Term::abs("f", Term::abs("x", {
            let mut body = Term::var("x");
            for _ in 0..n {
                body = Term::app(Term::var("f"), body);
            }
            body
        }))
    }
    
    let eval = CallByNameEval::new(EvalConfig::default());
    
    for n in [0, 1, 5, 10, 50].iter() {
        c.bench_function(&format!("church_numeral_{}", n), |b| {
            let num = church_numeral(*n);
            b.iter(|| {
                eval.normalize(black_box(&num))
            })
        });
    }
}

criterion_group!(benches, benchmark_identity, benchmark_church_numerals);
criterion_main!(benches);
```

**Run benchmarks**:
```bash
cargo bench

# View HTML report
xdg-open target/criterion/report/index.html
```

---

## Testing Best Practices

### 1. Test Naming Convention

```rust
#[test]
fn test_<component>_<scenario>_<expected_result>() {
    // test_substitution_with_capture_avoids_capture
    // test_evaluation_of_omega_times_out
    // test_free_vars_in_closed_term_is_empty
}
```

### 2. Use Descriptive Assertions

```rust
// ❌ Bad
assert!(x);

// ✅ Good
assert!(
    term.free_vars().is_empty(),
    "Expected closed term to have no free variables, got: {:?}",
    term.free_vars()
);
```

### 3. Test One Thing Per Test

```rust
// ❌ Bad: Tests multiple unrelated things
#[test]
fn test_everything() {
    test_free_vars();
    test_substitution();
    test_evaluation();
}

// ✅ Good: Separate tests
#[test]
fn test_free_vars() { /* ... */ }

#[test]
fn test_substitution() { /* ... */ }

#[test]
fn test_evaluation() { /* ... */ }
```

### 4. Use Test Helpers

```rust
#[cfg(test)]
mod test_helpers {
    use super::*;
    
    pub fn assert_evaluates_to(term: Term, expected: Term) {
        let eval = CallByNameEval::new(EvalConfig::default());
        let result = eval.normalize(&term).unwrap();
        assert_eq!(result, expected);
    }
    
    pub fn assert_free_vars(term: &Term, expected: &[&str]) {
        let fv = term.free_vars();
        let expected_set: HashSet<String> = 
            expected.iter().map(|s| s.to_string()).collect();
        assert_eq!(fv, expected_set);
    }
}

#[test]
fn test_with_helpers() {
    let term = Term::app(
        Term::abs("x", Term::var("x")),
        Term::var("v")
    );
    
    test_helpers::assert_evaluates_to(term, Term::var("v"));
}
```

### 5. Test Academic Examples

```rust
/// Test from TAPL Chapter 5, Example 5.2.1
#[test]
fn test_tapl_5_2_1() {
    // id = λx.x
    let id = Term::abs("x", Term::var("x"));
    
    // id v → v
    let term = Term::app(id, Term::var("v"));
    let eval = CallByNameEval::new(EvalConfig::default());
    let result = eval.normalize(&term).unwrap();
    
    assert_eq!(result, Term::var("v"));
}
```

---

## Running Tests

### Basic Commands

```bash
# Run all tests
cargo test

# Run with output
cargo test -- --nocapture

# Run specific test
cargo test test_free_vars

# Run tests matching pattern
cargo test "test_substitution*"

# Run tests in specific module
cargo test --lib            # Library tests only
cargo test --test integration  # Specific integration test file

# Run tests for specific crate
cargo test -p lambda-core
```

### Parallel Testing

```bash
# Use 4 threads
cargo test -- --test-threads=4

# Run serially (for debugging)
cargo test -- --test-threads=1
```

### Test Output Control

```bash
# Show output even for passing tests
cargo test -- --nocapture

# Show only failures
cargo test --quiet

# Capture output (default)
cargo test
```

---

## Continuous Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Install Rust
      uses: actions-rs/toolchain@v1
      with:
        toolchain: stable
        profile: minimal
        override: true
    
    - name: Run tests
      run: cargo test --verbose
    
    - name: Run clippy
      run: cargo clippy -- -D warnings
    
    - name: Check formatting
      run: cargo fmt --check
    
    - name: Generate coverage
      run: |
        cargo install cargo-tarpaulin
        cargo tarpaulin --out Xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v1
```

---

## Test Maintenance

### When to Update Tests

1. **Bug fixes**: Add regression test
2. **New features**: Add comprehensive test suite
3. **Refactoring**: Ensure existing tests still pass
4. **API changes**: Update affected tests

### Removing Obsolete Tests

```rust
// Mark test as ignored if temporarily broken
#[test]
#[ignore]
fn test_temporarily_broken() {
    // TODO: Fix after refactoring
}

// Remove test if feature is removed
// Delete the entire test function
```

---

## Next Steps

- **Performance benchmarks**: See [performance.md](performance.md)
- **Adding new tests**: See [extending.md](extending.md)
- **Academic validation**: See [integration.md](integration.md)
