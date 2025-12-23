# MkDocs Setup Guide - Lambda Calculus Research Repository

## Overview

This guide provides comprehensive instructions for setting up and using the modern MkDocs documentation system designed specifically for the Lambda Calculus Research Repository. The system is optimized for academic research documentation with advanced features for mathematical notation, bibliography management, and cross-reference systems.

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Pandoc (for bibliography management)
- Chrome/Chromium (for PDF generation)

### Automated Setup

1. **Run the setup script:**
   ```bash
   ./setup-mkdocs.sh
   ```

2. **Start the development server:**
   ```bash
   ./dev-server.sh
   ```

3. **Visit your documentation:**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser

## Manual Setup

If you prefer manual installation or need to customize the setup:

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install pandoc chromium-browser
```

**macOS:**
```bash
brew install pandoc chromium
```

**Windows:**
- Download Pandoc from [pandoc.org](https://pandoc.org/installing.html)
- Install Chrome or Chromium browser

### 4. Verify Installation

```bash
mkdocs --version
pandoc --version
```

## Configuration Features

### 1. Theme and Appearance

- **Material for MkDocs**: Modern, responsive theme optimized for academic content
- **Academic Color Scheme**: Professional blue-grey palette with dark mode support
- **Typography**: Roboto font family optimized for academic readability
- **Custom Academic CSS**: Enhanced styling for mathematical content and papers

### 2. Mathematical Notation

The system includes comprehensive support for lambda calculus notation:

```latex
# Basic lambda calculus
\lambda x. x                    # Lambda abstraction
(\lambda x. x) y               # Application
\lambda f. \lambda x. f x      # Curried function

# Type annotations
x : \tau                       # Type assignment
\Gamma \vdash e : \tau        # Typing judgment

# Advanced notation
\Pi x: A. B                    # Dependent product
\Sigma x: A. B                 # Dependent sum
```

**Custom Macros Available:**
- `\lam` → λ
- `\abs{x}{e}` → λx.e
- `\ty` → τ (types)
- `\ctx` → Γ (contexts)
- `\proves` → ⊢ (entailment)
- `\bred` → →β (beta reduction)
- Plus 50+ additional lambda calculus specific macros

### 3. Bibliography Management

Integrated BibTeX support with IEEE citation style:

```markdown
Citations use standard syntax: [@church1936]
Multiple citations: [@church1936; @curry1958]
In-text citations: @church1936 showed that...
```

**Configuration:**
- Main bibliography: `papers-archive/metadata/bibliography.bib`
- Additional BibTeX files can be added to `papers-archive/` directory
- IEEE citation style (customizable via CSL files)

### 4. PDF Generation

Academic-quality PDF export with:
- Automatic table of contents
- Proper page breaks
- Academic formatting
- Bibliography inclusion
- Mathematical notation preservation

**Generate PDF:**
```bash
./generate-pdf.sh
```

### 5. Search Capabilities

Advanced search features:
- Full-text search across all content
- Mathematical notation indexing
- Bibliography search
- Cross-reference search
- Instant search results
- Search highlighting

### 6. Navigation Structure

Hierarchical organization optimized for 31 lambda calculus categories:

```
├── Foundation (Core systems)
│   ├── Untyped Lambda Calculus
│   ├── Simply Typed Lambda Calculus
│   └── System F, CoC, MLTT
├── Type Systems (Extensions)
│   ├── Linear Types
│   ├── Session Types
│   └── Effect Systems, etc.
├── Advanced Variants
│   ├── Quantum Lambda Calculus
│   ├── Homotopy Type Theory
│   └── Cutting-edge research
└── Resources
    ├── Bibliography
    ├── Implementations
    └── Cross-references
```

## Content Organization

### File Structure

```
docs/
├── index.md                    # Main landing page
├── introduction/               # Repository overview
├── foundation/                # Core lambda calculus systems
├── type-systems/              # Type system extensions
├── advanced/                  # Specialized variants
├── theory/                    # Theoretical foundations
├── implementations/           # Practical implementations
├── bibliography/              # Academic references
├── resources/                 # Additional materials
├── appendices/                # Supporting content
├── javascripts/              # Custom JavaScript (MathJax)
├── stylesheets/              # Custom CSS
├── images/                   # Documentation images
└── includes/                 # Shared content (abbreviations)
```

### Content Types

1. **Category Pages**: Document each lambda calculus variant
2. **Cross-Reference Pages**: Show theoretical connections
3. **Implementation Pages**: Practical code examples and analysis
4. **Bibliography Pages**: Academic paper collections
5. **Resource Pages**: Educational materials and tools

### Writing Guidelines

#### Mathematical Content

Use standard LaTeX notation:
```markdown
The simply typed lambda calculus $\lambda^{\to}$ extends
the untyped calculus with types $\tau ::= \alpha \mid \tau_1 \to \tau_2$.

For typing judgments:
$$\Gamma \vdash e : \tau$$

Where $\Gamma$ is the context and $e$ is the expression.
```

#### Citations

Reference papers consistently:
```markdown
Church's original paper [@church1936] introduced the lambda calculus.
Later work by Curry and Feys [@curry1958] developed combinatory logic.
```

#### Cross-References

Link related concepts:
```markdown
See also:
- [Linear Lambda Calculus](/../type-systems/06-linear-lambda-calculus.md)
- [Session Types](/../type-systems/07-session-types.md)
- [Cross-Reference System](/../introduction/cross-reference-system.md)
```

#### Code Examples

Use appropriate syntax highlighting:
````markdown
```haskell
-- Simply typed lambda calculus in Haskell
data Type = TyVar String | TyFun Type Type
data Expr = Var String | Lam String Type Expr | App Expr Expr
```

```agda
-- Dependent types in Agda
data Vec (A : Set) : ℕ → Set where
  []  : Vec A zero
  _∷_ : {n : ℕ} → A → Vec A n → Vec A (suc n)
