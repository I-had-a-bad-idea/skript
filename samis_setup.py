#!/usr/bin/python3

# samis_setup.py
# Loads all resources needed for product development of SAMIS.
#
# Billy Arante <arantebillywilson@gmail.com>
# March 31, 2020

import webbrowser as wb
import os

def main():
    # github
    #wb.open('https://github.com/arantebw/project-rosheille/')

    # notes
    #wb.open('https://docs.google.com/document/d/1t7JTWJJGvRFVroua4vSY_enqXMsezR1fnwb-2dcP-EQ/edit')

    # documentation
    #wb.open('https://docs.google.com/document/d/1qSRVhDWPIa6qgssCAN_N1YXxTvDH3fcQRDYw7MhjxFY/edit')

    # start xampp
    #os.system('sudo /opt/lampp/lampp start')

    # phpmyadmin
    #wb.open('http://localhost/phpmyadmin')

    # tmux
    os.system('./tmux_setup.sh')

    # admin
    #wb.open_new('http://localhost:8000')

    # user
    #os.system('google-chrome -incognito http://localhost:8000')


if __name__ == '__main__':
    main()
