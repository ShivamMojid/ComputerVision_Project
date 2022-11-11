# # Import required packages
# import cv2
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\KARAN\AppData\Local\Tesseract-OCR\tesseract.exe'

# reading image
img = cv2.imread('5.jpeg')

widthImg = 1365
heightImg = 400

img = cv2.resize(img, (widthImg, heightImg))

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow("Thresh :",threshold)
# cv2.waitKey(0)

# using a findContours() function
contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing names of shapes
for contour in contours:

	# here we are ignoring first counter because
	# findcontour function detects whole image as shape
	if i == 0:
		i = 1
		continue

	# cv2.approxPloyDP() function to approximate the shape
	approx = cv2.approxPolyDP(
		contour, 0.01 * cv2.arcLength(contour, True), True)
	
	# using drawContours() function
	cv2.drawContours(img, [contour], 0, (0, 0, 255), 2)

	# finding center point of shape
	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

    
	if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            ratio = float(w)/h
            if ratio >= 0.9 and ratio <= 1.1:
                pass
                # img = cv2.drawContours(img, [contour], -1, (0,255,255), 3)
                # cv2.putText(img, 'Square', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            else:
                cv2.putText(img, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                img = cv2.drawContours(img, [contour], -1, (0,255,0), 3)

cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
