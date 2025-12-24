#!/usr/bin/env bash
#
# setup-mkdocs.sh
#
# Copyright (C) 2025 Lambda Research Collective
#
# This file is part of Lambda Calculus Research Repository.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


# Lambda Calculus Research Repository - MkDocs Setup Script
# Comprehensive setup for modern academic documentation system

set -e  # Exit on error

echo "=== Lambda Calculus Research Repository - MkDocs Setup ==="
echo "Setting up modern academic documentation system..."
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is required but not installed."
    exit 1
fi

print_status "Python 3 found: $(python3 --version)"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 is required but not installed."
    exit 1
fi

print_status "pip3 found: $(pip3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_status "Creating Python virtual environment..."
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_status "Virtual environment already exists"
fi

# Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Install core MkDocs and Material theme
print_status "Installing MkDocs and Material theme..."
pip install mkdocs>=1.5.0
pip install mkdocs-material>=9.4.0

# Install essential plugins
print_status "Installing MkDocs plugins..."

# Bibliography and citation management
pip install mkdocs-bibtex>=2.8.0

# PDF generation
pip install mkdocs-with-pdf>=0.9.0
pip install weasyprint>=60.0

# Search and navigation enhancements
pip install mkdocs-awesome-nav>=0.9.0
pip install mkdocs-exclude-search>=0.6.0

# Content organization
pip install mkdocs-tags-plugin>=0.6.0
pip install mkdocs-meta-plugin>=0.3.0

# Git integration
pip install mkdocs-git-revision-date-localized-plugin>=1.2.0

# Performance optimization
pip install mkdocs-minify-plugin>=0.7.0

# Mathematics rendering dependencies
print_status "Installing mathematics rendering dependencies..."
# Note: MathJax is loaded via CDN, no Python dependencies needed

# Check for Pandoc (required for mkdocs-bibtex)
if ! command -v pandoc &> /dev/null; then
    print_warning "Pandoc not found. Installing pandoc..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update && sudo apt-get install -y pandoc
    elif command -v brew &> /dev/null; then
        brew install pandoc
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y pandoc
    elif command -v yum &> /dev/null; then
        sudo yum install -y pandoc
    else
        print_error "Could not install pandoc automatically. Please install it manually."
        print_error "Visit: https://pandoc.org/installing.html"
        exit 1
    fi
    print_success "Pandoc installed"
else
    print_status "Pandoc found: $(pandoc --version | head -n1)"
fi

# Check for Chrome/Chromium (required for PDF generation)
if ! command -v chromium-browser &> /dev/null && ! command -v google-chrome &> /dev/null; then
    print_warning "Chrome/Chromium not found. Required for PDF generation."
    print_warning "Installing chromium-browser..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update && sudo apt-get install -y chromium-browser
    elif command -v brew &> /dev/null; then
        brew install chromium
    else
        print_warning "Could not install Chromium automatically."
        print_warning "Please install Chrome or Chromium for PDF generation."
    fi
fi

# Create necessary directories
print_status "Creating documentation directory structure..."

mkdir -p docs/{introduction,foundation,type-systems,advanced,theory,implementations,bibliography,resources,appendices}
mkdir -p docs/{javascripts,stylesheets,images,assets}
mkdir -p docs/includes

# Create hook scripts directory
mkdir -p hooks

# Create basic index page if it doesn't exist
if [ ! -f "docs/index.md" ]; then
    print_status "Creating main index page..."
    cat > docs/index.md << 'EOF'
# Lambda Calculus Research Repository

Welcome to the comprehensive Lambda Calculus Research Repository, a modern documentation system covering 31 lambda calculus variants, implementations, and theoretical foundations.

## Overview

This repository serves as a comprehensive resource for researchers, educators, and practitioners interested in lambda calculus and type theory. It provides:

