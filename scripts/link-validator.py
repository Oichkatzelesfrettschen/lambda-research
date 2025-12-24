#!/usr/bin/env python3
"""
Lambda Research Repository - Link Validator
Validates all external links in bibliography files and generates a report.
"""

import re
import requests
import time
from pathlib import Path
from urllib.parse import urlparse
import json
from datetime import datetime

def extract_links_from_md(file_path):
    """Extract all HTTP/HTTPS links from a markdown file."""
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find HTTP/HTTPS URLs
        url_pattern = r'https?://[^\s\)]+[^\s\.\,\)\>\]]*'
        matches = re.findall(url_pattern, content)

        for match in matches:
            # Clean up common markdown artifacts
            url = match.rstrip('.,;:)]}>*')
            if url.endswith('*'):
                url = url[:-1]
            links.append(url)

    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return links

def validate_url(url, timeout=10):
    """Validate a single URL and return status info."""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return {
            'status': 'OK',
            'status_code': response.status_code,
            'final_url': response.url,
            'redirected': response.url != url
        }
    except requests.exceptions.Timeout:
        return {'status': 'TIMEOUT', 'error': 'Request timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': 'CONNECTION_ERROR', 'error': 'Connection failed'}
    except requests.exceptions.RequestException as e:
        return {'status': 'ERROR', 'error': str(e)}
    except Exception as e:
        return {'status': 'UNKNOWN_ERROR', 'error': str(e)}

def main():
    """Main validation function."""
    print("Lambda Research Repository - Link Validator")
    print("=" * 50)

    # Find all bibliography files
    bib_files = list(Path('.').glob('**/bibliography.md'))
    print(f"Found {len(bib_files)} bibliography files")

    all_links = {}
    broken_links = []
    working_links = []

    # Extract links from each file
    for bib_file in bib_files:
        print(f"\nProcessing: {bib_file}")
        links = extract_links_from_md(bib_file)
        if links:
            all_links[str(bib_file)] = links
            print(f"  Found {len(links)} links")

    # Validate all unique links
    unique_links = set()
    for links in all_links.values():
        unique_links.update(links)

    print(f"\nValidating {len(unique_links)} unique links...")
    print("-" * 50)

    validation_results = {}
    for i, url in enumerate(sorted(unique_links), 1):
        print(f"[{i}/{len(unique_links)}] Checking: {url[:60]}...")

        result = validate_url(url)
        validation_results[url] = result

        if result['status'] == 'OK' and 200 <= result.get('status_code', 0) < 400:
            working_links.append(url)
            status = "[OK] OK"
            if result.get('redirected'):
                status += f" (redirected to {result['final_url'][:50]}...)"
        else:
            broken_links.append((url, result))
            status = f"[FAIL] {result['status']}"
            if 'error' in result:
                status += f": {result['error'][:30]}..."

        print(f"    {status}")

        # Rate limiting
        time.sleep(0.5)

    # Generate report
    print(f"\n{'='*50}")
    print("VALIDATION SUMMARY")
    print(f"{'='*50}")
    print(f"Total unique links: {len(unique_links)}")
    print(f"Working links: {len(working_links)} ({len(working_links)/len(unique_links)*100:.1f}%)")
    print(f"Broken links: {len(broken_links)} ({len(broken_links)/len(unique_links)*100:.1f}%)")

    if broken_links:
        print(f"\n{'='*50}")
        print("BROKEN LINKS REPORT")
        print(f"{'='*50}")
        for url, result in broken_links:
            print(f"\n[FAIL] {url}")
            print(f"   Status: {result['status']}")
            if 'error' in result:
                print(f"   Error: {result['error']}")
            if 'status_code' in result:
                print(f"   HTTP Code: {result['status_code']}")

    # Save detailed report
    report = {
        'timestamp': datetime.now().isoformat(),
        'summary': {
            'total_links': len(unique_links),
            'working_links': len(working_links),
            'broken_links': len(broken_links),
            'success_rate': len(working_links)/len(unique_links)*100
        },
        'files_scanned': list(all_links.keys()),
        'validation_results': validation_results,
        'broken_links': [{'url': url, 'result': result} for url, result in broken_links]
    }

    with open('link-validation-report.json', 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\nDetailed report saved to: link-validation-report.json")
    return len(broken_links)

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)