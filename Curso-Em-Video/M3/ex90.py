aluno ={}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] < 7:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')