#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261124.
Writes the prepared infographic to /output/entry.png.
Deterministic, no network: it only copies entry.png from this repo.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)

if __name__ == "__main__":
    sys.exit(main())
