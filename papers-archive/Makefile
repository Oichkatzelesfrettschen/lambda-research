# Lambda Calculus Papers Archive - Build System
# Automated management of paper downloads, metadata, and indices

SHELL := /bin/bash
PYTHON := python3

# Directories
ARCHIVE_DIR := .
SCRIPTS_DIR := $(ARCHIVE_DIR)/scripts
METADATA_DIR := $(ARCHIVE_DIR)/metadata

# Scripts
DOWNLOAD_SCRIPT := $(SCRIPTS_DIR)/download_papers.py
UPDATE_SCRIPT := $(SCRIPTS_DIR)/update_metadata.py
VERIFY_SCRIPT := $(SCRIPTS_DIR)/verify_access.py
INDEX_SCRIPT := $(SCRIPTS_DIR)/generate_index.py
SEARCH_SCRIPT := $(SCRIPTS_DIR)/search_papers.py

# Output files
BIBLIOGRAPHY := $(METADATA_DIR)/bibliography.bib
DOWNLOAD_CONFIG := $(METADATA_DIR)/download_sources.json
VERIFICATION_REPORT := $(METADATA_DIR)/verification_report.json
CITATION_INDEX := CITATION_INDEX.md

# Phony targets
.PHONY: all help clean download verify update-metadata generate-indices test install-deps

# Default target
all: verify update-metadata generate-indices

# Help target
help:
	@echo "Lambda Calculus Papers Archive - Build System"
	@echo ""
	@echo "Available targets:"
	@echo "  all                - Run verification, update metadata, and generate indices"
	@echo "  download           - Download all open access papers"
	@echo "  download-high      - Download only high priority papers"
	@echo "  download-category  - Download papers from specific category (set CATEGORY=name)"
	@echo "  verify             - Verify URL accessibility and download status"
	@echo "  update-metadata    - Update and validate metadata files"
	@echo "  generate-indices   - Generate all search indices and cross-references"
	@echo "  search             - Interactive search (set QUERY for direct search)"
	@echo "  report             - Generate comprehensive metadata report"
	@echo "  clean              - Clean generated files (not downloaded papers)"
	@echo "  install-deps       - Install Python dependencies"
	@echo "  test               - Run tests and validation"
	@echo ""
	@echo "Examples:"
	@echo "  make download-high"
	@echo "  make download-category CATEGORY=historical_papers"
	@echo "  make search QUERY='lambda calculus'"
	@echo "  make verify > verification.log"

# Install Python dependencies
install-deps:
	@echo "Installing Python dependencies..."
	$(PYTHON) -m pip install --user requests aiohttp certifi

# Download targets
download: $(DOWNLOAD_CONFIG)
	@echo "Downloading all open access papers..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(DOWNLOAD_SCRIPT) --config $(DOWNLOAD_CONFIG)

download-high: $(DOWNLOAD_CONFIG)
	@echo "Downloading high priority papers..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(DOWNLOAD_SCRIPT) --config $(DOWNLOAD_CONFIG) --priority high

download-medium: $(DOWNLOAD_CONFIG)
	@echo "Downloading medium priority papers..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(DOWNLOAD_SCRIPT) --config $(DOWNLOAD_CONFIG) --priority medium

download-category: $(DOWNLOAD_CONFIG)
ifndef CATEGORY
	@echo "Error: CATEGORY not specified. Use: make download-category CATEGORY=historical_papers"
	@exit 1
endif
	@echo "Downloading papers from category: $(CATEGORY)"
	cd $(ARCHIVE_DIR) && $(PYTHON) $(DOWNLOAD_SCRIPT) --config $(DOWNLOAD_CONFIG) --category $(CATEGORY)

# Verification targets
verify: $(VERIFICATION_REPORT)

$(VERIFICATION_REPORT): $(DOWNLOAD_CONFIG)
	@echo "Verifying URL accessibility..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(VERIFY_SCRIPT) --config $(DOWNLOAD_CONFIG) --output $@

verify-category:
ifndef CATEGORY
	@echo "Error: CATEGORY not specified. Use: make verify-category CATEGORY=historical_papers"
	@exit 1
