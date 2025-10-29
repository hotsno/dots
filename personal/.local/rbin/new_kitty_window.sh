#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title kitty (New Window)
# @raycast.mode silent

# Optional parameters:
# @raycast.icon images/kitty.png
# @raycast.packageName kitty

cd ~
/Applications/kitty.app/Contents/MacOS/kitty --single-instance &>/dev/null &
