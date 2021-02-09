# Dessa forma sera cortado os espaços quando inserir o nome. Lembrando
# que serão removidos os espaços do começo e fim.
nome = str(input('Digite seu nome: ')).strip()
print('O seu nome com todas as letras maiúsculas fica assim: ', nome.upper())
print('O seu nome com todas as letras minúsculas fica assim: ', nome.lower())
espaco = nome.count(' ')  # Adicionando os espaços dentro de uma variável
name = len(nome)  # Adicionando o nome dentro de uma variável
print('O seu nome possui {} letras'.format(name - espaco))  # Nome sem espaço
div = nome.split()
print('O seu primeiro nome tem {} letras'.format(len(div[0])))


# foma na qual o professor fez:

# nome = str(input('Digite seu nome: ')).strip()
# print('O seu nome com todas as letras maiúsculas
# fica assim: {}'.format(nome.upper()))
# print('O seu nome com todas as letras minúsculas
# fica assim: {}'.format(nome.lower()))
# Dessa forma sera feita a contagem do conteúdo
# da variável nome e em seguida a contagem dos espaços.
# Depois desse procedimento sera feita a subtração da
# contagem de letras menos os espaços.
# print('O seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
# print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
# separa = nome.split()
# print('O seu primeiro nome é {} e possui {}
# letras'.format(separa[0], len(separa[0])))
