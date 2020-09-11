# -*- coding: utf-8 -*-
"""
Tuplas são variaveis compostas imutaveis, que iniciadas com ()
    ex: lanche = ['pudin', 'pizza', 'suco','sanduiche']

    * os metodos de fatiamentos usados em strings podem ser usados em tuplas ex:
        -> print(lanche[1:]) -> comece do suco até o fim da tupla
            'pizza', 'suco','sanduiche'
        -> print(lanche[0:2]) -> vai so do zero até o 1 (o ultimo sempre é ignorado no python)
                'pudin', 'pizza'
        -> print(lanche[2]) -> mostra o segundo elemento da tupla
                'suco'
        -> len(lanche)-> mostra o comprimento da tupla.
        -> podemos somar tuplas.
        -> count(x) mostra quantos vezes 'x' aparece na tupla
        -> lanche.index(x) -> mostra a posição de 'x'.
        -> del(x) -> deleta uma tupla inteira.
    *Podemos usar as tuplas em estruturas de repetição.
            |for c in lanche:|
        ex: |     print (c)i |-> para cada comida em lanche ele irá mostrar uma comida de cada vez
            |                |
    * Além do for podemos utilizar o enumerate para capta o conteudo e a posição.
        ex: for posicao,comida in enumerate(lanche)
"""
#--------------------------TESTES------------------------------------------
lanche = ('sanduiche','suco','Pizza','pudim')
#print(lanche)
#print(lanche[1])
#print(lanche[-2]) -> mostra o sengundo da direita para a esquerda
#print(lanche[1:3])
#print(lanche[:2])
#print(lanche[-3:])
#print(sorted(lanche)) -> mostra na ordem
