print('Análise de dados em uma Tupla\n')

num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto e último número: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) +1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram:\n')
for n in num:
    if n % 2 == 0:
        print(n, end='')
