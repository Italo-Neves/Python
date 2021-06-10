def crie_matriz(linhas, colunas, valor):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor)
        matriz.append(linha)

    return matriz
def escrever_memoria(linha, coluna,matriz):
    linha = int(linha, 2) - 1
    for j in range(len(matriz)):
        if (coluna[j] == "1"):
            matriz[linha][j] = "#"


def imprimir_memoria(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (j < len(matriz) - 1):
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j])