from Modules_Ex import Ex112
from Modules import my_inputs
from termcolor2 import colored

preco = my_inputs.inputfloat('Escreve o preço de um produto, em euros: ', colored('ERRO: Escreva só o preço!\n', 'red'))
aumento = my_inputs.inputfloat('Escreve o aumento do preço do produto, em percentagem: ', colored('ERRO: Escreva só o número!\n', 'red'))
desconto = my_inputs.inputfloat('Escreve o aumento do preço do produto, em percentagem: ', colored('ERRO: Escreva só o número!\n', 'red'))
print('')
print(Ex112.price_manipulation(preco, aumento, desconto))
