jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['gols'] = []
qtd_p = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
for i in range(qtd_p):
    jogador['gols'].append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {i}?')))
jogador['Total'] = sum(jogador['gols'])
print('=-'*30)
print(jogador)
print('=-'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {qtd_p}')
for i,v in enumerate(jogador["gols"]):
    print(f'  =>Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["Total"]} gols')