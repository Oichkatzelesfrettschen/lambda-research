#!/usr/bin/env python3
"""
Fix Missing Sections in Index Files
Ensures that all index.md files in numbered folders have the required sections:
- Overview
- Syntax
- Properties
- Resources
"""

import os
import re
from pathlib import Path

def main():
    root = Path('docs')
    required_sections = ['Overview', 'Syntax', 'Properties', 'Resources']
    
    # Find all index.md in numbered directories
    # We look for directories starting with two digits
    for index_file in root.rglob('index.md'):
        if re.match(r'^\d{2}-', index_file.parent.name):
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            content_lower = content.lower()
            
            added = False
            for section in required_sections:
                # Check if section exists (simple check matches validator)
                if section.lower() not in content_lower:
                    print(f"Adding missing section '{section}' to {index_file}")
                    content += f"\n\n## {section}\n\nTODO: Add {section} content.\n"
                    added = True
            
            if added:
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    main()
