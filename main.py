import random

naipes = ['ouros','copas','paus','espadas']
numeros =['Ás',2,3,4,5,6,7,8,9,10,'J','Q','K']

cartas=[]

#For para naipes
for i in range(4):
#For para numeros
  for u in range(13):
    cartas.append(str(numeros[u])+" de "+(naipes[i]))
quantidade = int(input("degite a quantidade de cartas:"))
random.shuffle(cartas)
 
if quantidade < 52:
  for i in range(quantidade):
    print(cartas[i])
else:
  print("limite de possibilidades de cartas excedido")