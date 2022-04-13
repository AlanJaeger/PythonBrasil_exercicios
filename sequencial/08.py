#Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes. Calcule e mostre o total do seu salario no referido mes.

try:
    month_revenue = input('how much do you ear per hour? ')
    month_hours = input('how many hours you work? ')

    print('your salary is : {}$').format(month_revenue*month_hours)
except:
    print('pass numbers')