import cv2
import numpy as np

# Read the image in a 3 channel color format.
img = cv2.imread('opencv_logo_scr.png', cv2.IMREAD_COLOR)
# Display.
cv2.imshow('Orginal Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert the Image to HSV.
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define Lower and Upper HSV color bounds.
# Set range for red color.
r_lb = np.array([165, 50, 50], np.uint8)
r_ub = np.array([180, 255, 255], np.uint8)

# Set range for green color.
g_lb = np.array([35, 50, 50], np.uint8)
g_ub = np.array([80, 255, 255], np.uint8)

# Set range for blue color.
b_lb = np.array([95, 50, 50], np.uint8)
b_ub = np.array([125, 255, 255], np.uint8)

# Define a Color Mask for each Color.
# Define each color mask.
r_mask = cv2.inRange(img_hsv, r_lb, r_ub)
g_mask = cv2.inRange(img_hsv, g_lb, g_ub)
b_mask = cv2.inRange(img_hsv, b_lb, b_ub)

# Display each color mask.
cv2.imshow('Red mask', r_mask)
cv2.imshow('Green mask', r_mask)
cv2.imshow('Blue mask', r_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Segment the colors.
r_seg = cv2.bitwise_and(img, img, mask = r_mask)
g_seg = cv2.bitwise_and(img, img, mask = g_mask)
b_seg = cv2.bitwise_and(img, img, mask = b_mask)

# Display the segmented colors.
cv2.imshow('Red Color Segmented', r_seg)
cv2.imshow('Green Color Segmented', g_seg)
cv2.imshow('Blue Color Segmented', b_seg)
cv2.waitKey(0)
cv2.destroyAllWindows()