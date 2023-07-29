#!/usr/bin/env python3
import os
import subprocess
from multiprocessing import Pool

script_dir = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(script_dir, "../data/prod/")
dest = os.path.join(script_dir, "../data/prod_backup/")

def sync_files(path):
    src_path = os.path.join(src, path)
    dest_path = os.path.join(dest, path)
    subprocess.call(["rsync", "-arq", src_path, dest_path])

if __name__ == "__main__":
    pool = Pool()
    # Get the list of files/directories to sync and sort them
    items_to_sync = sorted(os.listdir(src))

    # Use multiprocessing to sync the data in parallel
    pool.map(sync_files, items_to_sync)

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()
