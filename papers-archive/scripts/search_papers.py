#!/usr/bin/env python3
"""
Lambda Calculus Papers Archive - Paper Search Utility

Provides full-text search capabilities across metadata, abstracts, and bibliographic information.
Supports boolean queries, faceted search, and relevance ranking.
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import logging
import re
from collections import defaultdict
from dataclasses import dataclass
import math

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class SearchResult:
    """Represents a single search result."""
    paper_id: str
    category: str
    title: str
    author: str
    year: int
    score: float
    matches: List[str]
    local_path: str
    url: str
    access_type: str

class PaperSearcher:
    """Provides search functionality for the papers archive."""

    def __init__(self, archive_dir: str):
        self.archive_dir = Path(archive_dir)
        self.metadata_dir = self.archive_dir / 'metadata'

        # Load metadata
        self.load_metadata()

        # Build search indices
        self.build_indices()

    def load_metadata(self) -> None:
        """Load all metadata files."""
        with open(self.metadata_dir / 'download_sources.json', 'r') as f:
            self.download_sources = json.load(f)

        with open(self.metadata_dir / 'author_index.json', 'r') as f:
            self.author_index = json.load(f)

        with open(self.metadata_dir / 'topic_tags.json', 'r') as f:
            self.topic_tags = json.load(f)

    def build_indices(self) -> None:
        """Build search indices for fast lookup."""
        self.word_index = defaultdict(set)  # word -> set of paper_ids
        self.author_index_lookup = defaultdict(set)  # author -> set of paper_ids
        self.year_index = defaultdict(set)  # year -> set of paper_ids
        self.category_index = defaultdict(set)  # category -> set of paper_ids
        self.access_type_index = defaultdict(set)  # access_type -> set of paper_ids

        # All papers for easy lookup
        self.papers = {}

        for category, papers in self.download_sources.get('download_sources', {}).items():
            for paper_id, paper_info in papers.items():
                # Store paper info
                full_paper_id = f"{category}/{paper_id}"
                self.papers[full_paper_id] = {
                    'category': category,
                    'paper_id': paper_id,
                    **paper_info
                }

                # Index by category
                self.category_index[category].add(full_paper_id)

                # Index by access type
                access_type = paper_info.get('access_type', '')
                if access_type:
                    self.access_type_index[access_type].add(full_paper_id)

                # Index by year
                year = paper_info.get('year')
                if year:
                    self.year_index[year].add(full_paper_id)

                # Index by author
                author = paper_info.get('author', '')
                if author:
                    self.author_index_lookup[author.lower()].add(full_paper_id)
                    # Also index individual author names
                    for author_part in re.split(r'[,;&]', author):
                        author_part = author_part.strip().lower()
                        if author_part:
                            self.author_index_lookup[author_part].add(full_paper_id)

                # Index searchable text
                searchable_text = self.get_searchable_text(paper_info)
                words = self.tokenize(searchable_text)
                for word in words:
                    self.word_index[word.lower()].add(full_paper_id)

    def get_searchable_text(self, paper_info: Dict) -> str:
        """Extract all searchable text from paper info."""
        text_parts = []

        # Add title
        title = paper_info.get('title', '')
        if title:
            text_parts.append(title)

        # Add author
        author = paper_info.get('author', '')
        if author:
            text_parts.append(author)

        # Add notes
        notes = paper_info.get('notes', '')
        if notes:
            text_parts.append(notes)

        # Add keywords if available
        # This would come from a more detailed metadata structure
        # For now, we'll extract from notes or other fields

        return ' '.join(text_parts)

    def tokenize(self, text: str) -> List[str]:
        """Tokenize text into searchable words."""
        # Simple tokenization - remove punctuation and split on whitespace
        text = re.sub(r'[^\w\s-]', ' ', text)
        words = text.split()
        return [word for word in words if len(word) > 2]  # Skip very short words

    def search_words(self, query_words: List[str], operator: str = 'AND') -> Set[str]:
        """Search for papers containing query words."""
        if not query_words:
            return set()

        result_sets = []
        for word in query_words:
            word_lower = word.lower()
            matching_papers = set()

            # Exact word match
            if word_lower in self.word_index:
                matching_papers.update(self.word_index[word_lower])

            # Partial word match (contains)
            for indexed_word in self.word_index:
                if word_lower in indexed_word or indexed_word in word_lower:
                    matching_papers.update(self.word_index[indexed_word])

            result_sets.append(matching_papers)

        # Combine results based on operator
        if operator.upper() == 'AND':
            result = result_sets[0] if result_sets else set()
            for result_set in result_sets[1:]:
                result = result.intersection(result_set)
        else:  # OR
            result = set()
            for result_set in result_sets:
                result = result.union(result_set)

        return result

    def search_author(self, author_query: str) -> Set[str]:
        """Search for papers by author."""
        author_lower = author_query.lower()
        matching_papers = set()

        for indexed_author in self.author_index_lookup:
            if author_lower in indexed_author or indexed_author in author_lower:
                matching_papers.update(self.author_index_lookup[indexed_author])

        return matching_papers

    def search_year_range(self, start_year: Optional[int], end_year: Optional[int]) -> Set[str]:
        """Search for papers in year range."""
        matching_papers = set()

        for year in self.year_index:
            if isinstance(year, int):
                if start_year and year < start_year:
                    continue
                if end_year and year > end_year:
                    continue
                matching_papers.update(self.year_index[year])

        return matching_papers

    def filter_by_category(self, papers: Set[str], categories: List[str]) -> Set[str]:
        """Filter papers by category."""
        if not categories:
            return papers

        filtered = set()
        for category in categories:
            if category in self.category_index:
                filtered.update(self.category_index[category].intersection(papers))

        return filtered

    def filter_by_access_type(self, papers: Set[str], access_types: List[str]) -> Set[str]:
        """Filter papers by access type."""
        if not access_types:
            return papers

        filtered = set()
        for access_type in access_types:
            if access_type in self.access_type_index:
                filtered.update(self.access_type_index[access_type].intersection(papers))

        return filtered

    def calculate_relevance_score(self, paper_id: str, query_words: List[str]) -> Tuple[float, List[str]]:
        """Calculate relevance score for a paper given query words."""
        if paper_id not in self.papers:
            return 0.0, []

        paper_info = self.papers[paper_id]
        searchable_text = self.get_searchable_text(paper_info).lower()

        score = 0.0
        matches = []

        for word in query_words:
            word_lower = word.lower()

            # Count occurrences
            occurrences = searchable_text.count(word_lower)
            if occurrences > 0:
                # TF component (term frequency)
                tf = occurrences / len(self.tokenize(searchable_text))

                # IDF component (inverse document frequency)
                docs_with_word = len(self.word_index.get(word_lower, set()))
                total_docs = len(self.papers)
                idf = math.log(total_docs / (docs_with_word + 1))

                # TF-IDF score
                word_score = tf * idf
                score += word_score

                # Track which fields matched
                title = paper_info.get('title', '').lower()
                author = paper_info.get('author', '').lower()

                if word_lower in title:
                    matches.append(f"title: {word}")
                    score += 2.0  # Boost for title matches
                if word_lower in author:
                    matches.append(f"author: {word}")
                    score += 1.5  # Boost for author matches

        return score, matches

    def search(self,
               query: str = '',
               author: str = '',
               start_year: Optional[int] = None,
               end_year: Optional[int] = None,
               categories: Optional[List[str]] = None,
               access_types: Optional[List[str]] = None,
               max_results: int = 50) -> List[SearchResult]:
        """Perform comprehensive search."""

        # Start with all papers if no query
        if query:
            query_words = self.tokenize(query)
            matching_papers = self.search_words(query_words)
        else:
            matching_papers = set(self.papers.keys())

        # Filter by author
        if author:
            author_papers = self.search_author(author)
            matching_papers = matching_papers.intersection(author_papers)

        # Filter by year range
        if start_year or end_year:
            year_papers = self.search_year_range(start_year, end_year)
            matching_papers = matching_papers.intersection(year_papers)

        # Filter by category
        if categories:
            matching_papers = self.filter_by_category(matching_papers, categories)

        # Filter by access type
        if access_types:
            matching_papers = self.filter_by_access_type(matching_papers, access_types)

        # Calculate relevance scores and create results
        results = []
        query_words = self.tokenize(query) if query else []

        for paper_id in matching_papers:
            paper_info = self.papers[paper_id]

            score, matches = self.calculate_relevance_score(paper_id, query_words)

            result = SearchResult(
                paper_id=paper_info['paper_id'],
                category=paper_info['category'],
                title=paper_info.get('title', 'Untitled'),
                author=paper_info.get('author', 'Unknown'),
                year=paper_info.get('year', 0),
                score=score,
                matches=matches,
                local_path=paper_info.get('local_path', ''),
                url=paper_info.get('url', ''),
                access_type=paper_info.get('access_type', '')
            )
            results.append(result)

        # Sort by relevance score (descending)
        results.sort(key=lambda r: r.score, reverse=True)

        return results[:max_results]

    def get_search_suggestions(self, partial_query: str) -> Dict[str, List[str]]:
        """Get search suggestions based on partial query."""
        suggestions = {
            'words': [],
            'authors': [],
            'categories': [],
            'access_types': []
        }

        partial_lower = partial_query.lower()

        # Word suggestions
        for word in self.word_index:
            if partial_lower in word and len(word) > 3:
                suggestions['words'].append(word)
        suggestions['words'] = sorted(suggestions['words'])[:10]

        # Author suggestions
        for author in self.author_index_lookup:
            if partial_lower in author:
                suggestions['authors'].append(author)
        suggestions['authors'] = sorted(suggestions['authors'])[:10]

        # Category suggestions
        for category in self.category_index:
            if partial_lower in category.lower():
                suggestions['categories'].append(category)

        # Access type suggestions
        for access_type in self.access_type_index:
            if partial_lower in access_type.lower():
                suggestions['access_types'].append(access_type)

        return suggestions


def format_results(results: List[SearchResult], show_scores: bool = False) -> str:
    """Format search results for display."""
    if not results:
        return "No papers found matching your search criteria."

    output_lines = [f"Found {len(results)} papers:"]
    output_lines.append("")

    for i, result in enumerate(results, 1):
        output_lines.append(f"{i}. **{result.title}** ({result.year})")
        output_lines.append(f"   *{result.author}*")
        output_lines.append(f"   Category: {result.category} | Access: {result.access_type}")

        if result.local_path:
            output_lines.append(f"   File: {result.local_path}")

        if result.url:
            output_lines.append(f"   URL: {result.url}")

        if show_scores and result.score > 0:
            output_lines.append(f"   Score: {result.score:.2f}")

        if result.matches:
            output_lines.append(f"   Matches: {', '.join(result.matches)}")

        output_lines.append("")

    return "\n".join(output_lines)


def main():
    """Main entry point for paper search."""
    parser = argparse.ArgumentParser(description='Search lambda calculus papers archive')
    parser.add_argument('--archive-dir', '-d',
                       default='.',
                       help='Archive directory (default: current directory)')
    parser.add_argument('--query', '-q',
                       help='Search query')
    parser.add_argument('--author', '-a',
                       help='Author name to search for')
    parser.add_argument('--start-year', type=int,
                       help='Start year for date range')
    parser.add_argument('--end-year', type=int,
                       help='End year for date range')
    parser.add_argument('--category', '-c', action='append',
                       help='Filter by category (can be used multiple times)')
    parser.add_argument('--access-type', action='append',
                       choices=['OA', 'AP', 'PD', 'IR', 'AR'],
                       help='Filter by access type (can be used multiple times)')
    parser.add_argument('--max-results', '-n', type=int, default=50,
                       help='Maximum number of results to show')
    parser.add_argument('--show-scores', action='store_true',
                       help='Show relevance scores')
    parser.add_argument('--suggestions', '-s',
                       help='Get search suggestions for partial query')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Interactive search mode')

    args = parser.parse_args()

    archive_dir = Path(args.archive_dir).resolve()
    searcher = PaperSearcher(archive_dir)

    if args.suggestions:
        suggestions = searcher.get_search_suggestions(args.suggestions)
        print("Search suggestions:")
        for category, items in suggestions.items():
            if items:
                print(f"\n{category.title()}:")
                for item in items:
                    print(f"  - {item}")
        return

    if args.interactive:
        print("Interactive Search Mode")
        print("Type 'quit' to exit, 'help' for commands")

        while True:
            try:
                query = input("\nSearch> ").strip()

                if query.lower() in ['quit', 'exit', 'q']:
                    break
                elif query.lower() in ['help', 'h']:
                    print("Commands:")
                    print("  <text>                 - Search for text")
                    print("  author:<name>          - Search by author")
                    print("  year:<start>-<end>     - Search by year range")
                    print("  category:<name>        - Filter by category")
                    print("  access:<type>          - Filter by access type")
                    print("  suggestions:<partial>  - Get suggestions")
                    continue
                elif query.lower().startswith('suggestions:'):
                    partial = query[12:].strip()
                    suggestions = searcher.get_search_suggestions(partial)
                    for category, items in suggestions.items():
                        if items:
                            print(f"{category.title()}: {', '.join(items[:5])}")
                    continue

                # Parse interactive query
                author = None
                start_year = None
                end_year = None
                categories = None
                access_types = None
                search_query = query

                # Simple parsing for special commands
                if query.startswith('author:'):
                    author = query[7:].strip()
                    search_query = ''
                elif query.startswith('year:'):
                    year_part = query[5:].strip()
                    if '-' in year_part:
                        start_str, end_str = year_part.split('-', 1)
                        try:
                            start_year = int(start_str) if start_str.strip() else None
                            end_year = int(end_str) if end_str.strip() else None
                        except ValueError:
                            print("Invalid year format. Use: year:1980-2000")
                            continue
                    search_query = ''

                results = searcher.search(
                    query=search_query,
                    author=author,
                    start_year=start_year,
                    end_year=end_year,
                    categories=categories,
                    access_types=access_types,
                    max_results=10  # Limit for interactive mode
                )

                print(format_results(results, True))

            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")

    else:
        # Single search
        results = searcher.search(
            query=args.query or '',
            author=args.author,
            start_year=args.start_year,
            end_year=args.end_year,
            categories=args.category,
            access_types=args.access_type,
            max_results=args.max_results
        )

        print(format_results(results, args.show_scores))


if __name__ == '__main__':
    main()