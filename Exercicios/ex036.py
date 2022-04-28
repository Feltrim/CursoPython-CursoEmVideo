print('Aprovando Empréstimo\n')

valorCasa = float(input('Qual o valor da casa?\nR$'))
salario = float(input('Qual o salário?\nR$'))
anos = int(input('Em quantos anos você irá pagar?\nR:'))

qtdeParcelas = anos * 12
valorParcelas = valorCasa / anos

if valorParcelas > salario / 10 * 3:
    print('\n\033[1;31mEMPRÉSTIMO NEGADO!')
    print('O valor das parcelas ultrapassa 30% do salário atual.')
else:
    print(f'\nO valor mensal das parcelas será de R${valorParcelas:.2f} durante {anos} anos')
