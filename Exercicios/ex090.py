print('Dicionário em Python\n')

aluno = {}
aluno['Nome'] = input('Nome\n>>>>> ')
aluno['Média'] = float(input(f'Média de {aluno["nome"]}\n>>>>>'))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print()
print('-=' * 30)
for k, v in aluno.itens():
    print(f'  - {k} é igual a {v}')
    