#Faca um Programa que peca a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
#multiply the temperature in degrees Celsius by 2, and then add 30

try:
    temp = input('pass temperature in celsius: ')
    print('the temperature in farenheit is: {farenheit}').format(farenheit=(temp*2)+30)
except:
    print('pass a number')