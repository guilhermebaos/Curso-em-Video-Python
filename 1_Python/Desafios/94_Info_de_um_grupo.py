grupo, mulheres, velhos = [], [], []
pessoa = {}
c1 = c3 = 0
while True:
    pessoa['nome'] = str(input('Nome do indivíduo: ')).strip()
    while True:
        pessoa['idade'] = str(input('Idade do indivíduo: ')).strip()
        if pessoa['idade'].isnumeric():
            pessoa['idade'] = int(pessoa['idade'])
            break
        else:
            print('Escreve só o número!\n')
    while True:
        pessoa['sexo'] = str(input('Sexo do indivíduo [M/F]: ')).strip().upper()
        if pessoa['sexo'] in ['M', 'F']:
            break
        else:
            print('Esreve só "M" ou "F"!\n')
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        p = str(input('Quer adicionar mais alguém ao grupo [S/N]? ')).strip().upper()
        if p in ['S', 'N']:
            break
        else:
            print('Escreve só "S" ou "N"!\n')
    if p == 'N':
        break
    else:
        print('-=' * 20)
for c2 in grupo:
    c3 += c2['idade']
    if c2['sexo'] == 'F':
        mulheres += [c2['nome']]
total = len(grupo)
med = c3/total
for c4 in grupo:
    if c4['idade'] > med:
        velhos += [c4['nome']]
print(f'''\n\nNo total foram registadas {total} pessoas
A média de idades é: {med:3}
As mulheres do grupo são: {', '.join(mulheres)}
As pessoas com idades acima da média são: {', '.join(velhos)}''')
