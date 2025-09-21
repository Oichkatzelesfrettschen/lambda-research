#!/usr/bin/env python3
"""
Bibliography Standardization Script for Lambda Calculus Research Repository

This script automates the standardization of bibliography files according to the
established format:

**Author, A.B.** (Year). *Title*. Venue, Volume(Issue), Pages.
- **Key Contribution**: Description
- **DOI**: When available
"""

import re
import sys
from pathlib import Path

def standardize_author_name(author_string):
    """Convert author names to standard format: Last, F.M."""
    # Handle multiple authors
    if '&' in author_string:
        authors = [a.strip() for a in author_string.split('&')]
        return ' & '.join([standardize_single_author(a) for a in authors])
    else:
        return standardize_single_author(author_string)

def standardize_single_author(author):
    """Convert single author name to standard format."""
    # Remove common prefixes/titles
    author = re.sub(r'^(Dr\.|Prof\.|Professor)\s+', '', author)

    # Simple heuristic for common patterns
    if ',' in author:
        # Already in Last, First format
        parts = author.split(',')
        last = parts[0].strip()
        first_parts = parts[1].strip().split()
        initials = '.'.join([p[0] for p in first_parts if p]) + '.'
        return f"{last}, {initials}"
    else:
        # First Last format
        parts = author.strip().split()
        if len(parts) >= 2:
            last = parts[-1]
            first_parts = parts[:-1]
            initials = '.'.join([p[0] for p in first_parts if p]) + '.'
            return f"{last}, {initials}"
    return author

def extract_entry_info(entry_text):
    """Extract bibliographic information from an entry."""
    lines = entry_text.strip().split('\n')

    # Pattern matching for current format
    header_pattern = r'### \d+\.\s*(.+?)\s*\((\d{4}(?:-\d{4})?)\)'
    title_pattern = r'\*\*"(.+?)"\*\*'

    info = {}
    for line in lines:
        # Extract author and year from header
        header_match = re.search(header_pattern, line)
        if header_match:
            info['author'] = header_match.group(1)
            info['year'] = header_match.group(2)

        # Extract title
        title_match = re.search(title_pattern, line)
        if title_match:
            info['title'] = title_match.group(1)

        # Extract venue information (heuristic)
        if line.startswith('- ') and ':' in line and 'contribution' not in line.lower():
            venue_line = line[2:].strip()
            if not venue_line.startswith('DOI:') and not venue_line.startswith('URL:'):
                info['venue'] = venue_line

        # Extract key contribution
        if 'contribution' in line.lower() or 'establishes' in line.lower():
            info['contribution'] = line[2:].strip()

    return info

def format_standardized_entry(info):
    """Format entry according to standard format."""
    if not all(key in info for key in ['author', 'year', 'title']):
        return None

    author = standardize_author_name(info['author'])
    year = info['year']
    title = info['title']
    venue = info.get('venue', 'Venue information needed')
    contribution = info.get('contribution', 'Key contribution description needed')

    entry = f"**{author}** ({year}). *{title}*. {venue}.\n"
    entry += f"- **Key Contribution**: {contribution}"

    if 'doi' in info:
        entry += f"\n- **DOI**: {info['doi']}"

    return entry

def process_bibliography_file(file_path):
    """Process a single bibliography file."""
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into sections
    sections = re.split(r'\n## ', content)

    # Process each section
    processed_sections = []
    for section in sections:
        if not section.strip():
            continue

        # Keep section header
        lines = section.split('\n')
        if not lines[0].startswith('#'):
            lines[0] = '## ' + lines[0]

        section_header = lines[0]
        section_content = '\n'.join(lines[1:])

        # Find numbered entries
        entries = re.split(r'\n### \d+\.', section_content)

        if len(entries) > 1:  # Has numbered entries
            processed_entries = [section_header]

            for entry in entries[1:]:  # Skip first empty split
                entry_text = '### ' + entry  # Restore the split marker
                info = extract_entry_info(entry_text)

                standardized = format_standardized_entry(info)
                if standardized:
                    processed_entries.append(standardized)
                else:
                    # Keep original if standardization fails
                    processed_entries.append(entry_text)

            processed_sections.append('\n\n'.join(processed_entries))
        else:
            # No numbered entries, keep as is
            processed_sections.append(section)

    # Combine processed sections
    result = '\n\n'.join(processed_sections)

    # Create backup
    backup_path = file_path.with_suffix('.md.backup')
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # Write processed content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"✅ Processed {file_path} (backup created at {backup_path})")

def main():
    """Main function to process bibliography files."""
    if len(sys.argv) < 2:
        print("Usage: python3 standardize_bibliography.py <file_path_or_pattern>")
        print("Example: python3 standardize_bibliography.py '*/papers/bibliography.md'")
        return

    pattern = sys.argv[1]

    # Find files matching pattern
    current_dir = Path('.')
    files = list(current_dir.glob(pattern))

    if not files:
        print(f"No files found matching pattern: {pattern}")
        return

    print(f"Found {len(files)} files to process:")
    for file_path in files:
        print(f"  {file_path}")

    confirm = input("\nProceed with standardization? (y/N): ")
    if confirm.lower() != 'y':
        print("Aborted.")
        return

    for file_path in files:
        try:
            process_bibliography_file(file_path)
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

if __name__ == "__main__":
    main()