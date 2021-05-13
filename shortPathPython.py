 __author__ = "Marcelot"

import sys # biblioteca para pegar um valor alto
import csv # biblioteca para Leitura/Escrita de csv, vamos apenas ler
import pandas as pd # biblioteca para data science, Em particular, oferece estruturas e operações para manipular tabelas numéricas e séries temporais.
import numpy as np # biblioteca para tratar números
import matplotlib.pyplot as plt # biblioteca para apresentação de dados na tela
from geopy.distance import geodesic # biblioteca para distâncias geodésicas
import folium # biblioteca para mapas
import seaborn as sns # biblioteca para mostrar matrix de distâncias
from itertools import permutations

#https://www.geeksforgeeks.org/permutation-and-combination-in-python/

def menorCaminho(data_):
    s=0
    return s

def gerarOrdem(stuff):
    comb = permutations(stuff, 3) 
    return comb

def insertA(combsSemA):
    combsComA = []
    r_=list()
    for r in list(combsSemA):
        r_=list(r)
        r_.insert(0,'A')
        #r.insert(0,'A')
        combsComA.append(r_)
    return combsComA

stuff = ['B', 'C', 'D']

combsSemA = gerarOrdem(stuff)

combFinal = insertA(combsSemA)

for i in list(combFinal): 
    print (i)
