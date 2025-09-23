# Untyped Lambda Calculus - Python Implementation

## Simple Interpreter

Here's a working implementation of untyped lambda calculus in Python:

```python
# untyped_lambda.py - Simple Lambda Calculus Interpreter

class LambdaTerm:
    """Base class for lambda calculus terms"""
    pass

class Variable(LambdaTerm):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Variable) and self.name == other.name

class Abstraction(LambdaTerm):
    def __init__(self, var, body):
        self.var = var  # Variable
        self.body = body  # LambdaTerm

    def __str__(self):
        return f"(λ{self.var}.{self.body})"

class Application(LambdaTerm):
    def __init__(self, func, arg):
        self.func = func  # LambdaTerm
        self.arg = arg    # LambdaTerm

    def __str__(self):
        return f"({self.func} {self.arg})"

def free_variables(term):
    """Return set of free variables in a term"""
    if isinstance(term, Variable):
        return {term.name}
    elif isinstance(term, Abstraction):
        return free_variables(term.body) - {term.var.name}
    elif isinstance(term, Application):
        return free_variables(term.func) | free_variables(term.arg)
    return set()

def substitute(term, var_name, replacement):
    """Substitute replacement for var_name in term, avoiding capture"""
    if isinstance(term, Variable):
        return replacement if term.name == var_name else term

    elif isinstance(term, Application):
        new_func = substitute(term.func, var_name, replacement)
        new_arg = substitute(term.arg, var_name, replacement)
        return Application(new_func, new_arg)

    elif isinstance(term, Abstraction):
        if term.var.name == var_name:
            return term  # Variable is bound, no substitution

        # Check for variable capture
        free_vars = free_variables(replacement)
        if term.var.name in free_vars:
            # Alpha conversion needed - rename bound variable
            new_var_name = fresh_variable(term.var.name, free_vars)
            new_var = Variable(new_var_name)
            new_body = substitute(term.body, term.var.name, new_var)
            new_body = substitute(new_body, var_name, replacement)
            return Abstraction(new_var, new_body)
        else:
            new_body = substitute(term.body, var_name, replacement)
            return Abstraction(term.var, new_body)

def fresh_variable(base_name, forbidden_names):
    """Generate a fresh variable name not in forbidden_names"""
    counter = 1
    while f"{base_name}{counter}" in forbidden_names:
        counter += 1
    return f"{base_name}{counter}"

def beta_reduce(term):
    """Perform one step of beta reduction if possible"""
    if isinstance(term, Application):
        if isinstance(term.func, Abstraction):
            # Beta reduction: (λx.M) N → M[x := N]
            return substitute(term.func.body, term.func.var.name, term.arg)
        else:
            # Try to reduce the function part
            reduced_func = beta_reduce(term.func)
            if reduced_func != term.func:
                return Application(reduced_func, term.arg)
            # Try to reduce the argument part
            reduced_arg = beta_reduce(term.arg)
            if reduced_arg != term.arg:
                return Application(term.func, reduced_arg)

    elif isinstance(term, Abstraction):
        reduced_body = beta_reduce(term.body)
        if reduced_body != term.body:
            return Abstraction(term.var, reduced_body)

    return term

def normalize(term, max_steps=100):
    """Normalize a term by repeated beta reduction"""
    current = term
    for step in range(max_steps):
        reduced = beta_reduce(current)
        if reduced == current:
            break
        current = reduced
        print(f"Step {step + 1}: {current}")
    return current

# Example usage and classic combinators
if __name__ == "__main__":
    # Variables
    x = Variable("x")
    y = Variable("y")
    z = Variable("z")
    f = Variable("f")

    # Identity function: λx.x
    identity = Abstraction(x, x)
    print(f"Identity: {identity}")

    # Application: (λx.x) y
    app = Application(identity, y)
    print(f"Application: {app}")
    print(f"Reduced: {beta_reduce(app)}")

    print("\n--- Classic Combinators ---")

    # K combinator: λx.λy.x
    K = Abstraction(x, Abstraction(y, x))
    print(f"K combinator: {K}")

    # S combinator: λx.λy.λz.((x z) (y z))
    xz = Application(x, z)
    yz = Application(y, z)
    xyz = Application(xz, yz)
    S = Abstraction(x, Abstraction(y, Abstraction(z, xyz)))
    print(f"S combinator: {S}")

    # Church numerals
    print("\n--- Church Numerals ---")

    # Zero: λf.λx.x
    zero = Abstraction(f, Abstraction(x, x))
    print(f"Zero: {zero}")

    # One: λf.λx.(f x)
    fx = Application(f, x)
    one = Abstraction(f, Abstraction(x, fx))
    print(f"One: {one}")

    # Two: λf.λx.(f (f x))
    ffx = Application(f, fx)
    two = Abstraction(f, Abstraction(x, ffx))
    print(f"Two: {two}")

    print("\n--- Beta Reduction Example ---")

    # Apply identity to itself: (λx.x)(λx.x)
    self_app = Application(identity, identity)
    print(f"Self-application: {self_app}")
    print("Normalizing:")
    result = normalize(self_app)
    print(f"Normal form: {result}")
```

## Usage Examples

Save the code above as `untyped_lambda.py` and run:

```bash
python untyped_lambda.py
```

Output:
```
Identity: (λx.x)
Application: ((λx.x) y)
Reduced: y

--- Classic Combinators ---
K combinator: (λx.(λy.x))
S combinator: (λx.(λy.(λz.((x z) (y z)))))

--- Church Numerals ---
Zero: (λf.(λx.x))
One: (λf.(λx.(f x)))
Two: (λf.(λx.(f (f x))))

--- Beta Reduction Example ---
Self-application: ((λx.x) (λx.x))
Normalizing:
Step 1: (λx.x)
Normal form: (λx.x)
```

## Features

- **Complete lambda calculus implementation**: Variables, abstractions, applications
- **Beta reduction**: Proper substitution with variable capture avoidance
- **Alpha conversion**: Automatic renaming to prevent variable capture
- **Normalization**: Reduction to normal form
- **Classic examples**: Identity, K/S combinators, Church numerals

## Theoretical Background

This implementation demonstrates:
- **Substitution**: `M[x := N]` with capture-avoiding substitution
- **Beta reduction**: `(λx.M) N → M[x := N]`
- **Alpha equivalence**: `λx.x ≡ λy.y`
- **Church encoding**: Numbers as higher-order functions

## Extensions

You can extend this with:
- **Eta reduction**: `λx.(M x) → M` (if x not free in M)
- **Combinatory logic**: SKI calculus translation
- **Church encoding**: Booleans, pairs, lists
- **Fixed-point combinators**: Y combinator for recursion