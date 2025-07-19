#!/usr/bin/env python3

# alliance_setup.py
#
# Author: Billy Arante <arantebillywilson@gmail.com>
# Created: 23 Sep 2022
# Updated: 23 Sep 2022
#
# How to use:
# python alliance_setup.py <path>

import os
import sys


def change_path(new_path):
    os.system(f"tmux send-keys 'cd {new_path}' C-m")


def main():
    project_path = sys.argv[1]

    os.system("tmux new-session -d -s 'alliance'")

    change_path(f"{project_path}/oauth/")
    os.system("tmux send-keys 'clear' C-m")

    os.system("tmux split-window -h")
    change_path(f"{project_path}/synflo-api/")
    os.system("tmux send-keys 'clear' C-m")

    os.system("tmux split-window -v")
    change_path(f"{project_path}/synflo-ui/")
    os.system("tmux send-keys 'clear' C-m")

    os.system("tmux select-pane -L")
    os.system("tmux split-window -v")
    change_path(project_path)
    os.system("tmux send-keys 'clear' C-m")

    os.system("tmux rename-window -t 0 'servers'")

    os.system("tmux -2 attach-session -d")

    os.system("tmux send-keys 'kitty @ set-window-title alliance' C-m")


if __name__ == "__main__":
    main()
