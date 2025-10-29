#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Trim Screen Recording
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🎥
# @raycast.packageName Screen Recording

export PATH="$PATH:/Users/hotsno/.local/bin"

# Find most recent MOV file
INPUT_FILE=$(find "$HOME/Pictures/Screenshots and Recordings" -type f -iname "*.mov" -print0 |
  xargs -0 ls -t | head -n1)

# Check if file was found
if [ -z "$INPUT_FILE" ]; then
  echo "No MOV file found in ~/Pictures/Screenshots"
  exit 1
fi

mpv "$INPUT_FILE"

OUTPUT_FILE=$(find "$HOME/Pictures/Screenshots and Recordings" -type f -iname "*.mp4" -print0 |
  xargs -0 ls -t | head -n1)

open -R "$OUTPUT_FILE"
