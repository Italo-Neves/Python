"""
# Funções são rotiinas que execultam código quando são solicitas, elas podem ou não recever parametros
-> def nomefuncao():  -> estrutura basica de uma função
->    codigo
os parametros das funções ficam sempre dentro dos parenteses

"""
"""
# exemplo de funções com parametros: 

def soma(x,y):
    s = x + y
    print(s)
print(soma(8,9))
print(soma(x= 8,y=2 )) # também podemos declarar da seguinte maneira
"""
# usando lista com funções:
"""
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+= 1


valores = [6,3,1,9,2,0]
dobra(valores)
print(valores)
"""
# Desempacotando parametros
"""
def soma(* valores):
    s = 0
    for num in valores:
        s+= num
    print(f'Somando os valores{valores} temos {s}')


soma(5,2)
soma(2,9,4)
"""