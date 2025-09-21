# Implementation Catalog: Combinatory Logic and Related Systems

## SKI Combinator Implementations

### HaSKI - FPGA-based SKI Calculus Evaluator
**Repository**: https://github.com/wyager/HaSKI
**Language**: Haskell/Clash
**Description**: Hardware-based evaluator for the Turing-complete SKI combinator calculus
**Features**:
- FPGA implementation using Clash
- Pure Haskell demo evaluator in `Haskell/Model/`
- Hardware implementation in `Haskell/`
- SKI program compiler
**Documentation**: Comprehensive with hardware synthesis details
**License**: Open source
**Maturity**: Complete implementation with documentation

### SKITypes - Type-Level SKI Implementation
**Repository**: https://github.com/adampalay/SKITypes
**Language**: Haskell
**Description**: Experiment implementing SKI combinator calculus in Haskell's type system
**Features**:
- Type-level implementation (`skiType.hs`)
- Value-level implementation (`skiValue.hs`)
- Demonstrates type-level computation
**Documentation**: Example-driven documentation
**License**: Open source
**Maturity**: Educational/experimental implementation

### lambda-ski - Functional Language with Graph Reduction
**Repository**: https://github.com/thma/lambda-ski
**Language**: Haskell
**Description**: Small functional language with combinator-based graph-reduction machine
**Features**:
- Lambda-calculus parser
- Compiler from lambda-calculus to combinatory logic
- Supports S, K, I, B, C, and Y combinators
- Graph reduction engine
**Documentation**: Well-documented with examples
**License**: Open source
**Maturity**: Complete educational implementation

### combinator-interactive - SKI Interpreter
**Repository**: https://hackage.haskell.org/package/combinator-interactive
**Language**: Haskell
**Description**: Interactive SKI combinator interpreter
**Features**:
- REPL interface
- SKI combinator evaluation
- Interactive exploration
**Documentation**: Hackage documentation
**License**: Open source
**Maturity**: Package on Hackage

## SECD Machine Implementations

### zachallaun/secd - Simple SECD Implementation
**Repository**: https://github.com/zachallaun/secd
**Language**: Various
**Description**: Simple implementation of the SECD abstract machine
**Features**:
- Functional programming abstractions (reduce, map, filter)
- Clear implementation of SECD components
- Educational focus
**Documentation**: Good explanatory documentation
**License**: Open source
**Maturity**: Complete educational implementation

### bwkimmel/secd - Assembly SECD Implementation
**Repository**: https://github.com/bwkimmel/secd
**Language**: x86 Assembly
**Description**: SECD machine implementation in x86 assembly
**Features**:
- Low-level implementation approach
- Direct assembly programming
- Performance-focused
**Documentation**: References Henderson's "Functional Programming" text
**License**: Open source
**Maturity**: Complete low-level implementation

### jpgauthier/secd - Haskell SECD Implementation
**Repository**: https://github.com/jpgauthier/secd
**Language**: Haskell
**Description**: Simple SECD abstract machine implementation in Haskell
**Features**:
- Pure functional implementation
- Clear state transitions
- Educational design
**Documentation**: Detailed component documentation
**License**: Open source
**Maturity**: Complete Haskell implementation

### kseo/secd - Another Haskell SECD
**Repository**: https://github.com/kseo/secd
**Language**: Haskell
**Description**: Haskell implementation of the SECD abstract machine
**Features**:
- Functional implementation
- Standard SECD operations
**Documentation**: Basic documentation
**License**: Open source
**Maturity**: Complete implementation

### BinderDavid/AbstractMachines - Collection of Abstract Machines
**Repository**: https://github.com/BinderDavid/AbstractMachines
**Language**: Haskell
**Description**: Collection of abstract machines for functional programming languages
**Features**:
- Multiple abstract machine implementations
- Includes SECD among others
- Educational collection
**Documentation**: Academic-oriented documentation
**License**: Open source
**Maturity**: Comprehensive collection

### Compact SECD Implementation
**Repository**: https://gist.github.com/ympbyc/4126037
**Language**: Various
**Description**: Compact SECD virtual machine implementation
**Features**:
- Minimal implementation
- Easy to understand
- Concise codebase
**Documentation**: Code comments
**License**: Open source
**Maturity**: Educational/minimal implementation

## Graph Reduction Engine Implementations

### STG Machine Implementations

