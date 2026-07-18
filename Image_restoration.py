import cv2
import numpy as np

def apply_restoration(img_array, noise_type, method):
    if noise_type == "Salt and pepper noise":
        if method == "Median filter":
            return cv2.medianBlur(img_array, 5)
        elif method == "Average filter":
            return cv2.blur(img_array, (5, 5))
        elif method == "An outlier method":
            mean_f = cv2.blur(img_array, (3, 3))
            diff = cv2.absdiff(img_array, mean_f)
            return np.where(diff > 40, mean_f, img_array)
            
    elif noise_type == "Gaussian noise":
        return cv2.GaussianBlur(img_array, (5, 5), 0)
    return img_array

def apply_morphology(img_array, method, sub_method=None):
    kernel = np.ones((5, 5), np.uint8)
    
    if method == "Image dilation":
        return cv2.dilate(img_array, kernel, iterations=1)
    elif method == "Image erosion":
        return cv2.erode(img_array, kernel, iterations=1)
    elif method == "Image opening":
        return cv2.morphologyEx(img_array, cv2.MORPH_OPEN, kernel)
    
    elif method == "Boundary Extraction":
        kernel_b = np.ones((3, 3), np.uint8)
        erosion = cv2.erode(img_array, kernel_b, iterations=1)
        dilation = cv2.dilate(img_array, kernel_b, iterations=1)
        
        if sub_method == "Internal boundary":
            return cv2.subtract(img_array, erosion)
        elif sub_method == "External boundary":
            return cv2.subtract(dilation, img_array)
        elif sub_method == "Morphological gradient":
            return cv2.subtract(dilation, erosion)
            
    return img_array