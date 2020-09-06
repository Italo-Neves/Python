# -*- coding: utf-8 -*-
nome = str(input("Digite o seu nome completo: ")).lower()

cout = nome.count('a')
first = nome.find('a')+1
last = nome.rfind('a')+1
print(f'Recorrencida da letra a: {cout}')
print(f'Posição da primeira letra a :{first}')
print(f'Ultima aparição da letra a: {last}')
