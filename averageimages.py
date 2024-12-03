import numpy as np
import cv2
import os

def average_images(images):
    shape = images[0].shape
    
    # Resize all images
    for i in range(1, len(images)):
        if images[i].shape != shape:
            images[i] = cv2.resize(images[i], (shape[1], shape[0]))
    
    images_float = [img.astype(np.float32) for img in images]
    avg_image = np.mean(images_float, axis=0)
    avg_image = np.clip(avg_image, 0, 255)
    return avg_image.astype(np.uint8)