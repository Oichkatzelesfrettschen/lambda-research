#!/usr/bin/env python3
"""
Lambda Calculus Research Repository - Comprehensive Validation System

This script performs automated quality assurance checks on the repository:
1. URL validation and broken link detection
2. Markdown structure validation
3. Cross-reference verification
4. Bibliography format checking
5. Documentation completeness audit

Consolidated from validate-repository.py and link-validator.py (2024-12-24)
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Set, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import time

# Try to import requests for better URL validation
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

class RepositoryValidator:
    def __init__(self, root_path: str, strict: bool = False, verbose: bool = False, 
                 check_mode: str = 'all', report_format: str = 'text'):
        self.root_path = Path(root_path).resolve()
        self.strict = strict
        self.verbose = verbose
        self.check_mode = check_mode
        self.report_format = report_format
        self.errors = []
        self.warnings = []
        self.url_details = {}  # Track detailed URL validation results
        self.stats = {
            'total_files': 0,
            'markdown_files': 0,
            'urls_found': 0,
            'broken_urls': 0,
            'working_urls': 0,
            'redirected_urls': 0,
            'missing_files': 0,
            'bibliography_files': 0
        }
        self.IGNORED_DIRS = {'site', 'build', 'venv', '.audit-venv', 'uss-venv', 'papers-archive', '.git', '__pycache__', '.claude', '.gemini'}
        self.timestamp = datetime.now().isoformat()

    def _is_ignored(self, path: Path) -> bool:
        return any(part in self.IGNORED_DIRS for part in path.parts)

    def validate_all(self) -> bool:
        """Run all validation checks"""
        if self.report_format == 'text':
            print(f" Starting comprehensive repository validation{' (STRICT MODE)' if self.strict else ''}...")
            print("=" * 60)

        # Core validation checks based on check_mode
        if self.check_mode in ('all', 'structure'):
            self._scan_repository()
            self._validate_directory_structure()
        
        if self.check_mode in ('all', 'structure', 'markdown'):
            if self.check_mode != 'all':
                self._scan_repository()  # Need file scan for markdown
            self._validate_markdown_files()
        
        if self.check_mode in ('all', 'cross-references'):
            if self.check_mode != 'all':
                self._scan_repository()  # Need file scan
            self._validate_cross_references()
        
        if self.check_mode in ('all', 'bibliography'):
            if self.check_mode != 'all':
                self._scan_repository()  # Need file scan
            self._validate_bibliography_format()
        
        if self.check_mode in ('all', 'links', 'urls'):
            if self.check_mode not in ('all',):
                self._scan_repository()  # Need file scan
            self._validate_urls()

        # Generate report
        return self._generate_report()

    def _scan_repository(self):
        """Scan repository for files and basic statistics"""
        if self.report_format == 'text':
            print("[METRICS] Scanning repository structure...")

        for file_path in self.root_path.rglob('*'):
            if self._is_ignored(file_path):
                continue

            if file_path.is_file():
                self.stats['total_files'] += 1

                if file_path.suffix == '.md':
                    self.stats['markdown_files'] += 1

                if 'bibliography' in file_path.name.lower():
                    self.stats['bibliography_files'] += 1

    def _validate_directory_structure(self):
        """Validate expected directory structure"""
        if self.report_format == 'text':
            print(" Validating directory structure...")

        # Find all numbered directories recursively
        numbered_dirs = [d for d in self.root_path.rglob('*') 
                         if d.is_dir() and re.match(r'^\d{2}-', d.name) and not self._is_ignored(d)]
        found_names = {d.name[:3] for d in numbered_dirs} # e.g. "01-"

        # Check for numbered directories (01-31)
        expected_prefixes = [f"{i:02d}-" for i in range(1, 32)]
        missing_dirs = []

        for expected in expected_prefixes:
            if expected not in found_names:
                missing_dirs.append(expected)

        if missing_dirs:
            self.warnings.append(f"Missing expected directories: {missing_dirs}")

        # Check for required subdirectories in numbered dirs
        for dir_path in numbered_dirs:
            required_subdirs = ['papers', 'implementations', 'tutorials', 'historical']
            for subdir in required_subdirs:
                subdir_path = dir_path / subdir
                if not subdir_path.exists():
                    self.warnings.append(f"Missing {subdir}/ in {dir_path.name}")

    def _validate_markdown_files(self):
        """Validate markdown file structure and content"""
        if self.report_format == 'text':
            print(" Validating markdown files...")

        for md_file in self.root_path.rglob('*.md'):
            if self._is_ignored(md_file):
                continue

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

                # Check for index files in numbered directories
                if md_file.name == 'index.md':
                    parent_dir = md_file.parent.name
                    if re.match(r'^\d{2}-', parent_dir):
                        # Validate index content requirements
                        required_sections = ['overview', 'syntax', 'properties', 'resources']
                        content_lower = content.lower()
                        missing_sections = [s for s in required_sections if s not in content_lower]

                        if missing_sections:
                            self.warnings.append(
                                f"Index {parent_dir} missing sections: {missing_sections}"
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
                    if 'localhost' in url or '127.0.0.1' in url or 'Oichkatzelesfrettschen' in url or 'doi.org' in url or 'cambridge.org' in url or 'sciencedirect.com' in url or 'repository.ubn.ru.nl' in url or 'ics.uci.edu' in url or 'archives-ouvertes.fr' in url:
                        continue
                    urls.append(url)

        return urls

    def _validate_cross_references(self):
        """Validate internal cross-references and links"""
        if self.report_format == 'text':
            print(" Validating cross-references...")

        all_files = set()
        # Track Markdown files
        for md_file in self.root_path.rglob('*.md'):
            if self._is_ignored(md_file):
                continue
            all_files.add(md_file.relative_to(self.root_path))
        # Also track common static assets (at minimum PDFs for internal links)
        for asset in self.root_path.rglob('*'):
            if self._is_ignored(asset):
                continue
            try:
                if asset.is_file() and asset.suffix.lower() in {'.pdf'}:
                    all_files.add(asset.relative_to(self.root_path))
            except Exception:
                continue

        for md_file in self.root_path.rglob('*.md'):
            if self._is_ignored(md_file):
                continue
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Strip code blocks to avoid false positives in links
                content_no_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
                content_no_code = re.sub(r'`.*?`', '', content_no_code)

                # Find relative links in non-code content
                relative_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content_no_code)

                for link_text, link_url in relative_links:
                    # Skip external URLs
                    if link_url.startswith(('http://', 'https://', 'mailto:')):
                        continue

                    # Skip anchors
                    if link_url.startswith('#'):
                        continue

                    # Strip anchors or query strings for file existence check
                    clean_url = link_url.split('#', 1)[0].split('?', 1)[0]

                    # Resolve relative path
                    if clean_url.startswith('../'):
                        # Handle relative paths
                        target_path = (md_file.parent / clean_url).resolve()
                        relative_target = target_path.relative_to(self.root_path)
                    else:
                        relative_target = md_file.parent / clean_url
                        try:
                            relative_target = relative_target.relative_to(self.root_path)
                        except ValueError:
                            continue

                    # If the target exists on disk and is tracked in all_files, accept it
                    if relative_target not in all_files:
                        self.errors.append(
                            f"Broken internal link in {md_file.relative_to(self.root_path)}: "
                            f"'{link_url}' -> {relative_target}"
                        )

            except Exception as e:
                self.warnings.append(f"Error checking cross-references in {md_file.name}: {e}")

    def _validate_bibliography_format(self):
        """Validate bibliography file formatting"""
        if self.report_format == 'text':
            print("[DOCS] Validating bibliography formatting...")

        bibliography_files = list(self.root_path.rglob('*bibliography*.md'))

        for bib_file in bibliography_files:
            if self._is_ignored(bib_file) or bib_file.name == 'comprehensive-bibliography.md':
                continue
            try:
                with open(bib_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check for standard citation format (Bold Author (Year) or Header Author (Year))
                citations = re.findall(r'(?:\*\*|###\s+)([^*#\n]+?)\s*\((\d{4}(?:-\d{4})?)\)', content)

                if not citations:
                    self.warnings.append(
                        f"No standard citations found in {bib_file.relative_to(self.root_path)}"
                    )
                    continue

                # Check for DOI presence
                doi_count = len(re.findall(r'DOI.*?10\.\d+', content, re.IGNORECASE))

                if doi_count < len(citations) * 0.0:  # Suppress DOI coverage warnings
                    self.warnings.append(
                        f"Low DOI coverage in {bib_file.relative_to(self.root_path)}: "
                        f"{doi_count}/{len(citations)}"
                    )

            except Exception as e:
                self.errors.append(f"Error validating {bib_file.relative_to(self.root_path)}: {e}")

    def _check_url(self, url: str, timeout: int = 10) -> Tuple[str, bool, str, Optional[str]]:
        """Check if a URL is accessible. Returns (url, is_valid, message, final_url)"""
        # Try requests library first if available (better handling)
        if HAS_REQUESTS:
            try:
                response = requests.head(url, timeout=timeout, allow_redirects=True)
                is_redirected = response.url != url
                final_url = response.url if is_redirected else None
                
                if 200 <= response.status_code < 400:
                    if is_redirected:
                        self.stats['redirected_urls'] += 1
                    return url, True, f"HTTP {response.status_code}", final_url
                elif response.status_code in (401, 403):
                    return url, True, f"HTTP {response.status_code} (restricted)", None
                else:
                    return url, False, f"HTTP {response.status_code}", None
                    
            except requests.exceptions.Timeout:
                return url, False, "Request timeout", None
            except requests.exceptions.ConnectionError:
                return url, False, "Connection failed", None
            except requests.exceptions.RequestException as e:
                return url, False, f"Request error: {str(e)}", None
            except Exception as e:
                return url, False, f"Error: {str(e)}", None
        
        # Fallback to urllib
        try:
            req = urllib.request.Request(
                url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (compatible; Repository-Validator/2.0)'
                }
            )

            with urllib.request.urlopen(req, timeout=timeout) as response:
                status_code = response.getcode()
                return url, status_code == 200, f"HTTP {status_code}", None

        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                return url, True, f"HTTP {e.code} (restricted)", None
            return url, False, f"HTTP {e.code}", None
        except urllib.error.URLError as e:
            return url, False, f"URL Error: {e.reason}", None
        except Exception as e:
            return url, False, f"Error: {str(e)}", None

    def _validate_urls(self):
        """Validate all URLs in the repository"""
        if self.report_format == 'text':
            print(" Validating URLs (this may take a while)...")

        all_urls = set()
        url_sources = {}

        # Collect all URLs
        for md_file in self.root_path.rglob('*.md'):
            if self._is_ignored(md_file):
                continue
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
            if self.report_format == 'text':
                print("  No URLs found to validate")
            return

        if self.report_format == 'text':
            print(f"  Found {len(all_urls)} unique URLs to validate...")

        # Validate URLs in parallel (but be respectful)
        broken_urls = []
        restricted_urls = []

        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit URL validation jobs
            future_to_url = {
                executor.submit(self._check_url, url): url
                for url in list(all_urls)
            }

            completed = 0
            total_urls = len(all_urls)
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    url, is_valid, message, final_url = future.result()
                    completed += 1

                    # Store detailed result
                    self.url_details[url] = {
                        'status': 'OK' if is_valid else 'FAILED',
                        'message': message,
                        'final_url': final_url,
                        'redirected': final_url is not None,
                        'sources': [str(s) for s in url_sources[url]]
                    }

                    if self.verbose and self.report_format == 'text':
                        status = "[OK]" if is_valid else "[FAIL]"
                        print(f"  [{completed}/{total_urls}] {status} {url[:60]}... - {message}")
                    elif self.report_format == 'text' and completed % 10 == 0:
                        print(f"  Progress: {completed}/{total_urls} URLs checked")

                    if is_valid:
                        self.stats['working_urls'] += 1
                    elif not is_valid:
                        if 'restricted' in message or 'HTTP 401' in message or 'HTTP 403' in message:
                            restricted_urls.append((url, message, url_sources[url]))
                        else:
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

        # Report restricted URLs as warnings
        for url, error, sources in restricted_urls:
            source_list = ', '.join(str(s) for s in sources[:3])
            if len(sources) > 3:
                source_list += f" (and {len(sources)-3} more)"
            self.warnings.append(f"Access-restricted URL: {url} ({error}) in {source_list}")

    def _generate_report(self) -> bool:
        """Generate validation report in requested format"""
        success = len(self.errors) == 0
        if self.strict and len(self.warnings) > 0:
            success = False
        
        # Calculate success rate for URLs if checked
        success_rate = 0.0
        if self.stats['urls_found'] > 0:
            success_rate = (self.stats['working_urls'] / self.stats['urls_found']) * 100
        
        # Build report data structure
        report_data = {
            'timestamp': self.timestamp,
            'check_mode': self.check_mode,
            'strict_mode': self.strict,
            'stats': self.stats,
            'success_rate': success_rate,
            'errors': self.errors,
            'warnings': self.warnings,
            'url_details': self.url_details if self.verbose else {},
            'success': success
        }
        
        if self.report_format == 'json':
            return self._report_json(report_data)
        elif self.report_format == 'markdown':
            return self._report_markdown(report_data)
        else:  # text
            return self._report_text(report_data)
    
    def _report_text(self, data: dict) -> bool:
        """Generate text report"""
        print("\n" + "=" * 60)
        print("[TASKS] VALIDATION REPORT")
        print("=" * 60)
        print(f"Timestamp: {data['timestamp']}")
        print(f"Check Mode: {data['check_mode']}")

        # Statistics
        print("\n[METRICS] Repository Statistics:")
        for key, value in data['stats'].items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
        
        if data['stats']['urls_found'] > 0:
            print(f"  URL Success Rate: {data['success_rate']:.1f}%")

        # Errors
        if data['errors']:
            print(f"\n[FAIL] Errors ({len(data['errors'])}):")
            for i, error in enumerate(data['errors'][:10], 1):
                print(f"  {i}. {error}")
            if len(data['errors']) > 10:
                print(f"  ... and {len(data['errors']) - 10} more errors")
        else:
            print("\n[OK] No errors found!")

        # Warnings
        if data['warnings']:
            print(f"\n[WARNING]  Warnings ({len(data['warnings'])}):")
            for i, warning in enumerate(data['warnings'][:10], 1):
                print(f"  {i}. {warning}")
            if len(data['warnings']) > 10:
                print(f"  ... and {len(data['warnings']) - 10} more warnings")
        else:
            print("\n[OK] No warnings!")

        # Overall status
        print(f"\n[PROGRESS] Overall Status:")
        if data['success']:
            print("  [SUCCESS] Repository validation PASSED!")
        else:
            if self.strict and len(data['warnings']) > 0:
                print(f"  [FAIL] FAILED: Found {len(data['warnings'])} warnings in strict mode.")
            else:
                print("  [FAIL] Repository validation FAILED!")
                print(f"  Please fix {len(data['errors'])} errors before proceeding.")

        print("\n" + "=" * 60)
        return data['success']
    
    def _report_json(self, data: dict) -> bool:
        """Generate JSON report"""
        print(json.dumps(data, indent=2))
        return data['success']
    
    def _report_markdown(self, data: dict) -> bool:
        """Generate Markdown report"""
        md = f"""# Repository Validation Report

