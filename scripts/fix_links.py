#!/usr/bin/env python3
"""
fix_links.py

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


import os
import re

# This script is designed to be run from the root of the lambda-research repository.

# Use a raw, triple-quoted string for the regex to avoid escaping issues.
link_regex = re.compile(r"""\[([^\]]+)\]\(([^)]+)\)""")

fixed_files_count = 0

print("Starting link harmonization script...")

for root, dirs, files in os.walk('.'):
    # Exclude the .git directory to avoid any issues there
    if '.git' in dirs:
        dirs.remove('.git')

    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Could not read {filepath}: {e}")
                continue

            original_content = content
            
            # Use a function for replacement to handle each match object
            def replacer(match):
                text = match.group(1)
                url = match.group(2)

                # Check if it's a relative link that needs fixing
                if not url.startswith(('http', '/', '#', 'mailto:')) and url:
                    # Prepend the leading slash to make it a root-absolute link
                    new_url = '/' + url
                    return f'[{text}]({new_url})'
                else:
                    # If it doesn't need fixing, return the original match
                    return match.group(0)

            # Use re.sub with the replacer function
            content = link_regex.sub(replacer, content)

            # Write the changes back to the file only if content was modified
            if content != original_content:
                fixed_files_count += 1
                print(f"Harmonizing links in: {filepath}")
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                except Exception as e:
                    print(f"Could not write to {filepath}: {e}")

print(f"\nLink harmonization complete. {fixed_files_count} files were updated.")