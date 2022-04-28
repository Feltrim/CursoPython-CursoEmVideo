from random import choice

print('Sorteando um item na lista\n')

n1 = input('Primeiro(a) aluno(a): ')
n2 = input('Segundo(a) aluno(a): ')
n3 = input('Terceiro(a) aluno(a): ')
n4 = input('Quarto(a) aluno(a): ')

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print(f'O(A) aluno(a) escolhido(a) foi o(a) {escolhido}')
