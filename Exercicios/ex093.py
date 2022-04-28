print('Cadastro de Jogador de Futebol\n')

jogador = {}
partidas = []
jogador['Nome'] = input('Nome do jogador\n>>>>> ')
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?\n>>>>> '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}?\n>>>>> ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print()
print('-=' * 30)
print(jogador)
print('-=' * 30)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print()
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
