val = float(input('Digite o valor do produto: '))
desc = (val * 0.05)
valat = val - desc

print('O valor do produto é R${}, com o desconto de 5% o preço do produto'
      'ficou R${:.2f}'.format(val, valat))
