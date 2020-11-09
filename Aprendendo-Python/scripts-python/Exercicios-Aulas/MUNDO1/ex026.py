frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira vez em que a letra A aparece é na {}ª posição'
      .format(frase.find('A') + 1))
print('A última vez em qua a letra A aparece é na {}ª posição'
      .format(frase.rfind('A') + 1))


# CÓDIGO FEITO PELO PROFESSOR

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A última letras A apareceu na posição {}'.format(frase.rfind('A') + 1))
