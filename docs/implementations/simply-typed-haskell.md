# Simply Typed Lambda Calculus - Haskell Implementation

## Type-Safe Implementation

Here's a working simply typed lambda calculus implementation in Haskell with type checking:

```haskell
-- SimplyTyped.hs - Simply Typed Lambda Calculus with Type Checking

{-# LANGUAGE GADTs #-}
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeFamilies #-}

module SimplyTyped where

import qualified Data.Map as Map
import Data.Map (Map)

-- | Simple types
data Type
  = BaseType String       -- Int, Bool, etc.
  | Arrow Type Type       -- A → B
  deriving (Eq, Show)

-- | Type context (environment)
type Context = Map String Type

-- | Raw lambda terms (before type checking)
data RawTerm
  = RVar String
  | RLam String Type RawTerm      -- λx:T.e
  | RApp RawTerm RawTerm
  | RLit Literal                  -- Constants
  deriving (Show)

-- | Literals
data Literal
  = LInt Int
  | LBool Bool
  deriving (Show, Eq)

-- | Typed lambda terms (after type checking)
data TypedTerm
  = TVar String Type
  | TLam String Type TypedTerm Type   -- λx:A.e : A → B
  | TApp TypedTerm TypedTerm Type     -- e₁ e₂ : B
  | TLit Literal Type
  deriving (Show)

-- | Get the type of a literal
literalType :: Literal -> Type
literalType (LInt _)  = BaseType "Int"
literalType (LBool _) = BaseType "Bool"

-- | Get the type of a typed term
termType :: TypedTerm -> Type
termType (TVar _ t) = t
termType (TLam _ _ _ t) = t
termType (TApp _ _ t) = t
termType (TLit _ t) = t

-- | Type checking errors
data TypeError
  = UnboundVariable String
  | TypeMismatch Type Type
  | NotAFunction Type
  deriving (Show, Eq)

-- | Type checking monad
type TypeCheck = Either TypeError

-- | Type inference and checking
typeCheck :: Context -> RawTerm -> TypeCheck TypedTerm
typeCheck ctx (RVar x) =
  case Map.lookup x ctx of
    Just t  -> Right (TVar x t)
    Nothing -> Left (UnboundVariable x)

typeCheck ctx (RLit lit) =
  let t = literalType lit
  in Right (TLit lit t)

typeCheck ctx (RLam x argType body) = do
  let ctx' = Map.insert x argType ctx
  typedBody <- typeCheck ctx' body
  let bodyType = termType typedBody
  let funcType = Arrow argType bodyType
  return (TLam x argType typedBody funcType)

typeCheck ctx (RApp func arg) = do
  typedFunc <- typeCheck ctx func
  typedArg  <- typeCheck ctx arg

  case termType typedFunc of
    Arrow argType' retType ->
      if termType typedArg == argType'
      then Right (TApp typedFunc typedArg retType)
      else Left (TypeMismatch argType' (termType typedArg))

    funcType -> Left (NotAFunction funcType)

-- | Evaluation of typed terms
data Value
  = VLit Literal
  | VClosure String TypedTerm (Map String Value)  -- Closure
  deriving (Show)

type Environment = Map String Value

-- | Evaluation
eval :: Environment -> TypedTerm -> Value
eval env (TVar x _) =
  case Map.lookup x env of
    Just v  -> v
    Nothing -> error "Unbound variable in evaluation"

eval env (TLit lit _) = VLit lit

eval env (TLam x _ body _) = VClosure x body env

eval env (TApp func arg _) =
  let funcVal = eval env func
      argVal  = eval env arg
  in case funcVal of
       VClosure param body closureEnv ->
         let env' = Map.insert param argVal closureEnv
         in eval env' body
       _ -> error "Application of non-function"

-- | Pretty printing
prettyType :: Type -> String
prettyType (BaseType s) = s
prettyType (Arrow t1 t2) =
  let left = case t1 of
               Arrow _ _ -> "(" ++ prettyType t1 ++ ")"
               _ -> prettyType t1
  in left ++ " → " ++ prettyType t2

prettyTerm :: RawTerm -> String
prettyTerm (RVar x) = x
prettyTerm (RLit (LInt n)) = show n
prettyTerm (RLit (LBool b)) = show b
prettyTerm (RLam x t body) =
  "λ" ++ x ++ ":" ++ prettyType t ++ "." ++ prettyTerm body
prettyTerm (RApp f a) =
  "(" ++ prettyTerm f ++ " " ++ prettyTerm a ++ ")"

-- | Example terms and usage
examples :: IO ()
examples = do
  putStrLn "=== Simply Typed Lambda Calculus Examples ==="

  let intType = BaseType "Int"
      boolType = BaseType "Bool"

  -- Identity function: λx:Int.x
  let identity = RLam "x" intType (RVar "x")
  putStrLn $ "Identity: " ++ prettyTerm identity

  case typeCheck Map.empty identity of
    Right typed -> putStrLn $ "Type: " ++ prettyType (termType typed)
    Left err -> putStrLn $ "Error: " ++ show err

  -- Function composition: λf:(Int→Int).λg:(Int→Int).λx:Int.(f (g x))
  let intToInt = Arrow intType intType
      compose = RLam "f" intToInt
                  (RLam "g" intToInt
                    (RLam "x" intType
                      (RApp (RVar "f")
                            (RApp (RVar "g") (RVar "x")))))

  putStrLn $ "\nComposition: " ++ prettyTerm compose
  case typeCheck Map.empty compose of
    Right typed -> putStrLn $ "Type: " ++ prettyType (termType typed)
    Left err -> putStrLn $ "Error: " ++ show err

  -- Application example: identity 42
  let app = RApp identity (RLit (LInt 42))
  putStrLn $ "\nApplication: " ++ prettyTerm app

  case typeCheck Map.empty app of
    Right typed -> do
      putStrLn $ "Type: " ++ prettyType (termType typed)
      let result = eval Map.empty typed
      putStrLn $ "Evaluates to: " ++ show result
    Left err -> putStrLn $ "Error: " ++ show err

  -- Type error example
  let badApp = RApp identity (RLit (LBool True))
  putStrLn $ "\nBad application: " ++ prettyTerm badApp

  case typeCheck Map.empty badApp of
    Right typed -> putStrLn $ "Type: " ++ prettyType (termType typed)
    Left err -> putStrLn $ "Type Error: " ++ show err

-- | Church numerals in simply typed lambda calculus
churchNumerals :: IO ()
churchNumerals = do
  putStrLn "\n=== Church Numerals (Simply Typed) ==="

  let intType = BaseType "Int"
      -- Church numeral type: ∀A. (A → A) → A → A
      -- In simply typed LC, we fix A to Int: (Int → Int) → Int → Int
      churchType = Arrow (Arrow intType intType) (Arrow intType intType)

  -- Zero: λf:(Int→Int).λx:Int.x
  let zero = RLam "f" (Arrow intType intType)
               (RLam "x" intType (RVar "x"))

  -- One: λf:(Int→Int).λx:Int.(f x)
  let one = RLam "f" (Arrow intType intType)
              (RLam "x" intType
                (RApp (RVar "f") (RVar "x")))

  putStrLn $ "Zero: " ++ prettyTerm zero
  case typeCheck Map.empty zero of
    Right typed -> putStrLn $ "Type: " ++ prettyType (termType typed)
    Left err -> putStrLn $ "Error: " ++ show err

  putStrLn $ "\nOne: " ++ prettyTerm one
  case typeCheck Map.empty one of
    Right typed -> putStrLn $ "Type: " ++ prettyType (termType typed)
    Left err -> putStrLn $ "Error: " ++ show err

main :: IO ()
main = do
  examples
  churchNumerals
```

