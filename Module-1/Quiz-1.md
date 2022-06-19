1. WEBP, PNG, GIF support transparency channel.

2. if in cv2.imread function cv2.IMREAD_UNCHANGED flag is called, 
   then number of output image channel will depend on the input image.

3. image.shape = (height, width, channel)

4. resized = cv2.resize(img, (width,height), interpolation = cv2.INTER_LINEAR)

5. If we use imread() function to read a grayscale image as a color image using 
   the cv2.IMREAD_COLOR flag, then image will be stored with 3 channel
   with same value of gray scale channel.

6. x = [[50, 100],
       [50, 100(x)]]
    if we print x[50:100, 50:100] we will get bottom right pixel marked as x.
    