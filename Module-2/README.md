#  Module 2 - Basic Image Operations

## Addition / Subtraction: Changes the Image Brightness
---
* Adding a constant value to the intensity of each pixel in an image will increase the brightness of the image.
* Likewise, subtracting a constant value from each pixel will decrease the brighhtness of an image.

* dst = cv2.add(src1, src2[, dst[, mask[, dtype]]])
* dst: Is the output image of the same size and depth as src1 and src2.

* The function has 2 required arguments:

  * src1: first input array or a scalar.
  * src2: second input array of or a scalar the same size and the same type as src1.

* The function has 2 optional argument:

  * mask: optional operation mask - 8-bit single channel array, 
    that specifies elements of the output array to be changed.
  * dtype: optional depth of the output array.


## Multiplication: Changes the Image Contrast
---
* Multiplying the intensity values of an image by a constant value (greater or less than 1) 
  will change the contrast of the image.
* Contrast is defined by the difference in the intensity values within an image.
* Multiplying by a factor less than one results in a lower contrast image and vice versa.
* dst = cv2.multiply(src1, src2[, dst[, scale[, dtype]]])

* The function has 2 required arguments:

  * src1: first input array.
  * src2: second input array of the same size and the same type as src1.

* The function has 2 optional argument:
  * scale: optional scale factor.
  * dtype: optional depth of the output array.

* Either we can multiply or we can use the scale option

### Handling Overflow using np.clip()
* np.clip(cv2.multiply(img , 0, 255)
* np.clip(cv2.multiply(img , min_pixel, max_pixel)


## Thresholding

* Two types of thresholding techniques.
  * Global thresholding
  * Adaptive thresholding

### 1. Global Thresholding

* Binary images are used extensively in computer vision applications, 
  as they allow you to selectively process specific regions of an image, 
  keeping the other regions intact.

* Image thresholding is used to create binary images from grayscale images.

* You can use different thresholds to create different binary images 
  from the same original image using the threshold() function.

* retval, dst = cv2.threshold(src, thresh, maxval, type[, dst])
* dst: The output array of the same size and type and the same number of channels as src.

* The function has 4 required arguments:

  * src: input array (multiple-channel, 8-bit or 32-bit floating point).
  * thresh: threshold value.
  * maxval: maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
  * type: thresholding type (see ThresholdTypes).


### 2. Adaptive Thresholding

* OCR can be accomplished by Thresholding.
* dst = cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])
* The function has 6 required arguments:
  * src: Source 8-bit single-channel image. 
  * maxValue: Non-zero value assigned to the pixels for which the condition is satisfied 
  * adaptiveMethod: Adaptive thresholding algorithm to use, see AdaptiveThresholdTypes. 
                    The BORDER_REPLICATE | BORDER_ISOLATED is used to process boundaries. 
  * thresholdType: Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV, see ThresholdTypes. 
  * blockSize: Size of a pixel neighborhood that is used to calculate a threshold value 
               for the pixel: 3, 5, 7, and so on. 
  * C: Constant subtracted from the mean or weighted mean (see the details below). 
       Normally, it is positive but may be zero or negative as well.


## Logical Operations

### Bitwise Operations on Images

* Example API for bitwise_and(). Others include: bitwise_not(), bitwise_or(), bitwise_xor()
* dst = cv2.bitwise_and( src1, src2[, dst[, mask]] )
* The function has 2 required arguments:

  * src1: first input array or a scalar.
  * src2: second input array or a scalar.
* 
* An important optional argument is:
  * mask: optional operation mask, 8-bit single channel array, 
          that specifies elements of the output array to be changed.


## Alpha Channel

* The alpha channel determines the transparency of a color.
* It's the grayscale fourth channel of an image that has pixel intensities ranging from 0-255. 
* 0 represents full transparency, 255 represents full opacity and intermediate values provide translucency.

#### Split the channel
* b, g, r, a = cv2.split(img)
* cv2.merge([c1, c2])


#### Putwatermark
* We are using addWeighted() function to put the watermarks.
* dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
* The function has 5 required arguments:

  * src: first input array.
  * alpha: weight of the first array elements.
  * src2: second input array.
  * beta: weight of the second array elements.
  * gamma: scalar added to each sum.
  * dtype : optional depth of the output array; 
    when both input arrays have the same depth, dtype can be set to -1, 
    which will be equivalent to src1.depth().
* ex : cv2.addWeighted(roi_2, 1, logo_bgr, 0.6, 0)
