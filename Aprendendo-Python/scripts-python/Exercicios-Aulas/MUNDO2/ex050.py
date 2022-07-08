cont = 0
lista = []
soma = 0
while cont != 7:
    num = int(input('Digite seis numeros: '))
    lista.append(num)
    cont += 1

for z in lista:
    print(lista[z])

# for c in lista:
#    if lista[c] % 2 == 0:
#        soma = soma + lista[c]
# print(soma)
