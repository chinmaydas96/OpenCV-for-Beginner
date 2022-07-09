# Histogram and Color Segmentation
---

## Introduction to Histograms

* retval = plt.hist(x[, bins[, range[, ...]]])

#### Flatten the image data into a single 1D array.
* img_flatten = img.ravel()

#### Compare calcHist() with plt.hist()
* hist = cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
* This function has 5 required arguments:

  * images: Source arrays. They all should have the same depth, CV_8U, CV_16U or CV_32F , 
  and the same size. Each of them can have an arbitrary number of channels.

  * channels: List of the dims channels used to compute the histogram. 
    The first array channels are numerated from 0 to images[0].channels()-1 , 
    the second array channels are counted from images[0].channels() to
    images[0].channels() + images[1].channels()-1, and so on.

  * mask: Optional mask. If the matrix is not empty, it must be an 8-bit array of the same size as images[i] . 
          The non-zero mask elements mark the array elements counted in the histogram.
  
  * histSize: Array of histogram sizes in each dimension.
  * ranges: Array of the dims arrays of the histogram bin boundaries in each dimension.
  * ex : hist1 = cv2.calcHist([img], [0], None, [256], [0, 255])

---

### Histogram Equalization

* An image histogram is a graphical representation of the tonal distribution of data. 
* Each histogram is simply an array with 256 bins, and each bins contains the number of pixels with that intensity. 
* Histogram Equalization is a non-linear method for enhancing contrast in an image.
* dst = cv2.equalizeHist(src[, dst])

### Right Histogram Equalization for color image

* Normal Histogram equalization perform on the three channels separately leads to poor results. 
* The reason is that when each color channel is non-linearly transformed independently. 
* You can get completely new and unrelated colors.
* The right way to transform the images to a space like the HSV colorspace 
  where colors/hue/tint is separated from the intensity.

  * WORKFLOW
    * Transform the image to HSV colorspace.
    * Perform histogram equalization only on the V channel.
    * Transform the image back to RGB colorspace.

```Python
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Perform histogram equalization only on the V channel, for value intensity.
img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:, :, 2])
# Convert back to BGR format.
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
```

## Color Segmentation
---

### Define a Color Mask for each Color

* dst = cv2.inRange(src, lowerb, upperb[, dst]) 
* The function has 3 required arguments:

  * src: first input array
  * lowerb: inclusive lower boundary array or a scalar
  * upperb: inclusive upper boundary array or a scalar

---
### Count non-zero pixels
* c = cv2.countNonZero(gray_img)
