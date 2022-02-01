import cv2 as cv
import sys

img = cv.imread("data/imgs/starry_night.jpeg")
cv.imshow("test", img)

k = cv.waitKey(10000)

if k == ord('s'):
    sys.exit()