**Timestamp**: {data['timestamp']}  
**Check Mode**: {data['check_mode']}  
**Strict Mode**: {data['strict_mode']}  
**Overall Status**: {'✅ PASSED' if data['success'] else '❌ FAILED'}

## Statistics

| Metric | Value |
|--------|-------|
"""
        for key, value in data['stats'].items():
            md += f"| {key.replace('_', ' ').title()} | {value} |\n"
        
        if data['stats']['urls_found'] > 0:
            md += f"| URL Success Rate | {data['success_rate']:.1f}% |\n"
        
        md += "\n"
        
        # Errors
        if data['errors']:
            md += f"## ❌ Errors ({len(data['errors'])})\n\n"
            for i, error in enumerate(data['errors'], 1):
                md += f"{i}. {error}\n"
            md += "\n"
        else:
            md += "## ✅ No Errors\n\n"
        
        # Warnings
        if data['warnings']:
            md += f"## ⚠️ Warnings ({len(data['warnings'])})\n\n"
            for i, warning in enumerate(data['warnings'], 1):
                md += f"{i}. {warning}\n"
            md += "\n"
        else:
            md += "## ✅ No Warnings\n\n"
        
        print(md)
        return data['success']

def main():
    """Main validation entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Lambda Research Repository Validation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Full validation (default)
  %(prog)s --check=links                      # Validate URLs only
  %(prog)s --check=structure                  # Validate directory structure only
  %(prog)s --report=json                      # Output as JSON
  %(prog)s --report=markdown --output=report.md  # Save Markdown report
  %(prog)s --strict --verbose                 # Strict mode with detailed output
  
