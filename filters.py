import cv2
import numpy as np
import pandas as pd
from scipy import ndimage
from scipy.ndimage import generic_filter

# linear filter

def avg_filter(image):
    kernel = np.ones((3, 3), np.float32)/9
    avg_image = cv2.filter2D(image, -1, kernel)
    return avg_image

def laplacian_filter(image):
    kernel = np.array([[1, -2, 1], 
                       [-2, 4, -2], 
                       [1, -2, 1]])
    laplacian_image = cv2.filter2D(image,-1, kernel) 
    return laplacian_image

## non-linear filter

def max_filter(image, size=3):
    max_image = ndimage.maximum_filter(image, size=size)    
    return max_image

def median_filter(image,size=3):
    median_image = cv2.medianBlur(image,size) 
    return median_image

def min_filter(image, size=3):
    min_image = ndimage.minimum_filter(image, size=size)
    return min_image

def mode_filter(image):
    def mode_func(window):
        window = window.astype(np.uint8)  
        return np.bincount(window).argmax()

    return generic_filter(image, mode_func, size=3)