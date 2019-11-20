import cv2
import numpy


img = cv2.imread('imagem.jpg')
img_to_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

cv2.imwrite('result.jpg', hist_equalization_result)

img = cv2.imread('imagem.jpg',0)
img_equalizada = cv2.imread('result.jpg',0)

cv2.imshow('Normal',img)
cv2.imshow('Equalizada',img_equalizada)
cv2.waitKey(0)
cv2.destroyAllWindows()