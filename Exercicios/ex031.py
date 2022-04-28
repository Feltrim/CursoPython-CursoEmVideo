print('Custo da Viagem\n')

Distancia = float(input('Qual a distância percorrida em Km?\n R: '))

if Distancia <= 200:
    print(f'O valor da passagem será de R${Distancia * 0.5:.2f}')

else:
    print(f'O valor da passagem será de R${Distancia * 0.45:.2f}')
