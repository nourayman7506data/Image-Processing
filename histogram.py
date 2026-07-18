import cv2
import numpy as np

def ensure_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# ===== COLOR OPERATIONS (RGB) =====

def increase_red(image):
    img = image.copy()
    img[:, :, 0] = np.clip(img[:, :, 0] + 50, 0, 255)
    return img


def swap_rg(image):
    img = image.copy()
    img[:, :, [0, 1]] = img[:, :, [1, 0]]
    return img


def remove_red(image):
    img = image.copy()
    img[:, :, 0] = 0
    return img


# ===== GRAYSCALE =====

def to_gray(image):
  
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# ===== HISTOGRAM OPERATIONS =====

def histogram_stretch(image):
    min_val = np.min(image)
    max_val = np.max(image)

    # prevent division error
    if max_val == min_val:
        return image

    return ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)


def histogram_equalization(image):
    return cv2.equalizeHist(image)