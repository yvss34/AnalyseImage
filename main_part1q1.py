import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Images2020/lisa.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

cv2.imshow('image', img)
cv2.imshow('gray', gray)

plt.plot(hist, color='black')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
