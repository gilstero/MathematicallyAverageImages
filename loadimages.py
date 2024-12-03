import numpy as np
import cv2
import os

def load_images(image_paths):
    images = []
    for path in image_paths:
        img = cv2.imread(path)
        if img is not None:
            images.append(img)
        else:
            print(f"Error loading image {path}")
    return images