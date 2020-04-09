lin0 = []
lin1 = []
lin2 = []
Matriz = [lin0, lin1, lin2]
for c1 in range(0, 3):
    for c2 in range(0, 3):
        n = str(input(f'Escreva o número para a posição [{c1}, {c2}]: ')).strip().ljust(4)
        if c1 == 0:
            lin0.append(n)
        elif c1 == 1:
            lin1.append(n)
        elif c1 == 2:
            lin2.append(n)
print(f'''{'_' * 20}
{' | '.join(Matriz[0])}
{'_' * 20}
{' | '.join(Matriz[1])}
{'_' * 20}
{' | '.join(Matriz[2])}
{'_' * 20}''')
