/*
 * LambdaCalculus.scala
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
 */


object LambdaCalculus {

  // 1. Define the Abstract Syntax Tree (AST)
  enum Term {
    case Var(name: String)
    case Abs(param: String, body: Term)
    case App(rator: Term, rand: Term)
  }
  import Term._

  // Helper for generating fresh variables
  private var freshVarCounter: Int = 0
  private def freshVar(): String = {
    freshVarCounter += 1
    s"v$freshVarCounter"
  }

  extension (t: Term) {

    // 2. Implement freeVars
    def freeVars: Set[String] = t match {
      case Var(name) => Set(name)
      case Abs(param, body) => body.freeVars - param
      case App(rator, rand) => rator.freeVars ++ rand.freeVars
    }

    // 3. Implement substitute (t[x := s])
    def substitute(x: String, s: Term): Term = t match {
      case Var(name) => if (name == x) s else Var(name)
      case Abs(param, body) =>
        if (param == x) Abs(param, body) // x is bound, no substitution
        else if (s.freeVars.contains(param)) {
          // Alpha-conversion needed to prevent variable capture
          val newParam = freshVar()
          val renamedBody = body.substitute(param, Var(newParam))
          Abs(newParam, renamedBody.substitute(x, s))
        } else {
          Abs(param, body.substitute(x, s))
        }
      case App(rator, rand) =>
        App(rator.substitute(x, s), rand.substitute(x, s))
    }

    // 4. Implement betaReduce (one step, call-by-name)
    def betaReduce: Option[Term] = t match {
      case App(Abs(param, body), rand) =>
        Some(body.substitute(param, rand))
      case App(rator, rand) =>
        rator.betaReduce.map(App(_, rand))
          .orElse(rand.betaReduce.map(App(rator, _)))
      case Abs(param, body) =>
        body.betaReduce.map(Abs(param, _))
      case _ => None
    }

    // 5. Implement normalize
    def normalize: Term = {
      var current = t
      var next: Option[Term] = current.betaReduce
      while (next.isDefined) {
        current = next.get
        next = current.betaReduce
      }
      current
    }

    // For pretty printing
    override def toString: String = t match {
      case Var(name) => name
      case Abs(param, body) => s"(λ$param.$body)"
      case App(rator, rand) => s"($rator $rand)"
    }
  }

  def main(args: Array[String]): Unit = {
    // Example: Identity function (λx.x)
    val id = Abs("x", Var("x"))
    println(s"Identity function: $id")

    // Example: Application of identity to 'y': (λx.x)y
    val appId = App(id, Var("y"))
    println(s"Application (λx.x)y: $appId")
    println(s"(λx.x)y normalizes to: ${appId.normalize}") // Expected: y

    // Example: K combinator (λx.λy.x)
    val k = Abs("x", Abs("y", Var("x")))
    println(s"K combinator: $k")

    // Example: (λx.λy.x) a b
    val appK = App(App(k, Var("a")), Var("b"))
    println(s"Application (λx.λy.x) a b: $appK")
    println(s"(λx.λy.x) a b normalizes to: ${appK.normalize}") // Expected: a

    // Example with potential capture (λx. (λy. (x y))) y
    val innerLam = Abs("y", App(Var("x"), Var("y")))
    val outerLam = Abs("x", innerLam)
    val captureExample = App(outerLam, Var("y"))
    println(s"Capture example (λx. (λy. (x y))) y: $captureExample")
    println(s"Normalizes to: ${captureExample.normalize}") // Expected: (λvX.(y vX)) where vX is a fresh var

    // Omega combinator (λx.x x) (λx.x x) - non-terminating
    val omegaBody = Abs("x", App(Var("x"), Var("x")))
    val omega = App(omegaBody, omegaBody)
    println(s"Omega combinator: $omega")
    // println(s"Omega normalizes to: ${omega.normalize}") // This will loop indefinitely
    println("(Evaluation of Omega commented out to prevent infinite loop)")
  }
}
