#!/usr/bin/env python3
"""
Add GPL-3.0 license headers to source files.
This script adds appropriate GPL license headers to all synthesized research code.
"""

import os
import sys
from pathlib import Path

# GPL-3.0 header templates for different file types

PYTHON_HEADER = '''#!/usr/bin/env python3
"""
{filename}

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
'''

SHELL_HEADER = '''#!/usr/bin/env bash
#
# {filename}
#
# Copyright (C) 2025 Lambda Research Collective
#
# This file is part of Lambda Calculus Research Repository.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

SCALA_HEADER = '''/*
 * {filename}
 *
 * Copyright (C) 2025 Lambda Research Collective
 *
 * This file is part of Lambda Calculus Research Repository.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */
'''

SCHEME_HEADER = ''';; {filename}
;;
;; Copyright (C) 2025 Lambda Research Collective
;;
;; This file is part of Lambda Calculus Research Repository.
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

SML_IDRIS_HEADER = '''(*
 * {filename}
 *
 * Copyright (C) 2025 Lambda Research Collective
 *
 * This file is part of Lambda Calculus Research Repository.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 *)
'''


def has_license_header(content: str) -> bool:
    """Check if file already has a GPL license header."""
    return 'GNU General Public License' in content or 'GPL' in content[:500]


def add_header(filepath: Path, dry_run: bool = False):
    """Add appropriate license header to a file."""
    
    # Read existing content
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has license
    if has_license_header(content):
        print(f"  ✓ {filepath.name} - Already has license header")
        return False
    
    # Determine appropriate header
    suffix = filepath.suffix
    filename = filepath.name
    
    if suffix == '.py':
        header = PYTHON_HEADER.format(filename=filename)
        # Remove old shebang if present
        if content.startswith('#!/'):
            lines = content.split('\n', 1)
            if len(lines) > 1:
                content = lines[1].lstrip()
    elif suffix == '.sh':
        header = SHELL_HEADER.format(filename=filename)
        if content.startswith('#!/'):
            lines = content.split('\n', 1)
            if len(lines) > 1:
                content = lines[1].lstrip()
    elif suffix == '.scala':
        header = SCALA_HEADER.format(filename=filename)
    elif suffix == '.rkt':
        header = SCHEME_HEADER.format(filename=filename)
        # Keep #lang directive
        if content.startswith('#lang'):
            lines = content.split('\n', 1)
            lang_directive = lines[0] + '\n'
            content = lines[1].lstrip() if len(lines) > 1 else ''
            header = lang_directive + '\n' + header
    elif suffix == '.sml':
        header = SML_IDRIS_HEADER.format(filename=filename)
    elif suffix == '.idr':
        header = SML_IDRIS_HEADER.format(filename=filename)
    else:
        print(f"  ? {filepath.name} - Unknown file type")
        return False
    
    new_content = header + '\n\n' + content
    
    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    print(f"  + {filepath.name} - Added GPL-3.0 header")
    return True


def main():
    repo_root = Path('/home/runner/work/lambda-research/lambda-research')
    
    # Files to update
    patterns = [
        'scripts/*.py',
        'scripts/*.sh',
        'implementations/scala/*.scala',
        'implementations/scheme/*.rkt',
        'implementations/sml/*.sml',
        'implementations/idris/*.idr',
    ]
    
    files_updated = 0
    
    print("Adding GPL-3.0 license headers to source files...")
    print()
    
    for pattern in patterns:
        for filepath in repo_root.glob(pattern):
            if filepath.name == 'add_license_headers.py':
                continue  # Skip this script itself
            if add_header(filepath, dry_run=False):
                files_updated += 1
    
    print()
    print(f"Completed: {files_updated} files updated with GPL-3.0 headers")


if __name__ == '__main__':
    main()
