notas = []
c = 0
r1 = ['S', 'N']


def isfloat(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


while True:
    n1 = n2 = p = 'a'
    n = str(input('Nome do aluno: ')).strip()
    while not isfloat(n1):
        n1 = str(input('Nota 1º teste: ')).strip()
        if not isfloat(n1):
            print('Escreva só o número!')
    n1 = float(n1)
    while not isfloat(n2):
        n2 = str(input('Nota 2º teste: ')).strip()
        if not isfloat(n2):
            print('Escreva só o número!')
    n2 = float(n2)
    c += 1
    aluno = [n, n1, n2]
    notas.append(aluno[:])
    while p not in r1:
        p = str(input('Quer inserir outro aluno [S/N]? ')).strip().upper()
        if p not in r1:
            print('Escreva só "S" ou "N"')
    if p == 'S':
        print('\n')
    else:
        break
print('-' * 20)
print('Nome do aluno...Média')
for c1 in notas:
    print(f'{c1[0]:.<10}.......{(c1[1] + c1[2]) / 2}')
print('-' * 20)
while True:
    c3 = 0
    a = str(input('Escreva o nome de um aluno para ver a sua média (para terminar, deixe em branco): ')).strip()
    if a == '':
        break
    else:
        for c2 in notas:
            c3 += 1
            if a == c2[0]:
                print(f'As notas desse aluno são: {c2[1]}, {c2[2]} e a sua média é: {(c2[1] + c2[2]) / 2}\n')
                break
            if c == c3:
                print('Aluno inexistente\n')
