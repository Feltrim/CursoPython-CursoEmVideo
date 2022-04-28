print('Maior e menor valores\n')

n1 = int(input('Insira o primeiro valor:\n'))
n2 = int(input('Insira o segundo valor:\n'))
n3 = int(input('Insira o terceiro valor:\n'))

#Checando o menor valor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Checando o maior valor:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
