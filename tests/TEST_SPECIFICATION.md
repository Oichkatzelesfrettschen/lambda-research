# Lambda Calculus Testing Framework Specification

## Overview

This document defines a comprehensive, cross-language testing framework for lambda calculus implementations. All implementations must pass these tests to be considered correct.

## Test Categories

### 1. Core Functionality Tests

#### 1.1 Term Construction
```yaml
test_cases:
  - name: variable_construction
    input: Var("x")
    expected: Variable with name "x"

  - name: abstraction_construction
    input: Abs("x", Var("x"))
    expected: Identity function

  - name: application_construction
    input: App(Var("f"), Var("x"))
    expected: Function application f x
```

#### 1.2 Free Variables
```yaml
test_cases:
  - name: free_var_simple
    input: Var("x")
    expected: ["x"]

  - name: free_var_abstraction
    input: Abs("x", App(Var("x"), Var("y")))
    expected: ["y"]

  - name: free_var_complex
    input: App(Abs("x", Var("y")), Var("z"))
    expected: ["y", "z"]
```

#### 1.3 Substitution
```yaml
test_cases:
  - name: subst_variable_match
    term: Var("x")
    substitute: ["x", Var("y")]
    expected: Var("y")

  - name: subst_variable_no_match
    term: Var("z")
    substitute: ["x", Var("y")]
    expected: Var("z")

  - name: subst_capture_avoiding
    term: Abs("y", Var("x"))
    substitute: ["x", Var("y")]
    expected: Abs("y'", Var("y"))  # Fresh variable
```

### 2. Reduction Tests

#### 2.1 Beta Reduction
```yaml
test_cases:
  - name: beta_reduction_simple
    input: App(Abs("x", Var("x")), Var("y"))
    expected: Var("y")

  - name: beta_reduction_nested
    input: App(Abs("x", Abs("y", Var("x"))), Var("z"))
    expected: Abs("y", Var("z"))

  - name: beta_reduction_complex
    input: App(App(Abs("x", Abs("y", App(Var("x"), Var("y")))), Var("f")), Var("a"))
    expected: App(Var("f"), Var("a"))
```

#### 2.2 Normalization
```yaml
test_cases:
  - name: normalize_identity
    input: App(Abs("x", Var("x")), Var("y"))
    expected: Var("y")
    steps_limit: 10

  - name: normalize_k_combinator
    input: App(App(Abs("x", Abs("y", Var("x"))), Var("a")), Var("b"))
    expected: Var("a")
    steps_limit: 10

  - name: normalize_s_combinator
    input: |
      App(App(App(
        Abs("x", Abs("y", Abs("z", App(App(Var("x"), Var("z")), App(Var("y"), Var("z")))))),
        Abs("a", Var("a"))),
        Abs("b", Var("b"))),
        Var("c"))
    expected: Var("c")
    steps_limit: 20
```

### 3. Church Encoding Tests

#### 3.1 Church Numerals
```yaml
test_cases:
  - name: church_zero
    input: church_numeral(0)
    expected: Abs("f", Abs("x", Var("x")))

  - name: church_one
    input: church_numeral(1)
    expected: Abs("f", Abs("x", App(Var("f"), Var("x"))))

  - name: church_addition
    input: church_add(church_numeral(2), church_numeral(3))
    normalized: church_numeral(5)
```

#### 3.2 Church Booleans
```yaml
test_cases:
  - name: church_true
    input: church_true
    expected: Abs("t", Abs("f", Var("t")))

  - name: church_false
    input: church_false
    expected: Abs("t", Abs("f", Var("f")))

  - name: church_and
    input: church_and(church_true, church_false)
    normalized: church_false
```

### 4. Property-Based Tests

#### 4.1 Confluence (Church-Rosser)
```python
def test_confluence(term):
    """Test that different reduction strategies reach same normal form"""
    nf_leftmost = normalize_leftmost(term)
    nf_rightmost = normalize_rightmost(term)
    nf_parallel = normalize_parallel(term)

    assert nf_leftmost == nf_rightmost == nf_parallel
```

#### 4.2 Substitution Lemma
```python
def test_substitution_lemma(t, x, s, y, r):
    """Verify substitution commutativity when variables are distinct"""
    if x != y and y not in free_vars(s):
        result1 = substitute(substitute(t, x, s), y, r)
        result2 = substitute(substitute(t, y, r), x, substitute(s, y, r))
        assert alpha_equivalent(result1, result2)
```

#### 4.3 Alpha Equivalence
```python
def test_alpha_equivalence():
    """Test that alpha-equivalent terms behave identically"""
    t1 = Abs("x", Var("x"))
    t2 = Abs("y", Var("y"))

    assert alpha_equivalent(t1, t2)
    assert normalize(t1) == normalize(t2)
```

### 5. Performance Tests

