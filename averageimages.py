import numpy as np
import cv2
import os

def average_images(images):
    images_float = [img.astype(np.float32) for img in images]
    avg_image = np.mean(images_float, axis=0)
    avg_image = np.clip(avg_image, 0, 255)
    return avg_image.astype(np.uint8)