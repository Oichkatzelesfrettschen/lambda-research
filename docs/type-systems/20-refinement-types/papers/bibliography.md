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

## Implementation Status

*Last updated: 2024-12-24*

### ⏳ Not Yet Implemented

No papers from this bibliography are currently implemented.

### 📋 Implementation Pipeline

- **Total papers in bibliography**: 50
- **Currently implemented**: 0
- **Awaiting implementation**: 50
- **Implementation priority**: Based on foundational importance and paper citation count
- **Roadmap phase**: Phase 3 (test coverage) → Phase 4 (new variants)

### 📊 Implementation Statistics

**Repository-wide metrics** (as of 2024-12-24):

- Total Rust LOC: 5,179
- Total test count: 38
- Average test coverage: 45%
- Quality score: 6.5/10
- Build status: ✅ Passing
- Clippy warnings: 5 (all in church-unsolvable-1936, low severity)

**Implementation focus areas**:

1. ✅ **Untyped Lambda Calculus** (Church 1936, 1941) - Complete
2. ✅ **Evaluation Strategies** (Pierce TAPL Ch. 5) - Complete but untested
3. 🔄 **Type Systems** (Pierce TAPL Ch. 9+) - Planned
4. 🔄 **Polymorphism** (System F) - Planned
5. 🔄 **Dependent Types** - Planned

### 🔗 Reference

- Implementation audit: `admin/implementation-status.json`
- Rust implementations: `sources/rust-implementations/`
- Academic papers: `papers-archive/`
- Documentation: See project README and individual crate documentation
