# MEU CÓDIGO
# import random
# aluno1 = input('Insira o nome do 1º Aluno: ')
# aluno2 = input('Insira o nome do 2º Aluno: ')
# aluno3 = input('Insira o nome do 3º Aluno: ')
# aluno4 = input('Insira o nome do 4º Aluno: ')
# sort = random.randint(1, 5)
# print('O aluno sorteado foi o {}!'.format(sort))

# CÓDIGO DO PROFESSOR
from random import choice
n1 = str(input('Digite o nome do 1º Aluno: '))
n2 = str(input('Digite o nome do 2º Aluno: '))
n3 = str(input('Digite o nome do 3º Aluno: '))
n4 = str(input('Digite o nome do 4º Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno sorteado foi o(a) {}'.format(escolhido))
