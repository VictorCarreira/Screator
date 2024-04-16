# -*- coding: utf-8 -*-
#------------------------------------------------------------------------#
# Programa que tem por objetivo realizar a leitura de um arquivo         #
# de imagem de uma seção geológica e a partir disso, realizar a          #
# segmentação desta imagem, em surfaces point para o gempy               #
#------------------------------------------------------------------------#

# Autor:
# - Victor Carreira


# Importando as bibliotecas necessárias (preâmbulo):
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import IPython as ipw
#-------------------------------------
#novos pacotes de imagem
import imageio
from skimage import data, io
#-------------------------------------
#Adicione os módulos internos aqui!
import os
import sys
# Obtenha o caminho absoluto do diretório que contém os módulos
dir_path = os.path.abspath('../mod/')
# Adicione o caminho ao sys.path
sys.path.insert(0, dir_path)
# Agora você pode importar os módulos
from modeling import drilling

########################################################################################################
################################## LEITURA DA SEÇÃO E CRIAÇÃO DOS  ###############################
########################################################################################################

# Leitura da seção geológica:
caminho_img = '../input/santos.png'
ma = io.imread(caminho_img, as_gray=False, pilmode="RGBA")

# conversão de coordenadas em pixel para metros

nx = np.shape(ma)[1]
nz = np.shape(ma)[0]

print("###### Dimensões da seção geológica em metros ######")
print("Distância horizontal (m):",nx)
print("Distância vertical (m):",nz)


print("############## Coordenadas da Surface ###############") 
x,y = drilling(ma) # Função para marcar as coordenadas da surface horizontalmente e verticalmente. e vertical
print("#####################################################") 

# Converta as coordenadas de pixel para metros
x_m = np.linspace(0, 20500, nx, endpoint=True)[[int(i) for i in x]]# alter the range of the x axis according to the real scale in meters
y_m = np.linspace(0, 8880, nz, endpoint=True)[[int(i) for i in y]] # alter the range of the y axis according to the real scale in meters

# Agora 'x_m' e 'y_m' são as coordenadas em metros

surface = input("Nome da surface: ")
# Crie um dataframe com as colunas X, Y, Z e Formation
df = pd.DataFrame({
    'X': [1000]*len(x_m),  # A coluna X terá o valor 1000 para todas as linhas
    'Y': x_m,
    'Z': y_m,
    'Formation': [surface]*len(x_m)  # A coluna Formation terá o mesmo valor para todas as linhas
})

# Salve o dataframe em um arquivo
df.to_csv('../output/' + surface +'.txt', index=False, sep=' ')
