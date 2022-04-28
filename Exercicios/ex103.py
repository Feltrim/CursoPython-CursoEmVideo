print('Ficha do Jogador\n')


def ficha(jog ='<Desconhecido>', gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = input('Nome do jogador\n>>>>> ')
g = input('Número de gols\n>>>>> ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
