import cv2
import numpy as np

contour_image = cv2.imread(r"c:\Users\91750\Downloads\contours.png")
gray = cv2.cvtColor(contour_image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
i=0
for contour in contours:
    i=i+1
    area = cv2.contourArea(contour)
    
    M = cv2.moments(contour)
    
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    else:
        cx, cy = 0, 0
    
    print(f'Contour{i} : Centroid = ({cx}, {cy}), Area = {area}')
    cv2.drawContours(contour_image, [contour], -1, (255, 255, 0), 2)
    cv2.circle(contour_image, (cx, cy), 5, (0, 0, 255), -1)

cv2.imshow('Final_Image', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()