- **Systematic Coverage**: Documentation of 31 lambda calculus variants
- **Implementation Analysis**: Detailed implementation comparisons and catalogs
- **Academic Resources**: Extensive bibliographies and paper collections
- **Cross-Reference System**: Interconnected theoretical relationships
- **Modern Tooling**: Searchable, accessible, and publication-ready documentation

## Repository Structure

### Foundation
Core lambda calculus systems that form the theoretical foundation:
- Untyped Lambda Calculus
- Simply Typed Lambda Calculus
- System F (Polymorphic Lambda Calculus)
- Calculus of Constructions
- Martin-Löf Type Theory

### Type Systems
Advanced type systems and extensions:
- Linear Lambda Calculus
- Session Types
- Dependent Types
- Substructural Types
- Effect Systems
- And many more...

### Advanced Variants
Specialized and cutting-edge variants:
- Quantum Lambda Calculus
- Probabilistic Types
- Homotopy Type Theory
- Cubical Type Theory
- Directed Type Theory

## Getting Started

1. Browse the [Cross-Reference System](introduction/cross-reference-system.md) to understand theoretical connections
2. Explore specific lambda calculus variants in the Foundation and Type Systems sections
3. Check the [Implementation Catalog](introduction/implementation-catalog.md) for practical applications
4. Use the comprehensive [Bibliography](bibliography/index.md) for research

## Features

- **Searchable Content**: Full-text search across all documentation
- **Mathematics Support**: Proper rendering of lambda calculus notation
- **Bibliography Management**: Integrated citation system
- **PDF Generation**: Academic paper-ready exports
- **Cross-References**: Linked theoretical relationships
- **Mobile Friendly**: Responsive design for all devices

---

*This documentation is generated using MkDocs with Material theme, optimized for academic research and mathematical content.*
EOF
    print_success "Main index page created"
fi

# Create section index pages
print_status "Creating section index pages..."

# Introduction section
cat > docs/introduction/index.md << 'EOF'
# Introduction

This section provides an overview of the Lambda Calculus Research Repository, its organization, and research methodology.

## Contents

- [Overview](overview.md) - General introduction and scope
- [Cross-Reference System](cross-reference-system.md) - Theoretical connections and relationships
- [Implementation Catalog](implementation-catalog.md) - Practical implementations and tools
- [Research Methodology](methodology.md) - Approach and principles
EOF

# Foundation section
cat > docs/foundation/index.md << 'EOF'
# Foundation

Core lambda calculus systems that form the theoretical foundation of type theory and functional programming.

## Lambda Cube

The foundation section covers the fundamental systems of the lambda cube:

- **Simply Typed Lambda Calculus** - Basic type safety
- **System F** - Parametric polymorphism
- **System F<sub>ω</sub>** - Higher-kinded types
- **Calculus of Constructions** - Dependent types and higher-order logic

## Historical Development

These systems represent the historical development and theoretical foundation upon which all modern type systems are built.

## Contents

1. [Untyped Lambda Calculus](01-untyped-lambda-calculus.md)
2. [Simply Typed Lambda Calculus](02-simply-typed-lambda-calculus.md)
3. [System F (Polymorphic)](03-system-f-polymorphic.md)
4. [Calculus of Constructions](04-calculus-of-constructions.md)
5. [Martin-Löf Type Theory](05-martin-lof-type-theory.md)
EOF

# Create requirements.txt for reproducible installations
print_status "Creating requirements.txt..."
cat > requirements.txt << 'EOF'
# MkDocs Core
mkdocs>=1.5.0
mkdocs-material>=9.4.0

# Essential Plugins
mkdocs-bibtex>=2.8.0
mkdocs-with-pdf>=0.9.0
mkdocs-awesome-nav>=0.9.0
mkdocs-exclude-search>=0.6.0
mkdocs-tags-plugin>=0.6.0
mkdocs-meta-plugin>=0.3.0
mkdocs-git-revision-date-localized-plugin>=1.2.0
mkdocs-minify-plugin>=0.7.0

# PDF Generation Dependencies
weasyprint>=60.0

