# -*- coding: utf-8 -*-
a1 =int(input('Digite o primeiro termo da PA: '))
r =int(input('Digite a razão: '))
termo = a1
cont = 1
while cont<= 10:
    print(f'{termo} => ', end=' ')
    termo += r
    cont +=1
