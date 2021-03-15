import modulos2
"""
# Vantagens da modularização
- Organização do código
- Facilidade na manutenção
- Ocultação de código detalhado
- Reutilizar o codigo em outros projetos

"""
num = int(input('Digite um valor'))
fat = modulos2.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {modulos2.dobro(num)}')