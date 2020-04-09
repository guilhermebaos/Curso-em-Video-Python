from Modules_Ex.Ex111 import Euro
from Modules import my_inputs

preco = my_inputs.inputfloat('Escreve o preço de um produto, em euros: ')
print(Euro.price_manipulation(preco, 20, 10))
