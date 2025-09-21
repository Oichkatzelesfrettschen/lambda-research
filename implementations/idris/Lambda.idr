module Lambda

%default total

data Term : Type where
  Var : String -> Term
  Lam : String -> Term -> Term
  App : Term -> Term -> Term

-- Function to generate a fresh variable name
freshVar : List String -> String -> String
freshVar used x = if elem x used then freshVar used (x ++ "'") else x

-- Calculate free variables in a term
freeVars : Term -> List String
freeVars (Var x) = [x]
freeVars (Lam x t) = delete x (freeVars t)
freeVars (App t1 t2) = freeVars t1 `union` freeVars t2

-- Perform substitution (t[x := s])
substitute : Term -> String -> Term -> Term
substitute (Var y) x s = if x == y then s else Var y
substitute (Lam y t) x s =
  if x == y then Lam y t
  else if elem y (freeVars s)
    then
      let y' = freshVar (freeVars t `union` freeVars s) y
          t' = substitute t y (Var y')
       in Lam y' (substitute t' x s)
    else Lam y (substitute t x s)
substitute (App t1 t2) x s = App (substitute t1 x s) (substitute t2 x s)

-- One step of beta-reduction (call-by-name)
eval1 : Term -> Maybe Term
eval1 (App (Lam x t) s) = Just (substitute t x s)
eval1 (App t1 t2) =
  case eval1 t1 of
    Just t1' => Just (App t1' t2)
    Nothing =>
      case eval1 t2 of
        Just t2' => Just (App t1 t2')
        Nothing => Nothing
eval1 (Lam x t) =
  case eval1 t of
    Just t' => Just (Lam x t')
    Nothing => Nothing
eval1 _ = Nothing

-- Normalize a term
normalize : Term -> Term
normalize t =
  case eval1 t of
    Just t' => normalize t'
    Nothing => t

-- Helper functions for List
delete : Eq a => a -> List a -> List a
delete _ [] = []
delete x (y :: ys) = if x == y then delete x ys else y :: delete x ys

union : Eq a => List a -> List a -> List a
union [] ys = ys
union (x :: xs) ys = if elem x ys then union xs ys else x :: union xs ys

elem : Eq a => a -> List a -> Bool
elem _ [] = False
elem x (y :: ys) = x == y || elem x ys

-- Example terms
-- Identity function: (\x.x)
idTerm : Term
idTerm = Lam "x" (Var "x")

-- Application of identity to y: ((\x.x) y)
appId : Term
appId = App idTerm (Var "y")

-- (\x.\y.x)
kTerm : Term
kTerm = Lam "x" (Lam "y" (Var "x"))

-- ((\x.\y.x) a b)
appK : Term
appK = App (App kTerm (Var "a")) (Var "b")

-- (\x.x x) (\x.x x) - Omega combinator (non-terminating)
omega : Term
omega = App (Lam "x" (App (Var "x") (Var "x"))) (Lam "x" (App (Var "x") (Var "x")))

-- Test cases
-- testId : Term
-- testId = normalize appId -- Should be Var "y"

-- testK : Term
-- testK = normalize appK -- Should be Var "a"

-- testOmega : Term
-- testOmega = normalize omega -- Should not terminate (or reach a fixed point if eval1 is not strict enough)
