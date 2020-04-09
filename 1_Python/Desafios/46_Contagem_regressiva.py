from time import sleep
from emoji import emojize
from termcolor import cprint, colored
i = str(input(colored('Pressiona [ Enter ] para começar a contagem decrescente', 'blue')))
for a in range(10, 0, -1):
    cprint(str(a), 'cyan')
    sleep(1)
cprint('0', 'cyan')
sleep(0.1)
print(emojize(':tada: :boom:', use_aliases=True))
