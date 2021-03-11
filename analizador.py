import re

expression = input("Digite a expresão a ser analizada")

def space(x):
    total_space = 0
    for i in x:
        if x.find(''):
            total_space += 1
            return total_space

print(f'\n Expressão:{expression}'
      f'\n Total de espaçosi: {space(expression)}')
