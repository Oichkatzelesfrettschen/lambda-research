#!/usr/bin/env python3
"""
verify_dataset_scale.py

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


import pandas as pd
import glob
import os

def count_terms():
    files = glob.glob("src/data/shards/*.parquet")
    total_count = 0
    print(f"Analyzing {len(files)} shards...")
    for f in files:
        try:
            df = pd.read_parquet(f) 
            count = len(df)
            total_count += count
            print(f"File {os.path.basename(f)}: {count} rows")
        except Exception as e:
            print(f"Error reading {f}: {e}")
    
    print("-" * 20)
    print(f"Total Terms: {total_count:,}")
    return total_count

if __name__ == "__main__":
    count_terms()
