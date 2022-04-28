print('Índice de Massa Corporal\n')

peso = float(input('Insira seu peso.\nR: '))
altura = float(input('Insira sua altura.\nR: '))

IMC = peso / altura**2

if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.1f} e você está ABAIXO DO PESO')

elif 18.5 < IMC <= 25:
    print(f'Seu IMC é de {IMC:.1f} e você está com o PESO IDEAL')

elif 25 < IMC <= 30:
    print(f'Seu IMC é de {IMC:.1f} e você está com SOBREPESO')

elif 30 < IMC <= 40:
    print(f'Seu IMC é de {IMC:.1f} e você está com OBESIDADE')

else:
    print(f'Seu IMC é de {IMC:.1f} e você está com OBESIDADE MÓRBIDA')
