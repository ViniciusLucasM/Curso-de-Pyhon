import random
aluno1 = input('Insira o nome do 1º Aluno(a): ')
aluno2 = input('Insira o nome do 2º Aluno(a): ')
aluno3 = input('Insira o nome do 3º Aluno(a): ')
aluno4 = input('Insira o nome do 4º Aluno(a): ')

sort = random.randint(1, 4)
ordem = [sort, sort, sort, sort]
print('A ordem sorteada foi {}'.format(ordem))
