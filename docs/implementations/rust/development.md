# Development Guide: Build, Test, and Debug

## Development Environment Setup

### Prerequisites

1. **Rust Toolchain** (1.70+ required)
   ```bash
   # Install rustup (if not already installed)
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   
   # Update to latest stable
   rustup update stable
   rustup default stable
   
   # Verify installation
   rustc --version
   cargo --version
   ```

2. **Additional Tools**
   ```bash
   # Formatter
   rustup component add rustfmt
   
   # Linter
   rustup component add clippy
   
   # Source code browser (optional)
   cargo install cargo-tree
   
   # Test coverage (optional)
   cargo install cargo-tarpaulin
   ```

3. **Repository Setup**
   ```bash
   cd /path/to/lambda-research
   cd sources/rust-implementations/tapl-rust
   
   # Build everything
   cargo build
   
   # Verify tests pass
   cargo test
   ```

---

## Build Commands

### Standard Builds

```bash
# Development build (fast, debug symbols)
cargo build

# Release build (optimized, no debug info)
cargo build --release

# Build specific crate
cargo build -p lambda-core
cargo build -p lambda-eval

# Build all crates
cargo build --workspace

# Clean build artifacts
cargo clean
```

### Build Output Locations

```
target/
├── debug/              # Development builds
│   ├── liblambda_core.rlib
│   ├── liblambda_eval.rlib
│   └── deps/
└── release/            # Optimized builds
    ├── liblambda_core.rlib
    ├── liblambda_eval.rlib
    └── deps/
```

### Build Profiles

**Development** (default for `cargo build`):
- Fast compilation
- No optimizations
- Debug symbols included
- Use for: rapid iteration, debugging

**Release** (with `--release` flag):
- Slow compilation
- Maximum optimization (opt-level=3)
- LTO enabled
- Use for: benchmarks, production, final testing

**Custom profiles** (can be added to Cargo.toml):
```toml
[profile.profiling]
inherits = "release"
debug = true  # Keep symbols for profiling
```

---

## Testing

### Running Tests

```bash
# Run all tests
cargo test

# Run tests with output (see println! statements)
cargo test -- --nocapture

# Run specific test by name
cargo test test_free_vars

# Run tests matching pattern
cargo test "test_substitution*"

# Run tests for specific crate
cargo test -p lambda-core
cargo test -p lambda-eval

# Run tests in release mode (faster for heavy tests)
cargo test --release

# Run with multiple threads
cargo test -- --test-threads=4

# Run ignored tests
cargo test -- --ignored
```

### Test Organization

**Unit Tests** (in same file as code):
```rust
// lambda-core/src/lib.rs
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_free_vars_var() {
        let term = Term::var("x");
        let expected = ["x"].iter().map(|s| s.to_string()).collect();
        assert_eq!(term.free_vars(), expected);
    }
}
```

**Integration Tests** (separate `tests/` directory):
```rust
// tests/integration_test.rs
use lambda_core::Term;
use lambda_eval::{CallByNameEval, EvalConfig};

#[test]
fn test_evaluation_pipeline() {
    let term = Term::app(
        Term::abs("x", Term::var("x")),
        Term::var("y")
    );
    
    let eval = CallByNameEval::new(EvalConfig::default());
    let result = eval.normalize(&term).unwrap();
    
    assert_eq!(result, Term::var("y"));
}
```

### Test Coverage

```bash
# Install tarpaulin (once)
cargo install cargo-tarpaulin

# Generate coverage report
cargo tarpaulin --out Html --output-dir coverage

# Open report
xdg-open coverage/index.html  # Linux
open coverage/index.html      # macOS
```

**Current Coverage Goal**: 80%+ for core functionality

---

## Code Quality Tools

### Formatting

```bash
# Check formatting (CI mode)
cargo fmt --check

# Format code
cargo fmt

# Format specific file
rustfmt src/lib.rs
```

**Configuration** (`.rustfmt.toml`):
```toml
max_width = 100
hard_tabs = false
tab_spaces = 4
```

