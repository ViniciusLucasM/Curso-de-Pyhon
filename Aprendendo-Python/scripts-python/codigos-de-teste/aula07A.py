num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
soma = num1 + num2
multi = num1 * num2
divi = num1 / num2
divint = num1 // num2
eleva = num1 ** num2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multi, divi))
print('Divisão inteira é {} e potência é {}'.format(divint, eleva))
