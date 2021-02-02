import random

letras_maiu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_minu = letras_maiu.lower()
numeros = '0123456789'
simbolos = '!@#$%&*'

masc, minu, num, simb = True, True, True, False

senha = ''

if masc:
    senha += letras_maiu
if minu:
    senha += letras_minu
if num:
    senha += numeros
if simb:
    senha += simbolos

tamanho = 16
montante = 10

for a in range(montante):
    password = ''.join(random.sample(senha, tamanho))
    print(password)
