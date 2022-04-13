#Faca um Programa que peca o raio de um circulo, calcule e mostre sua area

try:
    area = input('Set the area: ')
    calc = 3.14 * (area*area)
    print('the area of circle is: {}').format(calc)
except:
    print('pass a number')