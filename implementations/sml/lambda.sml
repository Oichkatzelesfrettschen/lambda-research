(*
 * lambda.sml
 *
 * Copyright (C) 2025 Lambda Research Collective
 *
 * This file is part of Lambda Calculus Research Repository.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 *)


datatype term = Var of string | Abs of string * term | App of term * term;

(* Helper for generating fresh variables to avoid capture during substitution *)
val fresh_var_counter = ref 0;
fun fresh_var () = 
  let
    val current_count = !fresh_var_counter;
  in
    fresh_var_counter := current_count + 1;
    "v" ^ Int.toString current_count
  end;

(* Function to find free variables in a term *)
fun free_vars term = 
  let 
    fun fv (Var x) = [x]
      | fv (Abs (x, t)) = List.filter (fn y => y <> x) (fv t)
      | fv (App (t1, t2)) = (fv t1) @ (fv t2)
  in
    fv term
  end;

(* Substitution: [x := s]t *)
fun substitute (x: string, s: term, t: term) : term = 
  case t of
    Var y => if y = x then s else Var y
  | Abs (y, t1) => 
      if y = x then Abs (y, t1) (* x is bound, no substitution *)
      else if not (List.exists (fn z => z = y) (free_vars s)) then (* y not in FV(s) *)
        Abs (y, substitute (x, s, t1))
      else (* y is in FV(s), alpha-convert y *)
        let
          val y_prime = fresh_var ()
          val t1_prime = substitute (y, Var y_prime, t1)
        in
          Abs (y_prime, substitute (x, s, t1_prime))
        end
  | App (t1, t2) => App (substitute (x, s, t1), substitute (x, s, t2));

(* Call-by-value evaluation strategy *)
fun eval (t: term) : term = 
  case t of
    Var _ => t
  | Abs _ => t
  | App (t1, t2) => 
      let
        val t1_val = eval t1
      in
        case t1_val of
          Abs (x, body) =>
            let
              val t2_val = eval t2
            in
              eval (substitute (x, t2_val, body))
            end
        | _ => App (t1_val, eval t2) (* t1_val is not an abstraction, so it's a stuck application *)
      end;

(* Function to print terms (for better readability) *)
fun term_to_string (Var x) = x
  | term_to_string (Abs (x, t)) = "(λ" ^ x ^ "." ^ term_to_string t ^ ")"
  | term_to_string (App (t1, t2)) = "(" ^ term_to_string t1 ^ " " ^ term_to_string t2 ^ ")";

(* Example Usage *)
(* Identity function: (λx.x) *)
val id = Abs ("x", Var "x");

(* Application of identity to y: (λx.x) y *)
val app_id_y = App (id, Var "y");

(* (λx.λy.x) a b  -- K combinator *)
val k_combinator = Abs ("x", Abs ("y", Var "x"));
val app_k_a_b = App (App (k_combinator, Var "a"), Var "b");

(* (λf.λx.f (f x)) (λz.z) y -- apply identity twice to y *)
val apply_twice = Abs ("f", Abs ("x", App (Var "f", App (Var "f", Var "x"))));
val app_twice_id_y = App (App (apply_twice, Abs ("z", Var "z")), Var "y");

(* (λx.x x) (λx.x x) -- Omega combinator (non-terminating in CBV) *)
val omega_body = Abs ("x", App (Var "x", Var "x"));
val omega = App (omega_body, omega_body);

val _ = print "\nLambda Calculus Implementation in Standard ML\n";
val _ = print "----------------------------------------\n";

val _ = print ("Identity function applied to y: " ^ term_to_string app_id_y ^ "\n");
val _ = print ("Result: " ^ term_to_string (eval app_id_y) ^ "\n\n");

val _ = print ("K combinator applied to a and b: " ^ term_to_string app_k_a_b ^ "\n");
val _ = print ("Result: " ^ term_to_string (eval app_k_a_b) ^ "\n\n");

val _ = print ("Apply identity twice to y: " ^ term_to_string app_twice_id_y ^ "\n");
val _ = print ("Result: " ^ term_to_string (eval app_twice_id_y) ^ "\n\n");

val _ = print ("Omega combinator (non-terminating in CBV, will loop if eval is not careful): " ^ term_to_string omega ^ "\n");
(* val _ = print ("Result: " ^ term_to_string (eval omega) ^ "\n\n"); *)
val _ = print "(Commented out evaluation of Omega to prevent infinite loop in simple CBV eval)\n\n";