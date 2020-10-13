from math import pow
cateop = float(input('Digite o cateto oposto do triangulo: '))
catead = float(input('Digite o cateto adjacente do triangulo: '))

hipot = (pow(cateop, 2) + pow(catead, 2)) ** (1/2)
# hipo = (cateop ** 2 + catead ** 2) ** (1/2)
# hipott = math.hypot(cateop, catead)
print('O comprimento da hipotenusa é {:.2f}'.format(hipot))
