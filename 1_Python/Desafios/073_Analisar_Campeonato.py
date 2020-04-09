from termcolor import cprint, colored
Equipas = ('FC Porto', 'Benfica', 'Sporting', 'Braga', 'Rio Ave', 'Chaves', 'Marítimo', 'Boavista',
           'Vitória de Guimarães', 'Portimonense', 'Tondela', 'Belenenses', 'Aves', 'Vitória Setúbal',
           'Moreirense', 'Feirense', 'Paços Ferreira', 'Estoril')
cprint(f'''
As equipas do campeonato são: {', '.join(Equipas)}
{'=-' * 145}
Os primeiro 4 classificados foram, por esta ordem: {', '.join(Equipas[0:4])}
{'=-' * 145}
Os últimos dois colocados foram, por esta ordem: {', '.join(Equipas[16:18])}
{'=-' * 145}
As euquipas, ordenadas por ordem alfabética são: {', '.join(sorted(Equipas))}''', 'green')
while True:
    e = str(input(colored('Escreve o nome de uma equipa e vê em que posição está: ', 'blue'))).strip()
    if e in Equipas:
        break
    else:
        cprint('Escreveste mal o nome da equipa!\n', 'red')
cprint(f'\nA equipa: "{Equipas[Equipas.index(e)]}" ficou em {Equipas.index(e) + 1}º lugar!', 'green')
