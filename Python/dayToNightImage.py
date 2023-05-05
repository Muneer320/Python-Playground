import numpy as np
from imageio import imwrite, imread
import cv2
import os

img = imread('DayImg.jpg')
arr = img * np.array([0.1, 0.2, 0.5])
arr2 = (255*arr/arr.max()).astype(np.uint8)

imwrite('2.png', arr2)

img2 = cv2.imread('2.png')

gamma = 2
gammaImg = np.array(255*(img2/255) **gamma, dtype='uint8')

cv2.imwrite('NightImg.png', gammaImg)

os.remove('2.png')

print('Conversion done!')