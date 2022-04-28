print('Aluguel de Carros\n')

dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KM o carro rodou? '))
vt = (dias * 60) + (km * 0.15)

print(f'Para {dias} dias alugados e {km}km rodados, o valor a ser pago será de R${vt:.2f}')