from PIL import Image
import hitherdither


palette = hitherdither.palette.Palette(
    [0x080000, 0x201A0B, 0x432817, 0x492910,
     0x234309, 0x5D4F1E, 0x9C6B20, 0xA9220F,
     0x2B347C, 0x2B7409, 0xD0CA40, 0xE8A077,
     0x6A94AB, 0xD5C4B3, 0xFCE76E, 0xFCFAE2]
)

img = Image.open('public/orchidz/orchid-frames/output_frame0002.png')
img_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(
    img, palette, order=8)
