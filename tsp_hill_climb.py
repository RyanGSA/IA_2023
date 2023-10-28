import math
import random

from Cidades import getCidades

def calcular_distancia(cidade1, cidade2):
    x1, y1 = (cidade1.xCoord, cidade1.yCoord)
    x2, y2 = (cidade2.xCoord, cidade2.yCoord)
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def custo_total_circuito(circuito):
    total = 0
    for i in range(len(circuito)):
        cidade_atual = cidades[circuito[i]]
        cidade_seguinte = cidades[circuito[(i + 1) % len(circuito)]]
        total += calcular_distancia(cidade_atual,cidade_seguinte)
    return total

def getVizinhos(circuito):
  vizinhos = []
  for i in range(len(circuito)):
    for j in range(i + 1, len(circuito)):
        vizinho = circuito.copy()
    vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
    vizinhos.append(vizinho)
  return vizinhos


def circuito_inicial(cidades):
    circuito = list(range(len(cidades)))
    random.shuffle(circuito)
    print("cir inicial: ", circuito)
    return circuito

def subida_encosta(cidades):
  melhor_circuito = circuito_inicial(cidades)
  melhor_custo = custo_total_circuito(melhor_circuito)

  while True:
    vizinhos = getVizinhos(melhor_circuito)
    melhor_vizinho = min(vizinhos, key=lambda x: custo_total_circuito(x))

    if custo_total_circuito(melhor_vizinho) < melhor_custo:
        melhor_circuito = melhor_vizinho
        melhor_custo = custo_total_circuito(melhor_vizinho)
    else:
        break

  return melhor_circuito, melhor_custo

if __name__ == "__main__":
  cidades = getCidades()

  melhor_circuito, melhor_custo = subida_encosta(cidades)

  print("Melhor circuito:", melhor_circuito)
  print("Custo:", melhor_custo)