#Faca um Programa que peca a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

try:
    temp = input('pass temperature in fahrenheit: ')
    print('the temperature in celsius is: {celsius}').format(celsius=5*(temp-32)/9)
except:
    print('pass a number')