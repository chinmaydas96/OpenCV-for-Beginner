import cv2
source = 'starter_files/race_car_slow_motion.mp4'
video_cap = cv2.VideoCapture(source)
win_name = 'Video Preview'
cv2.namedWindow(win_name)

while True:
    has_frame, frame = video_cap.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)
    key = cv2.waitKey(1)

    if key == ord('q') or key == ord('Q') or key == 27:
        break

video_cap.release()
cv2.destroyWindow(win_name)

