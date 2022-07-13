import cv2
import numpy as np

input_video = './starter_files/race_car.mp4'
# 0 for webcam
source = input_video

video_cap = cv2.VideoCapture(source)

if not video_cap.isOpened():
    print('Error opening video stream or file')

# ret, frame = video_cap.read()
# cv2.imshow('First frame', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

frame_w = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_h = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_fps = int(video_cap.get(cv2.CAP_PROP_FPS))

fourcc_avi = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
fourcc_mp4 = cv2.VideoWriter_fourcc(*'mp4v')

file_out_avi = 'video_out.avi'
file_out_mp4 = 'video_out.mp4'

frame_fps = int(frame_fps / 3)

out_avi = cv2.VideoWriter(file_out_avi, fourcc_avi, frame_fps, (frame_w, frame_h))
out_mp4 = cv2.VideoWriter(file_out_mp4, fourcc_mp4, frame_fps, (frame_w, frame_h))


def drawBannerText(frame, text, banner_height_percentage =0.05, text_color=(0, 255, 0)):
    banner_height = int(banner_height_percentage * frame.shape[0])
    cv2.rectangle(frame, (0, 0), (frame.shape[1], banner_height), (0,0,0), thickness=-1)

    left_offset = 20
    location = (left_offset, int(5 + (banner_height_percentage * frame.shape[0]) / 2))
    fontScale = 1.5
    fontThickness = 2
    cv2.putText(frame, text, location, cv2.FONT_HERSHEY_PLAIN, fontScale, text_color,
                fontThickness, cv2.LINE_AA)


frame_count = 0
while True:
    ok, frame = video_cap.read()
    if not ok:
        break
    frame_count += 1

    drawBannerText(frame, 'Frame : {} FPS : {}'.format(frame_count, frame_fps))

    out_avi.write(frame)
    out_mp4.write(frame)

video_cap.release()
out_avi.release()
out_mp4.release()
