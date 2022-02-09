lar = float(input('Lagura da parede? '))
alt = float(input('Altura da parede? '))
área =  lar * alt
print('Sua parede tem a dimensão de {} x {} e sua Área é de {}m²'.format(lar, alt, área))
tinta = área / 2
print('Para pintar essa parede precisará de {}l de tinta.'.format(tinta))
