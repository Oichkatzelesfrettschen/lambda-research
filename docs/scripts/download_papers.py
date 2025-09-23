#!/usr/bin/env python3
"""
Lambda Calculus Papers Archive - Automated Paper Download Script

This script downloads open access papers from various sources including:
- arXiv preprints
- Author homepages
- Institutional repositories
- Historical archives

Respects copyright, rate limiting, and fair use policies.
"""

import os
import sys
import json
import time
import requests
import argparse
from pathlib import Path
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PaperDownloader:
    """Handles downloading papers with respect for copyright and rate limiting."""

    def __init__(self, base_dir: str, config_file: str):
        self.base_dir = Path(base_dir)
        self.config_file = Path(config_file)
        self.session = requests.Session()

        # Load configuration
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

        # Set user agent for ethical scraping
        self.session.headers.update({
            'User-Agent': self.config.get('download_policies', {}).get(
                'user_agent',
                'Lambda Research Archive Bot (Academic Use)'
            )
        })

        # Rate limiting configuration
        self.rate_limits = self.config.get('download_policies', {}).get('rate_limiting', {})
        self.last_request_time = {}

    def _respect_rate_limit(self, domain: str) -> None:
        """Implement rate limiting for ethical downloading."""
        rate_limit = self.rate_limits.get(domain, self.rate_limits.get('general', 5))

        if domain in self.last_request_time:
            elapsed = time.time() - self.last_request_time[domain]
            if elapsed < rate_limit:
                sleep_time = rate_limit - elapsed
                logger.info(f"Rate limiting: sleeping {sleep_time:.1f}s for {domain}")
                time.sleep(sleep_time)

        self.last_request_time[domain] = time.time()

    def _get_domain(self, url: str) -> str:
        """Extract domain from URL for rate limiting."""
        return urlparse(url).netloc

    def _download_file(self, url: str, output_path: Path, max_retries: int = 3) -> bool:
        """Download a single file with retry logic."""
        domain = self._get_domain(url)
        self._respect_rate_limit(domain)

        retry_policy = self.config.get('download_policies', {}).get('retry_policy', {})
        backoff_factor = retry_policy.get('backoff_factor', 2)

        for attempt in range(max_retries):
            try:
                logger.info(f"Downloading {url} (attempt {attempt + 1}/{max_retries})")

                response = self.session.get(url, timeout=30)
                response.raise_for_status()

                # Check if response is actually a PDF
                content_type = response.headers.get('content-type', '').lower()
                if 'pdf' not in content_type and not url.endswith('.pdf'):
                    logger.warning(f"Response may not be PDF: {content_type}")

                # Ensure output directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Write file
                with open(output_path, 'wb') as f:
                    f.write(response.content)

                logger.info(f"Successfully downloaded to {output_path}")
                return True

            except requests.exceptions.RequestException as e:
                logger.error(f"Download failed (attempt {attempt + 1}): {e}")
                if attempt < max_retries - 1:
                    sleep_time = backoff_factor ** attempt
                    logger.info(f"Retrying in {sleep_time}s...")
                    time.sleep(sleep_time)

        logger.error(f"Failed to download {url} after {max_retries} attempts")
        return False

    def _download_arxiv_paper(self, arxiv_id: str, output_path: Path) -> bool:
        """Download paper from arXiv using the PDF API."""
        arxiv_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        return self._download_file(arxiv_url, output_path)

    def download_paper(self, paper_info: Dict) -> bool:
        """Download a single paper based on its information."""
        url = paper_info.get('url')
        local_path = paper_info.get('local_path')
        access_type = paper_info.get('access_type')

        if not url or not local_path:
            logger.error(f"Missing URL or local_path for paper: {paper_info.get('title', 'Unknown')}")
            return False

        output_path = self.base_dir / local_path

        # Check if file already exists
        if output_path.exists():
            logger.info(f"File already exists: {output_path}")
            return True

        # Handle arXiv papers specially
        if access_type == 'AR' and 'arxiv_id' in paper_info:
            arxiv_id = paper_info['arxiv_id']
            return self._download_arxiv_paper(arxiv_id, output_path)

        # Handle regular downloads
        return self._download_file(url, output_path)

    def download_category(self, category: str) -> Tuple[int, int]:
        """Download all papers in a specific category."""
        papers = self.config.get('download_sources', {}).get(category, {})

        if not papers:
            logger.warning(f"No papers found in category: {category}")
            return 0, 0

        logger.info(f"Downloading {len(papers)} papers from category: {category}")

        success_count = 0
        total_count = len(papers)

        for paper_id, paper_info in papers.items():
            logger.info(f"Processing: {paper_info.get('title', paper_id)}")

            if self.download_paper(paper_info):
                success_count += 1
            else:
                logger.error(f"Failed to download: {paper_id}")

        logger.info(f"Category {category}: {success_count}/{total_count} successful downloads")
        return success_count, total_count

    def download_all(self, priorities: Optional[List[str]] = None) -> Dict[str, Tuple[int, int]]:
        """Download all papers, optionally filtered by priority."""
        download_sources = self.config.get('download_sources', {})
        results = {}

        if priorities:
            # Filter papers by priority
            filtered_sources = {}
            for category, papers in download_sources.items():
                filtered_papers = {
                    pid: pinfo for pid, pinfo in papers.items()
                    if pinfo.get('download_priority') in priorities
                }
                if filtered_papers:
                    filtered_sources[category] = filtered_papers
            download_sources = filtered_sources

        for category in download_sources:
            success, total = self.download_category(category)
            results[category] = (success, total)

        return results

    def verify_downloads(self) -> Dict[str, Dict[str, bool]]:
        """Verify that downloaded files exist and are valid."""
        verification_results = {}

        for category, papers in self.config.get('download_sources', {}).items():
            verification_results[category] = {}

            for paper_id, paper_info in papers.items():
                local_path = self.base_dir / paper_info.get('local_path', '')

                if local_path.exists():
                    # Basic validation: check file size
                    file_size = local_path.stat().st_size
                    if file_size > 1000:  # Assume valid PDFs are > 1KB
                        verification_results[category][paper_id] = True
                    else:
                        verification_results[category][paper_id] = False
                        logger.warning(f"Suspicious file size for {paper_id}: {file_size} bytes")
                else:
                    verification_results[category][paper_id] = False

        return verification_results


