espaco = "0000"
num = int(input('Digite quatro números: '))
numb = espaco + num
tamanho = len(numb)
print(tamanho)
print('A unidade desse número é: ', numb[tamanho-1])
print('A dezena desse número é: ', numb[tamanho-2])
print('A centena desse número é: ', numb[tamanho-3])
print('A milhar desse número é: ', numb[tamanho-4])


# CÓDIGO FEITO PELO PROFESSOR

# num = int(input('Informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(u)) 
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))
