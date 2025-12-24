#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

def standardize_entry(content):
    # Pattern 1
    pattern1 = r'###\s+([^*#\n]+?)\s*\((\d{4}(?:-\d{4})?)\)\s*\n\s*\*\*"(.+?)"\*\*'
    replacement1 = r'**\1** (\2). *\3*.'
    content = re.sub(pattern1, replacement1, content)
    
    # Pattern 2: Ensure DOIs and URLs are on their own lines with consistent bullets
    content = re.sub(r'\n\s*-\s*DOI:', r'\n- **DOI**:', content)
    content = re.sub(r'\n\s*-\s*Repository:', r'\n- **Repository**:', content)
    
    return content

def process_file(file_path, check_only=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = standardize_entry(content)
    
    # Final cleanup: ensure single trailing newline
    new_content = new_content.strip() + '\n'
    
    if new_content != content:
        if check_only:
            print(f"[FAIL] {file_path} needs standardization")
            return False
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[OK] Standardized {file_path}")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', help='Glob pattern')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    
    files = list(Path('.').glob(args.pattern))
    success = True
    for f in files:
        if not process_file(f, args.check):
            success = False # Corrected from True to False to accurately reflect failure
    
    if args.check and not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
