import random
a1 = input('Escreve o nome de um aluno: ')
a2 = input('Escreve o nome de outro aluno: ')
a3 = input('Escreve o nome de ainda outro aluno: ')
a4 = input('Escreve o nome de um último aluno: ')
ordem = random.sample([a1, a2, a3, a4], k=4)
print('Os alunos vão apresentar por esta ordem: {}'.format(ordem))
