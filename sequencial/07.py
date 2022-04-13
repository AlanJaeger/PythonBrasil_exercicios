#Faca um Programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario.

try:
    side = input('set the square side: ')
    area = side*side
    print('the square area is {area} and his doble is {doble}').format(area=area, doble=area*2)
except:
    print('pass a number')