# Additional utilities
markdown>=3.4.0
pymdown-extensions>=10.0.0
EOF

# Create .gitignore for MkDocs
if [ ! -f ".gitignore" ]; then
    print_status "Creating .gitignore..."
    cat > .gitignore << 'EOF'
# MkDocs
site/
*.pdf

# Python
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
.cache/
EOF
fi

# Create development and build scripts
print_status "Creating utility scripts..."

# Development server script
cat > dev-server.sh << 'EOF'
#!/bin/bash
# Development server for Lambda Calculus Research Repository

echo "Starting MkDocs development server..."
echo "Documentation will be available at: http://127.0.0.1:8000"
echo "Press Ctrl+C to stop the server"
echo

source venv/bin/activate
mkdocs serve --dev-addr=127.0.0.1:8000
EOF

chmod +x dev-server.sh

# Build script
cat > build-docs.sh << 'EOF'
#!/bin/bash
# Build script for Lambda Calculus Research Repository

echo "Building Lambda Calculus Research Repository documentation..."

source venv/bin/activate

# Clean previous build
if [ -d "site" ]; then
    echo "Cleaning previous build..."
    rm -rf site/
fi

# Build documentation
echo "Building HTML documentation..."
mkdocs build

# Generate PDF if enabled
if [ "$ENABLE_PDF_EXPORT" = "true" ]; then
    echo "Generating PDF documentation..."
    ENABLE_PDF_EXPORT=true mkdocs build
fi

echo "Build complete!"
echo "Documentation available in: site/"
if [ "$ENABLE_PDF_EXPORT" = "true" ]; then
    echo "PDF available at: lambda-calculus-research.pdf"
fi
EOF

chmod +x build-docs.sh

# Create PDF generation script
cat > generate-pdf.sh << 'EOF'
#!/bin/bash
# PDF generation script for Lambda Calculus Research Repository

echo "Generating PDF documentation..."

source venv/bin/activate

# Set environment variable to enable PDF generation
export ENABLE_PDF_EXPORT=true

# Build with PDF generation
mkdocs build

if [ -f "lambda-calculus-research.pdf" ]; then
    echo "PDF generated successfully: lambda-calculus-research.pdf"
else
    echo "PDF generation failed. Check the build output above."
    exit 1
fi
EOF

chmod +x generate-pdf.sh

# Verify installation
print_status "Verifying installation..."

# Test MkDocs
if mkdocs --version &> /dev/null; then
    print_success "MkDocs installation verified: $(mkdocs --version)"
else
    print_error "MkDocs installation failed"
    exit 1
fi

# Test configuration
if mkdocs config &> /dev/null; then
    print_success "MkDocs configuration is valid"
else
    print_error "MkDocs configuration has errors"
    exit 1
fi

# Create completion message
echo
echo "================================================================"
print_success "Lambda Calculus Research Repository MkDocs setup complete!"
echo "================================================================"
echo
echo "Next steps:"
echo "1. Start development server: ./dev-server.sh"
echo "2. Build documentation: ./build-docs.sh"
echo "3. Generate PDF: ./generate-pdf.sh"
echo
echo "Documentation structure:"
echo "├── docs/                    # Documentation source"
echo "├── site/                    # Built documentation (auto-generated)"
echo "├── mkdocs.yml              # Main configuration"
echo "├── requirements.txt        # Python dependencies"
echo "├── venv/                   # Python virtual environment"
echo "└── *.sh                    # Utility scripts"
echo
echo "Key features enabled:"
echo "✓ Material for MkDocs theme with academic styling"
echo "✓ Mathematical notation rendering (MathJax)"
echo "✓ Bibliography and citation management"
echo "✓ PDF generation for academic publishing"
echo "✓ Advanced search capabilities"
echo "✓ Cross-reference system integration"
echo "✓ Responsive design for all devices"
echo
echo "For more information, see the documentation at:"
echo "https://squidfunk.github.io/mkdocs-material/"
echo
print_success "Setup completed successfully!"