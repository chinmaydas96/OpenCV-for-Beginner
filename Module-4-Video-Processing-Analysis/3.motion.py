import cv2
import numpy as np

source = 0
video_cap = cv2.VideoCapture(source)
first_frame = None
frame_count = 0

ksize = (5, 5)
red = (0, 0, 255)
yellow = (0, 255, 255)

knn = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = video_cap.read()
    if frame is None:
        break
    else:
        frame = cv2.resize(frame, (400, 400))
        frame_erode = frame.copy()

    fg_mask = knn.apply(frame)
    motion_area =  cv2.findNonZero(fg_mask)
    x, y, w, h = cv2.boundingRect(motion_area)

    if motion_area is not None:
        cv2.rectangle(frame, (x, y), (x+w, y+h), red, thickness=6)

    fg_mask_erode = cv2.erode(fg_mask, np.ones(ksize, np.uint8))
    motion_area_erode = cv2.findNonZero(fg_mask_erode)
    xe, ye, we, he = cv2.boundingRect(motion_area_erode)

    if motion_area is not None:
        cv2.rectangle(frame_erode, (xe, ye), (xe + we, ye + he), red, thickness=6)

    cv2.imshow('Output', frame)
    cv2.imshow('Mask', fg_mask)
    cv2.imshow('Output with erosion', frame_erode)
    cv2.imshow('Mask with erosion', fg_mask_erode)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()








