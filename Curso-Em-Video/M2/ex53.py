# -*- coding: utf-8 -*-
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#dividindo as palavras  
junto =''.join(palavras)#juntando todas as palavras sem espaço
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos im palíndromo')
print(junto, inverso)
