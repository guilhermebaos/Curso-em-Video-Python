from termcolor import cprint, colored
ni = float(input(colored('Primeiro termo da progressão aritmética: ', 'blue')))
pa = float(input(colored('Razão da progressão aritmética: ', 'blue')))
c = 0
p = 10
lp = []
lc = []
np = ni
while c < p:
    while c < p:
        lp += [str(np)]
        ne = len(str(np))
        np += pa
        c += 1
        e = ' ' * (ne - len(str(c)))
        lc += [str(c) + e]
    lps = ' | '.join(lp)
    lcs = ' | '.join(lc)
    cprint('Termos:      {}'.format(str(lps)), 'green')
    cprint('Nº do termo: {}'.format(str(lcs)), 'green')
    mp = int(input(colored('\n\nQuantos termos queres ver mais? ', 'cyan')))
    p += mp
