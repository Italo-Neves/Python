"""
# Tratamento de erros
- Erros de semantica são extremamente comuns, devido a erros ou mau uso do programa por parte do usúario ou por desatenção
do programador, para  resolver isso usamos o "try" da seguinte maneira:

    try:
        codigo x
    except:
        retorno

- Onde o código x é o bloco que o programa tentará execultar e o retorno é a menssagem de erro para o usuario, isso
que o programa "trave" e fique inútilizado para o usúario

"""
# Exemplo
"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # podemos ter varios exeptions para varios tipos de erros
    print(f'Problema encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally: # -> o que vai ocorrer sempre independente de ocorrido um erro ou não
    print('Volte sempre!')
"""
# Exemplo2
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou!')
except(ZeroDivisionError):
    print('Não é possivel dividir por zero!')
except KeyboardInterrupt:
    print('O usúario preferiu não informar os dados! ')
else:
    print(f'O resultado é {r:1.f}')
finally: # -> o que vai ocorrer sempre independente de ocorrido um erro ou não
    print('Volte sempre!')
