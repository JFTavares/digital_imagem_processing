
linha = 20
coluna = 40

vetor = [[1,2],[3,4],[5,6]]

vetor.append([linha, coluna])

print(vetor[1:])

vetor.pop()

while len(vetor) > 0:
    print(vetor.pop())

teste = len(vetor)
print(vetor[1:])
print(teste)