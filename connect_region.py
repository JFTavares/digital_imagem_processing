import numpy as np
import cv2
import random

img = cv2.imread('trabalho_coracao.png', 0)

cv2.imshow('Imagem Original',img)


ret,binary_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
row, column = binary_img.shape

valor_branco = 255
#new_img = np.array(binary_img)
new_img = np.zeros(shape=(row, column))

matrix = np.zeros(shape=(row, column), dtype=bool)
vetor = []
cor = 100
listaCores = []
listaCores.append(cor)

print(new_img)

def pixel_acima(pos_pixel):
    return pos_pixel[0]-1, pos_pixel[1]

def pixel_esquerda(pos_pixel):
    return pos_pixel[0], pos_pixel[1]-1

def pixel_direita(pos_pixel):
    return pos_pixel[0], pos_pixel[1]+1

def pixel_abaixo(pos_pixel):
    return pos_pixel[0]+1, pos_pixel[1]


def aumento_regiao(linha, coluna, cor):
    vetor.append([linha, coluna])
    matrix[linha, coluna] = True
    new_img[linha, coluna] = cor

    while len(vetor) > 0:
        analise_pixel = vetor.pop()

        if binary_img[pixel_acima(analise_pixel)] == 255 and matrix[
            pixel_acima(analise_pixel)] == False:
            new_img[pixel_acima(analise_pixel)] = cor
            matrix[pixel_acima(analise_pixel)] = True
            vetor.append(pixel_acima(analise_pixel))

        if binary_img[pixel_esquerda(analise_pixel)] == 255 and matrix[
            pixel_esquerda(analise_pixel)] == False:
            new_img[pixel_esquerda(analise_pixel)] = cor
            matrix[pixel_esquerda(analise_pixel)] = True
            vetor.append(pixel_esquerda(analise_pixel))

        if binary_img[pixel_direita(analise_pixel)] == 255 and matrix[
            pixel_direita(analise_pixel)] == False:
            new_img[pixel_direita(analise_pixel)] = cor
            matrix[pixel_direita(analise_pixel)] = True
            vetor.append(pixel_direita(analise_pixel))

        if binary_img[pixel_abaixo(analise_pixel)] == 255 and matrix[
            pixel_abaixo(analise_pixel)] == False:
            new_img[pixel_abaixo(analise_pixel)] = cor
            matrix[pixel_abaixo(analise_pixel)] = True
            vetor.append(pixel_abaixo(analise_pixel))


for linha in range(row):
    for coluna in range(column):
        if binary_img[linha, coluna] == valor_branco:
            #canto superior esquerdo
            if linha == 0 and coluna == 0 :
                new_img[linha, coluna] = 100

            # linha superior
            elif linha == 0 and coluna > 0 :
                new_img[linha, coluna] = 130

            # coluna esquerda
            elif linha > 0 and coluna == 0 :
                new_img[linha, coluna] = 150

            # coluna direita
            elif linha > 0 and coluna == (column - 1) :
                new_img[linha, coluna] = 180

            # coluna inferior
            elif linha == row-1 and coluna > 0 :
                new_img[linha, coluna] = 0

            # resto
            else:
                if matrix[linha, coluna] == 0:
                    aumento_regiao(linha, coluna, cor)
                    cor = cor + 10
                    listaCores.append(cor)


# Colorizing os pixels
output_img = np.zeros((row, column, 3), int)
labelColor = {0: (0, 0, 0)}
for linha in range(row):
    for coluna in range(column):
        label = new_img[linha, coluna]
        if label in listaCores:
            labelColor[label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            output_img[linha, coluna, :] = labelColor[label]


cv2.imwrite('trabalho_modificada.png', new_img)

img_modificada = cv2.imread('trabalho_modificada.png', 0)
cv2.imshow('Imagem modificada', img_modificada)

cv2.waitKey(0)
cv2.destroyAllWindows()