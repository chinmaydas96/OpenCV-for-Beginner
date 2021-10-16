# Getting started with image

## Image formation :

* size of image -> focal length
* Height of image -> (1 / Distance)

---

## Reading, Displaying and Saving Images

### OpenCV functions :

* Read Image :
	
	* retval = cv2.imread(filename[, flags])
	
	* flags :
	
	1. cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
	2. cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
	3. cv2.IMREAD_UNCHANGED or -1: Loads image using its original channels, which could include the alpha channel.

* Write image 
	* cv2.imwrite(filename, img[, params])
	
	* parameters :

		1. filename: This can be an absolute or a relative path.
		2. img: Image or Images to be saved. 

* Swap the color channel :
	* image[:,:, ::-1]

* Change color of image :
	
	* dst = cv2.cvtColor(src, code)
	* parameters : 
		* src: input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision floating-point.
		* code: color space conversion code (see ColorConversionCodes below).

* Split and merge of the image :
	
	* split() Divides a multi-channel array into several single-channel arrays.
	* merge() Merges several arrays to make a single multi-channel array. All the input matrices must have the same size.






