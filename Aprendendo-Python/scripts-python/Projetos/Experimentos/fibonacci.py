resu = 1
armazem = [0]
for c in range(0, 100):
    armazem.append(resu)
    resu = armazem[c] + resu
print(armazem)