numeros = []
manpl = []
menpl = []
for c1 in range(0, 5):
    n = float(input('Escreve um número: '))
    numeros += [n]
man = max(numeros)
men = min(numeros)
manv = numeros.count(man)
menv = numeros.count(men)
a1 = a2 = 0
for c2 in range(0, manv):
    manp = numeros.index(man, a1)
    manpl += [manp + 1]
    a1 = manp + 1
for c3 in range(0, menv):
    menp = numeros.index(men, a2)
    menpl += [menp + 1]
    a2 = menp + 1
print(f'''O maior número é {man} e foi escrito na(s) posição(ões): {', '.join(str(x) for x in manpl)}
O menor número é {men} e foi escrito na(s) posição(ões): {', '.join(str(x) for x in menpl)}''')
