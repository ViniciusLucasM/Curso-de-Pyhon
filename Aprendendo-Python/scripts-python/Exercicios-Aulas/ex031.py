kmV = int(input('Digite a distancia do voo: '))

if kmV <= 200:
    preco = kmV * 0.50
    print('A sua passagem custara R${}'.format(preco))
else:
    preco = kmV * 0.45
    print('A sua passagem custara R${}'.format(preco))
