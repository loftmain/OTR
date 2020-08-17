import sys
import cv2
import numpy as np
import random


img = cv2.imread('detectcirclesexample.png')

lower_blue = (94, 80, 2)
upper_blue = (120, 255, 255)

lower_green = (25, 52, 72)
upper_green = (102, 255, 255)

# lower_green1 = (71, 100, 50)
# upper_green1 = (80, 255, 255)

lower_red = (0, 106, 186)
upper_red = (179, 255, 255)
#
# lower_orange = (5, 161, 100)
# upper_orange = (13, 255, 255)



kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

canny_min = 5
canny_max = 50


blur = cv2.GaussianBlur(img, (7,7), 7)
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

# inRange
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red = cv2.inRange(hsv, lower_red, upper_red)


blue_edge = cv2.Canny(mask_blue, canny_min, canny_max)
red_edge = cv2.Canny(mask_red, canny_min, canny_max)


blue_edge_thick = cv2.morphologyEx(blue_edge, cv2.MORPH_CLOSE, kernel, iterations=5 )
red_edge_thick = cv2.morphologyEx(red_edge, cv2.MORPH_CLOSE, kernel, iterations=5 )

# orange_edge_thick = cv2.morphologyEx(orange_edge, cv2.MORPH_CLOSE, kernel, iterations=3 )

contours_b, _ = cv2.findContours(blue_edge_thick, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_r, _ = cv2.findContours(red_edge_thick, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, [contours_r[0]], 0, (0,0,0), 3)

# for cnt in contours_r:
#     cv2.drawContours(img, [cnt], 0, (0,0,0), 3)

# print(contours_r[0])
cv2.drawContours(img, [contours_b[0]], 0, (0,0,0), 3)

# BLUE
area = cv2.contourArea(contours_b[0])
x, y, w, h = cv2.boundingRect(contours_b[0])
imageFrame = cv2.rectangle(img, (int(x*0.95), int(y*0.95)),
                           (int((x + w)*1.05), int((y + h)*1.05)),
                           (255, 0, 0), 2)

cv2.putText(img, "Blue Colour", (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0, (255, 0, 0))

# RED
area = cv2.contourArea(contours_r[0])
x, y, w, h = cv2.boundingRect(contours_r[0])
imageFrame = cv2.rectangle(img, (int(x*0.95), int(y*0.95)),
                           (int((x + w)*1.05), int((y + h)*1.05)),
                           (0, 0, 255), 2)

cv2.putText(img, "RED Colour", (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0, (0, 0, 255))
cv2.imshow("", img)

cv2.waitKey()
cv2.destroyAllWindows()