nome = str(input('Digite seu nome completo: ')).strip()

lista = nome.split()
print('O seu primeiro nome é {}'.format(lista[0]))
#  Inverte a lista. EX: ['Vinicius', 'Lucas', 'de', 'Mesquita']
#  fica ['Mesquita', 'de', 'Lucas', 'Vinicius']
lista.reverse()
print('O seu último nome é {}'.format(lista[0]))
