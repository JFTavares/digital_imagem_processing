import numpy as np
import cv2

img = cv2.imread('trabalho_coracao.png', 0)

cv2.imshow('Imagem Original',img)


ret,binary_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
row, column = binary_img.shape

valor_branco = 255
#new_img = np.array(binary_img)
new_img = np.zeros(shape=(row, column))

matrix = np.zeros(shape=(row, column))
vetor = []
cor = 100

print(new_img)

def pixel_acima(linha, coluna):
    return linha-1, coluna

def pixel_esquerda(linha, coluna):
    return linha, coluna-1

def pixel_direita(linha, coluna):
    return linha, coluna+1

def pixel_abaixo(linha, coluna):
    return linha+1, coluna


def aumento_regiao(linha, coluna, cor):
    vetor.append([linha, coluna])
    matrix[linha, coluna] = 1
    new_img[linha, coluna] = cor

    while len(vetor) > 0:
        pixel_analisado = vetor.pop()

        if binary_img[pixel_acima(pixel_analisado[0], pixel_analisado[1])] == 255 and matrix[
            pixel_acima(
                pixel_analisado[0], pixel_analisado[1])] == 0:
            new_img[pixel_acima(pixel_analisado[0], pixel_analisado[1])] = cor
            matrix[pixel_acima(pixel_analisado[0], pixel_analisado[1])] = 1
            vetor.append(pixel_acima(pixel_analisado[0], pixel_analisado[1]))

        if binary_img[pixel_esquerda(pixel_analisado[0], pixel_analisado[1])] == 255 and matrix[
            pixel_esquerda(
                pixel_analisado[0], pixel_analisado[1])] == 0:
            new_img[pixel_esquerda(pixel_analisado[0], pixel_analisado[1])] = cor
            matrix[pixel_esquerda(pixel_analisado[0], pixel_analisado[1])] = 1
            vetor.append(pixel_esquerda(pixel_analisado[0], pixel_analisado[1]))

        if binary_img[pixel_direita(pixel_analisado[0], pixel_analisado[1])] == 255 and matrix[
            pixel_direita(
                pixel_analisado[0], pixel_analisado[1])] == 0:
            new_img[pixel_direita(pixel_analisado[0], pixel_analisado[1])] = cor
            matrix[pixel_direita(pixel_analisado[0], pixel_analisado[1])] = 1
            vetor.append(pixel_direita(pixel_analisado[0], pixel_analisado[1]))

        if binary_img[pixel_abaixo(pixel_analisado[0], pixel_analisado[1])] == 255 and matrix[
            pixel_abaixo(
                pixel_analisado[0], pixel_analisado[1])] == 0:
            new_img[pixel_abaixo(pixel_analisado[0], pixel_analisado[1])] = cor
            matrix[pixel_abaixo(pixel_analisado[0], pixel_analisado[1])] = 1
            vetor.append(pixel_abaixo(pixel_analisado[0], pixel_analisado[1]))


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
                    cor = cor + 50




cv2.imwrite('trabalho_modificada.png', new_img)

img_modificada = cv2.imread('trabalho_modificada.png', 0)
cv2.imshow('Imagem modificada', img_modificada)

cv2.waitKey(0)
cv2.destroyAllWindows()