nome = str(input('Digite seu nome: '))
# O código feito dessa forma se trata de uma estrutura composta, sem a utilização do ELSE se trata de uma estrutura simples.
if nome == 'Vinicius':
    print('Que nome lindo que você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
