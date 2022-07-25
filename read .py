import cv2 as cv

img = cv.imread('photos\lady.jpg')

cv.imshow('lady', img)

cv.waitKey(0)
