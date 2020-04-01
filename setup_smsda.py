#!/usr/bin/python3

# setup.py
# Loads all necessary resources for product development of SMSDA.
#
# Billy Arante <arantebillywilson@gmail.com>
# March 31, 2020

import webbrowser
import os

def main():
    # notes
    webbrowser.open('https://docs.google.com/document/d/1dFzUfaxnbzKsrsyQ2CEq2zpT0-o5HlzHeTXK8pI_QMg/edit#heading=h.u65jai413vty')

    # documentation
    webbrowser.open('https://docs.google.com/document/d/1ch2rQPegf52Bx8ESlJkv9beKWMAxh1lrWH4CPnsYD1c/edit')

    # phpmyadmin
    os.system('sudo /opt/lampp/lampp start')
    webbrowser.open('http://localhost/phpmyadmin')

    # admin
    webbrowser.open_new('http://localhost:8000');

    # users
    os.system('/usr/bin/google-chrome -incognito http://localhost:8000')

    # tmux
    os.system('tmux new-session -d -s \'SMSDA\'')
    os.system('tmux send-keys \'cd src/\' C-m')
    os.system('tmux split-window -h')
    os.system('tmux send-keys \'cd src/ && npm run watch-poll --scripts-prepend-node-path\' C-m')
    os.system('tmux split-window -v')
    os.system('tmux send-keys \'cd src/ && php artisan serve\' C-m')
    os.system('tmux new-window')
    os.system('tmux send-keys \'cd src/ && vim\' C-m')
    os.system('tmux -2 attach-session -d')


if __name__ == '__main__':
    main()
