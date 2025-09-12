import cv2
import numpy as np

img = cv2.imread("img.jpg")
res = cv2.resize(img, dsize=(640,480), interpolation=cv2.INTER_CUBIC)

