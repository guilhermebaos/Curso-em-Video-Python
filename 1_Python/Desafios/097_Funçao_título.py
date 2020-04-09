def tit(string):
    a = int(len(string) / 2 + 2)
    return f'''{'-=' * a}
{str(string):^{a * 2}}
{'-=' * a}'''


while True:
    txt = str(input('Escreve algo para o colocar como título! ')).strip()
    print(tit(txt))
    while True:
        cont = str(input('Queres escrever outra coisa [S/N]? ')).upper()
        if cont in ['S', 'N']:
            break
        else:
            print('Escreve só "S" ou "N"!')
    if cont == 'N':
        break
    else:
        print('\n')
