aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip()
while True:
    aluno['média'] = str(input('Nota final do aluno (0-5): ')).strip()
    if aluno['média'].isnumeric():
        break
    else:
        print('Escreve só o número!\n')
aluno['média'] = int(aluno['média'])
if aluno['média'] > 2:
    e = 'passou de ano!'
else:
    e = 'reprovou'
print(f'''\nO aluno {aluno['nome']}, com nota {aluno['média']}, {e}''')
