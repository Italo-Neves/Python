# -*- coding: utf-8 -*-
n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n != 999:
        s = s + n
        c += 1
print(f'Você digitou {c} numeros e a soma deles é: {s} ')
