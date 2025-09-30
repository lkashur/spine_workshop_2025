import os
from pathlib import Path
from datetime import datetime

data_dir = Path("/sdf/home/j/junjie/sdf-data/Michel/production/scripts/output_spine")

cutoff = datetime(2025, 9, 30, 12, 34)
cutoff_ts = cutoff.timestamp()

files = list(data_dir.glob("*.h5"))
files_before = [f for f in files if f.stat().st_mtime < cutoff_ts]
files_before.sort(key=lambda f: f.stat().st_mtime, reverse=True)

# take top 5
latest_5 = files_before[:5]

latest_15 = files_before[5:20]

# write result
with open("filelist_short.txt", "w") as f_out:
    for f in latest_5:
        f_out.write(f"{f}\n")

with open("filelist_long.txt", "w") as f_out:
    for f in latest_15:
        f_out.write(f"{f}\n")

print(f"Done: wrote to short and long file lists.")
