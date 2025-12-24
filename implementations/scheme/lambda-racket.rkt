#lang racket

;; lambda-racket.rkt
;;
;; Copyright (C) 2025 Lambda Research Collective
;;
;; This file is part of Lambda Calculus Research Repository.
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program. If not, see <https://www.gnu.org/licenses/>.


;; Define data structures for lambda calculus expressions

;; A variable is just a symbol
(struct var (name) #:transparent)

;; A lambda abstraction has a bound variable and a body expression
(struct lam (param body) #:transparent)

;; An application has a function expression and an argument expression
(struct app (rator rand) #:transparent)

;; --- Helper functions for substitution ---

;; Generates a fresh variable name (symbol)
(define next-fresh-idx 0)
(define (fresh-var)
  (set! next-fresh-idx (+ next-fresh-idx 1))
  (string->symbol (format "v~a" next-fresh-idx)))

;; Computes the set of free variables in an expression
(define (free-vars expr)
  (match expr
    [(var name) (list name)]
    [(lam param body) (remove* (list param) (free-vars body))]
    [(app rator rand) (append (free-vars rator) (free-vars rand))]))

;; --- Substitution function ---
;; (substitute old-var-symbol sub-expr target-expr)
;; Replaces all free occurrences of old-var-symbol in target-expr with sub-expr,
;; performing alpha-conversion to prevent variable capture.
(define (substitute old-var-symbol sub-expr target-expr)
  (match target-expr
    [(var name)
     (if (eq? name old-var-symbol)
         sub-expr
         target-expr)]
    [(lam param body)
     (cond
       ;; If the lambda's parameter is the variable we're substituting for,
       ;; then this lambda binds it, so we stop substitution in its body.
       [(eq? param old-var-symbol)
        target-expr]
       ;; If the lambda's parameter is a free variable in the substitution expression,
       ;; we need to alpha-convert the lambda to prevent capture.
       [(member param (free-vars sub-expr))
        (define new-param (fresh-var))
        ;; Substitute the old parameter with the new one in the body
        (define renamed-body (substitute param (var new-param) body))
        ;; Then perform the original substitution in the renamed body
        (lam new-param (substitute old-var-symbol sub-expr renamed-body))]
       ;; Otherwise, no capture risk, just recurse into the body.
       [else
        (lam param (substitute old-var-symbol sub-expr body))])]
    [(app rator rand)
     (app (substitute old-var-symbol sub-expr rator)
          (substitute old-var-symbol sub-expr rand))]))

;; --- Evaluation function (beta-reduction) ---
;; (eval-lc expr)
;; Performs one step of beta-reduction (call-by-value strategy).
(define (eval-lc expr)
  (match expr
    ;; Case 1: Application of a lambda to an argument
    [(app (lam param body) arg)
     (substitute param arg body)]
    ;; Case 2: Function part of an application can be reduced
    [(app rator rand)
     (define reduced-rator (eval-lc rator))
     (if (equal? reduced-rator rator)
         ;; If rator didn't reduce, try reducing rand
         (app rator (eval-lc rand))
         ;; If rator reduced, use the reduced rator
         (app reduced-rator rand))]
    ;; Case 3: Lambda body can be reduced (optional, for full reduction)
    [(lam param body)
     (lam param (eval-lc body))]
    ;; Variables and fully reduced lambdas are values, cannot be reduced further
    [_ expr]))

;; --- Full evaluation (repeated beta-reduction until normal form) ---
(define (full-eval-lc expr)
  (let loop ((current-expr expr))
    (define next-expr (eval-lc current-expr))
    (if (equal? current-expr next-expr)
        current-expr
        (loop next-expr))))

;; --- Examples ---

;; Identity function: (λx.x)
(define id (lam 'x (var 'x)))

;; Application of identity to 'y': (λx.x)y  -> y
(define ex1 (app id (var 'y)))
(printf "Example 1: (λx.x)y -> ~a\n" (full-eval-lc ex1)) ; Expected: (var 'y)

;; Constant function: (λx. (λy.x))
(define const-fn (lam 'x (lam 'y (var 'x))))

;; Application: ((λx. (λy.x)) z) w -> z
(define ex2 (app (app const-fn (var 'z)) (var 'w)))
(printf "Example 2: ((λx. (λy.x)) z) w -> ~a\n" (full-eval-lc ex2)) ; Expected: (var 'z)

;; Example with potential capture (alpha-conversion needed)
;; (λx. (λy. (x y))) y  -- if we substitute 'y' for 'x' in (λy. (x y)),
;;                        the inner 'y' would capture the outer 'y'.
;;                        So, (λy. (x y)) should become (λv1. (x v1)) first.
;; Then substitute 'y' for 'x' -> (λv1. (y v1))
(define inner-lam (lam 'y (app (var 'x) (var 'y))))
(define outer-lam (lam 'x inner-lam))
(define ex3 (app outer-lam (var 'y)))
(printf "Example 3: (λx. (λy. (x y))) y -> ~a\n" (full-eval-lc ex3)) ; Expected: (lam 'v1 (app (var 'y) (var 'v1)))

;; Another example: (λx. (λy. x)) (λz. z)
;; This should reduce to (λy. (λz. z))
(define ex4 (app (lam 'x (lam 'y (var 'x))) (lam 'z (var 'z))))
(printf "Example 4: (λx. (λy. x)) (λz. z) -> ~a\n" (full-eval-lc ex4)) ; Expected: (lam 'y (lam 'z (var 'z)))

;; Example with nested application: (λf. (λx. (f x))) (λy. y) z
;; This should reduce to (λx. ((λy. y) x)) z -> (λx. x) z -> z
(define apply-twice (lam 'f (lam 'x (app (var 'f) (var 'x)))))
(define ex5 (app (app apply-twice (lam 'y (var 'y))) (var 'z)))
(printf "Example 5: (λf. (λx. (f x))) (λy. y) z -> ~a\n" (full-eval-lc ex5)) ; Expected: (var 'z)
