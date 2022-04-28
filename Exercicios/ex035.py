print('Analisando Triângulo v1.0\n')

v1 = float(input('Insira o primeiro valor:\n'))
v2 = float(input('Insira o segundo valor:\n'))
v3 = float(input('Insira o terceiro valor:\n'))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('\nOs segmentos acima podem formar um triângulo')

else:
    print('\nOs segmentos acima não podem formar um triângulo')
