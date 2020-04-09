from termcolor import colored            # print(colored('Hellooo', 'grey', 'on_green'))


def tit(string):
    return colored(f'''{'-' * len(string) * 2}
{str(string):^{len(string) * 2}}
{'-' * len(string) * 2} \n''', 'grey', 'on_red')


def pyhelp():
    while True:
        print('\n' * 2)
        print(colored(f'''{"~" * 40}
{"Ajuda interativa do Python!":^40}
{"~" * 40}
''', "grey", "on_green"), end='')
        comando = input(f'{colored("Escreva um comando ou biblioteca para saber mais sobre ele:", "grey", "on_blue")} ')
        if comando == 'exit':
            break
        print('\033[7;30m')
        help(comando)
        print('\033[m')


pyhelp()
print(tit('Fim do PyHelp'))
