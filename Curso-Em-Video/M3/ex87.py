# -*- coding: utf-8 -*-
matrix = [[0,0,0],[0,0,0],[0,0,0]]
pair = 0
odd = 0
scol = 0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'Digite o valor [{l}][{c}]: '))
        if matrix[l][c] % 2 ==0:
            pair +=matrix[l][c]
        else:
            odd +=matrix[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]',end ='')
    print()
print(f'A soma dos pares é: {pair}')

for l in range(0,3):
    scol +=matrix[l][2]
print(f'A soma dos elementos da terceira coluna é: {scol}')
for c in range(0,3):
    if c ==0:
        hign = matrix[1][c]
    elif matrix[1][c] > hign:
        hign = matrix[1][c]
print(f'O maior valor da segunda linha é {hign}')
