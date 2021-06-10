from Prova.Funcoes import crie_matriz,escrever_memoria,imprimir_memoria
mat_memoria = []


if __name__ == '__main__':
    letra = input("Digite uma letra 'A','B' ou 'C'").upper()
    if letra == 'A':
        matriz = crie_matriz (8,8,".")
        escrever_memoria('00000001', '00011000',matriz)
        escrever_memoria('00000010', '00100100',matriz)
        escrever_memoria('00000011', '01000010',matriz)
        escrever_memoria('00000100', '01111110',matriz)
        escrever_memoria('00000101', '01000010',matriz)
        escrever_memoria('00000110', '01000010',matriz)
        escrever_memoria('00000111', '01000010',matriz)
        escrever_memoria('00001000', '00000000',matriz)

        imprimir_memoria(matriz)
    elif letra == 'B':
        matriz2 = crie_matriz(8, 8, ".")
        escrever_memoria('00000001', '00000000', matriz2)
        escrever_memoria('00000010', '01111110', matriz2)
        escrever_memoria('00000011', '01000001', matriz2)
        escrever_memoria('00000100', '01111110', matriz2)
        escrever_memoria('00000101', '01000010', matriz2)
        escrever_memoria('00000110', '01000001', matriz2)
        escrever_memoria('00000111', '01111110', matriz2)
        escrever_memoria('00001000', '00000000', matriz2)

        imprimir_memoria(matriz2)
    elif letra == 'C':
        matriz3 = crie_matriz(8, 8, ".")
        escrever_memoria('00000001', '00000111',matriz3)
        escrever_memoria('00000010', '00001000', matriz3)
        escrever_memoria('00000011', '00100000', matriz3)
        escrever_memoria('00000100', '01000000', matriz3)
        escrever_memoria('00000101', '01000000', matriz3)
        escrever_memoria('00000110', '00100000', matriz3)
        escrever_memoria('00000111', '00010000', matriz3)
        escrever_memoria('00001000', '00000111', matriz3)
        imprimir_memoria(matriz3)