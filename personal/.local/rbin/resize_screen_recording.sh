#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Compress Screen Recording
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🎥
# @raycast.packageName Screen Recording
# @raycast.argument1 { "type": "text", "placeholder": "Size in MB" }

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 TARGET_SIZE_MB"
    exit 1
fi

# Get target size in MB
SIZE_MB=$1

# Find most recent MOV file
INPUT_FILE=$(find ~/Pictures/Screenshots -type f -iname "*.mov" -print0 | \
    xargs -0 ls -t | head -n1)

# Check if file was found
if [ -z "$INPUT_FILE" ]; then
    echo "No MOV file found in ~/Pictures/Screenshots"
    exit 1
fi

# Create output filename
OUTPUT_FILE="${INPUT_FILE%.*}.mp4"

echo "Input file: $INPUT_FILE"
echo "Target size: ${SIZE_MB}MB"
echo "Output file: $OUTPUT_FILE"

# Convert using ffmpeg with target filesize
ffmpeg -i "$INPUT_FILE" \
    -loglevel quiet \
    -c:v libx264 \
    -c:a aac \
    -b:a 128k \
    -fs $((SIZE_MB * 1024 * 1024)) \
    "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "Conversion complete!"
    open -R "$OUTPUT_FILE"
else
    echo "Conversion failed!"
fi

