print('Aquele clássio da Média\n')

n1 = float(input('Digite a primeira nota do(a) aluno(a).\nR: '))
n2 = float(input('Digite a segunda nota do(a) aluno(a).\nR: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'\nMédia: {media} | Aluno(a) REPROVADO.')

elif 5.0 <= media <= 6.9:
    print(f'\nMédia: {media} | Aluno(a) de RECUPERAÇÃO.')

else:
    print(f'\nMédia: {media} | Aluno(a) APROVADO.')
