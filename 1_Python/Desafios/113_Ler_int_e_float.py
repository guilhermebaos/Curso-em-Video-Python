# from Modules import my_inputs as mi
#
# n_i = mi.inputint()
# n_f = mi.inputfloat()
#
# print(f'Escreveu o número inteiro {n_i} e o número com ponto flutuante {n_f}')

from termcolor2 import c


def ler_float():
    while True:
        f = input('Escreva um número real: ').strip()
        try:
            f = float(f)
            return f
        except ValueError:
            print(c('Por favor introduza um número válido!\n').red)
        except KeyboardInterrupt:
            print(c('O utilizador não inseriu nenhum dado.\n').red)
            return 0


def ler_int():
    while True:
        i = input('Escreva um número inteiro: ').strip()
        try:
            i = int(i)
            return i
        except ValueError:
            print(c('Por favor insira um número inteiro válido!\n').red)
        except KeyboardInterrupt:
            print(c('O utilizador não inseriu nunhum dado.\n').red)
            return 0


ni = ler_int()
nf = ler_float()

print(f'O utilizador escreveu os números: {ni} e {nf}')
