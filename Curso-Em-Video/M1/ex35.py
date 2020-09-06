# -*- coding: utf-8 -*-
r1 = float(input('Digite o valor da reta 01: '))
r2 = float(input('Digite o valor da reta 02: '))
r3 = float(input('Digite o valor da reta 03:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Esse valores geram um triagunlo ')
else:
    print('Esse valores não geram um triagunlo')