## Running the Code

Save as `SimplyTyped.hs` and run in GHCi:

```bash
ghci SimplyTyped.hs
*SimplyTyped> main
```

Expected output:
```
=== Simply Typed Lambda Calculus Examples ===
Identity: λx:Int.x
Type: Int → Int

Composition: λf:(Int → Int).λg:(Int → Int).λx:Int.(f (g x))
Type: (Int → Int) → (Int → Int) → Int → Int

Application: (λx:Int.x 42)
Type: Int
Evaluates to: VLit (LInt 42)

Bad application: (λx:Int.x True)
Type Error: TypeMismatch (BaseType "Int") (BaseType "Bool")

=== Church Numerals (Simply Typed) ===
Zero: λf:(Int → Int).λx:Int.x
Type: (Int → Int) → Int → Int

One: λf:(Int → Int).λx:Int.(f x)
Type: (Int → Int) → Int → Int
```

## Key Features

### Type System
- **Base types**: `Int`, `Bool`
- **Function types**: `A → B`
- **Type checking**: Prevents runtime type errors
- **Type inference**: Determines result types automatically

### Terms
- **Variables**: With explicit type annotations
- **Abstractions**: `λx:T.e` with parameter type
- **Applications**: Type-checked function calls
- **Literals**: Typed constants

### Safety Properties
- **Type preservation**: Well-typed terms remain well-typed after reduction
- **Progress**: Well-typed terms either are values or can reduce
- **Strong normalization**: All well-typed terms terminate

## Theoretical Foundation

This implements the **simply typed lambda calculus** with:

1. **Type judgment**: `Γ ⊢ e : T`
2. **Typing rules**:
   - Variables: `Γ, x:T ⊢ x : T`
   - Abstraction: `Γ, x:A ⊢ e : B ⇒ Γ ⊢ λx:A.e : A → B`
   - Application: `Γ ⊢ e₁ : A → B, Γ ⊢ e₂ : A ⇒ Γ ⊢ e₁ e₂ : B`

## Extensions

This can be extended with:
- **Polymorphism**: System F (second-order lambda calculus)
- **Dependent types**: Types that depend on values
- **Linear types**: Resource-aware computation
- **Effect systems**: Tracking computational effects