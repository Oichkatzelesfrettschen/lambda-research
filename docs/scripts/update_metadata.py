#!/usr/bin/env python3
"""
update_metadata.py

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
Lambda Calculus Papers Archive - Metadata Update Script

Maintains synchronization between BibTeX, JSON metadata, and actual files.
Updates citation indices and validates metadata consistency.
"""

import os
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Set
import logging
import re
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MetadataManager:
    """Manages metadata synchronization and validation."""

    def __init__(self, archive_dir: str):
        self.archive_dir = Path(archive_dir)
        self.metadata_dir = self.archive_dir / 'metadata'

        # Load existing metadata files
        self.load_metadata()

    def load_metadata(self) -> None:
        """Load all metadata files."""
        try:
            with open(self.metadata_dir / 'download_sources.json', 'r') as f:
                self.download_sources = json.load(f)
        except FileNotFoundError:
            logger.warning("download_sources.json not found")
            self.download_sources = {}

        try:
            with open(self.metadata_dir / 'author_index.json', 'r') as f:
                self.author_index = json.load(f)
        except FileNotFoundError:
            logger.warning("author_index.json not found")
            self.author_index = {}

        try:
            with open(self.metadata_dir / 'topic_tags.json', 'r') as f:
                self.topic_tags = json.load(f)
        except FileNotFoundError:
            logger.warning("topic_tags.json not found")
            self.topic_tags = {}

    def scan_files(self) -> Dict[str, List[Path]]:
        """Scan archive directories for actual files."""
        file_inventory = {}

        # Define the main categories
        categories = ['historical', 'classical', 'modern', 'recent', 'surveys']

        for category in categories:
            category_path = self.archive_dir / category
            if category_path.exists():
                file_inventory[category] = []
                for pdf_file in category_path.rglob('*.pdf'):
                    file_inventory[category].append(pdf_file.relative_to(self.archive_dir))

        return file_inventory

    def validate_file_existence(self) -> Dict[str, Dict[str, bool]]:
        """Check if files referenced in metadata actually exist."""
        validation_results = {}

        for category, papers in self.download_sources.get('download_sources', {}).items():
            validation_results[category] = {}

            for paper_id, paper_info in papers.items():
                local_path = paper_info.get('local_path')
                if local_path:
                    file_path = self.archive_dir / local_path
                    validation_results[category][paper_id] = file_path.exists()
                else:
                    validation_results[category][paper_id] = False

        return validation_results

    def extract_bibtex_entries(self) -> Dict[str, Dict]:
        """Parse BibTeX file and extract entries."""
        bibtex_file = self.metadata_dir / 'bibliography.bib'

        if not bibtex_file.exists():
            logger.error("bibliography.bib not found")
            return {}

        entries = {}

        with open(bibtex_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple regex to extract BibTeX entries
        # This is a basic parser - for production use, consider using a proper BibTeX library
        entry_pattern = r'@(\w+)\{([^,]+),\s*(.*?)\n\}'
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}'

        for match in re.finditer(entry_pattern, content, re.DOTALL):
            entry_type = match.group(1)
            entry_key = match.group(2)
            fields_text = match.group(3)

            entry = {
                'type': entry_type,
                'key': entry_key,
                'fields': {}
            }

            # Extract fields
            for field_match in re.finditer(field_pattern, fields_text):
                field_name = field_match.group(1)
                field_value = field_match.group(2)
                entry['fields'][field_name] = field_value

            entries[entry_key] = entry

        return entries

    def generate_citation_report(self) -> Dict:
        """Generate comprehensive citation and coverage report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {},
            'file_coverage': {},
            'metadata_consistency': {},
            'missing_files': [],
            'orphaned_files': []
        }

        # Get file inventory
        file_inventory = self.scan_files()
        total_files = sum(len(files) for files in file_inventory.values())

        # Get metadata coverage
        metadata_papers = 0
        for category in self.download_sources.get('download_sources', {}).values():
            metadata_papers += len(category)

        report['summary'] = {
            'total_files_on_disk': total_files,
            'total_papers_in_metadata': metadata_papers,
            'categories': list(file_inventory.keys())
        }

        # File coverage analysis
        validation_results = self.validate_file_existence()
        for category, papers in validation_results.items():
            total_in_category = len(papers)
            valid_in_category = sum(papers.values())
            report['file_coverage'][category] = {
                'total_referenced': total_in_category,
                'files_exist': valid_in_category,
                'coverage_percentage': (valid_in_category / total_in_category * 100) if total_in_category > 0 else 0
            }

            # Track missing files
            for paper_id, exists in papers.items():
                if not exists:
                    paper_info = self.download_sources.get('download_sources', {}).get(category, {}).get(paper_id, {})
                    report['missing_files'].append({
                        'category': category,
                        'paper_id': paper_id,
                        'title': paper_info.get('title', 'Unknown'),
                        'local_path': paper_info.get('local_path', 'Unknown')
                    })

        # Find orphaned files (files on disk not in metadata)
        referenced_files = set()
        for category, papers in self.download_sources.get('download_sources', {}).items():
            for paper_info in papers.values():
                local_path = paper_info.get('local_path')
                if local_path:
                    referenced_files.add(Path(local_path))

        for category, files in file_inventory.items():
            for file_path in files:
                if file_path not in referenced_files:
                    report['orphaned_files'].append({
                        'category': category,
                        'file_path': str(file_path)
                    })

        return report

    def update_citation_index(self) -> None:
        """Update the citation index markdown file."""
        bibtex_entries = self.extract_bibtex_entries()

        # Generate updated citation index
        citation_index_path = self.archive_dir / 'CITATION_INDEX.md'

        # This would regenerate the citation index based on current metadata
        # For now, we'll just log that it should be updated
        logger.info(f"Citation index should be updated with {len(bibtex_entries)} entries")

    def check_arxiv_updates(self) -> List[Dict]:
        """Check for updates to arXiv papers."""
        updates_needed = []

        for category, papers in self.download_sources.get('download_sources', {}).items():
            if category == 'recent_arxiv':
                for paper_id, paper_info in papers.items():
                    arxiv_id = paper_info.get('arxiv_id')
                    if arxiv_id:
                        # In a real implementation, this would check arXiv API for updates
                        # For now, just note papers that could be checked
                        updates_needed.append({
                            'paper_id': paper_id,
                            'arxiv_id': arxiv_id,
                            'title': paper_info.get('title', 'Unknown'),
                            'current_version': paper_info.get('version', 'v1')
                        })

        return updates_needed

    def validate_metadata_consistency(self) -> Dict[str, List[str]]:
        """Check for consistency issues in metadata."""
        issues = {
            'missing_local_paths': [],
            'invalid_access_types': [],
            'missing_titles': [],
            'invalid_years': []
        }

        valid_access_types = {'OA', 'AP', 'PD', 'IR', 'AR'}

        for category, papers in self.download_sources.get('download_sources', {}).items():
            for paper_id, paper_info in papers.items():
                # Check for missing local paths
                if not paper_info.get('local_path'):
                    issues['missing_local_paths'].append(f"{category}/{paper_id}")

                # Check for invalid access types
                access_type = paper_info.get('access_type')
                if access_type and access_type not in valid_access_types:
                    issues['invalid_access_types'].append(f"{category}/{paper_id}: {access_type}")

                # Check for missing titles
                if not paper_info.get('title'):
                    issues['missing_titles'].append(f"{category}/{paper_id}")

                # Check for invalid years
                year = paper_info.get('year')
                if year and (not isinstance(year, int) or year < 1900 or year > 2030):
                    issues['invalid_years'].append(f"{category}/{paper_id}: {year}")

        return issues

    def save_metadata(self) -> None:
        """Save updated metadata back to files."""
        # Save download sources
        with open(self.metadata_dir / 'download_sources.json', 'w') as f:
            json.dump(self.download_sources, f, indent=2)

        # Save author index
        with open(self.metadata_dir / 'author_index.json', 'w') as f:
            json.dump(self.author_index, f, indent=2)

        # Save topic tags
        with open(self.metadata_dir / 'topic_tags.json', 'w') as f:
            json.dump(self.topic_tags, f, indent=2)

        logger.info("Metadata files updated")


def main():
    """Main entry point for metadata update script."""
    parser = argparse.ArgumentParser(description='Update papers archive metadata')
    parser.add_argument('--archive-dir', '-d',
                       default='.',
                       help='Archive directory (default: current directory)')
    parser.add_argument('--report', action='store_true',
                       help='Generate comprehensive metadata report')
    parser.add_argument('--validate', action='store_true',
                       help='Validate metadata consistency')
    parser.add_argument('--check-arxiv', action='store_true',
                       help='Check for arXiv paper updates')
    parser.add_argument('--update-index', action='store_true',
                       help='Update citation index')
    parser.add_argument('--output', '-o',
                       help='Output file for reports')

    args = parser.parse_args()

    archive_dir = Path(args.archive_dir).resolve()
    manager = MetadataManager(archive_dir)

    if args.report:
        logger.info("Generating comprehensive metadata report...")
        report = manager.generate_citation_report()

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Report saved to {args.output}")
        else:
            print(json.dumps(report, indent=2))

    if args.validate:
        logger.info("Validating metadata consistency...")
        issues = manager.validate_metadata_consistency()

        total_issues = sum(len(issue_list) for issue_list in issues.values())
        if total_issues == 0:
            logger.info("No metadata consistency issues found")
        else:
            logger.warning(f"Found {total_issues} metadata issues:")
            for issue_type, issue_list in issues.items():
                if issue_list:
                    logger.warning(f"  {issue_type}: {len(issue_list)} issues")
                    for issue in issue_list[:5]:  # Show first 5 issues
                        logger.warning(f"    - {issue}")
                    if len(issue_list) > 5:
                        logger.warning(f"    ... and {len(issue_list) - 5} more")

    if args.check_arxiv:
        logger.info("Checking for arXiv updates...")
        updates = manager.check_arxiv_updates()

        if updates:
            logger.info(f"Found {len(updates)} arXiv papers to check for updates:")
            for update in updates:
                logger.info(f"  - {update['title']} ({update['arxiv_id']})")
        else:
            logger.info("No arXiv papers found in metadata")

    if args.update_index:
        logger.info("Updating citation index...")
        manager.update_citation_index()


if __name__ == '__main__':
    main()