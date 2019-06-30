#!/usr/bin/env python3

# backup.py
# A program that creates a backup copy of a config file.
#
# Billy Wilson Arante <arantebillywilson@gmail.com>

import sys
import shutil
import os

def main():
    src = sys.argv[1]
    dst = os.environ['HOME'] + "/Documents/config-files/"
    shutil.copy2(src, dst)
    # Confirm file was copied/updated
    
if __name__ == "__main__":
    main()
