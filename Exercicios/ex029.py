print('Radar eletrônico\n')

VelocidadeCarro = int(input('Qual a velocidade em que o carro estava?\nR: '))

ValorMulta = (VelocidadeCarro - 80) * 7

if VelocidadeCarro > 80:
    print('A velocidade excedeu o limite de 80km/h')
    print(f'O valor da multa será de R${ValorMulta:.2f}.')

else:
    print('Você estava dentro da velocidade limite')