### Linting with Clippy

```bash
# Run all lints
cargo clippy

# Treat warnings as errors (CI mode)
cargo clippy -- -D warnings

# Run all pedantic lints
cargo clippy -- -W clippy::pedantic

# Fix auto-fixable issues
cargo clippy --fix

# Check specific crate
cargo clippy -p lambda-core -- -D warnings
```

**Common Clippy Warnings**:
```rust
// Suppress specific lint
#[allow(clippy::needless_return)]
fn example() -> i32 {
    return 42;
}

// Suppress for module
#![allow(clippy::module_name_repetitions)]
```

### Documentation

```bash
# Generate documentation
cargo doc

# Generate and open in browser
cargo doc --open

# Document private items
cargo doc --document-private-items

# Check for broken links
cargo doc --no-deps
```

---

## Running Examples

### Current Examples

```bash
# List available examples
cargo run --example

# Run specific example
cargo run --example church_encodings
cargo run --example y_combinator
cargo run --example type_checking

# Run with release optimizations
cargo run --release --example performance_test
```

### Creating New Examples

```bash
# Create file: lambda-examples/examples/my_example.rs
```

```rust
// lambda-examples/examples/my_example.rs
use lambda_core::Term;
use lambda_eval::{CallByNameEval, EvalConfig};

fn main() {
    // Your example code
    let term = Term::app(
        Term::abs("x", Term::var("x")),
        Term::var("hello")
    );
    
    println!("Original: {}", term);
    
    let eval = CallByNameEval::new(EvalConfig::default());
    let result = eval.normalize(&term).unwrap();
    
    println!("Result: {}", result);
}
```

Then run:
```bash
cargo run --example my_example
```

---

## Debugging

### Debugging with rust-lldb / rust-gdb

```bash
# Build with debug symbols
cargo build

# Debug with lldb (macOS/Linux)
rust-lldb target/debug/examples/my_example

# Debug with gdb (Linux)
rust-gdb target/debug/examples/my_example
```

**Common debugger commands**:
```
(lldb) b lambda_core::Term::substitute  # Set breakpoint
(lldb) r                                # Run
(lldb) p term                           # Print variable
(lldb) bt                               # Backtrace
(lldb) c                                # Continue
(lldb) q                                # Quit
```

### Debugging Tests

```bash
# Run test under debugger
rust-lldb --batch \
  -o "breakpoint set -n lambda_core::Term::substitute" \
  -o "run" \
  target/debug/deps/lambda_core-<hash>

# Or get test binary name first
cargo test --no-run
# Note the binary path, then:
rust-lldb target/debug/deps/lambda_core-<hash>
```

### Print Debugging

```rust
#[test]
fn test_substitution_debug() {
    let term = Term::abs("x", Term::var("y"));
    let replacement = Term::var("z");
    
    // Debug print
    dbg!(&term);
    dbg!(&replacement);
    
    let result = term.substitute("y", &replacement);
    
    dbg!(&result);
    
    assert_eq!(result, Term::abs("x", Term::var("z")));
}
```

### Using RUST_BACKTRACE

```bash
# Full backtrace on panic
RUST_BACKTRACE=1 cargo test

# Full backtrace with source lines
RUST_BACKTRACE=full cargo test

# Shorter backtrace
RUST_BACKTRACE=short cargo test
```

### Using RUST_LOG

```bash
# Add to Cargo.toml:
# env_logger = "0.10"

# In your code:
use log::{info, debug, trace};

fn main() {
    env_logger::init();
    
    debug!("Starting evaluation");
    info!("Result: {:?}", result);
}

# Run with logging
RUST_LOG=debug cargo run
RUST_LOG=trace cargo test
RUST_LOG=lambda_core=trace cargo test
```

---

## IDE Setup

### Visual Studio Code

**Extensions**:
1. **rust-analyzer** (essential)
   - IntelliSense
   - Code completion
   - Inline errors
   - Go to definition

2. **CodeLLDB** (debugging)
   - Visual debugger
   - Breakpoints
   - Variable inspection

