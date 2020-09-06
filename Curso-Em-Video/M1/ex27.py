# -*- coding: utf-8 -*-
nome=str(input("Digite o seu nome completo: ")).strip()
lista= nome.split()
first= lista[0]
last = lista[len(lista)-1]

print(f'\nPrimeiro nome: {first}\nUltimo nome: {last}')
