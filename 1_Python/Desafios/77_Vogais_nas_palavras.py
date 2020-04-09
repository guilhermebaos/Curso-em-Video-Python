palavras = ('viva', 'oi', 'gostar', 'amar', 'mestres', 'escolheste', 'todos', 'viver', 'nascer', 'certo', 'sistema')
c1 = c2 = -1
c3 = 0
vogais = []
while len(palavras) > c1 + 1:
    c1 += 1
    while len(palavras[c1]) > c2 + 1:
        c2 += 1
        if palavras[c1][c2] in 'aeiou':
            vogais += palavras[c1][c2]
    vogais = ', '.join(vogais)
    print(f'A palavra {palavras[c1]} têm estas vogais: {vogais}')
    c2 = -1
    vogais = []
