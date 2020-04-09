def inputint(s='Escreva um número inteiro: '):
    while True:
        n2 = input(s)
        try:
            n2 = int(n2)
            return n2
        except ValueError:
            print('ERRO! Escreva um número inteiro!\n')


n = inputint()
print(f'Escreveu o núemro {n}!')
