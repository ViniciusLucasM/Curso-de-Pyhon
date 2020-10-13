metros = float(input('Digite os metros desejado: '))
centi = metros * 100
mili = metros * 1000
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000
print('{} metros convertido para centimetros é {}cm'.format(metros, centi))
print('{} metros convertido para milimitros é {}mm'.format(metros, mili))
print('{} metros convertidos para decimeros é {}dm'.format(metros, dm))
print('{} metros convertidos para decametros é {}dam'.format(metros, dam))
print('{} metros convertidos para hectometros é {}hm'.format(metros, hm))
print('{} metros convertidos para quilômetro é {}km'.format(metros, km))
