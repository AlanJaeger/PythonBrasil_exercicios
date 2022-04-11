#Faca um Programa que converta metros para centimetros.
try:
    mt = input('set the meter: ')

    print('{mt} meter are {ct} centimeters').format(mt=mt, ct=mt*100)
except:
    print('You need type numbers')