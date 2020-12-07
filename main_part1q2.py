import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Images2020/barbara.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# creating a Histograms Equalization
equalized = cv2.equalizeHist(gray)

hist = cv2.calcHist([equalized], [0], None, [256], [0, 256])

cv2.imshow('image', equalized)

plt.plot(hist, color='black')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()