from PIL import Image 
import os, sys


if len(sys.argv) != 3:
    print("Usage: python script.py <input_directory> <output_directory>")
    sys.exit(1)

old_format_folder = sys.argv[1]
new_format_folder = sys.argv[2]

if not (os.path.exists(new_format_folder)):
    os.mkdir(new_format_folder)

# for img in os.listdir(old_format_folder):
#         image_path = os.path.join(old_format_folder, img)
#         destination_path = os.path.join(new_format_folder, img.split('.')[0] + ".png")
#         print(destination_path)

#         with Image.open(image_path) as img:
#             img.save(f"{destination_path}")
    
for file in os.listdir(old_format_folder):
    img = Image.open(f"{old_format_folder}{file}")
    # img.save(f"{new_format_folder}{file.split('.')[0]}.png", "png") # one way of doing it
    clean_name = os.path.splitext(file)[0]
    img.save(f"{new_format_folder}{clean_name}.png", "png")
    print("done")