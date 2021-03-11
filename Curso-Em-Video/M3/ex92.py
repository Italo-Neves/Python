from datetime import datetime
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano_nasc'] = int(input('Ano de nascimento: '))
pessoa['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))

now = datetime.now()
pessoa['idade'] = now.year - pessoa['Ano_nasc']
if pessoa['Ctps'] !=0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salário: '))
    pessoa['Aposentadora'] = pessoa['idade'] + (pessoa['contratacao'] + 35) - now.year
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
else:
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')