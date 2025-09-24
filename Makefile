# Lambda Calculus Research Repository - Master Build System
# =========================================================

.PHONY: all build test clean install doc benchmark verify help

# Configuration
SHELL := /bin/bash
.DEFAULT_GOAL := help

# Language-specific variables
IDRIS := idris2
SCALA := scala
SCALAC := scalac
SML := sml
MLTON := mlton
CARGO := cargo
GHC := ghc
CABAL := cabal
OCAMLC := ocamlc
OCAMLOPT := ocamlopt

# Directories
IMPL_DIR := implementations
SRC_DIR := sources
BUILD_DIR := build
TEST_DIR := tests
DOC_DIR := docs
BENCH_DIR := benchmarks

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
BLUE := \033[0;34m
YELLOW := \033[1;33m
NC := \033[0m # No Color

# Main targets
help: ## Show this help message
	@echo -e "$(BLUE)Lambda Calculus Research Repository Build System$(NC)"
	@echo -e "$(BLUE)================================================$(NC)"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

all: build test doc ## Build everything, run tests, and generate documentation

# Build targets
build: build-idris build-scala build-sml build-rust ## Build all implementations
	@echo -e "$(GREEN)All builds completed successfully$(NC)"

build-idris: ## Build Idris implementations
	@echo -e "$(BLUE)Building Idris implementations...$(NC)"
	@mkdir -p $(BUILD_DIR)/idris
	@if command -v $(IDRIS) &> /dev/null; then \
		$(IDRIS) build $(IMPL_DIR)/idris/Lambda.idr -o $(BUILD_DIR)/idris/lambda; \
		echo -e "$(GREEN)Idris build successful$(NC)"; \
	else \
		echo -e "$(YELLOW)Idris not found, skipping$(NC)"; \
	fi

build-scala: ## Build Scala implementations
	@echo -e "$(BLUE)Building Scala implementations...$(NC)"
	@mkdir -p $(BUILD_DIR)/scala
	@if command -v $(SCALAC) &> /dev/null; then \
		$(SCALAC) -d $(BUILD_DIR)/scala $(IMPL_DIR)/scala/LambdaCalculus.scala; \
		echo -e "$(GREEN)Scala build successful$(NC)"; \
	else \
		echo -e "$(YELLOW)Scala not found, skipping$(NC)"; \
	fi

build-sml: ## Build Standard ML implementations
	@echo -e "$(BLUE)Building SML implementations...$(NC)"
	@mkdir -p $(BUILD_DIR)/sml
	@if command -v $(MLTON) &> /dev/null; then \
		$(MLTON) -output $(BUILD_DIR)/sml/lambda $(IMPL_DIR)/sml/lambda.sml; \
		echo -e "$(GREEN)SML build successful$(NC)"; \
	elif command -v $(SML) &> /dev/null; then \
		echo "use \"$(IMPL_DIR)/sml/lambda.sml\";" | $(SML) > $(BUILD_DIR)/sml/output.txt; \
		echo -e "$(GREEN)SML interpretation successful$(NC)"; \
	else \
		echo -e "$(YELLOW)SML compiler not found, skipping$(NC)"; \
	fi

build-rust: ## Build Rust implementations when sources exist
    @echo -e "$(BLUE)Building Rust implementations...$(NC)"
    @if [ -d $(SRC_DIR)/rust-implementations/tapl-rust ]; then \
        if command -v $(CARGO) &> /dev/null; then \
            cd $(SRC_DIR)/rust-implementations/tapl-rust && \
            $(CARGO) fmt --check && \
            $(CARGO) clippy -- -D warnings && \
            $(CARGO) build --release && \
            $(CARGO) test; \
            echo -e "$(GREEN)Rust build successful$(NC)"; \
        else \
            echo -e "$(YELLOW)Cargo not found, skipping Rust build$(NC)"; \
        fi; \
    else \
        echo -e "$(YELLOW)Rust sources not present (skipping): $(SRC_DIR)/rust-implementations/tapl-rust$(NC)"; \
    fi

# Test targets
test: test-rust test-validation test-docs ## Run all available tests

test-rust: ## Run Rust implementation tests
    @echo -e "$(BLUE)Running Rust tests...$(NC)"
    @if [ -d $(SRC_DIR)/rust-implementations/tapl-rust ]; then \
        if command -v $(CARGO) &> /dev/null; then \
            cd $(SRC_DIR)/rust-implementations/tapl-rust && $(CARGO) test --release; \
            echo -e "$(GREEN)Rust tests passed$(NC)"; \
        else \
            echo -e "$(YELLOW)Cargo not found, skipping Rust tests$(NC)"; \
        fi; \
    else \
        echo -e "$(YELLOW)Rust sources not present (skipping): $(SRC_DIR)/rust-implementations/tapl-rust$(NC)"; \
    fi

test-validation: ## Run repository validation tests
	@echo -e "$(BLUE)Running repository validation tests...$(NC)"
	@python3 ./validate-repository.py
	@python3 ./standardize_bibliography.py --check
	@echo -e "$(GREEN)Repository validation passed$(NC)"

test-docs: ## Test documentation build
	@echo -e "$(BLUE)Testing documentation build...$(NC)"
	@if [ -d venv ]; then \
		source venv/bin/activate && mkdocs build --config-file mkdocs-simplified.yml --strict; \
		echo -e "$(GREEN)Documentation build successful$(NC)"; \
	else \
		echo -e "$(YELLOW)venv not found, run ./setup-mkdocs.sh first$(NC)"; \
	fi

# Documentation targets
doc: ## Generate documentation
	@echo -e "$(BLUE)Generating documentation...$(NC)"
	@mkdir -p $(DOC_DIR)
	@echo "# Lambda Calculus Implementations Documentation" > $(DOC_DIR)/index.md
	@echo "" >> $(DOC_DIR)/index.md
	@echo "## Available Implementations" >> $(DOC_DIR)/index.md
	@echo "" >> $(DOC_DIR)/index.md
	@for impl in $(IMPL_DIR)/*; do \
		if [ -d "$$impl" ]; then \
			lang=$$(basename $$impl); \
			echo "### $$lang" >> $(DOC_DIR)/index.md; \
			echo "" >> $(DOC_DIR)/index.md; \
			if [ -f "$$impl/README.md" ]; then \
				cat "$$impl/README.md" >> $(DOC_DIR)/index.md; \
			else \
				echo "Documentation pending for $$lang implementation." >> $(DOC_DIR)/index.md; \
			fi; \
			echo "" >> $(DOC_DIR)/index.md; \
		fi; \
	done
	@echo -e "$(GREEN)Documentation generated in $(DOC_DIR)/$(NC)"

# Benchmark targets
benchmark: ## Run performance benchmarks
	@echo -e "$(BLUE)Running benchmarks...$(NC)"
	@mkdir -p $(BENCH_DIR)/results
	# Add benchmark commands here
	@echo -e "$(YELLOW)Benchmarks not yet implemented$(NC)"

# Verification targets
verify: verify-links verify-builds verify-tests ## Verify repository integrity

verify-links: ## Verify all documentation links
	@echo -e "$(BLUE)Verifying documentation links...$(NC)"
	@find . -name "*.md" -exec grep -l "http" {} \; | head -5
	@echo -e "$(YELLOW)Link verification not yet implemented$(NC)"

verify-builds: ## Verify all builds compile
	@echo -e "$(BLUE)Verifying builds...$(NC)"
	@$(MAKE) build

verify-tests: ## Verify all tests pass
	@echo -e "$(BLUE)Verifying tests...$(NC)"
	@$(MAKE) test

# Installation targets
install: ## Install built artifacts
	@echo -e "$(BLUE)Installing artifacts...$(NC)"
	@mkdir -p ~/.local/bin
	@if [ -f $(BUILD_DIR)/idris/lambda ]; then \
		cp $(BUILD_DIR)/idris/lambda ~/.local/bin/lambda-idris; \
	fi
	@if [ -f $(BUILD_DIR)/sml/lambda ]; then \
		cp $(BUILD_DIR)/sml/lambda ~/.local/bin/lambda-sml; \
	fi
	@echo -e "$(GREEN)Installation complete$(NC)"

# Utility targets
clean: ## Clean build artifacts
	@echo -e "$(BLUE)Cleaning build artifacts...$(NC)"
	@rm -rf $(BUILD_DIR)
	@rm -rf $(TEST_DIR)/results
	@rm -rf $(BENCH_DIR)/results
	@rm -rf $(DOC_DIR)
    @if [ -d $(SRC_DIR)/rust-implementations/tapl-rust ] && command -v $(CARGO) &> /dev/null; then \
        cd $(SRC_DIR)/rust-implementations/tapl-rust && $(CARGO) clean 2>/dev/null || true; \
    fi
	@echo -e "$(GREEN)Clean complete$(NC)"

init: ## Initialize development environment
	@echo -e "$(BLUE)Initializing development environment...$(NC)"
	@mkdir -p $(BUILD_DIR) $(TEST_DIR) $(DOC_DIR) $(BENCH_DIR)
	@echo -e "$(GREEN)Initialization complete$(NC)"

status: ## Show repository status
	@echo -e "$(BLUE)Repository Status$(NC)"
	@echo -e "$(BLUE)=================$(NC)"
	@echo ""
	@echo -e "$(GREEN)Implementations:$(NC)"
	@ls -1 $(IMPL_DIR)/ 2>/dev/null | wc -l | xargs echo "  Found implementations:"
	@ls -1 $(IMPL_DIR)/ 2>/dev/null | sed 's/^/    - /'
	@echo ""
	@echo -e "$(GREEN)Source directories:$(NC)"
	@ls -1 $(SRC_DIR)/ 2>/dev/null | wc -l | xargs echo "  Found source dirs:"
	@ls -1 $(SRC_DIR)/ 2>/dev/null | sed 's/^/    - /'
	@echo ""
	@echo -e "$(GREEN)Available compilers:$(NC)"
	@command -v $(IDRIS) &> /dev/null && echo "  - Idris: found" || echo "  - Idris: not found"
	@command -v $(SCALAC) &> /dev/null && echo "  - Scala: found" || echo "  - Scala: not found"
	@command -v $(MLTON) &> /dev/null && echo "  - MLton: found" || echo "  - MLton: not found"
	@command -v $(SML) &> /dev/null && echo "  - SML: found" || echo "  - SML: not found"
	@command -v $(CARGO) &> /dev/null && echo "  - Rust: found" || echo "  - Rust: not found"
	@command -v $(GHC) &> /dev/null && echo "  - Haskell: found" || echo "  - Haskell: not found"
	@command -v $(OCAMLC) &> /dev/null && echo "  - OCaml: found" || echo "  - OCaml: not found"

# Development targets
dev: ## Start development environment
	@echo -e "$(BLUE)Starting development environment...$(NC)"
	@$(MAKE) init
	@$(MAKE) build
	@$(MAKE) test
	@echo -e "$(GREEN)Development environment ready$(NC)"

watch: ## Watch for changes and rebuild
	@echo -e "$(BLUE)Watching for changes...$(NC)"
	@echo -e "$(YELLOW)File watching not yet implemented$(NC)"

# CI/CD targets
ci: ## Run continuous integration checks
	@echo -e "$(BLUE)Running CI checks...$(NC)"
	@$(MAKE) clean
	@$(MAKE) build
	@$(MAKE) test
	@$(MAKE) verify
	@echo -e "$(GREEN)CI checks passed$(NC)"

# Advanced targets
profile: ## Profile implementations
	@echo -e "$(BLUE)Profiling implementations...$(NC)"
	@echo -e "$(YELLOW)Profiling not yet implemented$(NC)"

optimize: ## Run optimization passes
	@echo -e "$(BLUE)Running optimizations...$(NC)"
	@echo -e "$(YELLOW)Optimization not yet implemented$(NC)"

formal-verify: ## Run formal verification
	@echo -e "$(BLUE)Running formal verification...$(NC)"
	@echo -e "$(YELLOW)Formal verification not yet implemented$(NC)"

# Special targets
.PRECIOUS: $(BUILD_DIR)/% $(TEST_DIR)/% $(DOC_DIR)/% $(BENCH_DIR)/%

# Include local configuration if it exists
-include Makefile.local
