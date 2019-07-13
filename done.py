#!/usr/bin/env python3

# done.py
# Tags a file as done (listening, watching, etc.).
#
# Created by Billy Arante <arantebillywilson@gmail.com>

import sys
import os


def main():
    file = None
    if len(sys.argv) > 1:
        file = os.path.basename(sys.argv[1])
        filename = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]
        new_filename = '{}-[done]{}'.format(filename, extension)
        os.rename(file, new_filename)
        print('file tagged as done')
    else:
        print('provide target file')


if __name__ == '__main__':
    main()