#### quchen/stgi - Visual STG Implementation
**Repository**: https://github.com/quchen/stgi
**Language**: Haskell
**Description**: User-centric visual STG implementation for understanding GHC/Haskell execution
**Features**:
- Visual execution model
- Educational focus
- Step-by-step evaluation
- Human-readable output
**Documentation**: Excellent educational documentation
**License**: Open source
**Maturity**: Complete educational tool

#### fmthoma/stg - Simple STG Implementation
**Repository**: https://github.com/fmthoma/stg
**Language**: Haskell
**Description**: Simple STG implementation
**Features**:
- Basic STG machine
- Clean implementation
**Documentation**: Minimal documentation
**License**: Open source
**Maturity**: Basic implementation

#### lechimp-p/php-stg - PHP STG Implementation
**Repository**: https://github.com/lechimp-p/php-stg
**Language**: PHP
**Description**: Implementation of Peyton Jones' "Spineless Tagless G-machine" in PHP
**Features**:
- Cross-language implementation
- Educational port
- Demonstrates STG concepts
**Documentation**: References original paper
**License**: Open source
**Maturity**: Complete educational port

#### Neuromancer42/ministgwasm - STG to WebAssembly
**Repository**: https://github.com/Neuromancer42/ministgwasm
**Language**: Rust/WebAssembly
**Description**: Compiler from mini-STG to WebAssembly bytecode
**Features**:
- WebAssembly target
- Modern compilation approach
- Experimental status
**Documentation**: Work in progress documentation
**License**: Open source
**Maturity**: Experimental/incomplete

### G-Machine Implementations

#### puff-lang/g-machine - JavaScript G-Machine
**Repository**: https://github.com/puff-lang/g-machine
**Language**: JavaScript
**Description**: G-machine implementation in JavaScript
**Features**:
- Web-compatible implementation
- JavaScript functional programming
**Documentation**: Basic documentation
**License**: Open source
**Maturity**: Complete JavaScript implementation

#### bitfield/gmachine - Go G-Machine
**Repository**: https://github.com/bitfield/gmachine
**Language**: Go
**Description**: Set of Go exercises implementing a virtual computer system
**Features**:
- G-language assembler
- Binary format translation
- Educational exercises
**Documentation**: Exercise-based learning
**License**: Open source
**Maturity**: Educational implementation

### Advanced Graph Reduction Systems

#### tommythorn/Reduceron - FPGA Haskell Machine
**Repository**: https://github.com/tommythorn/Reduceron
**Language**: Haskell/FPGA
**Description**: High performance FPGA softcore for lazy functional programs
**Features**:
- Hardware garbage collection
- High degree of parallelism
- 60-150 MHz clock frequency
- Efficient graph evaluation
**Documentation**: Research-level documentation
**License**: Open source
**Maturity**: Research implementation with high performance

#### thma.github.io - Haskell Graph Reduction
**Repository**: https://github.com/thma/lambda-ski
**Language**: Haskell
**Description**: Classic combinator-based graph-reduction machine
**Features**:
- S, K, I, B, C, Y combinator support
- Graph data structure allocation
- Combinator graph reduction
**Documentation**: Blog posts and detailed explanations
**License**: Open source
**Maturity**: Complete educational implementation

## Combinatory Logic Interpreter Implementations

### bediger4000/combinatory-logic - Full-Featured CL Interpreter
**Repository**: https://github.com/bediger4000/combinatory-logic
**Language**: C
**Description**: Full-featured combinatory logic interpreter named `cl`
**Features**:
- Complete CL formal system implementation
- Graph reduction implementation
- Extensive testing with "To Mock A Mockingbird" examples
- Comprehensive command-line interface
**Documentation**: Extensive documentation with examples
**License**: Open source
**Maturity**: Production-quality implementation

### bediger4000/any-combinatory-logic - Extensible CL Interpreter
**Repository**: https://github.com/bediger4000/any-combinatory-logic
**Language**: C
**Description**: Combinatory logic interpreter with user-definable primitives
**Features**:
- User-specified primitive combinators
- User-defined bracket abstraction algorithms
- No built-in combinators
- Maximum flexibility
**Documentation**: Detailed configuration documentation
**License**: Open source
**Maturity**: Complete flexible implementation

### naderghanbari/cl-scala - Scala CL Implementation
**Repository**: https://github.com/naderghanbari/cl-scala
**Language**: Scala
**Description**: Simple combinatory logic and lambda calculus in Scala
**Features**:
- ADT + DSL for CL terms
- Term reduction in Scala
- AST, interpreter, and REPL
- Modern functional implementation
**Documentation**: Website with examples at https://naderghanbari.github.io/cl-scala/
**License**: Open source
**Maturity**: Complete Scala implementation

