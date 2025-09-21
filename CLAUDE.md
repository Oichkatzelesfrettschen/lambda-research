# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a comprehensive lambda calculus research repository containing:
- 31 numbered categories of lambda calculus variants and type systems (01-31)
- Extensive academic bibliographies with 708+ research papers
- Implementation catalogs across multiple programming languages
- Cross-reference system mapping theoretical connections
- Papers archive with automated download capabilities
- Source code repositories for major proof assistants and implementations

## Repository Structure

### Core Organization
- `01-XX-name/` - Numbered directories for lambda calculus variants
- `sources/` - Complete source code repositories (Agda, Coq, Idris2, Rust, etc.)
- `implementations/` - Research implementations organized by language
- `papers-archive/` - Academic paper collection with metadata
- Root-level `.md` files - Cross-references, bibliographies, and comprehensive indices

### Key Files
- `README.md` - Main repository documentation
- `COMPREHENSIVE_INDEX.md` - Complete academic index with 708+ papers
- `CROSS_REFERENCE_SYSTEM.md` - Theoretical connections between systems
- `mkdocs.yml` / `mkdocs-simplified.yml` - Modern documentation system
- Various `*_bibliography.md` files - Academic references by topic

## Build Systems and Development

### Multi-Language Build Infrastructure
This repository contains implementations in multiple languages with their respective build systems:

- **Rust**: Cargo workspaces in `sources/rust-implementations/tapl-rust/`
- **Haskell**: Cabal projects in `sources/agda-src/` and implementations
- **OCaml**: Dune build system in `sources/coq-src/`
- **Idris2**: Native IPkg system in `sources/idris2-src/`
- **Python**: Requirements files for documentation tooling

### Essential Commands

#### Documentation Development
```bash
# Set up MkDocs documentation system
./setup-mkdocs.sh                    # Initial setup (creates venv, installs deps)
source venv/bin/activate             # Activate Python environment
mkdocs serve --config-file mkdocs-simplified.yml  # Development server
mkdocs build --config-file mkdocs-simplified.yml  # Build static documentation
```

#### Testing and Validation
```bash
# Rust implementations
cd sources/rust-implementations/tapl-rust/
cargo test                           # Run all Rust tests
cargo build --release               # Build optimized binaries

# Haskell/Agda
cd sources/agda-src/
make install                         # Build and install Agda

# Coq/Rocq
cd sources/coq-src/
make world                          # Full build
make check                          # Run test suite
```

#### Paper Archive Management
```bash
cd papers-archive/
make download-high                  # Download high-priority papers
make search QUERY="linear logic"    # Search papers by topic
make verify                         # Verify URL accessibility
make status                         # Get repository status
```

## Code Architecture

### Academic Research Focus
This repository is primarily an academic research collection, not a production software system. The architecture reflects this:

1. **Bibliography-Centric**: Each topic has comprehensive academic references
2. **Implementation Diversity**: Multiple language implementations for comparison
3. **Theoretical Connections**: Cross-reference system maps relationships
4. **Educational Progression**: Organized from basic to advanced concepts

### Multi-Language Implementation Strategy
- **Language-Specific Directories**: Each major language has its own subtree
- **Independent Build Systems**: Respect existing language conventions
- **Cross-Language Testing**: Shared test cases in JSON format (when available)
- **Academic Validation**: Implementations validated against papers

### Key Implementation Patterns
- **Type-Safe Representations**: Use phantom types and GADTs where available
- **Church Encoding**: Fundamental lambda calculus representations
- **Effect Systems**: Separate pure computation from IO operations
- **Formal Verification**: Links to Coq/Agda proofs when available

## Development Workflow

### Adding New Lambda Calculus Variants
1. Create numbered directory (e.g., `32-new-variant/`)
2. Add subdirectories: `papers/`, `implementations/`, `tutorials/`, `historical/`
3. Create `papers/bibliography.md` with academic references
4. Update `COMPREHENSIVE_INDEX.md` with new content
5. Add cross-references in `CROSS_REFERENCE_SYSTEM.md`
6. Include implementations in appropriate language directories

### Bibliography Management
- Use academic citation standards (author, year, title, venue, pages)
- Include DOI links when available
- Verify URL accessibility regularly
- Maintain chronological and topical organization
- Follow existing formatting patterns in bibliography files

### Implementation Standards
- Include comprehensive comments explaining theoretical background
- Reference specific papers for algorithms
- Use language-appropriate testing frameworks
- Maintain compatibility with existing build systems
- Document performance characteristics and complexity

## Quality Standards

### Academic Rigor
- All theoretical claims must be referenced to academic sources
- Implementations should be validated against formal specifications
- Bibliography quality is paramount - verify sources and citations
- Maintain separation between educational and research content

### Code Quality
- Use language-specific linting tools (rustfmt, hlint, ocamlformat)
- Comprehensive test coverage for all implementations
- Performance benchmarking for algorithmic comparisons
- Cross-platform compatibility where applicable

### Documentation Standards
- Mathematical notation using MathJax in markdown
- Clear explanations of theoretical concepts
- Links between related implementations and papers
- Examples and educational material for complex topics

## Research Integration

### Paper Archive System
The `papers-archive/` directory contains:
- Automated download scripts for open-access papers
- Metadata management with BibTeX integration
- Copyright-compliant collection policies
- Search and indexing capabilities

### Cross-Reference Validation
The cross-reference system requires:
- Theoretical accuracy validation by category theory experts
- Regular verification of claimed relationships
- Citations for all theoretical connections
- Updates as new research emerges

### Implementation Validation
All implementations should be:
- Validated against academic specifications
- Cross-tested with equivalent implementations in other languages
- Benchmarked for performance characteristics
- Documented with complexity analysis

## Special Considerations

### Unicode Policy
Follow ANSI/ASCII-appropriate symbols only in code (per CLAUDE.md constraints).
Use standard mathematical notation in documentation.

### Academic Copyright
- Only include legally accessible papers
- Respect copyright restrictions
- Use open-access sources when possible
- Provide proper attribution for all sources

### Version Control Strategy
This is designed as a comprehensive academic resource, suitable for:
- Research collaboration
- Educational use
- Implementation comparison
- Literature review and survey work

## Dependencies and External Tools

### Required for Full Development
- Python 3.13+ with venv support
- Rust toolchain (latest stable)
- Haskell Platform or Stack
- OCaml and Dune
- Idris2 compiler
- Pandoc for bibliography processing
- Chrome/Chromium for PDF generation
- Git for version control

### Optional but Recommended
- LaTeX for mathematical document generation
- Formal verification tools (Coq, Agda, Lean)
- Performance profiling tools for each language
- Academic reference managers (Zotero, Mendeley)

This repository represents one of the most comprehensive academic resources on lambda calculus variants, suitable for research, education, and practical application across the full spectrum of type theory and programming language design.