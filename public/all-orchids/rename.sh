#!/bin/bash

counter=1

# Loop through all PNG files in the current directory
for file in *.png; do
    # Generate the new filename
    new_filename="orchid-$counter.png"
    
    # Rename the file
    mv "$file" "$new_filename"
    
    # Increment the counter
    ((counter++))
done

