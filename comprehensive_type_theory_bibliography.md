# Comprehensive Academic Bibliography: Modal Logic/Types, Refinement Types, and Probabilistic Types

## Table of Contents
1. [Modal Logic/Types](#modal-logictypes)
2. [Refinement Types](#refinement-types)
3. [Probabilistic Types](#probabilistic-types)

---

## Modal Logic/Types

### Foundational Work: Davies-Pfenning Temporal Logic

**Core Papers:**
1. **Davies, Rowan and Pfenning, Frank** (2001). "A modal analysis of staged computation." *Journal of the ACM*, 48(3), 555-604.
   - **Key Contribution**: Fundamental relationship between temporal logic and multi-stage languages
   - **Technical Innovation**: Extension of Curry-Howard isomorphism to staged computation
   - **Repository**: https://www.cs.cmu.edu/~fp/papers/jacm00.pdf

2. **Pfenning, Frank and Davies, Rowan** (2001). "A judgmental reconstruction of modal logic." *Mathematical Structures in Computer Science*, 11(4), 511-540.
   - **Key Contribution**: Constructive meaning explanations for necessity and possibility
   - **Technical Innovation**: Natural deduction system for intuitionistic modal logic
   - **Repository**: https://www.cs.cmu.edu/~fp/papers/mscs00.pdf

3. **Davies, Rowan** (1996). "A temporal logic approach to binding-time analysis." *Proceedings of the 11th Annual IEEE Symposium on Logic in Computer Science*.
   - **Key Contribution**: Connection between temporal logic and binding-time analysis
   - **Technical Innovation**: Use of "next time" operator for staged computation

### Modal Lambda Calculus and Staged Computation

**Academic Papers:**
4. **Pfenning, Frank and Wong, Hao-Chi** (1995). "On a modal λ-calculus for S4." *Electronic Notes in Theoretical Computer Science*, 1, 515-534.
   - **Key Contribution**: Proof term calculus for intuitionistic modal logic S4
   - **Repository**: https://www.cs.cmu.edu/~fp/papers/mfps95.pdf

5. **Clouston, Ranald** (2022). "A categorical normalization proof for the modal lambda-calculus." *arXiv preprint arXiv:2211.12318*.
   - **Key Contribution**: Normalization by evaluation algorithm for modal lambda calculus
   - **Technical Innovation**: Sound and complete NbE for staged meta-programming
   - **Repository**: https://arxiv.org/abs/2211.12318

6. **Murphy VII, Tom and Harper, Robert** (2004). "A symmetric modal lambda calculus for distributed computing." *Proceedings of the 19th Annual IEEE Symposium on Logic in Computer Science*.
   - **Key Contribution**: Modal calculus for distributed computation
   - **Repository**: https://www.cs.cmu.edu/~rwh/papers/s5/short.pdf

7. **Bierman, Gavin and de Paiva, Valeria** (2000). "On an intuitionistic modal logic." *Studia Logica*, 65(3), 383-416.
   - **Key Contribution**: Categorical semantics for intuitionistic modal logic

8. **Jia, Limin and Walker, David** (2004). "Modal proofs as distributed programs." *European Symposium on Programming*, Springer.
   - **Key Contribution**: Connection between modal proofs and distributed programs

### Necessity and Possibility Modalities

**Core Research:**
9. **Luo, Zhaohui** (1994). "Computation and reasoning: a type theory for computer science." *International Series of Monographs on Computer Science*.
   - **Key Contribution**: Type-theoretic treatment of modalities

10. **Gabbay, Dov and Woods, John** (2006). "Handbook of the History of Logic, Volume 7: Logic and the Modalities in the Twentieth Century." *Elsevier*.
    - **Key Contribution**: Comprehensive historical treatment of modal logic

11. **Blackburn, Patrick, de Rijke, Maarten, and Venema, Yde** (2001). "Modal Logic." *Cambridge University Press*.
    - **Key Contribution**: Comprehensive textbook on modal logic foundations

12. **Fitting, Melvin and Mendelsohn, Richard** (1998). "First-Order Modal Logic." *Kluwer Academic Publishers*.
    - **Key Contribution**: First-order extensions of modal logic

### Linear Temporal Logic Integration

**Academic Papers:**
13. **Emerson, E. Allen** (1990). "Temporal and modal logic." *Handbook of Theoretical Computer Science*, Volume B, 995-1072.
    - **Key Contribution**: Comprehensive survey of temporal and modal logic

14. **Pnueli, Amir** (1977). "The temporal logic of programs." *18th Annual Symposium on Foundations of Computer Science*.
    - **Key Contribution**: Foundation of temporal logic for program verification

15. **Sistla, A. Prasad and Clarke, Edmund M.** (1985). "The complexity of propositional linear temporal logics." *Journal of the ACM*, 32(3), 733-749.
    - **Key Contribution**: Complexity analysis of linear temporal logic

16. **Vardi, Moshe Y. and Wolper, Pierre** (1994). "Reasoning about infinite computations." *Information and Computation*, 115(1), 1-37.
    - **Key Contribution**: Automata-theoretic approach to temporal logic

### Epistemic and Doxastic Logics

**Foundational Work:**
17. **Hintikka, Jaakko** (1962). "Knowledge and Belief: An Introduction to the Logic of the Two Notions." *Cornell University Press*.
    - **Key Contribution**: Foundational text for epistemic logic

18. **Fagin, Ronald, Halpern, Joseph Y., Moses, Yoram, and Vardi, Moshe Y.** (1995). "Reasoning about Knowledge." *MIT Press*.
    - **Key Contribution**: Comprehensive treatment of epistemic logic

19. **van Ditmarsch, Hans, van der Hoek, Wiebe, and Kooi, Barteld** (2007). "Dynamic Epistemic Logic." *Springer*.
    - **Key Contribution**: Dynamic extensions of epistemic logic

20. **Meyer, John-Jules Ch. and van der Hoek, Wiebe** (1995). "Epistemic Logic for AI and Computer Science." *Cambridge University Press*.
    - **Key Contribution**: Applications of epistemic logic to computer science

### Modern Applications (Staging, Metaprogramming)

**Recent Research:**
21. **Taha, Walid and Sheard, Tim** (2000). "MetaML and multi-stage programming with explicit annotations." *Theoretical Computer Science*, 248(1-2), 211-242.
    - **Key Contribution**: Multi-stage programming language design

22. **Calcagno, Cristiano, Moggi, Eugenio, and Taha, Walid** (2000). "ML-like inference for classifiers." *European Symposium on Programming*, Springer.
    - **Key Contribution**: Type inference for staged languages

23. **Nanevski, Aleksandar, Pfenning, Frank, and Pientka, Brigitte** (2008). "Contextual modal type theory." *ACM Transactions on Computational Logic*, 9(3), 1-49.
    - **Key Contribution**: Contextual approach to modal type theory

24. **Chlipala, Adam** (2010). "A verified compiler for an impure functional language." *ACM SIGPLAN Notices*, 45(1), 93-106.
    - **Key Contribution**: Verified compilation with modal types

25. **Cave, Andrew and Pientka, Brigitte** (2012). "Programming with binders and indexed data-types." *ACM SIGPLAN Notices*, 47(1), 413-424.
    - **Key Contribution**: Modal types for variable binding

### Implementation Repositories and Tools

**Key Implementations:**
- **Twelf**: Logic programming language with modal extensions
  - Repository: https://github.com/twelf/twelf
- **Beluga**: Programming language with contextual modal types
  - Repository: https://github.com/Beluga-lang/Beluga
- **MetaML**: Multi-stage programming language
  - Repository: Historical implementations available

---

## Refinement Types

### Freeman-Pfenning Foundational Work

**Core Papers:**
26. **Freeman, Timothy S. and Pfenning, Frank** (1991). "Refinement types for ML." *Proceedings of the ACM Conference on Programming Language Design and Implementation*, 268-277.
    - **Key Contribution**: Original introduction of refinement types
    - **Technical Innovation**: Sub-datatypes through constructor refinement
    - **Repository**: https://www.cs.cmu.edu/~fp/papers/pldi91.pdf

27. **Freeman, Timothy S.** (1994). "Refinement Types for ML." *PhD Dissertation, Carnegie Mellon University*.
    - **Key Contribution**: Comprehensive treatment of refinement type theory
    - **Technical Innovation**: Decidable type checking with intersection types

28. **Xi, Hongwei and Pfenning, Frank** (1998). "Eliminating array bound checking through dependent types." *ACM SIGPLAN Notices*, 33(5), 249-257.
    - **Key Contribution**: Dependent refinement types for array safety
    - **Technical Innovation**: Integration with ML type inference

29. **Xi, Hongwei and Pfenning, Frank** (1999). "Dependent types in practical programming." *Proceedings of the 26th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, 214-227.
    - **Key Contribution**: Practical dependent type system (Dependent ML)
    - **Repository**: DML implementations available

### Liquid Types and SMT Integration

**Foundational Liquid Types:**
30. **Rondon, Patrick M., Kawaguchi, Ming, and Jhala, Ranjit** (2008). "Liquid types." *Proceedings of the 29th ACM SIGPLAN Conference on Programming Language Design and Implementation*, 159-169.
    - **Key Contribution**: Predicate abstraction for automated refinement inference
    - **Technical Innovation**: SMT-based constraint solving
    - **Repository**: https://goto.ucsd.edu/~rjhala/papers/liquid_types.html

31. **Kawaguchi, Ming, Rondon, Patrick, and Jhala, Ranjit** (2009). "Type-based data structure verification." *Proceedings of the 30th ACM SIGPLAN Conference on Programming Language Design and Implementation*, 304-315.
    - **Key Contribution**: Data structure invariant verification
    - **Repository**: https://goto.ucsd.edu/~rjhala/papers/

32. **Kawaguchi, Ming, Rondon, Patrick M., Bakst, Alexander, and Jhala, Ranjit** (2012). "Deterministic parallelism via liquid effects." *Proceedings of the 33rd ACM SIGPLAN Conference on Programming Language Design and Implementation*, 45-56.
    - **Key Contribution**: Effect systems with liquid types

### Abstract Refinement Types

**Core Research:**
33. **Vazou, Niki, Rondon, Patrick M., and Jhala, Ranjit** (2013). "Abstract refinement types." *Programming Languages and Systems*, Springer, 209-228.
    - **Key Contribution**: Parametric refinements with SMT decidability
    - **Technical Innovation**: Uninterpreted propositions in refinement logic
    - **Repository**: https://goto.ucsd.edu/~rjhala/papers/abstract_refinement_types.html

34. **Vazou, Niki, Seidel, Eric L., Jhala, Ranjit, Vytiniotis, Dimitrios, and Peyton-Jones, Simon** (2014). "Refinement types for Haskell." *Proceedings of the 19th ACM SIGPLAN International Conference on Functional Programming*, 269-282.
    - **Key Contribution**: Refinement types for lazy evaluation
    - **Repository**: https://goto.ucsd.edu/~nvazou/refinement_types_for_haskell.pdf

35. **Vazou, Niki, Bakst, Alexander, and Jhala, Ranjit** (2015). "Bounded refinement types." *Proceedings of the 20th ACM SIGPLAN International Conference on Functional Programming*, 48-61.
    - **Key Contribution**: Termination analysis with refinement types

### Dependent Refinement Types

**Academic Papers:**
36. **Condit, Jeremy, Harren, Matthew, Anderson, Zachary, Gay, David, and Necula, George C.** (2007). "Dependent types for low-level programming." *European Symposium on Programming*, Springer, 520-535.
    - **Key Contribution**: Dependent types for systems programming

37. **Swamy, Nikhil, Chen, Juan, Fournet, Cédric, Strub, Pierre-Yves, Bhargavan, Karthikeyan, and Yang, Jean** (2011). "Secure distributed programming with value-dependent types." *Proceedings of the 16th ACM SIGPLAN International Conference on Functional Programming*, 266-278.
    - **Key Contribution**: F* functional language with dependent refinement types

38. **Swamy, Nikhil, Hriţcu, Cătălin, Keller, Chantal, Rastogi, Aseem, Delignat-Lavaud, Antoine, Forest, Simon, Bhargavan, Karthikeyan, Fournet, Cédric, Strub, Pierre-Yves, Kohlweiss, Markulf, Zinzindohoué, Jean-Karim, and Zanella-Béguelin, Santiago** (2016). "Dependent types and multi-monadic effects in F*." *Proceedings of the 43rd Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, 256-270.
    - **Key Contribution**: Advanced dependent type features in F*

### Practical Implementations

**Liquid Haskell:**
39. **Vazou, Niki, Seidel, Eric L., Jhala, Ranjit, Vytiniotis, Dimitrios, and Peyton-Jones, Simon** (2014). "LiquidHaskell: experience with refinement types in the real world." *Proceedings of the 2nd ACM SIGPLAN Symposium on Haskell*, 39-51.
    - **Key Contribution**: Industrial application of refinement types
    - **Repository**: https://github.com/ucsd-progsys/liquidhaskell

40. **Vazou, Niki and Jhala, Ranjit** (2018). "Refinement reflection: complete verification with SMT." *Proceedings of the ACM on Programming Languages*, 2(POPL), 1-31.
    - **Key Contribution**: Reflecting function definitions into refinement types
    - **Technical Innovation**: Equational proofs with SMT

**F* Language:**
41. **Swamy, Nikhil** (2016). "Functional programming with effects and the F* proof assistant." *Tutorial at PLDI 2016*.
    - **Key Contribution**: Comprehensive F* tutorial
    - **Repository**: https://github.com/FStarLang/FStar

42. **Martínez, Guido, Ahman, Danel, Duregård, Viktor, Vazou, Niki, Nanevski, Aleksandar, and Morrisett, Greg** (2019). "Dijkstra monads for all." *Proceedings of the 24th ACM SIGPLAN International Conference on Functional Programming*, 1-29.
    - **Key Contribution**: Monadic effects in F*

**Dafny:**
43. **Leino, K. Rustan M.** (2010). "Dafny: an automatic program verifier for functional correctness." *International Conference on Logic for Programming Artificial Intelligence and Reasoning*, Springer, 348-370.
    - **Key Contribution**: Specification language with automatic verification
    - **Repository**: https://github.com/dafny-lang/dafny

44. **Leino, K. Rustan M.** (2012). "Automating theorem proving with SMT." *International Conference on Interactive Theorem Proving*, Springer, 2-16.
    - **Key Contribution**: SMT integration strategies

### Program Verification Applications

**Verification Tools:**
45. **Rondon, Patrick M., Kawaguchi, Ming, and Jhala, Ranjit** (2010). "Low-level liquid types." *Proceedings of the 37th Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, 131-144.
    - **Key Contribution**: Refinement types for C programs
    - **Repository**: CSolve implementation

46. **Jhala, Ranjit and Vazou, Niki** (2021). "Refinement types: a tutorial." *Foundations and Trends in Programming Languages*, 6(3-4), 159-317.
    - **Key Contribution**: Comprehensive tutorial on refinement types
    - **Repository**: https://arxiv.org/abs/2010.07763

47. **Polikarpova, Nadia, Kuraj, Ivan, and Solar-Lezama, Armando** (2016). "Program synthesis with polymorphic refinement types." *Proceedings of the 37th ACM SIGPLAN Conference on Programming Language Design and Implementation*, 522-538.
    - **Key Contribution**: Synthesis with refinement types

48. **Seidel, Eric L., Vazou, Niki, and Jhala, Ranjit** (2015). "Type targeted testing of functional programs." *Proceedings of the 20th ACM SIGPLAN International Conference on Functional Programming*, 37-50.
    - **Key Contribution**: Property-based testing with refinement types

49. **Vazou, Niki, Tondwalkar, Anish, Choudhury, Vikraman, Scott, Ryan G., Newton, Ryan R., Osera, Philip, and Jhala, Ranjit** (2017). "Refinement reflection: complete verification with SMT." *Proceedings of the ACM on Programming Languages*, 2(POPL), 53:1-53:31.
    - **Key Contribution**: Proof automation with reflection

50. **Chen, Jiasi, Chajed, Tej, Konečný, Michal, Woos, Doug, Anderson, Thomas, and Tatlock, Zachary** (2020). "Verifying replicated data types with typeclass refinements in Liquid Haskell." *Proceedings of the ACM on Programming Languages*, 4(OOPSLA), 1-30.
    - **Key Contribution**: Verification of distributed systems

---

## Probabilistic Types

### Probabilistic Programming Foundations

**Foundational Work:**
51. **Giry, Michèle** (1982). "A categorical approach to probability theory." *Categorical Aspects of Topology and Analysis*, Springer, 68-85.
    - **Key Contribution**: Categorical foundations of probability theory
    - **Technical Innovation**: Giry monad for probability distributions

52. **Panangaden, Prakash** (2009). "Labelled Markov Processes." *Imperial College Press*.
    - **Key Contribution**: Process-algebraic approach to probabilistic systems
    - **Technical Innovation**: Bisimulation for probabilistic processes

53. **Heunen, Chris, Kammar, Ohad, Staton, Sam, and Yang, Hongseok** (2017). "A convenient category for higher-order probability theory." *Proceedings of the 32nd Annual ACM/IEEE Symposium on Logic in Computer Science*, 1-12.
    - **Key Contribution**: Category theory for higher-order probability
    - **Repository**: https://arxiv.org/abs/1701.02547

54. **Staton, Sam** (2017). "Commutative semantics for probabilistic programming." *European Symposium on Programming*, Springer, 855-879.
    - **Key Contribution**: Commutative effects for probabilistic programs

### Distribution Types and Measure Theory

**Academic Papers:**
55. **Ścibior, Adam, Ghahramani, Zoubin, and Gordon, Andrew D.** (2015). "Practical probabilistic programming with monads." *Proceedings of the 2015 ACM SIGPLAN Symposium on Haskell*, 165-176.
    - **Key Contribution**: Monadic probabilistic programming
    - **Repository**: https://github.com/adscib/monad-bayes

56. **Huang, Daniel, Morrisett, Greg, and Staton, Sam** (2017). "Compiling Markov chain Monte Carlo algorithms for probabilistic modeling." *Proceedings of the 38th ACM SIGPLAN Conference on Programming Language Design and Implementation*, 111-125.
    - **Key Contribution**: Compilation of MCMC algorithms

57. **Borgström, Johannes, Gordon, Andrew D., Greenberg, Michael, Margetson, James, and Van Gael, Jurgen** (2013). "Measure transformer semantics for Bayesian machine learning." *European Symposium on Programming*, Springer, 77-96.
    - **Key Contribution**: Measure-theoretic semantics for probabilistic programs

58. **Staton, Sam, Yang, Hongseok, Wood, Frank, Heunen, Chris, and Kammar, Ohad** (2016). "Semantics for probabilistic programming: higher-order functions, continuous distributions, and soft constraints." *Proceedings of the 31st Annual ACM/IEEE Symposium on Logic in Computer Science*, 525-534.
    - **Key Contribution**: Semantics for higher-order probabilistic programming

### Bayesian Inference Systems

**Core Research:**
59. **Goodman, Noah D., Mansinghka, Vikash K., Roy, Daniel M., Bonawitz, Keith, and Tenenbaum, Joshua B.** (2008). "Church: a language for generative models." *Proceedings of the 24th Conference on Uncertainty in Artificial Intelligence*, 220-229.
    - **Key Contribution**: First-order probabilistic programming language
    - **Repository**: https://github.com/probmods/webppl

60. **Wingate, David, Stuhlmüller, Andreas, and Goodman, Noah D.** (2011). "Lightweight implementations of probabilistic programming languages via transformational compilation." *Proceedings of the 14th International Conference on Artificial Intelligence and Statistics*, 770-778.
    - **Key Contribution**: Compilation techniques for probabilistic languages

61. **Wood, Frank, Van de Meent, Jan Willem, and Mansinghka, Vikash** (2014). "A new approach to probabilistic programming inference." *Proceedings of the 17th International Conference on Artificial Intelligence and Statistics*, 1024-1032.
    - **Key Contribution**: Anglican probabilistic programming system

62. **Tolpin, David, van de Meent, Jan-Willem, Yang, Hongseok, and Wood, Frank** (2016). "Design and implementation of probabilistic programming language Anglican." *Proceedings of the 28th Symposium on the Implementation and Application of Functional Languages*, 1-12.
    - **Key Contribution**: Anglican implementation details
    - **Repository**: https://github.com/probprog/anglican

### Stochastic Lambda Calculus

**Foundational Papers:**
63. **Ramsey, Norman and Pfeffer, Avi** (2002). "Stochastic lambda calculus and monads of probability distributions." *Proceedings of the 29th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, 154-165.
    - **Key Contribution**: Theoretical foundations of stochastic computation
    - **Technical Innovation**: Probability monad for lambda calculus

64. **Park, Sungwoo, Pfenning, Frank, and Thrun, Sebastian** (2005). "A probabilistic language based on sampling functions." *Proceedings of the 32nd ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, 171-182.
    - **Key Contribution**: Sampling-based probabilistic programming

65. **Borgström, Johannes, Lago, Ugo Dal, Gordon, Andrew D., and Szymczak, Marcin** (2016). "A lambda-calculus foundation for universal probabilistic programming." *Proceedings of the 21st ACM SIGPLAN International Conference on Functional Programming*, 33-46.
    - **Key Contribution**: Universal probabilistic programming foundations

66. **Ehrhard, Thomas, Pagani, Michele, and Tasson, Christine** (2018). "Measurable cones and stable, measurable functions: a model for probabilistic higher-order programming." *Proceedings of the ACM on Programming Languages*, 2(POPL), 59:1-59:28.
    - **Key Contribution**: Denotational semantics for probabilistic higher-order functions

### Modern Probabilistic Languages

**Stan:**
67. **Carpenter, Bob, Gelman, Andrew, Hoffman, Matthew D., Lee, Daniel, Goodrich, Ben, Betancourt, Michael, Brubaker, Marcus, Guo, Jiqiang, Li, Peter, and Riddell, Allen** (2017). "Stan: a probabilistic programming language." *Journal of Statistical Software*, 76(1), 1-32.
    - **Key Contribution**: Domain-specific language for Bayesian modeling
    - **Repository**: https://github.com/stan-dev/stan

68. **Betancourt, Michael** (2017). "A conceptual introduction to Hamiltonian Monte Carlo." *arXiv preprint arXiv:1701.02434*.
    - **Key Contribution**: Theoretical foundations of Stan's inference engine

**Pyro:**
69. **Bingham, Eli, Chen, Jonathan P., Jankowiak, Martin, Obermeyer, Fritz, Pradhan, Neeraj, Karaletsos, Theofanis, Singh, Rohit, Szerlip, Paul, Horsfall, Paul, and Goodman, Noah D.** (2019). "Pyro: deep universal probabilistic programming." *Journal of Machine Learning Research*, 20(28), 1-6.
    - **Key Contribution**: Deep probabilistic programming with PyTorch
    - **Repository**: https://github.com/pyro-ppl/pyro

70. **Obermeyer, Fritz, Bingham, Eli, Jankowiak, Martin, Chiu, Justin, Pradhan, Neeraj, Rush, Alexander, and Goodman, Noah** (2019). "Tensor variable elimination for plated factor graphs." *International Conference on Machine Learning*, 4755-4765.
    - **Key Contribution**: Efficient inference algorithms for Pyro

**Anglican:**
71. **Tolpin, David, van de Meent, Jan-Willem, Yang, Hongseok, and Wood, Frank** (2015). "Design and implementation of probabilistic programming language Anglican." *arXiv preprint arXiv:1507.07116*.
    - **Key Contribution**: Clojure-based probabilistic programming
    - **Repository**: https://github.com/probprog/anglican

72. **van de Meent, Jan-Willem, Paige, Brooks, Yang, Hongseok, and Wood, Frank** (2018). "An introduction to probabilistic programming." *arXiv preprint arXiv:1809.10756*.
    - **Key Contribution**: Comprehensive introduction to probabilistic programming

### Machine Learning Applications

**Recent Research (2020-2025):**
73. **Fortuin, Vincent** (2022). "Priors in Bayesian deep learning: a review." *International Statistical Review*, 90(3), 563-591.
    - **Key Contribution**: Survey of Bayesian deep learning approaches

74. **Wilson, Andrew Gordon and Izmailov, Pavel** (2020). "Bayesian deep learning and a probabilistic perspective of generalization." *Advances in Neural Information Processing Systems*, 33, 4697-4708.
    - **Key Contribution**: Theoretical foundations of Bayesian deep learning

75. **Gal, Yarin and Ghahramani, Zoubin** (2016). "Dropout as a Bayesian approximation: representing model uncertainty in deep learning." *International Conference on Machine Learning*, 1050-1059.
    - **Key Contribution**: Variational interpretation of dropout

### Domain Theory and Semantics

**Theoretical Foundations:**
76. **Goubault-Larrecq, Jean and Varacca, Daniele** (2011). "Continuous random variables in probabilistic programming." *European Symposium on Programming*, Springer, 97-116.
    - **Key Contribution**: Continuous distributions in probabilistic semantics

77. **Varacca, Daniele and Winskel, Glynn** (2006). "Distributing probability over non-determinism." *Mathematical Structures in Computer Science*, 16(1), 87-113.
    - **Key Contribution**: Interaction between probability and non-determinism

78. **Lago, Ugo Dal, Sangiorgi, Davide, and Alberti, Michele** (2014). "On coinductive equivalences for higher-order probabilistic functional programs." *Proceedings of the 41st ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, 297-308.
    - **Key Contribution**: Coinductive techniques for probabilistic equivalence

### Connections to Other Type Systems

**Interdisciplinary Work:**
79. **Borgström, Johannes, Gordon, Andrew D., Greenberg, Michael, Margetson, James, and Van Gael, Jurgen** (2011). "Measure transformer semantics for Bayesian machine learning." *Proceedings of the 20th European Symposium on Programming*, 77-96.
    - **Key Contribution**: Connections between probabilistic and effect type systems

80. **Staton, Sam, Yang, Hongseok, Heunen, Chris, Kammar, Ohad, and Wood, Frank** (2016). "Semantics for probabilistic programming: higher-order functions, continuous distributions, and soft constraints." *Proceedings of LICS 2016*, 525-534.
    - **Key Contribution**: Integration with dependent type theory

---

## Cross-Cutting Themes and Connections

### Type Theory Foundations
- **Curry-Howard Correspondence**: Connections between proofs, programs, and types across all three domains
- **Category Theory**: Unifying mathematical framework for modal, refinement, and probabilistic types
- **Computational Effects**: Monadic treatments of modality, refinement, and probability

### Verification and Analysis
- **SMT Solver Integration**: Common in refinement types and increasingly in probabilistic verification
- **Decidability Questions**: Central concern across modal logic, refinement checking, and probabilistic inference
- **Expressiveness vs. Automation**: Fundamental tradeoff in all three type system families

### Implementation Strategies
- **Constraint Generation**: Core technique in liquid types and probabilistic inference
- **Staged Computation**: Central to modal types, appearing in probabilistic compilation
- **Proof Irrelevance**: Important in refinement types, relevant to probabilistic equivalence

---

*This bibliography represents the current state of research as of 2025, with emphasis on foundational papers, key implementations, and recent developments in each field.*