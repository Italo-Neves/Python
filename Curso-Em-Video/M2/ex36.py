# -*- coding: utf-8 -*-
valor = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salario: '))
qtd_anos =int(input('Em quantos anos você pretende pagar?'))

parcela = valor/(qtd_anos*12)
lim = sal + (sal * 30/100)

if parcela > lim:
    print(f'O valor do emprestimo execedeu 30% por tanto não é pssivel realizar o emprestimo')
elif parcela == lim:
    print(f'O emprestimo foi aprovado, com {qtd_anos*12} parcelas de {parcela} ')
else:
    print(f'O emprestimo foi aprovado, com {qtd_anos*12} parcelas de {parcela} ')