endif
	@echo "Verifying category: $(CATEGORY)"
	cd $(ARCHIVE_DIR) && $(PYTHON) $(VERIFY_SCRIPT) --config $(DOWNLOAD_CONFIG) --category $(CATEGORY)

# Metadata management
update-metadata:
	@echo "Updating metadata and validating consistency..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(UPDATE_SCRIPT) --archive-dir $(ARCHIVE_DIR) --validate

metadata-report:
	@echo "Generating comprehensive metadata report..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(UPDATE_SCRIPT) --archive-dir $(ARCHIVE_DIR) --report

# Index generation
generate-indices:
	@echo "Generating search indices and cross-references..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(INDEX_SCRIPT) --archive-dir $(ARCHIVE_DIR)

generate-author-index:
	@echo "Generating author index..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(INDEX_SCRIPT) --archive-dir $(ARCHIVE_DIR) --index-type author

generate-topic-index:
	@echo "Generating topic index..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(INDEX_SCRIPT) --archive-dir $(ARCHIVE_DIR) --index-type topic

generate-chronological-index:
	@echo "Generating chronological index..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(INDEX_SCRIPT) --archive-dir $(ARCHIVE_DIR) --index-type chronological

# Search functionality
search:
ifdef QUERY
	@echo "Searching for: $(QUERY)"
	cd $(ARCHIVE_DIR) && $(PYTHON) $(SEARCH_SCRIPT) --archive-dir $(ARCHIVE_DIR) --query "$(QUERY)"
else
	@echo "Starting interactive search..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(SEARCH_SCRIPT) --archive-dir $(ARCHIVE_DIR) --interactive
endif

search-author:
ifndef AUTHOR
	@echo "Error: AUTHOR not specified. Use: make search-author AUTHOR='Church'"
	@exit 1
endif
	@echo "Searching for papers by: $(AUTHOR)"
	cd $(ARCHIVE_DIR) && $(PYTHON) $(SEARCH_SCRIPT) --archive-dir $(ARCHIVE_DIR) --author "$(AUTHOR)"

search-year:
ifndef YEAR_RANGE
	@echo "Error: YEAR_RANGE not specified. Use: make search-year YEAR_RANGE='1980-2000'"
	@exit 1
endif
	@echo "Searching for papers in year range: $(YEAR_RANGE)"
	@IFS='-' read -r start_year end_year <<< "$(YEAR_RANGE)"; \
	cd $(ARCHIVE_DIR) && $(PYTHON) $(SEARCH_SCRIPT) --archive-dir $(ARCHIVE_DIR) --start-year $$start_year --end-year $$end_year

# Reporting
report: metadata-report $(VERIFICATION_REPORT)
	@echo "=== Archive Status Report ==="
	@echo ""
	@echo "=== Metadata Report ==="
	cd $(ARCHIVE_DIR) && $(PYTHON) $(UPDATE_SCRIPT) --archive-dir $(ARCHIVE_DIR) --report | head -50
	@echo ""
	@echo "=== Verification Summary ==="
	@if [ -f "$(VERIFICATION_REPORT)" ]; then \
		$(PYTHON) -c "import json; data=json.load(open('$(VERIFICATION_REPORT)')); print(f'Total URLs: {data[\"analysis\"][\"summary\"][\"total_urls\"]}'); print(f'Accessible: {data[\"analysis\"][\"summary\"][\"accessible\"]}'); print(f'Broken: {data[\"analysis\"][\"summary\"][\"broken\"]}')"; \
	else \
		echo "No verification report found. Run 'make verify' first."; \
	fi
	@echo ""
	@echo "=== File Statistics ==="
	@find historical classical modern recent surveys -name "*.pdf" 2>/dev/null | wc -l | xargs echo "PDF files found:"
	@echo ""

# Testing and validation
test: test-scripts test-metadata test-downloads

