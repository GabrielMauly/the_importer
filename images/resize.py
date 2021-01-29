import cv2


image = cv2.imread('fone22.jpeg')


image = cv2.resize(image, (480, 480), fx=0.5, fy=0.5)

cv2.imwrite('test.jpg', image)