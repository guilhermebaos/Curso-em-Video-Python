f = input('Escreve uma frase: ')

f = f.lower()
f1 = f.find('a') + 1
f2 = f.rfind('a') + 1
f3 = f.count('a')
print('A letra ''a'' aparece {} vezes'.format(f3))
print('Aparece pela primeira vez na {}ª posição e pela última na {}ª posição'.format(f1, f2))
