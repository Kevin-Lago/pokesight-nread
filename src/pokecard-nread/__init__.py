import os
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import cv2

DEBUG: bool = True


def load_data():
    data = tf.keras.utils.image_dataset_from_directory(
        'data',
        batch_size=8,  # Limits memory to be used (VRAM / RAM)
        # image_size=(128, 128)  # Limits size of images to be processed
    )
    data_iter = data.as_numpy_iterator()

    batch = data_iter.next()
    test = batch[1]

    fig, ax = plt.subplots(ncols=4, figsize=(20, 20))

    for idx, img in enumerate(batch[0][:4]):
        ax[idx].imshow(img.astype(int))
        ax[idx].title.set_text(batch[1][idx])
    fig.show()

    print()


def clean_image_data_dir(data_dir: str = 'data', image_exts: tuple = ('.jpeg', '.jpg', '.bmp', '.png')) -> None:
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
    # clean_image_data_dir()
    load_data()
