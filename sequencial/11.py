# Faca um Programa que peca 2 numeros inteiros e um numero real. Calcule e mostre:
    # 1 - o produto do dobro do primeiro com metade do segundo .
    # 2 - a soma do triplo do primeiro com o terceiro.
    # 3 - o terceiro elevado ao cubo.

int1 = input('set the first integer number: ') 
int2 = input('set the second integer number: ') 
realn = input('set the real number: ')

if isinstance(int1, int) and isinstance(int2, int):
    print('Product: {}').format((int1*2)*(int2/2))
    print('Triple sum: {}').format((int1*3)+realn)
    print('Cube: {}').format(realn**3)
else:
    print('you need to pass a integer number')
    



