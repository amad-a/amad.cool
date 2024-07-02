#!/bin/bash

# Check if interval argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 [interval (per minute)]"
    exit 1
fi

interval=$1

# Check if the interval is a positive integer
if ! [[ $interval =~ ^[1-9][0-9]*$ ]]; then
    echo "Error: Please provide a valid positive integer for the interval."
    exit 1
fi

# Infinite loop to change wallpaper
while true; do
    # Get a list of gif files in the current directory
    gif_files=(*.gif)

    # Check if there are gif files
    if [ ${#gif_files[@]} -eq 0 ]; then
        echo "No gif files found in the current directory."
        exit 1
    fi

    # Iterate over gif files and set wallpaper
    for gif_file in "${gif_files[@]}"; do
        feh --bg-tile "$gif_file"
        sleep "$((interval * 60))"  # Convert interval to seconds
    done
done
