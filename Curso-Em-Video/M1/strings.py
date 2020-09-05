# -*- coding: utf-8 -*-
"""
* podemos fatiar uma string da seguinte maneira:
    -> frase = 'curso em video python'
        -> cada letra representa um espaço na memoria no total temos 21(contando com os espaços)
    frase[9:21]
        -> o Comando a cima indica que queremos mostra do espaço nove até o 20(o ultimo sempre é ignorado)
    frase[9:21:2]
        -> o terceiro parametro indica que iremos percorrer de 9 a 20 de 2 em 2 casas
    frase[:5]
        -> do 0 até o 4
    frase[15:]
        -> do 15 até o fim
    fase[3::9]
        -> de 3 a 9 pulando de 3 em 3
* funções
   # len(frase)
        -> mostra a quantidade de caracteres que a string possui(neste caso 21)
   # frase.count('o')
        -> conta a quantidade de caracteres 'o' existem dentro da string
        -> Podemos usar o fatiamento adicionando mais dois parametros ex: fase.cont('o',0,13)
           conte 'o' de 0 a 13
   # fase.find('deo')
        -> mostra o numeros da string relacionados aos caracteres especificados, em outras palavras
        em que numero começa a sequencia 'deo' caso o parametro não exista na string a função retornra
        -1
   # 'curso' in frase
        -> verifica se existe a string curso em frase
   #fase.replace('python','android')
        -> troca o primeiro parametro pelo segundo
   # fase.lower()
        -> deixa minusculo
   #fase.upper()
        -> deixa maiusculo

   #fase.capitalize()
        -> deixa apenas o primeiro caracter maiusculo

   #frase.title()
        -> A primeira letra de todas as palavras da string será maiscula
   #frase.strip()
        -> remove os espaços vazios no inicio e no fim da string
        -> lstrip remove os espaços da esquerda
   #frase.split()
        -> gera uma lista com as palavras separadas entre espaços da string
   #'-'.join(frase)
        -> transfor uma lista em uma string única, o que vem antes do ponto ficara entre as strings unidas.


"""
frase = 'Curso em video python'
print(frase.count('O'))
