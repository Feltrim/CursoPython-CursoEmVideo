print('Lista composta e análise de dados\n')

dados = list()
temp = list()
mai = men = 0
while True:
    temp.append(input('Nome: ').strip().capitalize())
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    dados.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [Sim / Não]\n>>>>> ').strip()[0]
    if resp in 'Nn':
        break
print()
print('-=' * 30)
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {mai:.1f}Kg. Peso de ', end='')
for p in dados:
    if p[1] == mai:
        print(f'\033[1;31m{p[0]} ', end='')
print('\033[m')
print(f'O menor peso foi de {men:.1f}Kg. Peso de ', end='')
for p in dados:
    if p[1] == men:
        print(f'\033[1;31m{p[0]} ', end='')
print('\033[m')
