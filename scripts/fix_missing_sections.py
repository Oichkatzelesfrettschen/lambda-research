#!/usr/bin/env python3
"""
fix_missing_sections.py

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
