import cv2
import numpy as np


# define preprocess function
def preprocess(img):
    # This function will resize image to 64x64 and convert it to grayscale
    img = cv2.resize(img, (64, 48))
    img = np.array(img, dtype=np.float32)
    # Flatten image
    img = img.flatten()
    return img
