# -*- coding: utf-8 -*-
cont = ('zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove',
        'Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezenove','Vinte')

n = int(input('Digite um número de 0 a 20: '))

if n > 20:
    while n>20:
        n = int(input('Por favor digite apenas números de 0 a 20'))
if n <= 20:
    for posi,ext in enumerate(cont):
        if posi == n:
            print(f'Você digitou {ext}')