#### 5.1 Reduction Performance
```yaml
benchmarks:
  - name: factorial_5
    term: factorial_church(5)
    max_time_ms: 100
    max_steps: 1000

  - name: fibonacci_10
    term: fibonacci_church(10)
    max_time_ms: 500
    max_steps: 5000

  - name: ackermann_2_2
    term: ackermann_church(2, 2)
    max_time_ms: 1000
    max_steps: 10000
```

#### 5.2 Memory Usage
```yaml
memory_limits:
  - name: large_term_construction
    operation: construct_balanced_tree(depth=15)
    max_memory_mb: 100

  - name: deep_recursion
    operation: y_combinator_iteration(1000)
    max_memory_mb: 50
```

### 6. Error Handling Tests

#### 6.1 Invalid Operations
```yaml
test_cases:
  - name: unbound_variable
    input: eval(Var("undefined"))
    expected_error: UnboundVariableError

  - name: non_function_application
    input: eval(App(Var("x"), Var("y")))  # x is not a function
    expected_error: ApplicationError

  - name: infinite_recursion_detection
    input: normalize_with_timeout(omega, timeout_ms=1000)
    expected_error: TimeoutError
```

### 7. Cross-Language Compatibility Tests

#### 7.1 Term Serialization
```yaml
test_cases:
  - name: serialize_deserialize_roundtrip
    implementations: [idris, scala, sml, rust]
    test: |
      for each pair of implementations (impl1, impl2):
        term = impl1.create_complex_term()
        serialized = impl1.serialize(term)
        deserialized = impl2.deserialize(serialized)
        result = impl2.normalize(deserialized)
        assert impl1.serialize(impl1.normalize(term)) == impl2.serialize(result)
```

#### 7.2 Result Consistency
```yaml
test_cases:
  - name: cross_language_normalization
    term: "(λf.(λx.f (x x)) (λx.f (x x))) (λn.λf.λx.if (iszero n) x (f ((pred n) f x)))"
    implementations: [idris, scala, sml, rust]
    test: |
      results = [impl.normalize(term) for impl in implementations]
      assert all(alpha_equivalent(results[0], r) for r in results)
```

## Test Implementation Guidelines

### 1. Test Runner Architecture

```python
class LambdaTestRunner:
    def __init__(self, implementation):
        self.impl = implementation
        self.results = []

    def run_test_suite(self):
        self.run_core_tests()
        self.run_reduction_tests()
        self.run_church_encoding_tests()
        self.run_property_tests()
        self.run_performance_tests()
        self.run_error_tests()
        return self.generate_report()
```

### 2. Test Data Generation

```haskell
-- QuickCheck generators for lambda terms
genTerm :: Int -> Gen Term
genTerm 0 = Var <$> genVarName
genTerm n = oneof
  [ Var <$> genVarName
  , Abs <$> genVarName <*> genTerm (n-1)
  , App <$> genTerm (n `div` 2) <*> genTerm (n `div` 2)
  ]

genWellTypedTerm :: Type -> Gen Term
-- Generate only well-typed terms for typed variants
```

### 3. Test Assertions

```scala
trait LambdaAssertions {
  def assertAlphaEquivalent(t1: Term, t2: Term): Unit
  def assertNormalForm(t: Term): Unit
  def assertReducesTo(from: Term, to: Term, maxSteps: Int = 1000): Unit
  def assertConfluent(t: Term): Unit
  def assertTerminates(t: Term, maxSteps: Int = 10000): Unit
}
```

## Coverage Requirements

- **Unit Test Coverage**: Minimum 90% of core functions
- **Property Test Coverage**: 100+ generated test cases per property
- **Integration Test Coverage**: All cross-language combinations
- **Performance Test Coverage**: All standard benchmarks

## Continuous Integration

```yaml
# .github/workflows/test.yml
test_matrix:
  strategy:
    matrix:
      implementation: [idris, scala, sml, rust, haskell]
      test_suite: [core, reduction, church, property, performance]
  steps:
    - run: make test-${{ matrix.test_suite }}-${{ matrix.implementation }}
    - run: make coverage-report
    - run: make benchmark-compare
```

## Test Documentation

Each test must include:
1. **Purpose**: What property/behavior is being tested
2. **Theory**: Mathematical foundation or theorem
3. **Input**: Test data specification
4. **Expected**: Expected output or behavior
5. **References**: Academic papers or specifications

## Failure Analysis

When tests fail:
1. Generate detailed trace of reduction steps
2. Highlight divergence point
3. Suggest potential fixes
4. Link to relevant documentation

## Future Extensions

1. **Fuzzing**: Grammar-based fuzzing for parser robustness
2. **Mutation Testing**: Verify test quality
3. **Formal Verification**: Connect to Coq/Agda proofs
4. **Visual Testing**: Reduction graph visualization
5. **Performance Regression**: Historical performance tracking