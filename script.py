from PIL import Image
from pillow_heif import register_heif_opener
import sys
import os


if len(sys.argv) < 3:
    print('Usage: python script.py <heic folder path> <output folder path>')
    exit(1)

heic_folder_path = sys.argv[1]
output_folder_path = sys.argv[2]

if os.path.isdir(heic_folder_path) == False:
    print('Error: heic folder path is not a directory')
    exit(1)

if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)

if heic_folder_path == output_folder_path:
    if not os.path.exists(heic_folder_path + '_converted'):
        os.mkdir(heic_folder_path + '_converted')
    output_folder_path = heic_folder_path + '_converted'


register_heif_opener()

for filename in os.listdir(heic_folder_path):
    if filename.endswith(".heic"):
        i = Image.open(os.path.join(heic_folder_path, filename))
        i.save(os.path.join(output_folder_path, filename.replace('.heic', '.jpg')))