n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('A sua média foi boa!')
else:
    print('A sua média precisa ser melhorada!')

# Dessa forma o IF ELSE está sendo estruturado de forma simples.
# print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')
