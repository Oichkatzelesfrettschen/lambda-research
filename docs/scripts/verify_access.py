#!/usr/bin/env python3
"""
verify_access.py

Copyright (C) 2025 Lambda Research Collective

This file is part of Lambda Calculus Research Repository.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


"""
Lambda Calculus Papers Archive - Access Verification Script

Validates URLs, checks for broken links, and verifies open access status.
Helps maintain the integrity of download sources.
"""

import json
import asyncio
import aiohttp
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging
from datetime import datetime
import ssl
import certifi

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AccessVerifier:
    """Verifies URL accessibility and open access status."""

    def __init__(self, config_file: str, max_concurrent: int = 5):
        self.config_file = Path(config_file)
        self.max_concurrent = max_concurrent

        # Load configuration
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

        # SSL context for HTTPS requests
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())

        # Results storage
        self.verification_results = {}

    async def check_url(self, session: aiohttp.ClientSession, url: str,
                       paper_id: str) -> Dict:
        """Check a single URL for accessibility."""
        result = {
            'paper_id': paper_id,
            'url': url,
            'status': 'unknown',
            'status_code': None,
            'content_type': None,
            'content_length': None,
            'redirect_url': None,
            'error': None,
            'timestamp': datetime.now().isoformat()
        }

        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with session.get(url, timeout=timeout, allow_redirects=True) as response:
                result['status_code'] = response.status
                result['content_type'] = response.headers.get('content-type', '')
                result['content_length'] = response.headers.get('content-length')

                # Check for redirects
                if str(response.url) != url:
                    result['redirect_url'] = str(response.url)

                if response.status == 200:
                    # Check if it's actually a PDF
                    content_type = result['content_type'].lower()
                    if 'pdf' in content_type:
                        result['status'] = 'accessible_pdf'
                    elif 'html' in content_type:
                        # Might be a page with PDF link
                        result['status'] = 'accessible_html'
                    else:
                        result['status'] = 'accessible_unknown'
                elif response.status in [301, 302, 303, 307, 308]:
                    result['status'] = 'redirect'
                elif response.status == 404:
                    result['status'] = 'not_found'
                elif response.status in [403, 401]:
                    result['status'] = 'access_denied'
                else:
                    result['status'] = 'error'

        except asyncio.TimeoutError:
            result['status'] = 'timeout'
            result['error'] = 'Request timeout'
        except aiohttp.ClientError as e:
            result['status'] = 'client_error'
            result['error'] = str(e)
        except Exception as e:
            result['status'] = 'unknown_error'
            result['error'] = str(e)

        return result

    async def verify_category(self, category: str, papers: Dict) -> List[Dict]:
        """Verify all URLs in a category."""
        logger.info(f"Verifying {len(papers)} papers in category: {category}")

        connector = aiohttp.TCPConnector(
            limit=self.max_concurrent,
            ssl=self.ssl_context
        )

        headers = {
            'User-Agent': self.config.get('download_policies', {}).get(
                'user_agent',
                'Lambda Research Archive Verifier (Academic Use)'
            )
        }

        async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
            tasks = []

            for paper_id, paper_info in papers.items():
                url = paper_info.get('url')
                if url:
                    task = self.check_url(session, url, paper_id)
                    tasks.append(task)

            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Filter out exceptions and convert to proper results
            valid_results = []
            for result in results:
                if isinstance(result, Exception):
                    logger.error(f"Task failed with exception: {result}")
                else:
                    valid_results.append(result)

            return valid_results

    async def verify_all_sources(self, priorities: Optional[List[str]] = None) -> Dict:
        """Verify all download sources."""
        download_sources = self.config.get('download_sources', {})
        all_results = {}

        for category, papers in download_sources.items():
            # Filter by priority if specified
            if priorities:
                filtered_papers = {
                    pid: pinfo for pid, pinfo in papers.items()
                    if pinfo.get('download_priority') in priorities
                }
                if not filtered_papers:
                    continue
                papers = filtered_papers

            category_results = await self.verify_category(category, papers)
            all_results[category] = category_results

        return all_results

    def analyze_results(self, results: Dict) -> Dict:
        """Analyze verification results and generate summary."""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_urls': 0,
                'accessible': 0,
                'broken': 0,
                'redirect': 0,
                'access_denied': 0,
                'timeout': 0,
                'error': 0
            },
            'by_category': {},
            'issues': [],
            'recommendations': []
        }

        for category, category_results in results.items():
            category_summary = {
                'total': len(category_results),
                'accessible': 0,
                'broken': 0,
                'issues': []
            }

            for result in category_results:
                analysis['summary']['total_urls'] += 1

                status = result.get('status', 'unknown')

                if status in ['accessible_pdf', 'accessible_html', 'accessible_unknown']:
                    analysis['summary']['accessible'] += 1
                    category_summary['accessible'] += 1
                elif status == 'not_found':
                    analysis['summary']['broken'] += 1
                    category_summary['broken'] += 1
                    category_summary['issues'].append({
                        'paper_id': result['paper_id'],
                        'issue': '404 Not Found',
                        'url': result['url']
                    })
                elif status == 'redirect':
                    analysis['summary']['redirect'] += 1
                    # Check if redirect is to a different domain
                    original_domain = result['url'].split('/')[2] if '/' in result['url'] else ''
                    redirect_domain = result.get('redirect_url', '').split('/')[2] if result.get('redirect_url') else ''
                    if original_domain != redirect_domain:
                        category_summary['issues'].append({
                            'paper_id': result['paper_id'],
                            'issue': f'Redirected to different domain: {redirect_domain}',
                            'url': result['url']
                        })
                elif status in ['access_denied']:
                    analysis['summary']['access_denied'] += 1
                    category_summary['issues'].append({
                        'paper_id': result['paper_id'],
                        'issue': 'Access denied',
                        'url': result['url']
                    })
                elif status == 'timeout':
                    analysis['summary']['timeout'] += 1
                    category_summary['issues'].append({
                        'paper_id': result['paper_id'],
                        'issue': 'Request timeout',
                        'url': result['url']
                    })
                else:
                    analysis['summary']['error'] += 1
                    category_summary['issues'].append({
                        'paper_id': result['paper_id'],
                        'issue': f"Error: {status}",
                        'url': result['url'],
                        'error': result.get('error', 'Unknown error')
                    })

                # Check for non-PDF content types
                content_type = result.get('content_type', '').lower()
                if result.get('status_code') == 200 and 'pdf' not in content_type:
                    category_summary['issues'].append({
                        'paper_id': result['paper_id'],
                        'issue': f'Non-PDF content type: {content_type}',
                        'url': result['url']
                    })

            analysis['by_category'][category] = category_summary

            # Add category issues to global issues
            for issue in category_summary['issues']:
                analysis['issues'].append({
                    'category': category,
                    **issue
                })

        # Generate recommendations
        total_urls = analysis['summary']['total_urls']
        broken_pct = (analysis['summary']['broken'] / total_urls * 100) if total_urls > 0 else 0

        if broken_pct > 10:
            analysis['recommendations'].append(
                f"High broken link rate ({broken_pct:.1f}%). Consider updating URLs."
            )

        if analysis['summary']['access_denied'] > 0:
            analysis['recommendations'].append(
                "Some URLs deny access. Check if papers moved or access policies changed."
            )

        if analysis['summary']['timeout'] > 2:
            analysis['recommendations'].append(
                "Multiple timeouts detected. Consider increasing timeout or checking network."
            )

        return analysis

    def save_results(self, results: Dict, analysis: Dict, output_file: str) -> None:
        """Save verification results to file."""
        output_data = {
            'verification_results': results,
            'analysis': analysis
        }

        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)

        logger.info(f"Results saved to {output_file}")


async def main():
    """Main entry point for access verification."""
    parser = argparse.ArgumentParser(description='Verify paper download sources')
    parser.add_argument('--config', '-c',
                       default='metadata/download_sources.json',
                       help='Configuration file path')
    parser.add_argument('--output', '-o',
                       help='Output file for results')
    parser.add_argument('--category',
                       help='Verify only specific category')
    parser.add_argument('--priority',
                       choices=['high', 'medium', 'low'],
                       help='Verify only papers with specific priority')
    parser.add_argument('--concurrent', type=int, default=5,
                       help='Maximum concurrent requests')
    parser.add_argument('--summary-only', action='store_true',
                       help='Show only summary, not detailed results')

    args = parser.parse_args()

    # Convert relative paths to absolute
    script_dir = Path(__file__).parent
    config_path = script_dir / args.config

    if not config_path.exists():
        logger.error(f"Configuration file not found: {config_path}")
        return

    verifier = AccessVerifier(config_path, args.concurrent)

    # Run verification
    priorities = [args.priority] if args.priority else None

    if args.category:
        # Verify specific category
        papers = verifier.config.get('download_sources', {}).get(args.category, {})
        if priorities:
            papers = {
                pid: pinfo for pid, pinfo in papers.items()
                if pinfo.get('download_priority') in priorities
            }

        if papers:
            results = {args.category: await verifier.verify_category(args.category, papers)}
        else:
            logger.error(f"No papers found in category: {args.category}")
            return
    else:
        # Verify all sources
        results = await verifier.verify_all_sources(priorities)

    # Analyze results
    analysis = verifier.analyze_results(results)

    # Output results
    if args.output:
        verifier.save_results(results, analysis, args.output)

    # Print summary
    summary = analysis['summary']
    logger.info(f"Verification Summary:")
    logger.info(f"  Total URLs checked: {summary['total_urls']}")
    logger.info(f"  Accessible: {summary['accessible']} ({summary['accessible']/summary['total_urls']*100:.1f}%)")
    logger.info(f"  Broken: {summary['broken']} ({summary['broken']/summary['total_urls']*100:.1f}%)")
    logger.info(f"  Redirects: {summary['redirect']}")
    logger.info(f"  Access denied: {summary['access_denied']}")
    logger.info(f"  Timeouts: {summary['timeout']}")
    logger.info(f"  Other errors: {summary['error']}")

    if analysis['issues'] and not args.summary_only:
        logger.warning(f"\nFound {len(analysis['issues'])} issues:")
        for issue in analysis['issues'][:10]:  # Show first 10 issues
            logger.warning(f"  {issue['category']}/{issue['paper_id']}: {issue['issue']}")
        if len(analysis['issues']) > 10:
            logger.warning(f"  ... and {len(analysis['issues']) - 10} more issues")

    if analysis['recommendations']:
        logger.info(f"\nRecommendations:")
        for rec in analysis['recommendations']:
            logger.info(f"  - {rec}")


if __name__ == '__main__':
    asyncio.run(main())