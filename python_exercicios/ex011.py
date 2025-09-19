largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
tinta = área / 2
print('Sua parade tem a dimensão de {}x{} e sua área é de {}m².'.format(altura, largura, área))
print('Para pintar essa parede, você precisara´de {}l de tinta.'.format(tinta))