i =0
m =[]
for l in range(1):
    for c in range(0,i):
        op = True
        while op ==True:
            m[l][c] = int(input(f'Digite um valor para linha e coluna {l} e {c}'))
            op = int(input('Deseja continuar?'))
            if op == False:
                break
for l in range(1):
    for c in range(0,i):
