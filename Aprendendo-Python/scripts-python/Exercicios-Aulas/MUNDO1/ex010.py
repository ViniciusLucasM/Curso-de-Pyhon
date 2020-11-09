real = float(input('Digite a quantidade de reais você tem: '))
dolar = real / 5.41
euro = real / 6.37
iene = real / 0.052
print('Com R${} reais, você consegue comprar US${:.2f} dólar'
      .format(real, dolar))
print('Com R${} reais, você consegue comprar EUR${:.2f} euro'
      .format(real, euro))
print('Com R${} reais, você consegue comprar IENE${:.2f} iene'
      .format(real, iene))