3. **crates** (dependency management)
   - Version hints
   - Update notifications

4. **Better TOML** (Cargo.toml editing)

**Configuration** (`.vscode/settings.json`):
```json
{
  "rust-analyzer.checkOnSave.command": "clippy",
  "rust-analyzer.cargo.features": "all",
  "editor.formatOnSave": true,
  "[rust]": {
    "editor.defaultFormatter": "rust-lang.rust-analyzer"
  }
}
```

**Launch Configuration** (`.vscode/launch.json`):
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "lldb",
      "request": "launch",
      "name": "Debug unit tests",
      "cargo": {
        "args": ["test", "--no-run", "--lib"],
        "filter": {
          "name": "lambda-core",
          "kind": "lib"
        }
      },
      "args": [],
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

### IntelliJ IDEA / CLion

**Plugins**:
1. **Rust** (official plugin)
2. **TOML** (for Cargo.toml)

**Configuration**:
- Enable Clippy: Settings → Languages & Frameworks → Rust → External Linters
- Enable format on save: Settings → Tools → Actions on Save → Reformat code

### Vim/Neovim

**Plugins** (using vim-plug):
```vim
Plug 'rust-lang/rust.vim'           " Syntax highlighting
Plug 'neoclide/coc.nvim'            " LSP support
Plug 'dense-analysis/ale'           " Linting
```

**CoC configuration**:
```json
{
  "rust-analyzer.serverPath": "rust-analyzer",
  "rust-analyzer.checkOnSave.command": "clippy"
}
```

### Emacs

**Packages** (using use-package):
```elisp
(use-package rust-mode)
(use-package cargo)
(use-package flycheck-rust)
(use-package lsp-mode
  :hook (rust-mode . lsp))
```

---

## Common Development Workflows

### Workflow 1: Adding a New Feature

```bash
# 1. Create feature branch (if using git)
git checkout -b feature/new-combinator

# 2. Write failing test first (TDD)
# Edit lambda-core/src/lib.rs
#[test]
fn test_new_combinator() {
    let result = combinators::my_new_combinator();
    assert_eq!(result, expected_value);
}

# 3. Run test (should fail)
cargo test test_new_combinator

# 4. Implement feature
# Edit lambda-core/src/lib.rs
pub fn my_new_combinator() -> Term {
    // implementation
}

# 5. Run test (should pass)
cargo test test_new_combinator

# 6. Run all tests
cargo test

# 7. Check formatting and lints
cargo fmt
cargo clippy -- -D warnings

# 8. Commit
git add .
git commit -m "feat: add new combinator"
```

### Workflow 2: Fixing a Bug

```bash
# 1. Reproduce bug with test
# Edit lambda-core/src/lib.rs
#[test]
fn test_bug_reproduction() {
    let term = /* setup that triggers bug */;
    let result = term.substitute("x", &replacement);
    assert_eq!(result, /* expected correct behavior */);
}

# 2. Verify test fails
cargo test test_bug_reproduction

# 3. Debug
RUST_BACKTRACE=1 cargo test test_bug_reproduction

# 4. Fix code
# Edit implementation

# 5. Verify fix
cargo test test_bug_reproduction
cargo test  # Run all tests

# 6. Check for regressions
cargo clippy -- -D warnings
```

### Workflow 3: Performance Optimization

```bash
# 1. Benchmark before (see performance.md)
cargo bench

# 2. Profile
cargo build --release --profile profiling
perf record --call-graph=dwarf target/profiling/my_binary
perf report

# 3. Optimize code

# 4. Benchmark after
cargo bench

# 5. Compare results
# Check criterion output for improvements
```

### Workflow 4: Refactoring

```bash
# 1. Ensure tests pass before refactoring
cargo test

# 2. Make refactoring changes
# Edit code

# 3. Run tests continuously
cargo watch -x test  # Requires: cargo install cargo-watch

# 4. Verify no behavior change
cargo test
cargo clippy

# 5. Check performance hasn't regressed
cargo bench
```

---

