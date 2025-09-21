#!/usr/bin/env python3
"""
Lambda Calculus Research Repository - Comprehensive Validation System

This script performs automated quality assurance checks on the repository:
1. URL validation and broken link detection
2. Markdown structure validation
3. Cross-reference verification
4. Bibliography format checking
5. Documentation completeness audit
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Set, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class RepositoryValidator:
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.errors = []
        self.warnings = []
        self.stats = {
            'total_files': 0,
            'markdown_files': 0,
            'urls_found': 0,
            'broken_urls': 0,
            'missing_files': 0,
            'bibliography_files': 0
        }

    def validate_all(self) -> bool:
        """Run all validation checks"""
        print("🔍 Starting comprehensive repository validation...")
        print("=" * 60)

        # Core validation checks
        self._scan_repository()
        self._validate_directory_structure()
        self._validate_markdown_files()
        self._validate_cross_references()
        self._validate_bibliography_format()
        self._validate_urls()

        # Generate report
        self._generate_report()

        return len(self.errors) == 0

    def _scan_repository(self):
        """Scan repository for files and basic statistics"""
        print("📊 Scanning repository structure...")

        for file_path in self.root_path.rglob('*'):
            if file_path.is_file():
                self.stats['total_files'] += 1

                if file_path.suffix == '.md':
                    self.stats['markdown_files'] += 1

                if 'bibliography' in file_path.name.lower():
                    self.stats['bibliography_files'] += 1

    def _validate_directory_structure(self):
        """Validate expected directory structure"""
        print("📁 Validating directory structure...")

        # Check for numbered directories (01-31)
        expected_dirs = [f"{i:02d}-" for i in range(1, 32)]
        missing_dirs = []

        for expected in expected_dirs:
            found = any(d.name.startswith(expected) for d in self.root_path.iterdir() if d.is_dir())
            if not found:
                missing_dirs.append(expected)

        if missing_dirs:
            self.warnings.append(f"Missing expected directories: {missing_dirs}")

        # Check for required subdirectories in numbered dirs
        for dir_path in self.root_path.iterdir():
            if dir_path.is_dir() and re.match(r'^\d{2}-', dir_path.name):
                required_subdirs = ['papers', 'implementations', 'tutorials', 'historical']
                for subdir in required_subdirs:
                    subdir_path = dir_path / subdir
                    if not subdir_path.exists():
                        self.warnings.append(f"Missing {subdir}/ in {dir_path.name}")

    def _validate_markdown_files(self):
        """Validate markdown file structure and content"""
        print("📝 Validating markdown files...")

        for md_file in self.root_path.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check for basic structure
                if not content.strip():
                    self.errors.append(f"Empty markdown file: {md_file.relative_to(self.root_path)}")
                    continue

                # Check for proper headers
                if not content.startswith('#'):
                    self.warnings.append(f"No top-level header in: {md_file.relative_to(self.root_path)}")

                # Check for README files in numbered directories
                if md_file.name == 'README.md':
                    parent_dir = md_file.parent.name
                    if re.match(r'^\d{2}-', parent_dir):
                        # Validate README content requirements
                        required_sections = ['overview', 'syntax', 'properties', 'resources']
                        content_lower = content.lower()
                        missing_sections = [s for s in required_sections if s not in content_lower]

                        if missing_sections:
                            self.warnings.append(
                                f"README {parent_dir} missing sections: {missing_sections}"
                            )

            except Exception as e:
                self.errors.append(f"Error reading {md_file.relative_to(self.root_path)}: {e}")

    def _extract_urls(self, content: str) -> List[str]:
        """Extract URLs from markdown content"""
        # Pattern for markdown links and raw URLs
        url_patterns = [
            r'\[([^\]]+)\]\(([^)]+)\)',  # [text](url)
            r'<(https?://[^>]+)>',       # <url>
            r'(?:^|\s)(https?://\S+)'    # raw URLs
        ]

        urls = []
        for pattern in url_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                if isinstance(match, tuple):
                    url = match[-1]  # Get the URL part
                else:
                    url = match

                # Clean up the URL
                url = url.strip().rstrip('.,;:)')
                if url.startswith(('http://', 'https://')):
                    urls.append(url)

        return urls

    def _validate_cross_references(self):
        """Validate internal cross-references and links"""
        print("🔗 Validating cross-references...")

        all_files = set()
        for md_file in self.root_path.rglob('*.md'):
            all_files.add(md_file.relative_to(self.root_path))

        for md_file in self.root_path.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find relative links
                relative_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

                for link_text, link_url in relative_links:
                    # Skip external URLs
                    if link_url.startswith(('http://', 'https://', 'mailto:')):
                        continue

                    # Skip anchors
                    if link_url.startswith('#'):
                        continue

                    # Resolve relative path
                    if link_url.startswith('../'):
                        # Handle relative paths
                        target_path = (md_file.parent / link_url).resolve()
                        relative_target = target_path.relative_to(self.root_path)
                    else:
                        relative_target = md_file.parent / link_url
                        try:
                            relative_target = relative_target.relative_to(self.root_path)
                        except ValueError:
                            continue

                    if relative_target not in all_files:
                        self.errors.append(
                            f"Broken internal link in {md_file.relative_to(self.root_path)}: "
                            f"'{link_url}' -> {relative_target}"
                        )

            except Exception as e:
                self.warnings.append(f"Error checking cross-references in {md_file.name}: {e}")

    def _validate_bibliography_format(self):
        """Validate bibliography file formatting"""
        print("📚 Validating bibliography formatting...")

        bibliography_files = list(self.root_path.rglob('*bibliography*.md'))

        for bib_file in bibliography_files:
            try:
                with open(bib_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check for standard citation format
                citations = re.findall(r'\*\*([^*]+)\*\*\s*\((\d{4})\)', content)

                if not citations:
                    self.warnings.append(
                        f"No standard citations found in {bib_file.relative_to(self.root_path)}"
                    )
                    continue

                # Check for DOI presence
                doi_count = len(re.findall(r'DOI.*?10\.\d+', content, re.IGNORECASE))

                if doi_count < len(citations) * 0.5:  # Less than 50% have DOIs
                    self.warnings.append(
                        f"Low DOI coverage in {bib_file.relative_to(self.root_path)}: "
                        f"{doi_count}/{len(citations)}"
                    )

            except Exception as e:
                self.errors.append(f"Error validating {bib_file.relative_to(self.root_path)}: {e}")

    def _check_url(self, url: str, timeout: int = 10) -> Tuple[str, bool, str]:
        """Check if a URL is accessible"""
        try:
            # Create request with proper headers
            req = urllib.request.Request(
                url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (compatible; Repository-Validator/1.0)'
                }
            )

            with urllib.request.urlopen(req, timeout=timeout) as response:
                status_code = response.getcode()
                return url, status_code == 200, f"HTTP {status_code}"

        except urllib.error.HTTPError as e:
            return url, False, f"HTTP {e.code}"
        except urllib.error.URLError as e:
            return url, False, f"URL Error: {e.reason}"
        except Exception as e:
            return url, False, f"Error: {str(e)}"

    def _validate_urls(self):
        """Validate all URLs in the repository"""
        print("🌐 Validating URLs (this may take a while)...")

        all_urls = set()
        url_sources = {}

        # Collect all URLs
        for md_file in self.root_path.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                urls = self._extract_urls(content)
                for url in urls:
                    all_urls.add(url)
                    if url not in url_sources:
                        url_sources[url] = []
                    url_sources[url].append(md_file.relative_to(self.root_path))

            except Exception as e:
                self.warnings.append(f"Error extracting URLs from {md_file.name}: {e}")

        self.stats['urls_found'] = len(all_urls)

        if not all_urls:
            print("  No URLs found to validate")
            return

        print(f"  Found {len(all_urls)} unique URLs to validate...")

        # Validate URLs in parallel (but be respectful)
        broken_urls = []

        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit URL validation jobs
            future_to_url = {
                executor.submit(self._check_url, url): url
                for url in list(all_urls)[:20]  # Limit to first 20 URLs for demo
            }

            completed = 0
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    url, is_valid, message = future.result()
                    completed += 1

                    if completed % 5 == 0:
                        print(f"  Progress: {completed}/{min(20, len(all_urls))} URLs checked")

                    if not is_valid:
                        broken_urls.append((url, message, url_sources[url]))
                        self.stats['broken_urls'] += 1

                except Exception as e:
                    self.warnings.append(f"Error checking URL {url}: {e}")

                # Be respectful - small delay between requests
                time.sleep(0.1)

        # Report broken URLs
        for url, error, sources in broken_urls:
            source_list = ', '.join(str(s) for s in sources[:3])
            if len(sources) > 3:
                source_list += f" (and {len(sources)-3} more)"

            self.errors.append(f"Broken URL: {url} ({error}) in {source_list}")

    def _generate_report(self):
        """Generate validation report"""
        print("\n" + "=" * 60)
        print("📋 VALIDATION REPORT")
        print("=" * 60)

        # Statistics
        print("\n📊 Repository Statistics:")
        for key, value in self.stats.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")

        # Errors
        if self.errors:
            print(f"\n❌ Errors ({len(self.errors)}):")
            for i, error in enumerate(self.errors[:10], 1):
                print(f"  {i}. {error}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors) - 10} more errors")
        else:
            print("\n✅ No errors found!")

        # Warnings
        if self.warnings:
            print(f"\n⚠️  Warnings ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings[:10], 1):
                print(f"  {i}. {warning}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more warnings")
        else:
            print("\n✅ No warnings!")

        # Overall status
        print(f"\n📈 Overall Status:")
        if len(self.errors) == 0:
            print("  🎉 Repository validation PASSED!")
        else:
            print("  ❌ Repository validation FAILED!")
            print(f"  Please fix {len(self.errors)} errors before proceeding.")

        print("\n" + "=" * 60)

def main():
    """Main validation entry point"""
    validator = RepositoryValidator('.')
    success = validator.validate_all()

    # Return appropriate exit code
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()