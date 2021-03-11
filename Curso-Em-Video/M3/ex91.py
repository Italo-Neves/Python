from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
rankng = []

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
rankng = sorted(jogo.items(), key=itemgetter(1), reverse=True)# usa a função itemgeter para pegar os valores das chavers e ordenalos

for i, v in enumerate(rankng):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)