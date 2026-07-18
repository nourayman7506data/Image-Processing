import cv2
import numpy as np

def addition(image, value=50):
    value_img = np.ones(image.shape, dtype=np.uint8) * value
    return cv2.add(image, value_img)

def subtraction(image, value=50):
    value_img = np.ones(image.shape, dtype=np.uint8) * value
    return cv2.subtract(image, value_img)

def division(image, value=2):
    return cv2.divide(image, value)

def complement(image):
    return cv2.bitwise_not(image)