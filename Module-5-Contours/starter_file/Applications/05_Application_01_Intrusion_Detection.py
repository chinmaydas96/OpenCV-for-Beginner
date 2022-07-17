import cv2
import numpy as np

source = './intruder_1.mp4'

video_cap = cv2.VideoCapture(source)
if not video_cap.isOpened():
    print('Unable to open: ' + source)

frame_w = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_h = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video_cap.get(cv2.CAP_PROP_FPS))

size = (frame_w, frame_h)
size_quad = (int(2*frame_w), int(2*frame_h))

video_out_alert_file = 'video_out_alert_1.mp4'
video_out_quad_file = 'video_out_quad_1.mp4'

# Create video writer objects.
video_out_alert = cv2.VideoWriter(video_out_alert_file, cv2.VideoWriter_fourcc(*'XVID'), fps, size)
video_out_quad = cv2.VideoWriter(video_out_quad_file, cv2.VideoWriter_fourcc(*'XVID'), fps, size_quad)

def drawBannerText(frame, text, banner_height_percent = 0.08, font_scale = 0.8, text_color = (0, 255, 0), 
                   font_thickness = 2):
    # Draw a black filled banner across the top of the image frame.
    # percent: set the banner height as a percentage of the frame height.
    banner_height = int(banner_height_percent * frame.shape[0])
    cv2.rectangle(frame, (0, 0), (frame.shape[1], banner_height), (0, 0, 0), thickness = -1)

    # Draw text on banner.
    left_offset = 20
    location = (left_offset, int(10 + (banner_height_percent * frame.shape[0]) / 2))
    cv2.putText(frame, text, location, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, 
                font_thickness, cv2.LINE_AA)

bg_sub = cv2.createBackgroundSubtractorKNN(history = 200)

ksize = (5, 5)        # Kernel size for erosion.
max_contours = 3      # Number of contours to use for rendering a bounding rectangle.
frame_count = 0
frame_start = 5       # Allow this number of frames to bootstrap the generation of a background model.
red    = (0, 0, 255)
yellow = (0, 255, 255)
green  = (0, 255, 0)

# Quad view that will be built.
#----------------------------------------
# frame_fg_mask         :  frame
# frame_fg_mask_erode_c :  frame_erode_c
#----------------------------------------

# Process video frames.
while True: 
    ret, frame = video_cap.read()
    frame_count += 1
    if frame is None:
        break
    else:
        frame_erode_c = frame.copy()
        
    # Stage 1: Create a foreground mask for the current frame.
    fg_mask = bg_sub.apply(frame)
    
    # Wait a few frames for the background model to learn.
    if frame_count > frame_start:
    
        # Stage 1: Motion area based on foreground mask.
        motion_area = cv2.findNonZero(fg_mask)
        if motion_area is not None:
            x, y, w, h = cv2.boundingRect(motion_area)
            cv2.rectangle(frame, (x, y), (x + w, y + h), red, thickness=2)
            drawBannerText(frame, 'Intrusion Alert', text_color=red)

        # Stage 2: Stage 1 + Erosion.
        fg_mask_erode_c = cv2.erode(fg_mask, np.ones(ksize, np.uint8))
        motion_area_erode = cv2.findNonZero(fg_mask_erode_c)
        if motion_area_erode is not None:
            xe, ye, we, he = cv2.boundingRect(motion_area_erode)
            cv2.rectangle(frame_erode_c, (xe, ye), (xe + we, ye + he), red, thickness=2)
            drawBannerText(frame_erode_c, 'Intrusion Alert', text_color=red)

        # Convert foreground masks to color so we can build a composite video with color annotations.
        frame_fg_mask = cv2.cvtColor(fg_mask, cv2.COLOR_GRAY2BGR)
        frame_fg_mask_erode_c = cv2.cvtColor(fg_mask_erode_c, cv2.COLOR_GRAY2BGR)

        # Stage 3: Stage 2 + Contours.
        contours_erode, hierarchy = cv2.findContours(fg_mask_erode_c, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours_erode) > 0:

            # Annotate eroded foreground mask with cotours.
            cv2.drawContours(frame_fg_mask_erode_c, contours_erode, -1, green, thickness=2)

            # Sort contours based on area.
            contours_sorted = sorted(contours_erode, key = cv2.contourArea, reverse=True)
            
            # Compute bounding rectangle for the top N largest contours.
            for idx in range(min(max_contours, len(contours_sorted))):
                xc, yc, wc, hc = cv2.boundingRect(contours_sorted[idx])
                if idx == 0:
                    x1 = xc
                    y1 = yc
                    x2 = xc + wc
                    y2 = yc + hc
                else:
                    x1 = min(x1, xc)
                    y1 = min(y1, yc)
                    x2 = max(x2, xc + wc)
                    y2 = max(y2, yc + hc)

            # Draw bounding rectangle for top N contours on output frame.
            cv2.rectangle(frame_erode_c, (x1, y1), (x2, y2), yellow, thickness=2)
            drawBannerText(frame_erode_c, 'Intrusion Alert', text_color=red)

        # Annotate each video frame.
        drawBannerText(frame_fg_mask, 'Foreground Mask')
        drawBannerText(frame_fg_mask_erode_c, 'Foreground Mask (Eroded + Contours)')

        # Build quad view.
        frame_top = np.hstack([frame_fg_mask, frame])
        frame_bot = np.hstack([frame_fg_mask_erode_c, frame_erode_c])
        frame_composite = np.vstack([frame_top, frame_bot])

        # Annotate quad view with dividers.
        fc_h, fc_w, _ = frame_composite.shape
        cv2.line(frame_composite, (int(fc_w/2), 0), (int(fc_w/2), fc_h), yellow , thickness=3, lineType=cv2.LINE_AA)
        cv2.line(frame_composite, (0, int(fc_h/2)), (fc_w, int(fc_h/2)), yellow, thickness=3, lineType=cv2.LINE_AA)

        # Write video output files.
        video_out_alert.write(frame_erode_c)    # Alert 
        video_out_quad.write(frame_composite)   # Analysis quad view
        # Resize for proper view.
        frame_composite = cv2.resize(frame_composite, None, fx = 0.4, fy = 0.4)
        cv2.imshow('Composite Frame', frame_composite)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

video_cap.release()
video_out_alert.release()
video_out_quad.release()
cv2.destroyAllWindows()

