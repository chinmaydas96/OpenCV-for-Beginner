import cv2

# Use source = 0 to specify the web cam as the video source, OR
# specify the pathname to a video file to read.
source = 'race_car_slow_motion.mp4'

# Create a video capture object from the VideoCapture Class.
video_cap = cv2.VideoCapture(source)

# Create a named window for the video display.
win_name = 'Video Preview'
cv2.namedWindow(win_name)

# Enter a while loop to read and display the video frames one at a time.
while True:
    # Read one frame at a time using the video capture object.
    has_frame, frame = video_cap.read()
    if not has_frame:
        break
    # Display the current frame in the named window.
    cv2.imshow(win_name, frame)

    # Use the waitKey() function to monitor the keyboard for user input.
    # key = cv2.waitKey(0) will display the window indefinitely until any key is pressed.
    # key = cv2.waitKey(1) will display the window for 1 ms
    key = cv2.waitKey(0)

    # The return value of the waitKey() function indicates which key was pressed.
    # You can use this feature to check if the user selected the `q` key to quit the video stream.
    if key == ord('Q') or key == ord('q') or key == 27:
        # Exit the loop.
        break

video_cap.release()
cv2.destroyWindow(win_name)
