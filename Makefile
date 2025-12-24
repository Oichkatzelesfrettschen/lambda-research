# Lambda Calculus Research Repository - Integrated Master Build System
# ====================================================================
# This Makefile orchestrates builds, tests, documentation, 
# academic archiving, and high-performance neural synthesis.

.PHONY: all help build test lint deploy clean verify setup-all \
        build-impl test-validation doc papers-archive uss-experiment \
        uss-generate uss-profile

# Configuration
SHELL := /bin/bash
.DEFAULT_GOAL := help
PYTHON := python3
VENV := venv
USS_VENV := uss-venv

# Language-specific variables
IDRIS := idris2
SCALA := scala
SCALAC := scalac
SML := sml
MLTON := mlton
CARGO := cargo

# Directories
IMPL_DIR := implementations
SRC_DIR := sources
BUILD_DIR := build
TEST_DIR := tests
DOC_DIR := docs
BIN_DIR := ~/.local/bin
SCRIPTS_DIR := scripts
ADMIN_DIR := admin
ARCHIVE_DIR := papers-archive
LOG_DIR := logs

# Colors
BLUE := [0;34m
GREEN := [0;32m
RED := [0;31m
YELLOW := [1;33m
NC := [0m

# Main Targets
help:
	@echo -e "$(BLUE)Lambda Calculus Research Repository Build System$(NC)"
	@echo -e "$(BLUE)================================================$(NC)"
	@echo ""
	@echo "Standard Actions:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

all: lint build test doc ## Run build, test, and documentation generation (strict)

build: uss-build
	$(MAKE) build-impl

test: test-validation test-rust test-archive ## Run all tests (strict)

lint: ## Lint all scripts and markdown files (warnings are errors)
	@echo -e "$(BLUE)Linting Python scripts...$(NC)"
	$(PYTHON) -m py_compile $(SCRIPTS_DIR)/*.py
	@echo -e "$(BLUE)Checking bibliography standardization...$(NC)"
	$(PYTHON) $(SCRIPTS_DIR)/standardize_bibliography.py '**/bibliography.md' --check --force

deploy: doc ## Build documentation and prepare for deployment
	@echo -e "$(BLUE)Building static site (strict)...$(NC)"
	@source $(VENV)/bin/activate && mkdocs build --strict
	@echo -e "$(GREEN)Deployment artifacts ready in site/$(NC)"

clean: ## Clean build artifacts, logs, and site
	@echo -e "$(BLUE)Cleaning build artifacts...$(NC)"
	@rm -rf $(BUILD_DIR) site $(LOG_DIR)/*
	@$(MAKE) -C $(ARCHIVE_DIR) clean
	@if [ -d $(SRC_DIR)/rust-implementations/tapl-rust ] && command -v $(CARGO) &> /dev/null; then \
		cd $(SRC_DIR)/rust-implementations/tapl-rust && $(CARGO) clean 2>/dev/null || true; \
	fi

verify: test-validation ## Verify repository integrity and links
	@echo -e "$(BLUE)Verifying bibliography standardization...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/standardize_bibliography.py '**/bibliography.md' --check
	@echo -e "$(BLUE)Verifying dataset scale...$(NC)"
	@$(USS_VENV)/bin/python3 $(SCRIPTS_DIR)/verify_dataset_scale.py

audit: ## Audit documentation for missing sections (TODOs)
	@echo -e "$(BLUE)Auditing documentation debt...$(NC)"
	@grep -r "TODO" docs/ | grep -v "site" | cut -d: -f1 | sort | uniq -c | sort -nr > $(ADMIN_DIR)/TODO_AUDIT.md
	@echo -e "$(GREEN)Audit report generated in $(ADMIN_DIR)/TODO_AUDIT.md$(NC)"

# --- Setup Targets ---
setup-all: setup-venv setup-uss-venv ## Initialize all virtual environments and dependencies

setup-venv: ## Setup MkDocs virtual environment
	@if [ ! -d "$(VENV)" ]; then \
		$(PYTHON) -m venv $(VENV) && \
		source $(VENV)/bin/activate && \
		pip install --upgrade pip && \
		pip install mkdocs-material mkdocs-bibtex mkdocs-with-pdf mkdocs-git-revision-date-localized-plugin mkdocs-minify-plugin pypandoc && \
		python3 -c "import pypandoc; pypandoc.download_pandoc()"; \
	fi

setup-uss-venv: ## Setup USS Experimental virtual environment
	@if [ ! -d "$(USS_VENV)" ]; then \
		$(PYTHON) -m venv $(USS_VENV) && \
		source $(USS_VENV)/bin/activate && \
		pip install -r requirements_experiments.txt; \
	fi

# --- Implementation Builds ---
build-impl: build-idris build-scala build-sml build-rust ## Build polyglot implementations

build-idris:
	@mkdir -p $(BUILD_DIR)/idris
	@if command -v $(IDRIS) &> /dev/null; then \
		$(IDRIS) build $(IMPL_DIR)/idris/Lambda.idr -o $(BUILD_DIR)/idris/lambda; \
	else echo -e "$(YELLOW)Idris not found, skipping$(NC)"; fi

build-scala:
	@mkdir -p $(BUILD_DIR)/scala
	@if command -v $(SCALAC) &> /dev/null; then \
		$(SCALAC) -d $(BUILD_DIR)/scala $(IMPL_DIR)/scala/LambdaCalculus.scala; \
	else echo -e "$(YELLOW)Scala not found, skipping$(NC)"; fi

build-sml:
	@mkdir -p $(BUILD_DIR)/sml
	@if command -v $(MLTON) &> /dev/null; then \
		$(MLTON) -output $(BUILD_DIR)/sml/lambda $(IMPL_DIR)/sml/lambda.sml; \
	elif command -v $(SML) &> /dev/null; then \
		echo "use \"$(IMPL_DIR)/sml/lambda.sml\";" | $(SML) > $(BUILD_DIR)/sml/output.txt; \
	else echo -e "$(YELLOW)SML compiler not found, skipping$(NC)"; fi

build-rust:
	@if [ -d $(SRC_DIR)/rust-implementations/tapl-rust ] && command -v $(CARGO) &> /dev/null; then \
		cd $(SRC_DIR)/rust-implementations/tapl-rust && RUSTFLAGS="-D warnings" $(CARGO) build --release; \
	fi

# --- Test Targets ---
test-validation: ## Run comprehensive repository validation (warnings as errors)
	@echo -e "$(BLUE)Running repository validation tests...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/validate-repository.py --strict

test-rust:
	@if [ -d $(SRC_DIR)/rust-implementations/tapl-rust ] && command -v $(CARGO) &> /dev/null; then \
		cd $(SRC_DIR)/rust-implementations/tapl-rust && $(CARGO) test --release; \
	fi

test-archive: ## Validate papers archive metadata
	@$(MAKE) -C $(ARCHIVE_DIR) test-metadata

# --- Papers Archive Targets ---
archive-update: ## Update papers archive indices and verify access
	@$(MAKE) -C $(ARCHIVE_DIR) update-all

archive-indices: ## Re-generate archive search indices
	@$(MAKE) -C $(ARCHIVE_DIR) generate-indices

# --- Experimental Targets: USS ---
uss-build: ## Build optimized Triton kernels for USS
	@echo -e "$(BLUE)USS: Building optimized kernels...$(NC)"
	@# Triton kernels are JIT-compiled, but we verify syntax here
	@source $(USS_VENV)/bin/activate && $(PYTHON) -m py_compile src/kernels/*.py

uss-generate: ## Generate 10M synthetic terms for USS
	@echo -e "$(BLUE)USS: Generating 10M terms...$(NC)"
	@source $(USS_VENV)/bin/activate && $(PYTHON) src/data/generator.py

uss-experiment: ## Execute end-to-end USS training pipeline
	@echo -e "$(BLUE)USS: Executing experimental pipeline...$(NC)"
	@export PYTHONPATH=$${PYTHONPATH}:. && source $(USS_VENV)/bin/activate && $(PYTHON) src/experiments/uss_pipeline.py

uss-profile: ## Run deep hardware profiling for USS
	@echo -e "$(BLUE)USS: Running hardware profile...$(NC)"
	@export PYTHONPATH=$${PYTHONPATH}:. && source $(USS_VENV)/bin/activate && bash scripts/profile_uss.sh

# --- Documentation ---
doc: archive-indices ## Generate documentation index and build site (strict)
	@echo -e "$(BLUE)Generating documentation site (strict)...$(NC)"
	@# (Insert logic to auto-generate index from IMPL_DIR if needed)
	@export PATH=$${PATH}:/home/eirikr/bin && source $(VENV)/bin/activate && mkdocs build --strict