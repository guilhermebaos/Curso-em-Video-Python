from Modules import my_format as mf
from Modules import my_inputs as mi
from termcolor2 import c


def menu():
    print(c(mf.tit('Menu Principal')).cyan)
    print(c('Opções:').magenta)
    print(f'''{c('1 ->').yellow} {c('Registar um novo utilizador').blue}
{c('2 ->').yellow} {c('Ver Lista de utilizadores registados').blue}
{c('3 ->').yellow} {c('Elimnar um utilizador').blue}
{c('4 ->').yellow} {c('Terminar o Programa').blue}\n''')
    esc = mi.inputthis(c('Digite o número da operação a executar: ').green, ('1', '2', '3', '4'),
                       c('Escreva só 1, 2, 3 ou 4!').red)
    return esc


def ver_users():
    while True:
        try:
            with open('115_Sistema_Registo_Utilizadores.txt', 'r') as f:
                utilizadores = f.read()
                break
        except FileNotFoundError:
            open('115_Sistema_Registo_Utilizadores.txt', 'w+')
    utilizadores = utilizadores.split(', ')
    n_max_user = len(str(len(utilizadores) / 2)) + 1
    lengh = 6 + n_max_user + 25 + 7
    print(c(mf.tit('Utilizadores Registados', lengh)).cyan)
    for n, item in enumerate(utilizadores):
        if n == 0:
            n_user = 1
            print(c(f'{"Número":<{7 + n_max_user}}'
                    f'{"Nome":<25}'
                    f'Idade\n').yellow)
        elif n % 2 == 0:
            n_user += 1
        if n % 2 == 0:
            print(c(f'User nº{str(n_user) + ":":<{n_max_user}}'
                    f'{item:<25}').blue, end='')
        else:
            print(c(f'{item} anos').blue)


def registar_user():
    print(c(mf.tit('Registar Utilizador')).cyan)
    nome = str(input(c('Nome do novo utilizador: ').green)).strip()
    idade = str(mi.inputint(c('Idade do novo utilizador: ', c('Escreva um número inteiro válido!').red, False).green))
    while True:
        try:
            with open('115_Sistema_Registo_Utilizadores.txt', 'a') as f:
                f.write(f', {nome}, {idade}')
                break
        except FileNotFoundError:
            open('115_Sistema_Registo_Utilizadores.txt', 'w+')


def delete_user():
    print(c(mf.tit('Eliminar Utilizador')).cyan)
    try:
        with open('115_Sistema_Registo_Utilizadores.txt', 'r') as f:
            utilizadores = f.read()
    except FileNotFoundError:
        print('Ainda não há nenhum utilizador registado!')
        return
    while True:
        try:
            num = mi.inputint(c('Número do utilizador: ').green, c('Escreva um número inteiro válido!').red, False)
            utilizadores = utilizadores.split(', ')
            utilizadores.pop(2 * num - 2)
            utilizadores.pop(2 * num - 2)
            utilizadores = mf.join_list(utilizadores, ', ')
            break
        except IndexError:
            print(c('Utilizador inválido!\n').red)
    with open('115_Sistema_Registo_Utilizadores.txt', 'w') as f:
        f.write(utilizadores)
