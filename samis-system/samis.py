#!/usr/bin/env python3

# samis.py
# Loads all resources needed for product development of SAMIS.
#
# Billy Arante <arantebillywilson@gmail.com>
# March 31, 2020

import webbrowser as wb
import os


def main():
    # start xampp
    os.system('sudo /opt/lampp/lampp start')

    # github project
    wb.open('https://github.com/arantebw/project-rosheille/projects/1?fullscreen=true')

    # notes
    wb.open('https://docs.google.com/document/d/1t7JTWJJGvRFVroua4vSY_enqXMsezR1fnwb-2dcP-EQ/edit')

    # documentation
    wb.open('https://docs.google.com/document/d/1qSRVhDWPIa6qgssCAN_N1YXxTvDH3fcQRDYw7MhjxFY/edit')

    # phpmyadmin
    wb.open('http://localhost/phpmyadmin')

    # admin
    wb.open_new('http://localhost:8000')

    # user
    os.system('google-chrome -incognito http://localhost:8000')

    # tmux
    os.system('./tmux.sh')


if __name__ == '__main__':
    main()
