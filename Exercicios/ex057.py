print('Validação de Dados\n')

sexo = input('Informe seu sexo [M/F/NB]:\nR:').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input(f'Sexo {sexo} inválido. Por favor, informe seu sexo apenas com [M/F/]')
print(f'Sexo {sexo} registrado com sucesso')
