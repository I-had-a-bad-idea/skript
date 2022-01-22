#!/usr/bin/env python

# append_filename.py
#
# Billy Wilson Arante <arantebillywilson@gmail.com>
# April 21, 2020

import sys
import os


def main(files_list, text):
    for file in files_list:
        os.rename(file, f'{text}{file}')


if __name__ == '__main__':
    main(sys.argv[1:-1], sys.argv[-1])
