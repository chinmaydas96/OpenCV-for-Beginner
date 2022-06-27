1. Different methods to convert from RGB to BGR value
    * output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    * output = img[. . ., ::-1] 
    * output = img[:, :, ::-1] 