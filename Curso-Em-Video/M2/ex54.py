# -*- coding: utf-8 -*-
c = 1
maior = 0
for i in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    c += 1
    idade = 2020 - ano
    if idade >= 18:
        maior += 1
print(f'Das 7 pessas {maior} atigiram a maior idade!')

