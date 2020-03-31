#!/usr/bin/python3

# setup.py
# Loads all necessary resources for product development of SMSDA.
#
# Billy Arante <arantebillywilson@gmail.com>
# March 31, 2020

import webbrowser
import os

def main():
    # Notes
    webbrowser.open('https://docs.google.com/document/d/1dFzUfaxnbzKsrsyQ2CEq2zpT0-o5HlzHeTXK8pI_QMg/edit#heading=h.u65jai413vty')

    # Documentation
    webbrowser.open('https://docs.google.com/document/d/1ch2rQPegf52Bx8ESlJkv9beKWMAxh1lrWH4CPnsYD1c/edit')

    # PHPMyAdmin
    os.system('sudo /opt/lampp/lampp start')
    webbrowser.open('http://localhost/phpmyadmin')

    # Web app for admin
    webbrowser.open_new('http://localhost:8000');

    # Web app for regular users
    os.system('/usr/bin/google-chrome -incognito http://localhost:8000')


if __name__ == '__main__':
    main()
