#!/usr/bin/env bash
#
# check-health.sh
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

# Repository Health Dashboard - Quick Metrics Collection
# Run daily to track progress against baseline

set -e

REPO_ROOT="/home/eirikr/Research/Algorithms/lambda-research"
cd "$REPO_ROOT"

echo "=========================================="
echo "Lambda Calculus Repository Health Dashboard"
echo "Date: $(date +%Y-%m-%d)"
echo "=========================================="
echo ""

# === CRITICAL METRICS (Must Pass) ===
echo "[CRITICAL] CRITICAL METRICS (Must Pass Daily)"
echo "----------------------------------------"

# 1. Build Status
cd "$REPO_ROOT/sources/rust-implementations/tapl-rust"
if cargo build --workspace --quiet 2>/dev/null; then
    echo "[x] Build Status: PASS"
    BUILD_STATUS="PASS"
else
    echo " Build Status: FAIL"
    BUILD_STATUS="FAIL"
fi

# 2. Test Status
if cargo test --workspace --quiet 2>/dev/null; then
    TEST_COUNT=$(cargo test --workspace 2>&1 | grep -oP '\d+(?= passed)' | head -1)
    echo "[x] Test Suite: PASS ($TEST_COUNT tests)"
    TEST_STATUS="PASS"
else
    echo " Test Suite: FAIL"
    TEST_STATUS="FAIL"
fi

# 3. Linter Status
cd "$REPO_ROOT/sources/rust-implementations/tapl-rust"
if cargo clippy --workspace -- -D warnings 2>&1 | grep -q "Finished"; then
    echo "[x] Linter (Clippy): PASS (0 warnings)"
    LINT_STATUS="PASS"
else
    WARNING_COUNT=$(cargo clippy --workspace 2>&1 | grep -c "warning:" || echo "0")
    echo " Linter (Clippy): FAIL ($WARNING_COUNT warnings)"
    LINT_STATUS="FAIL"
fi

# 4. Git Cleanliness
cd "$REPO_ROOT"
UNTRACKED_COUNT=$(git status --porcelain | wc -l)
if [ "$UNTRACKED_COUNT" -eq 0 ]; then
    echo "[x] Git Status: CLEAN (0 untracked)"
    GIT_STATUS="PASS"
else
    echo " Git Status: DIRTY ($UNTRACKED_COUNT untracked)"
    GIT_STATUS="FAIL"
fi

# 5. Repository Size
REPO_SIZE=$(du -sh . 2>/dev/null | awk '{print $1}')
REPO_SIZE_GB=$(du -sb . 2>/dev/null | awk '{printf "%.1f", $1/1024/1024/1024}')
if (( $(echo "$REPO_SIZE_GB < 2.0" | bc -l) )); then
    echo "[x] Repository Size: $REPO_SIZE (< 2GB target)"
    SIZE_STATUS="PASS"
else
    echo " Repository Size: $REPO_SIZE (> 2GB target)"
    SIZE_STATUS="WARN"
fi

echo ""

# === HIGH PRIORITY METRICS ===
echo "[HIGH] HIGH PRIORITY METRICS (Weekly Target)"
echo "----------------------------------------"

# 6. Test Count Trend
echo "[METRICS] Test Count: $TEST_COUNT tests"
echo "   Baseline: 8 tests (2025-12-23)"
echo "   Target: 40 tests (50% coverage)"

# 7. Documentation TODO Count
TODO_COUNT=$(find docs -name "*.md" -exec grep -l "TODO\|FIXME\|XXX" {} \; 2>/dev/null | wc -l)
echo "[METRICS] Incomplete Docs: $TODO_COUNT files with TODO/FIXME"
echo "   Baseline: 19 files (2025-12-23)"
echo "   Target: <5 files"

# 8. Rust LOC
RUST_LOC=$(find sources/rust-implementations/tapl-rust -name "*.rs" -path "*/src/*" -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $1}')
echo "[METRICS] Rust Source LOC: $RUST_LOC lines"
echo "   Baseline: 482 lines (2025-12-23)"

# 9. Documentation Files
DOC_COUNT=$(find . -name "*.md" -type f | wc -l)
echo "[METRICS] Documentation Files: $DOC_COUNT markdown files"
echo "   Baseline: 167 files (2025-12-23)"

# 10. Citation Count (corrected metric)
CITATION_COUNT=$(find docs -name "bibliography.md" -exec cat {} \; 2>/dev/null | grep -c "^\*   \*\*" || echo "0")
echo "[METRICS] Verified Citations: $CITATION_COUNT formal bibliography entries"
echo "   Baseline: 33 entries (2025-12-23)"
echo "   Target: 100+ entries"

echo ""

# === HEALTH SCORE CALCULATION ===
echo "[PROGRESS] OVERALL HEALTH SCORE"
echo "----------------------------------------"

# Calculate score
SCORE=0

# Critical metrics (60 points total, 12 each)
[ "$BUILD_STATUS" = "PASS" ] && SCORE=$((SCORE + 12))
[ "$TEST_STATUS" = "PASS" ] && SCORE=$((SCORE + 12))
[ "$LINT_STATUS" = "PASS" ] && SCORE=$((SCORE + 12))
[ "$GIT_STATUS" = "PASS" ] && SCORE=$((SCORE + 12))
[ "$SIZE_STATUS" = "PASS" ] && SCORE=$((SCORE + 12))

# Test coverage (20 points based on test count)
if [ "$TEST_COUNT" -ge 40 ]; then
    SCORE=$((SCORE + 20))
elif [ "$TEST_COUNT" -ge 20 ]; then
    SCORE=$((SCORE + 10))
elif [ "$TEST_COUNT" -ge 10 ]; then
    SCORE=$((SCORE + 5))
fi

# Documentation completeness (20 points based on TODO count)
if [ "$TODO_COUNT" -le 5 ]; then
    SCORE=$((SCORE + 20))
elif [ "$TODO_COUNT" -le 10 ]; then
    SCORE=$((SCORE + 15))
elif [ "$TODO_COUNT" -le 15 ]; then
    SCORE=$((SCORE + 10))
fi

# Display score with visual indicator
echo "Score: $SCORE / 100"

if [ "$SCORE" -ge 75 ]; then
    echo "Status: [MEDIUM] HEALTHY"
elif [ "$SCORE" -ge 50 ]; then
    echo "Status: [HIGH] FAIR"
elif [ "$SCORE" -ge 25 ]; then
    echo "Status: 🟠 NEEDS IMPROVEMENT"
else
    echo "Status: [CRITICAL] CRITICAL"
fi

echo ""
echo "Baseline Score: 42/100 (2025-12-23)"
echo "Current Score:  $SCORE/100"
if [ "$SCORE" -gt 42 ]; then
    IMPROVEMENT=$((SCORE - 42))
    echo "Progress: +$IMPROVEMENT points [PROGRESS]"
elif [ "$SCORE" -lt 42 ]; then
    DECLINE=$((42 - SCORE))
    echo "Progress: -$DECLINE points "
else
    echo "Progress: No change"
fi

echo ""
echo "=========================================="
echo "Dashboard generation complete"
echo "=========================================="
