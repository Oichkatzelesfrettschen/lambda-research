# License Migration Summary

**Date**: 2025-12-24  
**Migration**: MIT → GPL-3.0 / LGPL-3.0

## Overview

This document summarizes the complete migration of the Lambda Calculus Research Repository from MIT License to GNU GPL v3.0 (with LGPL v3.0 for library components).

## Rationale

Per project requirements: "All synthesized research documents; anything that can be licensed and all that can be within this repo; must be licensed under the most recent GPL license, with a fallback to LGPL where absolutely necessary."

The most recent GPL license is **GNU General Public License v3.0** (released June 29, 2007).

## What Changed

### 1. Core License Files

- **LICENSE**: Replaced MIT license with full GPL-3.0 text
- **LICENSE.LGPL**: Added LGPL-3.0 license for library components
- **COPYING**: Created comprehensive licensing guide explaining dual licensing
- **LICENSE.MIT.backup**: Preserved original MIT license for reference

### 2. Source Code Headers (25 files)

All synthesized source code now includes GPL-3.0 headers:

#### Python Scripts (18 files)
- `scripts/orchestrator.py`
- `scripts/validate-repository.py`
- `scripts/standardize_bibliography.py`
- `scripts/scaffold_directories.py`
- `scripts/verify_dataset_scale.py`
- `scripts/fix_links.py`
- `scripts/fix_missing_sections.py`
- `scripts/add_license_headers.py`
- `docs/scripts/download_papers.py`
- `docs/scripts/generate_index.py`
- `docs/scripts/update_metadata.py`
- `docs/scripts/verify_access.py`
- `docs/scripts/search_papers.py`
- `papers-archive/scripts/download_papers.py`
- `papers-archive/scripts/generate_index.py`
- `papers-archive/scripts/update_metadata.py`
- `papers-archive/scripts/verify_access.py`
- `papers-archive/scripts/search_papers.py`

#### Shell Scripts (3 files)
- `scripts/setup-mkdocs.sh`
- `scripts/profile_uss.sh`
- `check-health.sh`

#### Implementations (4 files)
- `implementations/scala/LambdaCalculus.scala`
- `implementations/scheme/lambda-racket.rkt`
- `implementations/sml/lambda.sml`
- `implementations/idris/Lambda.idr`

### 3. Documentation Updates (9 files)

- **README.md**: Added comprehensive licensing section
- **CITATION.cff**: Updated license field to GPL-3.0-or-later
- **docs/appendices/license.md**: Complete rewrite explaining dual licensing
- **CLAUDE.md**: Added licensing section for AI assistant guidance
- **GEMINI.md**: Added licensing section for AI assistant guidance
- **implementations/scala/README.md**: Added license note
- **implementations/scheme/README.md**: Added license note
- **implementations/sml/README.md**: Added license note
- **implementations/idris/README.md**: Added license note
- **papers-archive/README.md**: Added licensing clarification

## What Remains Unchanged

### Academic Papers

PDF files and academic papers in `docs/` and `papers-archive/` retain their **original copyrights**:

- These are NOT relicensed under GPL
- Included under fair use for research and educational purposes
- Each paper maintains its own copyright and licensing terms

### External Dependencies

Any third-party libraries or tools maintain their original licenses.

## License Structure

### GPL-3.0 (Primary)

Applies to all synthesized research content:
- Implementation code (Scala, Scheme, SML, Idris)
- Python scripts and automation tools
- Shell scripts
- Documentation markdown files
- Repository structure and organization

### LGPL-3.0 (Libraries)

Available for reusable library components:
- Lambda calculus implementation libraries
- Standalone utility modules designed for linking

### Original Copyrights (Academic Papers)

Academic papers maintain original copyrights:
- PDF files in documentation
- External citations and bibliographies
- Research materials

## Contributor Guidelines

By contributing to this repository after this migration, contributors agree to:

1. License code contributions under GPL-3.0 (or LGPL-3.0 for library components)
2. Respect academic paper copyrights
3. Follow the licensing structure outlined in COPYING file

## Verification

### Files Created/Modified

- 3 license files (LICENSE, LICENSE.LGPL, COPYING)
- 25 source files with GPL headers
- 9 documentation files updated
- 1 migration summary (this file)

### Total Changes

- **38 files** modified or created
- **100%** of synthesized source code now GPL-licensed
- **0 academic papers** relicensed (maintaining original copyrights)

## References

- GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
- LGPL-3.0: https://www.gnu.org/licenses/lgpl-3.0.html
- GNU Licenses: https://www.gnu.org/licenses/

## Questions?

See `COPYING` file for detailed licensing information, or refer to the licenses themselves in `LICENSE` and `LICENSE.LGPL`.

---

*Migration completed: 2025-12-24*  
*Repository: https://github.com/Oichkatzelesfrettschen/lambda-research*
