import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('imagem.jpg',0)

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('Titulo da imagem',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

