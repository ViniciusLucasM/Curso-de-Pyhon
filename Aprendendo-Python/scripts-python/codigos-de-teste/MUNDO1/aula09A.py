frase = 'Curso em Vídeo Python'

# Nesse caso ele está indo do começo do conteúdo da frase até o final
# printando casas de dois em dois
print('A frase pulando de dois em dois é: ', frase[::2])

# Busca pela letra "o" dentro de frase
print('A busca por uma letra é um total de: ', frase.count('o'))

# Coloca todas as letras em maiúsculas e busca pela letra "O",
# retornando quantas tem.
print('A busca por uma letra maiúscula é um total de: ',
      frase.upper().count('O'))

# Mostra o tamanho do conteúdo da variável
print('Total de letras na variavel é de: ', len(frase))

# Mostra o tamanho do conteúdo da variável, mas nesse caso
# ele remove os espaços
print('Total de letras na varialvel é de: ', len(frase.strip()))

# Troca uma palavra dentro do conteúdo da variável e remove os espaços
print('A frase com uma palavra trocada ficou: ',
      frase.strip().replace('Python', 'Android'))

# Captura a letra na posição determinada
print('A letra capturada é: ', frase[0])

# Adicionando o conteúdo modificado de uma variável dentro de outra variável
troca = frase.replace('Python', 'Android')
print('A frase com a palavra trocada fico: ', troca)

# Verifica se a palavra desejada se encontra dentro da variável
print('O conteúdo é: ', 'Curso' in frase)

# Ele identifica a posição da primeira letra da palavra inserida.
print('A posição da palavra é: ', frase.find('Curso'))

# Caso coloque um valor inesistente para busca, ele ira retornar -1
print('A posição da palavra é: ', frase.find('curso'))

# Nesse caso ele coloca todo o conteúdo da variável em minúsculo,
# depois ele faz a busca pela palavra desejada.
# Como mudou todo o conteúdo da variável para minúsculo não sera retornado -1
print('A posição da palavra é: ', frase.lower().find('curso'))

# Aqui nesse caso o split está pegando o conteúdo da frase e em todos os
# lugares que possue um espaço ele está cortando e separando as palavras,
# logo depois disso ele adiciona elas em uma lista
print('A frase dividida é: ', frase.split())

# Nessa parte o conteúdo da frase está sendo dividio e adicionado em forma
# de lista dentro da variável dividido. Na parte do printe ele está retornando
# o primeiro conteúdo da variável dividido
dividido = frase.split()
print('A palavra capturada na lista é: ', dividido[0])

# Aqui o print está mostando a variável dividio capturando a palavra dentro da
# lista e retornando somente a 3ª letra
print('A letra capturada da palavra da lista é: ', dividido[0][2])

# print('OI')

# print('''The first department store was created in Paris, in 1850. It was
#      conceived as a big place with a lot of options in products and brands.
#      They wouldn’t sell just a specific product:
#      there you could  find clothes, shoes, jewels, make up and many others
#      things. That concept remained until today. So, if you want to buy many
#      things with good prices, you can choose from one of the
#      thousands in the world.
#      Every year, on the day after Thanksgiving, most of this stores have a
#      big sale called Black Friday.
#      On this day, it is possible to buy products with big discounts and you
#      also have the option to buy
#      things online. In 2016, more than 154 million people spent USD 3,3
#      billion dollars shopping only on
#      the internet.''')
