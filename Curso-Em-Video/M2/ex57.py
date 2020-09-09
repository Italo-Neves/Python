# -*- coding: utf-8 -*-
sexo = str(input('Digite o seu sexo [M] para masculino ou [F] para feminino')).strip().upper()[0]
while sexo not in 'MmFf':
   sexo =str(input('Digie um valor valido[M/F]: '))
print('Dado registrado com sucesso!')
