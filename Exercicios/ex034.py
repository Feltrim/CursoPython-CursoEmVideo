print('Aumentos múltiplos\n')

salarioInicial = float(input('Digite seu salário incial:\nR$:'))

if salarioInicial <= 1250:
    salarioNovo = salarioInicial + salarioInicial * 15 / 100
else:
    salarioNovo = salarioInicial + salarioInicial * 10 / 100

print(f'Seu salário passará de R${salarioInicial:.2f} para R${salarioNovo:.2f}')
