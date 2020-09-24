lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(lar, alt, area))
print('Para pintar essa parade, você precisara de {:.4f}L de tinta'.format(tinta))
