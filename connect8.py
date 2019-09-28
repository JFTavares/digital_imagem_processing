import cv2
import numpy as np
import random

label = []
label_dict = {}

def getLabel(neighbours):

	# If the 8 connected neighbouring pixels are 0 i.e black assign a new label to the pixel
	if all(x==0 for x in neighbours):
		if len(label) == 0:
			label.append(1)
			return max(label)
		else:
			label.append(max(label) + 1)
			return max(label)

	# If all the 8 connected neighbouring pixels are not 0 i.e black
	# case 1: If there are no conflicting labels assign the label to the pixel
	# case 2: If there are conflicting labels assign the smallest label and add an entry in the label dictionary
	else:
		max_label = 0
		min_label = 0

		neighbours = [x for x in neighbours if x != 0]
		neighbours.sort()

		min_label = neighbours[0]
		max_label = neighbours[len(neighbours)-1]

		if max_label == min_label:
			return min_label
		else:
			label_dict[max_label] = min_label
			return min_label


img = cv2.imread('trabalho.png', 0)

cv2.imshow('Imagem Original',img)

ret,binary_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

row, column = binary_img.shape

v = 255
new_img = np.array(binary_img)


# First Pass
for linha in range(row):
	for coluna in range(column):

		# Only interested in pixels with value v [255] i.e white pixels
		if new_img[linha, coluna] == v:

			# Checking for different positions of pixels
			if linha == 0 and coluna == 0:
				new_img[linha, coluna] = getLabel([])

			elif linha == 0 and coluna > 0:
				new_img[linha, coluna] = getLabel([new_img[linha, coluna - 1]])

			elif linha > 0 and coluna == 0:
				new_img[linha, coluna] = getLabel([new_img[linha - 1, coluna], new_img[linha - 1, coluna + 1]])

			elif linha > 0 and coluna == (column - 1):
				new_img[linha, coluna] = getLabel([new_img[linha - 1, coluna - 1], new_img[linha - 1, coluna], new_img[linha, coluna - 1]])

			elif linha > 0 and coluna > 0:
				new_img[linha, coluna] = getLabel([new_img[linha - 1, coluna - 1], new_img[linha - 1, coluna], new_img[linha - 1, coluna + 1], new_img[linha, coluna - 1]])


# Second Pass
for k in range(len(label_dict)):
	for linha in range(row):
	    for coluna in range(column):
	        if new_img[linha][coluna] in label_dict:
	            new_img[linha][coluna] = label_dict[new_img[linha][coluna]]




# Colorizing the labels
output_img = np.zeros((row, column, 3), int)
labelColor = {0: (0, 0, 0)}
for linha in range(row):
    for coluna in range(column):
        label = new_img[linha, coluna]
        if label not in labelColor:
            labelColor[label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

			output_img[linha, coluna, :] = labelColor[label]


cv2.imwrite('output_img.png', output_img)

img_modificada = cv2.imread('output_img.png', 0)
cv2.imshow('Imagem modificada', img_modificada)
cv2.waitKey(0)