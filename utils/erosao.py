import cv2
import numpy as np

img= cv2.imread('imagem.jpg',0)
cv2.imshow("Original",img)
kernel=np.ones((1,1),np.uint8)
#kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
erosion=cv2.erode(img,kernel,iterations=1)
cv2.imshow("erosao",erosion)
cv2.waitKey(0)