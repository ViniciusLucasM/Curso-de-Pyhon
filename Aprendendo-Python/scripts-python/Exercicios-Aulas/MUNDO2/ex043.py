peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO, SEU IMC É {:.1f}'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('VOCÊ ESTÁ NO SEU PESO IDEAL, SEU IMC É {:.1f}'.format(imc))
elif imc >= 25 and imc <= 30:
    print('VOCÊ ESTÁ COM SOBRE PESO, SEU IMC É {:.1f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('VOCÊ ESTÁ COM OBESIDADE, SEU IMC É {:.1f}'.format(imc))
elif imc > 40:
    print('VOCÊ ESTÁ COM OBESIDADE MORBIDA, SEU IMC É {:.1f}'.format(imc))
