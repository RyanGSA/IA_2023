# -*- coding: utf-8 -*-

import math
import random

xCoords = []
yCoords = []
cidades = []

class Cidade:
    def __init__(self, nome, xCoord, yCoord):
        self.nome = nome
        self.xCoord = xCoord
        self.yCoord = yCoord

with open("input.txt", "r") as arquivo:
  xCoords = list(map(float, arquivo.readline().split()))
  yCoords = list(map(float, arquivo.readline().split()))

for i in range(len(xCoords)):
  nomeCidade = "Cd-" + str(i + 1)
  c = Cidade(nomeCidade, xCoords[i], yCoords[i])
  cidades.append(c)

print()
for i in range(len(cidades)):
  print(str(cidades[i].nome) + " " + "X: " + str(cidades[i].xCoord) + " " + "Y: " + str(cidades[i].yCoord))
print()

def calcularDistancia(x1,x2,y1,y2):
  return math.sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))

#Troca as Cidades, recebe uma copida da lista de cidades,
#e o Indice das cidades que devem ser trocadas
# Ex:  [A,B,C,D,E,F] trocarCidades(1,3) => [A,D,C,B,E,F]
def trocarCidades(cidadesCopia, x, y):

  auxX = cidadesCopia[x]
  auxY = cidadesCopia[y]

  cidadesCopia[x] = auxY
  cidadesCopia[y] = auxX

#Inverte as Cidades, recebe uma copida da lista de cidades,
#e o Indice das cidades que devem ter todos os seguimentos delas trocados
# Ex:  [B,D,A,F,E,C], inverterCidades(1, 4) obterá o estado [B,E,F,A,D,C]
def inverterCidades(cidadesCopia, x, y):
  while(x < y):
    trocarCidades(cidadesCopia,x,y);
    x += 1
    y -= 1

#Gera uma ordem aleatória das cidades para 
#ser usada como ponto de partida em um algoritmo
#qtdCidades é um int, precisa que seja passado um len(listaDeCidades) 
#como parametro
def organizacaoRandomica(qtdCidades):
    lista = list(range(qtdCidades))
    random.shuffle(lista)
    return lista

#Fazendo um copia da lista pra teste
listaTest = cidades.copy();
inverterCidades(listaTest, 1,5);


#Nova lista após a inverter todos os seguimentos dado dois valores X e Y
print()
for i in range(len(listaTest)):
  print(str(listaTest[i].nome) + " " + "X: " + str(listaTest[i].xCoord) + " " + "Y: " + str(listaTest[i].yCoord))
print()
