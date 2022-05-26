import matplotlib.image as mpimg
from matplotlib import pyplot as plt

img = mpimg.imread("image.jpg")
plt.imshow(img)
plt.show()

red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

imgGray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
plt.imshow(imgGray, cmap='gray')
plt.show()