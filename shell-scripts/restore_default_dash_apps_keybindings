#!/bin/bash

# Restore the dashboard apps keybindings to defaults
for i in {1..9}; do
  gsettings set org.gnome.shell.keybindings switch-to-application-$i "['<Super>$i']"
done

echo "<Super> 1-9 dashboard apps keybindings have been restored"