def main():
    """Main entry point for the download script."""
    parser = argparse.ArgumentParser(description='Download lambda calculus papers')
    parser.add_argument('--config', '-c',
                       default='metadata/download_sources.json',
                       help='Configuration file path')
    parser.add_argument('--output', '-o',
                       default='.',
                       help='Output directory (default: current directory)')
    parser.add_argument('--category',
                       help='Download only specific category')
    parser.add_argument('--priority',
                       choices=['high', 'medium', 'low'],
                       help='Download only papers with specific priority')
    parser.add_argument('--verify', action='store_true',
                       help='Verify existing downloads instead of downloading')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be downloaded without downloading')

    args = parser.parse_args()

    # Convert relative paths to absolute
    if Path(args.config).is_absolute():
        config_path = Path(args.config)
    else:
        # If relative, try both from current dir and from script dir
        config_path = Path(args.config)
        if not config_path.exists():
            script_dir = Path(__file__).parent
            config_path = script_dir / args.config

    output_dir = Path(args.output).resolve()

    if not config_path.exists():
        logger.error(f"Configuration file not found: {config_path}")
        sys.exit(1)

    downloader = PaperDownloader(output_dir, config_path)

    if args.verify:
        logger.info("Verifying existing downloads...")
        results = downloader.verify_downloads()

        total_papers = 0
        valid_papers = 0

        for category, papers in results.items():
            category_total = len(papers)
            category_valid = sum(papers.values())
            total_papers += category_total
            valid_papers += category_valid

            logger.info(f"{category}: {category_valid}/{category_total} valid")

        logger.info(f"Overall: {valid_papers}/{total_papers} papers verified")

    elif args.dry_run:
        logger.info("Dry run mode - showing what would be downloaded:")

        if args.category:
            papers = downloader.config.get('download_sources', {}).get(args.category, {})
            logger.info(f"Category {args.category}: {len(papers)} papers")
            for paper_id, paper_info in papers.items():
                logger.info(f"  - {paper_info.get('title', paper_id)}")
        else:
            priorities = [args.priority] if args.priority else None
            for category, papers in downloader.config.get('download_sources', {}).items():
                if priorities:
                    papers = {
                        pid: pinfo for pid, pinfo in papers.items()
                        if pinfo.get('download_priority') in priorities
                    }
                if papers:
                    logger.info(f"Category {category}: {len(papers)} papers")

    else:
        if args.category:
            success, total = downloader.download_category(args.category)
            logger.info(f"Downloaded {success}/{total} papers from {args.category}")
        else:
            priorities = [args.priority] if args.priority else None
            results = downloader.download_all(priorities)

            total_success = sum(s for s, t in results.values())
            total_papers = sum(t for s, t in results.values())

            logger.info(f"Overall download results: {total_success}/{total_papers} successful")
            for category, (success, total) in results.items():
                logger.info(f"  {category}: {success}/{total}")


if __name__ == '__main__':
    main()