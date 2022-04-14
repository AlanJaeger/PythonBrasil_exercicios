# Joao Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diario de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de Sao Paulo (50 quilos) deve pagar uma multa 
# de R$ 4,00 por quilo excedente. Joao precisa que voce faca um programa que leia a variavel peso (peso de peixes) e calcule o excesso. 
# Gravar na variavel excesso a quantidade de quilos alem do limite e na variavel multa o valor da multa que Joao devera pagar. 
# Imprima os dados do programa com as mensagens adequadas.


weight = input("Set the weight fish: ")
exceed = int(weight) - 50

if weight > 50:
    print('The limit is 50KG, you exceed {exceed}KG and wanna pay a {ticket}R$ ticket.').format(exceed = exceed, ticket = exceed*4)