## Continuous Integration Workflow

### Local CI Simulation

```bash
# Run full CI pipeline locally
./ci-local.sh
```

**ci-local.sh**:
```bash
#!/bin/bash
set -e

echo "=== Building ==="
cargo build --release

echo "=== Testing ==="
cargo test

echo "=== Formatting ==="
cargo fmt --check

echo "=== Linting ==="
cargo clippy -- -D warnings

echo "=== Documentation ==="
cargo doc --no-deps

echo "✓ All checks passed!"
```

Make executable:
```bash
chmod +x ci-local.sh
```

### Pre-commit Hook

```bash
# .git/hooks/pre-commit
#!/bin/bash

echo "Running pre-commit checks..."

cargo fmt --check || {
    echo "❌ Code is not formatted. Run: cargo fmt"
    exit 1
}

cargo clippy -- -D warnings || {
    echo "❌ Clippy warnings found"
    exit 1
}

cargo test --quiet || {
    echo "❌ Tests failed"
    exit 1
}

echo "✓ Pre-commit checks passed"
```

Make executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## Troubleshooting

### Build Failures

**Problem**: Compilation errors
```
error[E0425]: cannot find value `x` in this scope
```

**Solution**:
1. Read error message carefully
2. Check variable names and imports
3. Consult Rust error codes: `rustc --explain E0425`

---

**Problem**: Dependency resolution failed
```
error: failed to select a version for `serde`
```

**Solution**:
```bash
# Update dependencies
cargo update

# Or clean and rebuild
cargo clean && cargo build
```

---

### Test Failures

**Problem**: Test passes locally but fails in CI

**Solution**:
1. Check for non-deterministic behavior
2. Verify test doesn't depend on local environment
3. Run in clean environment: `cargo clean && cargo test`

---

**Problem**: Test timeout

**Solution**:
```rust
#[test]
#[timeout(5000)]  // 5 second timeout
fn test_long_running() {
    // test code
}
```

---

### Performance Issues

**Problem**: Slow compile times

**Solution**:
1. Use `cargo check` instead of `cargo build` during development
2. Enable incremental compilation (on by default)
3. Use faster linker:
   ```toml
   # .cargo/config.toml
   [target.x86_64-unknown-linux-gnu]
   linker = "clang"
   rustflags = ["-C", "link-arg=-fuse-ld=lld"]
   ```

---

**Problem**: Slow test execution

**Solution**:
```bash
# Run tests in release mode
cargo test --release

# Run tests in parallel
cargo test -- --test-threads=8
```

---

### Clippy Warnings

**Problem**: Too many warnings

**Solution**:
```bash
# Fix auto-fixable issues
cargo clippy --fix

# Allow specific lints in code
#[allow(clippy::too_many_arguments)]

# Configure allowed lints globally
# Cargo.toml
[lints.clippy]
too_many_arguments = "allow"
```

---

## Useful Commands Reference

```bash
# Build
cargo build                      # Debug build
cargo build --release            # Release build
cargo check                      # Fast syntax check
cargo clean                      # Clean build artifacts

# Testing
cargo test                       # Run all tests
cargo test --release             # Test with optimizations
cargo test -- --nocapture        # Show output
cargo test <pattern>             # Run matching tests

# Quality
cargo fmt                        # Format code
cargo fmt --check                # Check formatting
cargo clippy                     # Run lints
cargo clippy -- -D warnings      # Fail on warnings

# Documentation
cargo doc                        # Generate docs
cargo doc --open                 # Open docs in browser

# Dependencies
cargo tree                       # Show dependency tree
cargo update                     # Update dependencies
cargo outdated                   # Check for outdated deps

# Utilities
cargo expand                     # Expand macros
cargo watch -x test              # Run tests on change
cargo bloat --release            # Binary size analysis
```

---

## Next Steps

- **New contributor?** Read [extending.md](extending.md) for how to add features
- **Performance work?** See [performance.md](performance.md) for benchmarking
- **Academic integration?** See [integration.md](integration.md) for citation workflow
