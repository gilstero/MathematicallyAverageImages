import numpy as np
import cv2
import os

def load_images(image_paths):
    images = []
    for path in os.listdir(image_paths):
        file_path = os.path.join(image_paths, path)
        img = cv2.imread(file_path)
        if img is not None:
            images.append(img)
        else:
            print(f"Error loading image {path}")
    return images