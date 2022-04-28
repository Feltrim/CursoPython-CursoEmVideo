print('Calculando Descontos\n')

pp = float(input('Qual o preço do produto? R: R$'))
np = pp - pp / 100 * 5
print(f'O novo preço do seu produto com 5% de desconto será de R${np}')
