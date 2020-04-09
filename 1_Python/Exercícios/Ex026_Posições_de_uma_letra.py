n = str(input('Escreve uma frase: ')).strip().lower()
print('''A letra 'a' aparece {} vezes na frase
A primeira letra 'a' apareceu na frase na {}ª posição
A última letra 'a' apareceu na {}ª posição'''.format(n.count('a'), n.find('a') + 1, n.rfind('a') + 1))
