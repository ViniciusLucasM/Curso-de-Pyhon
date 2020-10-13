# MEU CÓDIGO
# from random import choice
# aluno1 = input('Insira o nome do 1º Aluno(a): ')
# aluno2 = input('Insira o nome do 2º Aluno(a): ')
# aluno3 = input('Insira o nome do 3º Aluno(a): ')
# aluno4 = input('Insira o nome do 4º Aluno(a): ')
# lista = [aluno1, aluno2, aluno3, aluno4]
# ordem = choice(lista)
# print('A ordem sorteada foi {}'.format(ordem))

# CÓDIGO DO PROFESSOR
from random import shuffle
aluno1 = str(input('Digite o nome do 1º Aluno(a): '))
aluno2 = str(input('Digite o nome do 2º Aluno(a): '))
aluno3 = str(input('Digite o nome do 3º Aluno(a): '))
aluno4 = str(input('Digite o nome do 4º Aluno(a): '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))
