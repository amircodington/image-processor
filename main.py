import os
import sys

from PIL import Image
from pathlib import Path
from image_processor import ImageProcessor

def get_args():
    if len(sys.argv) != 3:
        print("Usage: python image_processing_cleaner.py [output_format] [output_width]")
        sys.exit(1)

    image_format = sys.argv[1]
    image_width = int(sys.argv[2])

    return image_format, image_width


if __name__ == '__main__':
    Path('edited_images').mkdir(parents=True, exist_ok=True)
    img_format, img_width = get_args()
    img_files = os.listdir('images')
    for img_file in img_files:
        try:
            img = ImageProcessor(img_file)
            img.resize_image(img_width)
            img.convert_image(img_format)
            img.archive_image()
        except TypeError as e:
            print(e)
