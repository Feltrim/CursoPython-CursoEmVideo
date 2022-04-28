print('Tratando vários valores v1.0\n')

n = cont = soma = 0
n = int(input('Digite um número [999 para parar]:'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]:'))
print(f'\nVocê digitou {cont} números e a soma entre eles foi {soma}')
