from math import sin, cos, tan, radians

print('Seno, Cosseno e Tangente\n')

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo {angulo}º possui seno de: {seno:.2f}')
print(f'O ângulo {angulo}º possui cosseno de: {cosseno:.2f} ')
print(f'O ângulo {angulo}º possui tangente de: {tangente:.2f}')
