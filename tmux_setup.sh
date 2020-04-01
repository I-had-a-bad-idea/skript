#!/usr/bin/bash

# tmux_setup.sh
# Setup a simple tmux session for SAMIS.
#
# Billy Arante <arantebillywilson@gmail.com>
# March 31, 2020

tmux new-session -d -s 'SAMIS'
tmux split-window -h
tmux send-keys 'cd src/ && npm run watch-poll --scripts-prepend-node-path' C-m
tmux split-window -v
tmux send-keys 'cd src/ && php artisan serve' C-m
tmux new-window 'cd src/ && vim'
tmux -2 attach-session -d
