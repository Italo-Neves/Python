# -*- coding: utf-8 -*-
listagem = ('lapis',1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',120.32,
            'Caneta',22.30,
            'Livro',34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(f'-' * 40)
for pos in range(0,len(listagem)):
    if pos % 2 ==0: #veja a tupla a cima e perceba que o nome dos produtos estão sempre em posições pares
        print(f'{listagem[pos]:.<30}', end='')# '.<30' -> alinhado a esquerda com 30 caracteres ocupados com pontos 
    else:
        print(f'R${listagem[pos]:>7}')
print('-' * 40)