test-scripts:
	@echo "Testing script syntax..."
	@for script in $(SCRIPTS_DIR)/*.py; do \
		echo "Checking $$script..."; \
		$(PYTHON) -m py_compile "$$script" || exit 1; \
	done
	@echo "All scripts passed syntax check."

test-metadata:
	@echo "Validating metadata consistency..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(UPDATE_SCRIPT) --archive-dir $(ARCHIVE_DIR) --validate

test-downloads:
	@echo "Verifying downloaded files..."
	cd $(ARCHIVE_DIR) && $(PYTHON) $(DOWNLOAD_SCRIPT) --config $(DOWNLOAD_CONFIG) --verify

# Maintenance targets
clean:
	@echo "Cleaning generated files..."
	rm -f AUTHOR_INDEX.md TOPIC_INDEX.md CHRONOLOGICAL_INDEX.md ACCESS_TYPE_INDEX.md
	rm -f ARCHIVE_STATISTICS.md
	rm -f $(VERIFICATION_REPORT)
	rm -f $(METADATA_DIR)/generated_statistics.json
	@echo "Generated files cleaned. Downloaded papers preserved."

clean-cache:
	@echo "Cleaning Python cache files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true

# Development targets
dev-setup: install-deps
	@echo "Setting up development environment..."
	@echo "Development setup complete."

dry-run:
	@echo "Performing dry run of all operations..."
	@echo "1. Download dry run (high priority):"
	cd $(ARCHIVE_DIR) && $(PYTHON) $(DOWNLOAD_SCRIPT) --config metadata/download_sources.json --priority high --dry-run
	@echo ""
	@echo "2. Metadata validation:"
	cd $(ARCHIVE_DIR) && $(PYTHON) $(UPDATE_SCRIPT) --archive-dir $(ARCHIVE_DIR) --validate
	@echo ""
	@echo "3. Index generation (dry run):"
	@echo "Would generate: AUTHOR_INDEX.md, TOPIC_INDEX.md, CHRONOLOGICAL_INDEX.md, ACCESS_TYPE_INDEX.md"

# Batch operations
update-all: download verify update-metadata generate-indices
	@echo "Full archive update completed."

quick-update: download-high update-metadata generate-indices
	@echo "Quick archive update completed."

# Status check
status:
	@echo "=== Lambda Calculus Papers Archive Status ==="
	@echo ""
	@echo "Scripts:"
	@ls -la $(SCRIPTS_DIR)/*.py 2>/dev/null | wc -l | xargs echo "  Python scripts:"
	@echo ""
	@echo "Metadata:"
	@ls -la $(METADATA_DIR)/*.json $(METADATA_DIR)/*.bib 2>/dev/null | wc -l | xargs echo "  Metadata files:"
	@echo ""
	@echo "Papers:"
	@find historical classical modern recent surveys -name "*.pdf" 2>/dev/null | wc -l | xargs echo "  PDF files:"
	@echo ""
	@echo "Indices:"
	@ls -la *_INDEX.md 2>/dev/null | wc -l | xargs echo "  Generated indices:"
	@echo ""
	@if [ -f "$(VERIFICATION_REPORT)" ]; then \
		echo "Last verification:"; \
		$(PYTHON) -c "import json; data=json.load(open('$(VERIFICATION_REPORT)')); print(f'  {data[\"analysis\"][\"timestamp\"]}')" 2>/dev/null || echo "  Unknown"; \
	else \
		echo "Last verification: Never"; \
	fi

# Integration with main repository
integrate:
	@echo "Integrating papers archive with main lambda-research repository..."
	@if [ ! -f "../README.md" ]; then \
		echo "Error: Not in papers-archive subdirectory of lambda-research"; \
		exit 1; \
	fi
	@echo "Updating main repository documentation..."
	@echo "<!-- Papers Archive Status -->" >> ../README.md
	@echo "## Papers Archive" >> ../README.md
	@echo "" >> ../README.md
	@echo "The papers-archive/ directory contains a systematic collection of lambda calculus research papers." >> ../README.md
	@echo "See [papers-archive/README.md](papers-archive/README.md) for details." >> ../README.md
	@echo "" >> ../README.md
	cd $(ARCHIVE_DIR) && $(PYTHON) $(INDEX_SCRIPT) --archive-dir $(ARCHIVE_DIR) --index-type all
	@echo "Integration completed. Main README.md updated."