from termcolor import cprint, colored
lista = ('Monitor', 270, 'Caixa', 30, 'Placa gráfica', 330, 'Processador', 170)
cprint(f'''{'-' * 30}
{'Lista de preços':^30}
{'-' * 30}''', 'cyan')
cprint(f'''{lista[0]:.<20}{lista[1]:>}€
{lista[2]:.<20}{lista[3]:>}€
{lista[4]:.<20}{lista[5]:>}€
{lista[6]:.<20}{lista[7]:>}€''', 'green')
cprint('-' * 30, 'cyan')
