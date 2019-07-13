#!/usr/bin/env python3

# rename.py
# Renames a file/directory into my specified format.
#
# Billy Arante <arantebillywilson@gmail.com>

import sys
import os


def main():
    target_file = sys.argv[1]
    new_file_name = target_file.lower().replace(' ', '-')
    os.rename(target_file, new_file_name)


if __name__ == "__main__":
    main()
