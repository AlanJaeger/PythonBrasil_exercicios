#Faca um Programa que peca dois numeros e imprima a soma.

try:
    number1 = input('type the first number: ')
    number2 = input('type the second: ')
    
    print('the sum are: {soma}').format(soma=number1+number2)
except:
    print('You need type numbers')

