import os
from PIL import Image

def create_collage(image_folder, output_path, images_per_row=4, image_size=(200, 200), padding=10):
    jpeg_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]  
    images = [Image.open(os.path.join(image_folder, file)).resize(image_size) for file in jpeg_files]
    
    rows = (len(images) + images_per_row - 1) // images_per_row
    actual_images_per_row = min(len(images), images_per_row)
    grid_width = actual_images_per_row * (image_size[0] + padding) - padding
    grid_height = rows * (image_size[1] + padding) - padding
    grid_image = Image.new('RGB', (grid_width, grid_height), color=(255, 255, 255))
    
    for index, image in enumerate(images):
        row, col = divmod(index, actual_images_per_row)
        x = col * (image_size[0] + padding)
        y = row * (image_size[1] + padding)
        grid_image.paste(image, (x, y))
    grid_image.save(output_path, format='TIFF')


def process_directories(base_dir, output_dir, images_per_row=4, image_size=(200, 200), padding=10):
    abs_base_dir = os.path.abspath(base_dir)
    abs_output_dir = os.path.abspath(output_dir)
    subdirs = [d for d in os.listdir(abs_base_dir) if os.path.isdir(os.path.join(abs_base_dir, d))]
    if not os.path.exists(abs_output_dir):
        os.makedirs(abs_output_dir)
    for subdir in subdirs:
        subdir_path = os.path.join(abs_base_dir, subdir)
        output_path = os.path.join(abs_output_dir, f"{subdir}.tiff")
        create_collage(subdir_path, output_path, images_per_row, image_size, padding)


base_dir = './Для тестового'
output_dir = './output_collages'

process_directories(base_dir, output_dir)
