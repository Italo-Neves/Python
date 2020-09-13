# -*- coding: utf-8 -*-
token = list()
while True:
    name =str(input('Digite o nome do aluno: '))
    grd1 = float(input('Nota 1: '))
    grd2 = float(input('Nota 2: '))
    avg = (grd1 + grd2)/2
    token.append([name,[grd1,grd2],avg])
    op =str(input('Deseja continuar? '))
    if op in 'Nn':
        break
print('-=-'*30)
print(f'{"NO.":<4}{"NOME":10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(token):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*36)
    opn =int(input('Mostrar as notas de qual aluno? (999 interrompe)'))
    if opn ==999:
        print('Finalizando...')
        break
    if opn<= len(token) - 1:
        print(f'Notas de {token[opn][0]} são {ficha[opc][1]}')
