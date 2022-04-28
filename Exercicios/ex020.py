from random import shuffle

print('Sorteando uma ordem na lista\n')

n1 = input('Primeiro(a) aluno(a): ')
n2 = input('Segundo(a) aluno(a): ')
n3 = input('Terceiro(a) aluno(a): ')
n4 = input('Quarto(a) aluno(a): ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação será:\n', lista)
