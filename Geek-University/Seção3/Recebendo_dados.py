"""
# Recebendo  dados dos  usúario

input ->  Todo dado receebido via input é do tipo string

Em python, string é tuod que estiver em:
    - Aspas Simples;
    - Aspas duplas;
    - Aspas simples triplas;
    - Aspas duplas triplas;

Exemplos:
    - Aspas Simples -> 'Anjelina jolie'
    - Aspas Duplas -> "angelina"
"""

# Entrada de dados
print('Qual é o seu nome? ')
nome = input() # Input -> entrada

# Exemplos de print 'Antigo' 2.X
# print('Seja bem-vindo(a) %s' %nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo {nome}')

print("Qual é a sua idade? ")
idade = input()
# Processamento

# Saída
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos %' (nome,idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))