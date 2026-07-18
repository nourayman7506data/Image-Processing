import cv2
import numpy as np

def global_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, res = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return res


def otsu_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, res = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return res


def adaptive_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return cv2.adaptiveThreshold(gray, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 2)


def sobel_edge(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, 3)
    y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, 3)
    res = cv2.magnitude(x, y)
    return np.uint8(np.absolute(res))