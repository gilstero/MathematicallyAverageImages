# Mathemetically Average Images
# Written by Olin Gilster

import numpy as np
import cv2
import os
import loadimages
import averageimages

def main():
    image_folder = "/Users/olingilster/Desktop/Projects/AverageImages/images"
    image_files = loadimages.load_images(image_folder)

    avg_image = averageimages.average_images(image_files)
    output_path = "./average_image.jpg"
    print(avg_image)
    cv2.imwrite(output_path, avg_image)
    cv2.imshow('Average Image', avg_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()

