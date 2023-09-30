import os
import sys
from PIL import Image
from pathlib import Path


def get_args():
    if len(sys.argv) != 3:
        print("Usage: python image_processing_cleaner.py [output_format] [output_width]")
        sys.exit(1)

    image_format = sys.argv[1]
    image_width = int(sys.argv[2])

    return image_format, image_width


def process_image(image_file, image_format, image_width):
    supported_formats = (".jpg", ".png")
    images_folder = 'images'
    edited_images_folder = 'edited_images'

    if image_file.lower().endswith(supported_formats):
        try:
            image = Image.open(os.path.join(images_folder, image_file))
            image = image.resize((
                image_width,
                int(image_width * image.height / image.width)))
            edited_image = f'{os.path.splitext(image_file)[0]}.{image_format.lower()}'
            edited_image_path = os.path.join(edited_images_folder, edited_image)
            image.save(edited_image_path, format=image_format.upper())
            os.rename(edited_image_path, edited_image_path)
            print(f"Processed: {image_file} | Format: {image_format} | Width: {image_width}px")
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}\n")
    else:
        print(f'Unsupported format for {image_file}')


if __name__ == '__main__':
    Path('edited_images').mkdir(parents=True, exist_ok=True)
    img_format, img_width = get_args()
    img_files = os.listdir('images')
    for img_file in img_files:
        process_image(img_file, img_format, img_width)