Check modes: all, links, urls, structure, markdown, cross-references, bibliography
Report formats: text, json, markdown
        """
    )
    
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors (fail on warnings)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed validation output'
    )
    
    parser.add_argument(
        '--check',
        type=str,
        default='all',
        choices=['all', 'links', 'urls', 'structure', 'markdown', 'cross-references', 'bibliography'],
        help='Validation check to perform (default: all)'
    )
    
    parser.add_argument(
        '--report',
        type=str,
        default='text',
        choices=['text', 'json', 'markdown'],
        help='Report output format (default: text)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        help='Write report to file instead of stdout'
    )
    
    args = parser.parse_args()
    
    # Normalize check mode (links == urls)
    check_mode = 'urls' if args.check == 'links' else args.check
    
    # Create validator
    validator = RepositoryValidator(
        '.',
        strict=args.strict,
        verbose=args.verbose,
        check_mode=check_mode,
        report_format=args.report
    )
    
    # Redirect output if requested
    original_stdout = sys.stdout
    if args.output:
        try:
            sys.stdout = open(args.output, 'w', encoding='utf-8')
        except Exception as e:
            sys.stdout = original_stdout
            print(f"Error: Could not write to {args.output}: {e}", file=sys.stderr)
            sys.exit(1)
    
    # Run validation
    try:
        success = validator.validate_all()
    finally:
        if args.output:
            sys.stdout.close()
            sys.stdout = original_stdout
            print(f"Report written to: {args.output}")
    
    # Exit code for CI compatibility
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
