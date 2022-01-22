#!/usr/bin/env python

# remove_empty_lines.py
# This program removes empty (blank) lines in a file.
#
# Billy Wilson Arante <arantebillywilson@gmail.com>
# April 24, 2020

import sys


def main(file):
    non_empty_lines = []
    with open(file, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                non_empty_lines.append(line)
    f.close()

    with open(file, 'w+') as f:
        for line in non_empty_lines:
            f.write(line)
    f.close()


if __name__ == '__main__':
    if sys.argv[1] == '--help':
        print('how to use:')
        print('remove-empty-lines <file>')
    else:
        main(sys.argv[1])
