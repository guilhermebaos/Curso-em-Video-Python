from termcolor import colored
v = str(input(colored('Qual é a velocidade atual do carro (em km/h)? ', 'blue'))).strip()
v0 = float(v)
if v0 > 80:
    print(colored('''    ULTRAPASSOU O LIMITE DE 80Km/h!
    Terá de pagar uma multa de {}€'''.format((v0 - 80) * 2), 'red'))
print(colored('Tenha um bom dia e conduza com segurança!', 'green'))
