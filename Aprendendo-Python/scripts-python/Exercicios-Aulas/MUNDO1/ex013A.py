preco = float(input('Qual é o valor do produto desejado? R$'))
avis = preco - (preco * 10 / 100)
parce = preco + (preco * 8 / 100)
print('O produto com o valor R${:.2f}, com pagamento avista, o valor do '
      'produto ficara em R${:.2f}'.format(preco, avis))
print('O produto com o valor R${:.2f}, com pagamento parcelado, o valor do'
      'produto ficara em R${:.2f}'.format(preco, parce))
