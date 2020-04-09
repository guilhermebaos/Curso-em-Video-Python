import random
import time
jogos = []
pc = []
print(f'''{'-' * 20}
Ajuda a apostar
{'-' * 20}''')
while True:
    n = str(input('Quantos jogos quer sortear? '))
    if n.isnumeric():
        n = int(n)
        break
    else:
        print('Escreva só o número!')
for c1 in range(0, n):
    while True:
        r = random.randint(1, 60)
        if r not in pc:
            pc.append(r)
        if len(pc) == 6:
            break
    jogos.append(pc.copy())
    pc.clear()
for c3 in range(0, n):
    print(f'''Números para o Jogo {c3 + 1}: {', '.join(str(x) for x in jogos[c3])}''')
    time.sleep(0.7)
