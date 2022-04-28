from math import hypot

print('Catetos e Hipotenusa\n')


co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
h = hypot(co, ca)
print(f'A hipotenusa desse triângulo terá medida de {h}')