### codereport/cl-cpp - C++ CL Code
**Repository**: https://github.com/codereport/cl-cpp
**Language**: C++
**Description**: Code from combinatory logic livestreams in C++
**Features**:
- Educational content
- Live coding examples
- C++ implementation approaches
**Documentation**: Livestream-based learning
**License**: Open source
**Maturity**: Educational/experimental code

### combinators/cls-scala - Combinatory Logic Synthesizer
**Repository**: https://github.com/combinators/cls-scala
**Language**: Scala
**Description**: Combinatory Logic Synthesizer (CL)S framework in Scala
**Features**:
- Synthesis framework
- Advanced CL applications
- Research-oriented approach
**Documentation**: Academic/research documentation
**License**: Open source
**Maturity**: Research framework

### Online Interactive Implementations

#### John's Combinatory Logic Playground
**URL**: https://tromp.github.io/cl/cl.html
**Language**: JavaScript/Web
**Description**: Online interpreter for combinatory logic
**Features**:
- Web-based interface
- S and K combinator basis
- Interactive evaluation
- Educational tool
**Documentation**: Online help and examples
**License**: Open source
**Maturity**: Complete web implementation

## Categorical Model Implementations

### con-kitty/categorifier - Cartesian Closed Category Interpreter
**Repository**: https://github.com/con-kitty/categorifier
**Language**: Haskell
**Description**: Interpret Haskell programs into any cartesian closed category
**Features**:
- Novel interpretations of Haskell programs
- Cartesian closed category framework
- Generic categorical interpretation
- Research-oriented implementation
**Documentation**: Academic-level documentation
**License**: Open source
**Maturity**: Research implementation

### data-category - Category Theory Library
**Repository**: https://hackage.haskell.org/package/data-category
**Language**: Haskell
**Description**: Collection of categories and categorical constructions
**Features**:
- GADT-based arrow types
- Object representation at value level
- Various categorical constructions
- Type-safe category theory
**Documentation**: Hackage documentation with examples
**License**: Open source
**Maturity**: Stable library on Hackage

### Category Theory Collections
**Repository**: https://github.com/topics/category-theory?l=haskell
**Language**: Haskell
**Description**: Various repositories implementing category theory concepts
**Features**:
- Multiple implementations
- Educational resources
- Applied category theory examples
**Documentation**: Varies by repository
**License**: Various open source licenses
**Maturity**: Range from educational to research-level

## Research and Educational Resources

### Applied Category Theory Implementations
**Repository**: https://github.com/topics/applied-category-theory
**Language**: Various
**Description**: Repositories tagged with applied category theory
**Features**:
- Solutions and exercises
- Practical applications
- Educational materials
**Documentation**: Educational focus
**License**: Various open source licenses
**Maturity**: Educational and research implementations

### Haskell Category Theory Documentation
**Repository**: https://github.com/lotz84/haskell/blob/master/docs/category-theory.md
**Language**: Haskell
**Description**: Curated documentation on category theory in Haskell
**Features**:
- Comprehensive resource collection
- Theoretical explanations
- Practical examples
**Documentation**: Extensive curated documentation
**License**: Open source
**Maturity**: Comprehensive reference

## Implementation Summary

This catalog represents a comprehensive collection of implementations covering:

1. **SKI Combinators**: From hardware FPGA implementations to type-level Haskell
2. **SECD Machines**: Multiple language implementations including assembly and functional approaches
3. **Graph Reduction Engines**: STG machines, G-machines, and advanced parallel implementations
4. **Combinatory Logic Interpreters**: Full-featured interpreters with extensive functionality
5. **Categorical Models**: Implementations of cartesian closed categories and category theory concepts

The implementations range from educational tools to research-quality systems, with particular strength in Haskell implementations reflecting the language's strong connection to functional programming theory and practice.

### Recommended Starting Points:
- **Beginners**: `zachallaun/secd` for SECD machines, `adampalay/SKITypes` for SKI combinators
- **Practical Use**: `bediger4000/combinatory-logic` for CL interpretation, `quchen/stgi` for understanding STG
- **Research**: `tommythorn/Reduceron` for high-performance graph reduction, `con-kitty/categorifier` for categorical models
- **Educational**: `thma/lambda-ski` for graph reduction, John's online playground for interactive learning

All implementations listed are open source and actively maintained or represent complete reference implementations suitable for study and extension.