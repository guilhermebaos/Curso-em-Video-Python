from random import randint
from time import sleep
from termcolor import colored
n = (randint(0, 5))  # = a int(uniform(0,6))  Computador pensa num número
print(colored('-=-', 'yellow') * 18)
print('Vou pensar num número entre 0 e 5. Tenta adivinhar...')
print(colored('-=-', 'yellow') * 18)
n1 = int(input(colored('Em que número pensei? ', 'red')))   # Resposta do jogador
print(colored('PROCESSANDO...', 'magenta'))
sleep(1.5)
if n1 == n:
    print(colored('PARABÉNS! Acertaste! Tinha pensado no {}', 'green').format(n))
else:
    print(colored(' Parece que não acertaste...Tenta outra vez! \n Tinha pensado no {}', 'green').format(n))
