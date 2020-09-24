temp = float(input('Qual é a temperadura desejada em ºC: '))
tempf = (temp * 1.8) + 32
tempk = temp + 273.15
print('A temperatura {:.1f}ºC, em fahrenheit é {:.1f}ºF'.format(temp, tempf))
print('A temperatura {:.1f}ºC, em kelvin é {:.1f}K'.format(temp, tempk))
