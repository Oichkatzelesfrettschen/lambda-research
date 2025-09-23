#!/usr/bin/env python3
"""
Lambda Calculus Papers Archive - Index Generation Script

Generates searchable indices, bibliography listings, and cross-reference tables
from metadata and downloaded papers.
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Set
import logging
from datetime import datetime
from collections import defaultdict
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class IndexGenerator:
    """Generates various indices and cross-references for the papers archive."""

    def __init__(self, archive_dir: str):
        self.archive_dir = Path(archive_dir)
        self.metadata_dir = self.archive_dir / 'metadata'

        # Load metadata
        self.load_metadata()

    def load_metadata(self) -> None:
        """Load all metadata files."""
        with open(self.metadata_dir / 'download_sources.json', 'r') as f:
            self.download_sources = json.load(f)

        with open(self.metadata_dir / 'author_index.json', 'r') as f:
            self.author_index = json.load(f)

        with open(self.metadata_dir / 'topic_tags.json', 'r') as f:
            self.topic_tags = json.load(f)

    def extract_bibtex_info(self) -> Dict:
        """Extract information from BibTeX file."""
        bibtex_file = self.metadata_dir / 'bibliography.bib'
        bibtex_entries = {}

        if not bibtex_file.exists():
            logger.warning("bibliography.bib not found")
            return {}

        with open(bibtex_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple BibTeX parser
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

            bibtex_entries[entry_key] = entry

        return bibtex_entries

    def generate_author_index_md(self) -> str:
        """Generate markdown author index."""
        authors = self.author_index.get('authors', {})

        md_content = [
            "# Author Index",
            "",
            "Comprehensive index of authors in the lambda calculus papers archive.",
            "",
            "## Quick Navigation",
            ""
        ]

        # Generate alphabetical navigation
        first_letters = sorted(set(author.split(',')[0][0].upper() for author in authors.keys()))
        nav_links = [f"[{letter}](#{letter.lower()})" for letter in first_letters]
        md_content.append(" | ".join(nav_links))
        md_content.append("")

        # Group authors by first letter
        authors_by_letter = defaultdict(list)
        for author_name in sorted(authors.keys()):
            first_letter = author_name.split(',')[0][0].upper()
            authors_by_letter[first_letter].append(author_name)

        # Generate author entries
        for letter in first_letters:
            md_content.append(f"## {letter}")
            md_content.append("")

            for author_name in authors_by_letter[letter]:
                author_info = authors[author_name]
                md_content.append(f"### {author_name}")

                # Basic info
                if 'birth_year' in author_info:
                    birth_year = author_info['birth_year']
                    death_year = author_info.get('death_year', 'present')
                    md_content.append(f"**Lifespan**: {birth_year}–{death_year}")

                if 'affiliation' in author_info:
                    md_content.append(f"**Affiliation**: {author_info['affiliation']}")

                # Major contributions
                if 'major_contributions' in author_info:
                    md_content.append("**Major Contributions**:")
                    for contribution in author_info['major_contributions']:
                        md_content.append(f"- {contribution}")

                # Papers in archive
                if 'papers_in_archive' in author_info:
                    md_content.append("**Papers in Archive**:")
                    for paper in author_info['papers_in_archive']:
                        year = paper.get('year', 'Unknown')
                        title = paper.get('title', 'Untitled')
                        path = paper.get('path', '')
                        coauthors = paper.get('coauthors', [])

                        if coauthors:
                            coauthor_str = f" (with {', '.join(coauthors)})"
                        else:
                            coauthor_str = ""

                        md_content.append(f"- **{year}**: [{title}]({path}){coauthor_str}")

                        if 'significance' in paper:
                            md_content.append(f"  - *{paper['significance']}*")

                # External resources
                if 'external_resources' in author_info:
                    md_content.append("**External Resources**:")
                    for resource_name, url in author_info['external_resources'].items():
                        resource_display = resource_name.replace('_', ' ').title()
                        md_content.append(f"- [{resource_display}]({url})")

                md_content.append("")

        return "\n".join(md_content)

    def generate_topic_index_md(self) -> str:
        """Generate markdown topic index."""
        taxonomy = self.topic_tags.get('topic_taxonomy', {})

        md_content = [
            "# Topic Index",
            "",
            "Comprehensive topic classification for lambda calculus research.",
            "",
        ]

        for category, subcategories in taxonomy.items():
            category_title = category.replace('_', ' ').title()
            md_content.append(f"## {category_title}")
            md_content.append("")

            for subcategory, topics in subcategories.items():
                subcategory_title = subcategory.replace('_', ' ').title()
                md_content.append(f"### {subcategory_title}")
                md_content.append("")

                for topic in topics:
                    md_content.append(f"- {topic}")

                md_content.append("")

        # Add cross-references
        cross_refs = self.topic_tags.get('cross_references', {})
        if cross_refs:
            md_content.append("## Cross-References")
            md_content.append("")

            for topic, refs in cross_refs.items():
                topic_title = topic.replace('_', ' ').title()
                md_content.append(f"### {topic_title}")

                if 'related_topics' in refs:
                    md_content.append("**Related Topics**:")
                    for related in refs['related_topics']:
                        md_content.append(f"- {related.replace('_', ' ').title()}")

                if 'foundational_papers' in refs:
                    md_content.append("**Foundational Papers**:")
                    for paper in refs['foundational_papers']:
                        md_content.append(f"- {paper}")

                md_content.append("")

        return "\n".join(md_content)

    def generate_chronological_index_md(self) -> str:
        """Generate chronological index of papers."""
        papers_by_year = defaultdict(list)

        # Collect all papers from download sources
        for category, papers in self.download_sources.get('download_sources', {}).items():
            for paper_id, paper_info in papers.items():
                year = paper_info.get('year', 0)
                papers_by_year[year].append({
                    'category': category,
                    'paper_id': paper_id,
                    'info': paper_info
                })

        md_content = [
            "# Chronological Index",
            "",
            "Papers organized by publication year, showing the evolution of lambda calculus research.",
            "",
        ]

        # Sort years and generate entries
        for year in sorted(papers_by_year.keys(), reverse=True):
            if year == 0:
                continue  # Skip papers without year

            md_content.append(f"## {year}")
            md_content.append("")

            for paper in sorted(papers_by_year[year], key=lambda p: p['info'].get('title', '')):
                info = paper['info']
                title = info.get('title', 'Untitled')
                author = info.get('author', 'Unknown Author')
                local_path = info.get('local_path', '')
                access_type = info.get('access_type', 'Unknown')

                md_content.append(f"**[{title}]({local_path})**")
                md_content.append(f"*{author}* | Access: {access_type}")

                if 'url' in info:
                    md_content.append(f"Source: {info['url']}")

                if 'notes' in info:
                    md_content.append(f"*{info['notes']}*")

                md_content.append("")

        return "\n".join(md_content)

    def generate_access_type_index_md(self) -> str:
        """Generate index organized by access type."""
        papers_by_access = defaultdict(list)

        # Collect papers by access type
        for category, papers in self.download_sources.get('download_sources', {}).items():
            for paper_id, paper_info in papers.items():
                access_type = paper_info.get('access_type', 'Unknown')
                papers_by_access[access_type].append({
                    'category': category,
                    'paper_id': paper_id,
                    'info': paper_info
                })

        access_type_names = {
            'OA': 'Open Access',
            'AP': 'Author Permission',
            'PD': 'Public Domain',
            'IR': 'Institutional Repository',
            'AR': 'arXiv Preprints'
        }

        md_content = [
            "# Access Type Index",
            "",
            "Papers organized by their access classification and availability.",
            "",
            "## Access Type Legend",
            "",
            "- **OA**: Open Access (freely available online)",
            "- **AP**: Author Permission (personal copies with permission)",
            "- **PD**: Public Domain (historical works, expired copyright)",
            "- **IR**: Institutional Repository (university archives)",
            "- **AR**: arXiv Preprints (e-print archives)",
            "",
        ]

        # Generate entries for each access type
        for access_code in ['OA', 'PD', 'AR', 'IR', 'AP']:
            if access_code not in papers_by_access:
                continue

            access_name = access_type_names[access_code]
            papers = papers_by_access[access_code]

            md_content.append(f"## {access_name} ({access_code})")
            md_content.append(f"*{len(papers)} papers*")
            md_content.append("")

            for paper in sorted(papers, key=lambda p: (p['info'].get('year', 0), p['info'].get('title', ''))):
                info = paper['info']
                title = info.get('title', 'Untitled')
                author = info.get('author', 'Unknown Author')
                year = info.get('year', 'Unknown')
                local_path = info.get('local_path', '')

                md_content.append(f"**[{title}]({local_path})** ({year})")
                md_content.append(f"*{author}*")

                if 'url' in info:
                    md_content.append(f"Source: [{info['url']}]({info['url']})")

                md_content.append("")

        return "\n".join(md_content)

    def generate_readme_sections(self) -> Dict[str, str]:
        """Generate sections for updating the main README."""
        total_papers = 0
        papers_by_category = {}

        for category, papers in self.download_sources.get('download_sources', {}).items():
            papers_by_category[category] = len(papers)
            total_papers += len(papers)

        statistics = {
            'total_papers': total_papers,
            'by_category': papers_by_category,
            'last_updated': datetime.now().strftime('%Y-%m-%d')
        }

        # Generate statistics section
        stats_md = [
            "## Archive Statistics",
            "",
            f"**Total Papers**: {total_papers}",
            f"**Last Updated**: {statistics['last_updated']}",
            "",
            "### By Category",
            ""
        ]

        for category, count in papers_by_category.items():
            category_name = category.replace('_', ' ').title()
            stats_md.append(f"- **{category_name}**: {count} papers")

        return {
            'statistics': "\n".join(stats_md),
            'metadata': statistics
        }

    def save_index(self, content: str, filename: str) -> None:
        """Save generated index to file."""
        output_path = self.archive_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(f"Generated index: {output_path}")


def main():
    """Main entry point for index generation."""
    parser = argparse.ArgumentParser(description='Generate papers archive indices')
    parser.add_argument('--archive-dir', '-d',
                       default='.',
                       help='Archive directory (default: current directory)')
    parser.add_argument('--index-type', '-t',
                       choices=['author', 'topic', 'chronological', 'access', 'all'],
                       default='all',
                       help='Type of index to generate')
    parser.add_argument('--output-dir', '-o',
                       help='Output directory (default: archive directory)')

    args = parser.parse_args()

    archive_dir = Path(args.archive_dir).resolve()
    output_dir = Path(args.output_dir).resolve() if args.output_dir else archive_dir

    generator = IndexGenerator(archive_dir)

    # Generate requested indices
    if args.index_type in ['author', 'all']:
        author_index = generator.generate_author_index_md()
        output_path = output_dir / 'AUTHOR_INDEX.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(author_index)
        logger.info(f"Generated author index: {output_path}")

    if args.index_type in ['topic', 'all']:
        topic_index = generator.generate_topic_index_md()
        output_path = output_dir / 'TOPIC_INDEX.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(topic_index)
        logger.info(f"Generated topic index: {output_path}")

    if args.index_type in ['chronological', 'all']:
        chrono_index = generator.generate_chronological_index_md()
        output_path = output_dir / 'CHRONOLOGICAL_INDEX.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(chrono_index)
        logger.info(f"Generated chronological index: {output_path}")

    if args.index_type in ['access', 'all']:
        access_index = generator.generate_access_type_index_md()
        output_path = output_dir / 'ACCESS_TYPE_INDEX.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(access_index)
        logger.info(f"Generated access type index: {output_path}")

    # Always generate README sections
    readme_sections = generator.generate_readme_sections()
    stats_path = output_dir / 'ARCHIVE_STATISTICS.md'
    with open(stats_path, 'w', encoding='utf-8') as f:
        f.write(readme_sections['statistics'])
    logger.info(f"Generated statistics: {stats_path}")

    # Save metadata for programmatic use
    metadata_path = output_dir / 'metadata' / 'generated_statistics.json'
    with open(metadata_path, 'w') as f:
        json.dump(readme_sections['metadata'], f, indent=2)
    logger.info(f"Saved metadata: {metadata_path}")

    logger.info("Index generation completed successfully")


if __name__ == '__main__':
    main()