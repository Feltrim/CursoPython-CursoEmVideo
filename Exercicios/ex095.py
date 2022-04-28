print('Aprimorando os Dicionários\n')

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador\n>>>>> ')
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?\n>>>>> '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}?\n>>>>> ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [Sim / Não]\n>>>>> ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas Sim ou Não.')
    if resp == 'N':
        break
print()
print('-=' * 30)
print()
print('COD', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]\n>>>>> '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
