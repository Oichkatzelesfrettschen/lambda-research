#!/usr/bin/env python3
"""
scaffold_directories.py

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
Scaffold Missing Directories in Numbered Folders
Ensures that all numbered folders (01-31) have the required subdirectories:
- papers/
- implementations/
- tutorials/
- historical/
Adds a .gitkeep file to empty directories to ensure they are tracked.
"""

import os
import re
from pathlib import Path

def main():
    root = Path('docs')
    required_subdirs = ['papers', 'implementations', 'tutorials', 'historical']
    
    # Find all numbered directories recursively
    numbered_dirs = [d for d in root.rglob('*') if d.is_dir() and re.match(r'^\d{2}-', d.name)]
    
    print(f"Found {len(numbered_dirs)} numbered directories.")
    
    created_count = 0
    
    for d in numbered_dirs:
        for subdir in required_subdirs:
            subdir_path = d / subdir
            if not subdir_path.exists():
                subdir_path.mkdir(parents=True, exist_ok=True)
                print(f"Created: {subdir_path}")
                created_count += 1
            
            # Ensure .gitkeep if empty
            if not any(subdir_path.iterdir()):
                gitkeep = subdir_path / '.gitkeep'
                if not gitkeep.exists():
                    gitkeep.touch()
                    print(f"Added .gitkeep to: {subdir_path}")

    print(f"Scaffolding complete. Created {created_count} missing directories.")

if __name__ == '__main__':
    main()