```
````

## Customization

### Theme Customization

Modify `docs/stylesheets/academic.css` for:
- Color schemes
- Typography adjustments
- Layout modifications
- Academic-specific styling

### Plugin Configuration

Key plugins can be configured in `mkdocs.yml`:

```yaml
plugins:
  - bibtex:
      bib_file: "papers-archive/metadata/bibliography.bib"
      csl_file: "https://path/to/custom/style.csl"

  - with-pdf:
      output_path: "custom-filename.pdf"
      cover_title: "Custom Title"

  - search:
      lang: en
      separator: '[\s\-\.]+'
```

### Math Macros

Add custom macros in `docs/javascripts/mathjax.js`:

```javascript
macros: {
  "custom": ["\\mathsf{Custom}_{#1}", 1],
  "newop": "\\operatorname{newop}"
}
```

## Development Workflow

### 1. Daily Development

```bash
# Start development server
./dev-server.sh

# Edit content in docs/ directory
# Changes are reflected immediately at http://127.0.0.1:8000
```

### 2. Content Creation

1. Create new markdown files in appropriate directories
2. Update navigation in `mkdocs.yml` if needed
3. Add bibliography entries to BibTeX files
4. Include cross-references and mathematical notation
5. Test locally before committing

### 3. Building for Production

```bash
# Build HTML documentation
./build-docs.sh

# Generate PDF version
./generate-pdf.sh

# Deploy to hosting platform
# (GitHub Pages, ReadtheDocs, etc.)
```

## Advanced Features

### 1. Cross-Reference Integration

The system integrates with the existing cross-reference system:
- Automatic linking between related concepts
- Visual relationship maps
- Theoretical connection tracking

### 2. Implementation Matrix

Feature comparison tables:
```markdown
| Feature | Haskell | OCaml | Rust | Agda |
|---------|---------|-------|------|------|
| Higher-rank types | ✓ | ✓ | Partial | ✓ |
| Linear types | Extensions | ✓ | ✓ | ✓ |
```

### 3. Timeline Visualization

Historical development tracking:
```markdown
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-year">1936</div>
    <div class="timeline-content">
      Church introduces lambda calculus
    </div>
  </div>
</div>
```

### 4. Academic Paper Cards

Structured paper presentations:
```markdown
<div class="paper-card">
  <div class="paper-title">The Lambda Calculus</div>
  <div class="paper-authors">Alonzo Church</div>
  <div class="paper-venue">Annals of Mathematics, 1936</div>
  <div class="paper-abstract">...</div>
</div>
```

## Troubleshooting

### Common Issues

1. **MathJax not rendering:**
   - Check JavaScript console for errors
   - Verify MathJax CDN connectivity
   - Ensure proper LaTeX syntax

2. **PDF generation fails:**
   - Install Chrome/Chromium browser
   - Check WeasyPrint dependencies
   - Verify `ENABLE_PDF_EXPORT=true` environment variable

3. **Bibliography not working:**
   - Install Pandoc
   - Check BibTeX file syntax
   - Verify file paths in configuration

4. **Search not working:**
   - Rebuild the site
   - Check for JavaScript errors
   - Verify search plugin configuration

### Performance Optimization

1. **Large repositories:**
   - Use `mkdocs-exclude-search` for non-essential files
   - Enable minification plugin
   - Optimize images and assets

2. **Build time:**
   - Disable PDF generation during development
   - Use incremental builds where possible
   - Cache dependencies

## Deployment Options

### GitHub Pages

```yaml
# .github/workflows/docs.yml
name: Deploy Documentation
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force
```

### ReadtheDocs

Configure `.readthedocs.yaml`:
```yaml
version: 2
mkdocs:
  configuration: mkdocs.yml
python:
  version: "3.9"
  install:
    - requirements: requirements.txt
```

### Self-hosted

```bash
# Build static site
./build-docs.sh

# Serve with any web server
python -m http.server 8000 --directory site/
```

## Maintenance

### Regular Tasks

1. **Update dependencies:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Validate links:**
   ```bash
   mkdocs build --strict
   ```

3. **Update bibliography:**
   - Add new papers to BibTeX files
   - Verify citation formatting
   - Update cross-references

4. **Performance monitoring:**
   - Check build times
   - Monitor site size
   - Optimize assets

### Version Control

- Commit configuration changes
- Version control content files
- Tag releases for stable versions
- Document breaking changes

## Support and Resources

- **MkDocs Documentation**: [mkdocs.org](https://www.mkdocs.org/)
- **Material Theme**: [squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
- **Mathematical Notation**: [MathJax Documentation](https://docs.mathjax.org/)
- **Bibliography Management**: [mkdocs-bibtex](https://github.com/shyamd/mkdocs-bibtex)

For project-specific support, see the repository issues and documentation.

---

This setup provides a comprehensive, modern documentation system specifically designed for academic research in lambda calculus and type theory, with all the features needed for professional academic publishing and collaboration.