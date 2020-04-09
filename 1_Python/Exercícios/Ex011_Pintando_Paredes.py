lar = float(input('Qual é a lardura da parede que queres pintar (em metros): '))
comp = float(input('E qual é a altura da parede (também em metros): '))
a = lar * comp
t = a / 2
print('A parede tem uma área de {}m ({}m x {}m)'. format(a, lar, comp))
print('Para pintar essa parede, serão necessários {}l de tinta'.format(t))
