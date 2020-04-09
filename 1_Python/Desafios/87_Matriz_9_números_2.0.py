lin0 = []
lin1 = []
lin2 = []
pares = col2 = 0
Matriz = [lin0, lin1, lin2]
for c1 in range(0, 3):
    for c2 in range(0, 3):
        while True:
            n = str(input(f'Escreva o número para a posição [{c1}, {c2}]: ')).strip()
            if n.isnumeric():
                n = int(n)
                break
            else:
                print('Escreva só o número!\n')
        if c1 == 0:
            lin0.append(n)
        elif c1 == 1:
            lin1.append(n)
        elif c1 == 2:
            lin2.append(n)
        if n % 2 == 0:
            pares += n
        if c2 == 2:
            col2 += n
print(f'''{'_' * 20}
{' | '.join(str(x).ljust(5) for x in Matriz[0])}
{'_' * 20}
{' | '.join(str(x).ljust(5) for x in Matriz[1])}
{'_' * 20}
{' | '.join(str(x).ljust(5) for x in Matriz[2])}
{'_' * 20}''')
print(f'''A soma dos valores pares digitados é: {pares}
A soma dos valores da terceira coluna é {col2}
O maior valor da segunda linha é: {max(Matriz[1])}''')
