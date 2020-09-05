# -*- coding: utf-8 -*-
x = input("Digite algo: ")
print(f'O tipo primitivo deste valor é: {type(x)}')
print(f'Só tem espaços? {x.isspace()}')
print(f'so tem numero? {x.isnumeric()}')
print(f'É alfanumerico? {x.isalpha()}')
print(f'Está entre maiusculas? {x.isupper()}')
print(f'está em minusculas? {x.islower()}')
print(f'Está capitalizada? {x.istitle()}')
