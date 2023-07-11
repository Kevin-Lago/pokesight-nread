import os
import tensorflow as tf
import cv2

DEBUG: bool = True


def clean_image_data_dir(data_dir: str = 'data', image_exts: list = ['jpeg', 'jpg', 'bmp', 'png']) -> None:
    for image_dir in os.listdir(data_dir):
        for image in os.listdir(os.path.join(data_dir, image_dir)):
            image_path = os.path.join(data_dir, image_dir, image)
            image_path, image_ext = os.path.splitext(image_path)

            try:
                img = cv2.imread(image_path)
                if image_ext not in image_exts:
                    print(f'Image type not supported: {image_ext}')
                    os.remove(image_path)
                else:
                    if DEBUG:
                        print(f'Image processed: {image_path}')
            except Exception as e:
                print(f'Issue with image {image_path}')
                # os.remove(image_path)


if __name__ == '__main__':
    clean_image_data_dir()
