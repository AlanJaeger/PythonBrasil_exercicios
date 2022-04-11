#Faca um Programa que peca um numero e entao mostre a mensagem O numero informado foi [numero].

try:
    number = input('Type a number: ')
    print('the number are: {number}').format(number=number)
except:
    print('type a number')