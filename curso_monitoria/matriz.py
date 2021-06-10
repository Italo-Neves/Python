print("Vamos criar um tabuleiro de tamanho:  N x N")
n=int(input("Valor de N: ") )

for linha in range(n):
    for coluna in range(n):
        print("x  ",end='')
    print()