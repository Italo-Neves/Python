# -*- coding: utf-8 -*-
a1 =int(input('Digite o primeiro termo da PA: '))
r =int(input('Digite a razão: '))
termo = a1
cont = 1
total =0
mais = 10
while mais != 0:
    total = total + mais
    while cont<= total:
        print(f'{termo} => ', end=' ')
        termo += r
        cont +=1
    mais = int(input('\nDeseja mostrar quantos termos a  mais? '))
print(f'Total de termos usados {total}')
print('fim')
