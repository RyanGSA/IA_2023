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
  nomeCidade = "Cd-" + chr(i + 65)
  c = Cidade(nomeCidade, xCoords[i], yCoords[i])
  cidades.append(c)
  
def getCidades():
    return cidades