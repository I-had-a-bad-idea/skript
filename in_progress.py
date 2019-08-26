#!/usr/bin/env python3

# in_progress.py
# Tag a file as in-progress.
#
# Created by Billy Arante <arantebillywilson@gmail.com>

import sys
import os


def main():
    if (len(sys.argv) > 1):
        file = os.path.basename(sys.argv[1])
        if (os.path.isdir(file)):
            new_filename = "{} [in-progress]".format(file)
        else:
            filename = os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]
            new_filename = "{}-[in-progress]{}".format(filename, extension)
        os.rename(file, new_filename)
        print("File tagged as in-progress.")
    else:
        print("Provide target file.")


if __name__ == "__main__":
    main()
