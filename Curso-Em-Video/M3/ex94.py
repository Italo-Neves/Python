grupo =list()
pessoa = dict()
soma = media =0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma+= pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        resp =str(input('Quer continuar? [S/N].')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO responda S ou N.')
    if resp =='N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media = soma/ len(grupo)
print(f'B) A média de idade é {media:5.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['Sexo'] in'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ', end='')
for p in grupo:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}',end='')
        print()
print('<< ENCERRADO>> ')