# -*- coding: utf-8 -*-
"""
* Podemos importar bibliotecas do python com: import <biblioteca>
    -> Na necessidade de apenas uma função de um modulo especifico: from <biblioteca> import <função>

* Exmplo de modulos usados:
    math -> biblioteco de funções matematicas
        - ceil: Arredonda um valor para cima
        - floor: Arredonda um valor para baixo
        - trunc: Trunca um número(Elimina o que esta depois da virgula)
        - pow: pontenciação
        - sqrt: Calcula a raiz quadrada de um número
        - Fatorial: olha o nome.
    random -> funções com números randomicos
* pesquise o PyId no site oficial do python para ver o index de bibliotecas
"""
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é {raiz}')
