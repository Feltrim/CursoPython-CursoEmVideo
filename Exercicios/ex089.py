print('Boletim com listas compostas\n')

ficha = list()
while True:
    nome = input('Nome:\n>>>>> ')
    nota1 = float(input('Nota 1:\n>>>>> '))
    nota2 = float(input('Nota 2:\n>>>>> '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [Sim / Não]\n>>>>> ').strip()[0]
    if resp in 'Nn':
        break
print()
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? [999 para interromper]\n>>>>> '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
