
mkdir bulk-dither-test

for FILE in ./*.png; do
    chmod u+x $FILE
    convert $FILE -colorspace RGB -resize 500x500 -ordered-dither o8x8 bulk-dither-test/dithered-${FILE##*/}
done