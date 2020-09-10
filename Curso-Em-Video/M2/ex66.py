# -*- coding: utf-8 -*-
c = 0
s = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        s += n
        c += 1
    if n == 999:
        break
print(f'Você digitou {c} números a soma de todos eles é: {s}')
