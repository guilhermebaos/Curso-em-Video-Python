import random
a1 = input('Escreve o nome de uma aluno: ')
a2 = input('Agora escreve o nome de outro aluno: ')
a3 = input('Mais um: ')
a4 = input('E mais um: ')
ae = random.choice([a1, a2, a3, a4])
print('O aluno escolhido é o: {}'.format(ae))
