# Quick Reference: tapl-rust

## Essential Commands

```bash
# Build
cargo build                    # Debug build
cargo build --release          # Optimized build

# Test
cargo test                     # Run all tests
cargo test <name>              # Run specific test

# Code Quality
cargo fmt                      # Format code
cargo clippy                   # Lint code
cargo clippy -- -D warnings    # Fail on warnings

# Documentation
cargo doc --open               # Generate and open docs
```

## File Locations

```
sources/rust-implementations/tapl-rust/
├── lambda-core/          → Term representation, substitution
├── lambda-eval/          → Evaluation strategies
├── lambda-types/         → Type systems (planned)
├── lambda-parser/        → Parsing (planned)
└── lambda-examples/      → Examples (planned)
```

## Core API

### Term Construction

```rust
use lambda_core::Term;

Term::var("x")                              // Variable
Term::abs("x", Term::var("x"))              // λx.x
Term::app(Term::var("f"), Term::var("x"))   // (f x)
```

### Operations

```rust
term.free_vars()                    // Get free variables
term.substitute("x", &replacement)  // Substitute x := replacement
term.is_value()                     // Check if value (abstraction)
```

### Evaluation

```rust
use lambda_eval::{CallByNameEval, EvalConfig};

let eval = CallByNameEval::new(EvalConfig::default());
let result = eval.normalize(&term)?;
```

### Combinators

```rust
use lambda_core::combinators::*;

identity()        // I = λx.x
k_combinator()    // K = λx.λy.x
s_combinator()    // S = λx.λy.λz.((x z) (y z))
y_combinator()    // Y = λf.(λx.f (x x)) (λx.f (x x))
omega()           // Ω = (λx.x x) (λx.x x)
```

## Documentation Map

| For | Read |
|-----|------|
| Getting started | [README.md](README.md) |
| Understanding design | [architecture.md](architecture.md) |
| Setting up dev env | [development.md](development.md) |
| Adding features | [extending.md](extending.md) |
| Code examples | [examples.md](examples.md) |
| Writing tests | [testing.md](testing.md) |
| Performance | [performance.md](performance.md) |
| Academic citations | [integration.md](integration.md) |

## Common Patterns

### Creating Terms

```rust
// Identity: λx.x
let id = Term::abs("x", Term::var("x"));

// Application: id v
let app = Term::app(id, Term::var("v"));

// Nested: λf.λx.f x
let nested = Term::abs("f", Term::abs("x", 
    Term::app(Term::var("f"), Term::var("x"))
));
```

### Evaluation

```rust
use lambda_eval::{CallByNameEval, CallByValueEval, EvalConfig};

// Call-by-name (lazy)
let cbn = CallByNameEval::new(EvalConfig::default());
let result = cbn.normalize(&term)?;

// Call-by-value (strict)
let cbv = CallByValueEval::new(EvalConfig::default());
let result = cbv.normalize(&term)?;
```

### Error Handling

```rust
use lambda_eval::EvalError;

match eval.normalize(&term) {
    Ok(result) => println!("Result: {}", result),
    Err(EvalError::NonTerminating { limit }) => {
        println!("Did not terminate within {} steps", limit);
    }
    Err(e) => println!("Error: {}", e),
}
```

## Testing Patterns

```rust
#[test]
fn test_example() {
    let term = Term::abs("x", Term::var("x"));
    let result = term.substitute("y", &Term::var("z"));
    assert_eq!(result, term);  // y not in term
}
```

## Academic References

- **TAPL**: Pierce (2002), "Types and Programming Languages"
  - Chapter 5: Untyped Lambda Calculus → `lambda-core/`, `lambda-eval/`
- **Bibliography**: See `01-untyped-lambda-calculus/bibliography.md`
- **Papers**: See `papers-archive/` directory

## Troubleshooting

```bash
# Clean rebuild
cargo clean && cargo build

# Full test output
cargo test -- --nocapture

# Backtrace on error
RUST_BACKTRACE=1 cargo test

# Check specific crate
cargo test -p lambda-core
```

## Performance Tips

1. Use `--release` for benchmarks
2. Profile before optimizing
3. Consider De Bruijn indices for substitution-heavy code
4. Cache free variables when repeated

## Code Quality Checklist

- [ ] `cargo build` succeeds
- [ ] `cargo test` passes
- [ ] `cargo fmt` applied
- [ ] `cargo clippy` clean
- [ ] Documentation updated
- [ ] Academic references cited

## Links

- **Full docs**: `docs/implementations/rust/README.md`
- **Code**: `sources/rust-implementations/tapl-rust/`
- **Examples**: See [examples.md](examples.md)
- **Repository**: https://github.com/lambda-research/lambda-calculus

---

*For detailed information, see the full documentation in this directory.*
