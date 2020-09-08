# -*- coding: utf-8 -*-
r1 = float(input('Digite o valor da reta 01: '))
r2 = float(input('Digite o valor da reta 02: '))
r3 = float(input('Digite o valor da reta 03:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    triangulo = True
    print('Esse valores geram um triagunlo ')
else:
    triagunlo = False
    print('Esse valores não geram um triagunlo')

if triangulo == True and r1 == r2 == r3:
    print('Por possuir todos os lados iguais esse triagunlo é EQUILATERO')
elif triangulo == True and r1 == r2 != r3  or r2 == r3 != r1 or r3 == r1 != r2:
    print('Por possuir dois lados iguais esse triangulo é isórceles')
elif triangulo == True and r1 != r2 != r3:
    print('Por possuir todos os lados diferentes esse triangulo é Escaleno')

