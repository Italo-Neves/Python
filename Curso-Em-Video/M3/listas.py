# -*- coding: utf-8 -*-
"""
#Listas são variaveis compostas mutaveis
    * Podemos adicionar itens a uma lista com o cumando append()
        ex: lista.append('x') -> adiciona o elemento 'x' na lista
    * Podemos definir onde será adicionado o novo item com o comando insert()
        ex: lista.insert(0,'x') -> adicion o elemento 'x' na posição 0 da lista
    * Podemos apagar intens de uma lista com o comando del, pop ou remove
        ex: -  del lista[x] -> deleta o elemento  xº elemento da lista.
            - lista.pop(x) -> deleta o xº elemento da lista, caso não receba nenhum parametro o ultimo elemento da lista será deletado.
            - lista.remove('x') deleta o VALOR 'x' da lista.

    * Podemos utilizar os operadore if in para verificar a existencia
      de determinados itens na lista.

    * Podemos utilizar o range para criar uma lista.
        ex: lista = list(range(4,11)) -> gera a lista :[4,5,6,7,8,9,10]
        OBS: o enumerate também funciona em listas

    * Podemos utilizar o metodo sort para ordenar os valores de uma lista
        ex: lista.sort()
        obs: caso queia a ordem inversa utilize o parametro reverse =True
            ex: lista.sort(reverse=True)
    * Podemos usar o len para contar os elementos de uma lista
        ex: lista.len()
"""
num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(2)
print(num)
num.remove(2)#remover ira remover o primeiro elemento de valor '2' da esquerda para a direita
num.sort()
print(num)
num.sort(reverse=True)
print(num)
a = [2,3,4,7]
# a = b -> neste caso estamos ligando duas listas de forma que a alteração em uma seja repetida na outra
b = a[:] # -> neste caso estamos fazendo com que 'b' receba todos os itens de 'a' em outras palavras estamos fazendo uma copia de 'b'
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

