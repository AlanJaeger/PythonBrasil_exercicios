#Faca um Programa que peca as 4 notas bimestrais e mostre a media.
try:
    n1 = input('type the first grade: ')
    n2 = input('type the second grade: ')
    n3 = input('type the third grade: ')
    n4 = input('type the fourth grade: ')

    print('Your avg are: {soma}').format(soma=(n1+n2+n3+n4)/4)
except:
    print('You need type numbers')