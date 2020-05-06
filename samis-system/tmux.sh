#!/usr/bin/env bash

# tmux.sh
# Setup a simple tmux session for SAMIS.
#
# Billy Arante <arantebillywilson@gmail.com>
# March 31, 2020

tmux new-session -d -s 'SAMIS'
tmux split-window -h
tmux send-keys 'cd project-rosheille/ && npm run watch-poll --scripts-prepend-node-path' C-m
tmux split-window -v
tmux send-keys 'cd project-rosheille/ && php artisan serve' C-m
tmux new-window 'cd project-rosheille/ && vim .'
tmux -2 attach-session -d
