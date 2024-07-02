import os
from PIL import Image

def average_color(image):
    # Convert the image to RGB if it's not already
    image = image.convert('RGB')
    color = image.resize((1, 1)).getpixel((0, 0))
    return color

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def process_images(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    avg_colors = {}

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        with Image.open(image_path) as img:
            avg_color = average_color(img)
            avg_colors[image_file] = rgb_to_hex(avg_color)

    sorted_files = sorted(avg_colors.keys(), key=lambda x: avg_colors[x])
    
    output_file = os.path.join(folder_path, 'sorted_filenames.txt')
    with open(output_file, 'w') as f:
        for filename in sorted_files:
            f.write(filename + '\n')
    
    print(f'Sorted filenames have been written to {output_file}')

# Example usage
folder_path = '.'
process_images(folder_path)

