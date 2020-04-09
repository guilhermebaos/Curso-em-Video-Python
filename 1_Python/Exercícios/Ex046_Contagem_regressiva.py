from emoji import emojize
from time import sleep
print('Contagem decrescente até ao fogo de artifício:')
for c1 in range(10, -1, -1):
    sleep(1)
    print(c1)
print(emojize(':boom:', use_aliases=True))
