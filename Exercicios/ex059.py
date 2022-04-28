from time import sleep

print('Criando um Menu de Opções\n')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''\n[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do Programa''')
    opcao = int(input('\n>>>>> Qual é a sua opção?\nR: '))
    if opcao == 1:
        resultado = n1 + n2
        print(f'\nO resultado de {n1} + {n2} é = {resultado}')
    elif opcao == 2:
        resultado = n1 * n2
        print(f'\nO resultado de {n1} x {n2} é = {resultado}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\nO maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('\nInforme os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\nFinalizando...')
        sleep(1)
    else:
        print('\nOpção inválida. Tente novamente.')
    print('-=' * 10)
print('Progama finalizado com sucesso. Volte sempre!')
