import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['image.cmap'] = 'gray'


# Create a numpy array of 20x20x1 filled with zero values, equivalent to a black grayscale image.
black_img = np.zeros([20, 20, 1])

# Flatten the image data into a single 1D array.
black_flatten = black_img.ravel()

# Display the image and histogram.
plt.figure(figsize=[18, 4])

plt.subplot(131)
plt.imshow(black_img)
plt.title('Black Image')

plt.subplot(132) 
plt.hist(black_flatten, range = [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('Histogram of black image')
plt.show()
# Press q to close the plot.
plt.close()

# Create a histogram from a binary image.
# Read the image.
img = cv2.imread('checkerboard_18x18.png', cv2.IMREAD_GRAYSCALE)

# Flatten the image data into a single 1D array.
img_flatten = img.ravel()

# Display the image and histograms.
plt.figure(figsize = [18, 4])

plt.subplot(131)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(132) 
plt.hist(img_flatten, 5, [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('5 Bins')

plt.subplot(133)
plt.hist(img_flatten, 50, [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('50 Bins')
plt.show()
# Press q to close the plot.
plt.close()

# Create a histogram from a grayscale image (example 1).
# Read the image.
img = cv2.imread('MNIST_3_18x18.png', cv2.IMREAD_GRAYSCALE)

# Flatten the image data into a single 1D array.
img_flatten = img.ravel()

# Display the image and histograms.
plt.figure(figsize = [18, 4])

plt.subplot(131)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(132)
plt.hist(img_flatten, 5, [0, 256]);
plt.xlim([0, 256])
plt.title('5 Bins')
plt.subplot(133)
plt.hist(img_flatten, 50, [0, 256])
plt.xlim([0, 256])
plt.title('50 Bins')
plt.show()
# Press q to close the plot.
plt.close()

# Create a histogram from a grayscale image (example 2).
# Read the image.
img = cv2.imread('Apollo-8-Launch.jpg', cv2.IMREAD_GRAYSCALE)

# Flatten the image data into a single 1D array.
img_flatten = img.ravel()

# Display the image and histograms.
plt.figure(figsize = [18, 4])
plt.subplot(131)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(132)
plt.hist(img_flatten, 50, [0,256])
plt.xlim([0, 256])
plt.title('50 Bins')
plt.subplot(133)
plt.hist(img_flatten, 256, [0,256])
plt.xlim([0, 256])
plt.title('256 Bins')
plt.show()
# Press q to close the plot.
plt.close()

# Compare calcHist() with plt.hist().
# Read the image.
img = cv2.imread('Apollo-8-Launch.jpg', 0)

# Use calcHist() in OpenCV.
hist = cv2.calcHist(images = [img], channels = [0], mask = None, histSize = [256], ranges = [0,255])

# Flatten the image data.
img_flatten = img.ravel()

# Display the image and histograms.
plt.figure(figsize = [18, 4])
plt.subplot(131)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(132)
plt.plot(hist)
plt.xlim([0, 256])
plt.title('cv2.calcHist()')
plt.subplot(133)
plt.hist(img_flatten,256,[0,256])
plt.xlim([0, 256])
plt.title('np.ravel(), plt.hist()')
plt.show()
# Press q to close the plot.
plt.close()

# Different images with identical histograms.
# Load in the two gradient images.
img_gradient = cv2.imread('linear_graident.png', cv2.IMREAD_GRAYSCALE)
img_noisy = cv2.imread('noisy.png', cv2.IMREAD_GRAYSCALE)

# Flatten the image data into a single 1D arrays.
gradient_flatten = img_gradient.ravel()
noisy_flatten = img_noisy.ravel()

# Display the images and histograms.
plt.figure(figsize = [18, 10])

plt.subplot(221); plt.imshow(img_gradient); plt.title('Linear Gradient')

plt.subplot(222) 
plt.hist(gradient_flatten, range = [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('Histogram of linear gradient')

plt.subplot(223)
plt.imshow(img_noisy)
plt.title('Noisy Image')

plt.subplot(224) 
plt.hist(noisy_flatten, range = [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('Histogram of noisy image')
plt.show()
# Press q to close the plot.
plt.close()

# Color histograms.
# Read the color images.
img = cv2.imread('Emerald_Lakes_New_Zealand.jpg')

# Compute histograms for each color channel for both images.
hist1 = cv2.calcHist([img], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([img], [1], None, [256], [0, 255])
hist3 = cv2.calcHist([img], [2], None, [256], [0, 255])

# Display the images and histogram plots.
plt.figure(figsize = [18, 10])
plt.subplot(221); plt.imshow(img[:, :, ::-1])

plt.subplot(222) 
plt.plot(hist1, 'b')
plt.plot(hist2, 'g')
plt.plot(hist3, 'r') 
plt.xlim([0, 256])
plt.ylim([0, 200000])
plt.show()
# Press q to close the plot.
plt.close()

# Using a mask with calcHist().
# Read the color images.
img = cv2.imread('Emerald_Lakes_New_Zealand.jpg')

# Create a mask to filter the image for the histogram calculation.
mask_hist = np.zeros((img.shape[0], img.shape[1]), dtype = 'uint8')

# Select a region that isolates the green lake.
mask_hist[2100:2400, 1500:2200] =  255

# Create a similar mask to show the selected region in the image (for display purposes only).
# The mask must have the same number of color channels as the image, but each color channel will
# contain the same information.
mat = [mask_hist, mask_hist, mask_hist]
mask_3ch = cv2.merge(mat, 3)

# Create an image that only shows the selected region of interest.
img_roi = cv2.bitwise_and(img, mask_3ch)

# Compute histograms for each color channel for both images.
hist1_lake = cv2.calcHist([img], [0], mask_hist, [256], [0, 255])
hist2_lake = cv2.calcHist([img], [1], mask_hist, [256], [0, 255])
hist3_lake = cv2.calcHist([img], [2], mask_hist, [256], [0, 255])

# Display the images and histogram plots.
plt.figure(figsize = [18, 10])
plt.subplot(223)
plt.imshow(img_roi[:, :, ::-1])
plt.subplot(224)
plt.plot(hist1_lake, 'b')
plt.plot(hist2_lake, 'g')
plt.plot(hist3_lake, 'r') 
plt.xlim([0, 256])
plt.ylim([0, 10000])
plt.show()
# Press q to close the plot.
plt.close()

# Histogram Equalization for Grayscale Images.
# Read the image in grayscale format.
img = cv2.imread('parrot.jpg', cv2.IMREAD_GRAYSCALE)

# Display the images.
plt.figure(figsize = (18, 6))
plt.imshow(img)
plt.title('Original Image')
plt.show()
# Press q to close the plot.
plt.close()


# Equalize histogram
img_eq = cv2.equalizeHist(img)

# Display the images.
plt.figure(figsize = (18, 6))
plt.subplot(121)
plt.imshow(img_eq)
plt.title('Equalized Image')
plt.subplot(122)
plt.hist(img_eq.ravel(), 256, [0, 256])
plt.title('Equalized Histogram')
plt.show()
# Press q to close the plot.
plt.close()

# Histogram Equalization for Color Images.
# Read color image
img = cv2.imread('parrot.jpg')
img_eq = np.zeros_like(img)

# Peform histogram equalization on each channel separately.
for i in range(0, 3):
    img_eq[:, :, i] = cv2.equalizeHist(img[:, :, i])

# Display the images.
plt.figure(figsize = (18, 6))
plt.subplot(121)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')
plt.subplot(122)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Wrong Equalized Image')
plt.show()
# Press q to close the plot.
plt.close()

# Right way to histogram equalise color image.
# Convert to HSV.
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Perform histogram equalization only on the V channel, for value intensity.
img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:, :, 2])

# Convert back to BGR format.
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

# Display the images.
plt.figure(figsize = (18, 6))
plt.subplot(121)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')
plt.subplot(122)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')
plt.show()
# Press q to close the plot.
plt.close()

# Compare.
# Display the histograms.
plt.figure(figsize = [15,4])
plt.subplot(121)
plt.hist(img.ravel(),256,[0,256])
plt.title('Original Image')
plt.subplot(122)
plt.hist(img_eq.ravel(),256,[0,256])
plt.title('Histogram Equalized')
plt.show()
# Press q to close the plot.
plt.close()