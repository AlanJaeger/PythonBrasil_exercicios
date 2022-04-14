# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes formulas:
    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7

height = input('pass the height: ')
print('If you are a male, your ideal weight is: {male} \nIf you are a female, your ideal weight is: {female}').format(male = (72.7*height)-58, female=(62.1*height)-44.7)