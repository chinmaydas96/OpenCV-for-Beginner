# Getting started with image

## Reading, Displaying and Saving Images

### OpenCV functions :

#### Read Image :
	
* retval = cv2.imread(filename[, flags])
  
* flags :
  * cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
  * cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
  * cv2.IMREAD_UNCHANGED or -1: Loads image using its original channels, which could include the alpha channel.

#### Write image 
* cv2.imwrite(filename, img[, params])
* It expect BGR format image to be saved.
  
* parameters :
  1. filename: This can be an absolute or a relative path.
  2. img: Image or Images to be saved. 

#### Swap the color channel :
	* image[:,:, ::-1]

#### Change color of image :
	
* dst = cv2.cvtColor(src, code)
* parameters : 
    * src: input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision floating-point.
    * code: color space conversion code (see ColorConversionCodes below).
    * ex1: cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    * ex2: cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#### Split and merge of the image :
	
* split() Divides a multi-channel array into several single-channel arrays.
* merge() Merges several arrays to make a single multi-channel array. All the input matrices must have the same size.


#### Resize image :

* dst = cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    * cv2.resize(image, None, fx = 2, fy = 2)
    * cv2.resize(image, dsize = (w,h), interpolation = cv2.INTER_AREA)
    * cv2.resize(image, dsize = (w,h), interpolation = cv2.INTER_AREA)


#### Flipping image :

* dst = cv2.flip(src, flipCode[, dst])
* parameters :
    * src: input image
    * flipCode: a flag to specify how to flip the array; 
      * 0 means flipping around the x-axis 
      * Positive value (for example, 1) means flipping around y-axis. 
      * Negative value (for example, -1) means flipping around both axes.
        
### Annotating Image
#### Drawing a Line
---
* img = cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])

* The function has 4 required arguments:
  * img: Image on which we will draw a line
  * pt1: First point (x, y) location of the line segment
  * pt2: Second point of the line segment
  * color: Color of the line which will be drawn

  Optional arguments that are commonly used include:
  * thickness: Integer specifying the line thickness. Default value is 1.
  * lineType: Type of the line. Default value is cv2.LINE_8 which stands for an 8-connected line. Usually, cv2.LINE_AA (antialiased or smooth line) is used for the lineType.

#### Drawing a Circle
* img = cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
  * The function has 4 required arguments:
    * img: Image on which we will draw a line
    * center: Center of the circle
    * radius: Radius of the circle
    * color: Color of the circle which will be drawn

  * Optional arguments that are commonly used include:
    * thickness: Thickness of the circle outline (if positive). If a negative value is supplied for this argument, it will result in a filled circle.
    * lineType: Type of the circle boundary. This is exact same as lineType argument in cv2.line()
        
#### Drawing a Rectangle
* img = cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
* The function has 4 required arguments:
  * img: Image on which the rectangle is to be drawn.
  * pt1: Vertex of the rectangle. Usually we use the top-left vertex here.
  * pt2: Vertex of the rectangle opposite to pt1. Usually we use the bottom-right vertex here.
  * color: Rectangle color
* Optional arguments that are commonly used include:
  * thickness: Thickness of the circle outline (if positive). If a negative value is supplied for this argument, it will result in a filled rectangle. 
  * lineType: Type of the circle boundary. This is exact same as lineType argument in cv2.line()


#### Adding Text
* img = cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
* The function has 6 required arguments:
  * img: Image on which the text has to be written. 
  * text: Text string to be written. 
  * org: Bottom-left corner of the text string in the image. 
  * fontFace: Font type 
  * fontScale: Font scale factor that is multiplied by the font-specific base size. 
  * color: Font color
* Optional arguments that are commonly used include:
  * thickness: Integer specifying the line thickness for the text. Default value is 1. 
  * lineType: Type of the line. Default value is 8 which stands for an 8-connected line. Usually, cv2.LINE_AA (antialiased or smooth line) is used for the lineType.
  
