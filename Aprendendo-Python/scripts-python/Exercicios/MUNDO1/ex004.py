n = input('Digite algo: ')

print('O tipo desta variável é: ', type(n))
print('Esta variável é composta somente por espaço? ', n.isspace())
print('Esta variável é composta somente por letras minusculas? ', n.islower())
print('Esta variável é composta somente por letras maiusculas? ', n.isupper())
print('Esta variável é composta somente por números? ', n.isnumeric())
print('Esta variável é composta somente por letras? ', n.isalpha())
print('Esta variável é composta somente por alpha númericos? ', n.isalnum())
