import os
from PIL import Image


class ImageProcessor:
    def __init__(self, image_file):
        self.image_file = image_file
        self.images_folder = 'images'
        self.edited_images_folder = 'edited_images'

        self.check_valid_format()
        self.img = Image.open(f'{self.images_folder}/{self.image_file}')
        self.new_image = self.image_file

    def check_valid_format(self):
        supported_formats = (".jpg", ".png")
        if not self.image_file.lower().endswith(supported_formats):
            raise TypeError(f'Unsupported format for {self.image_file}')

    def rename_image(self, new_format):
        self.new_image = f'{os.path.splitext(self.image_file)[0]}.{new_format.lower()}'

    def resize_image(self, new_width):
        try:
            self.img = self.img.resize((
                new_width,
                int(new_width * self.img.height / self.img.width)
            ))

        except Exception as e:
            print(f"Error resizing {self.image_file}: {str(e)}\n")

    def convert_image(self, new_format: str):
        self.rename_image(new_format)
        try:
            self.img.save(self.new_image, format=new_format.upper())

        except Exception as e:
            print(f"Error converting {self.image_file}: {str(e)}\n")

    def archive_image(self):
        os.rename(self.new_image, f'{self.edited_images_folder}/{self.new_image}')
        old_size = os.path.getsize(f'{self.images_folder}/{self.image_file}')
        new_size = os.path.getsize(f'{self.edited_images_folder}/{self.new_image}')
        compress = int((1 - (new_size / old_size)) * 100)
        print(f'✅ {self.new_image} | compress: {compress}%')
