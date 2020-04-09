from datetime import date
info = dict()
info['nome'] = str(input('Nome: ')).strip()
dn = int(input('Ano de nascimento: '))
ano = date.today().year
info['idade'] = ano - dn
while True:
    info['trabalho'] = str(input('Trabalhas [S/N]? ')).strip().upper()
    if info['trabalho'] in ['S', 'N']:
        break
    else:
        print('Escreve só "S" ou "N"!\n')
if info['trabalho'] != 'N':
    ac = int(input('Ano de contratação: '))
    info['tempo de trabalho'] = 2018 - ac
    info['idade de reforma'] = info['idade'] + (35 - info['tempo de trabalho'])
print(f'''O Sr(a). {info['nome']}, com {info['idade']} anos de idade, trabalha há {info['tempo de trabalho']} e vai-se reformar com {info['idade de reforma']} anos''')
