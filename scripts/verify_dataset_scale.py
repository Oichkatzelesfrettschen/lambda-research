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
