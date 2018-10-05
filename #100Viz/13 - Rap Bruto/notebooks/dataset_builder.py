# Este script toma todas las cuentas de POS y crea un nuevo dataset de ellas.

import pandas as pd
import os

datasets = [file for file in os.listdir(os.path.join("..","data","processed")) if "POS" in file]

filepath_in = os.path.join("..","data","processed", datasets[0])

data = pd.DataFrame()

for data_file in datasets:
    filepath_in = os.path.join("..","data","processed", data_file)
    df = pd.read_csv(filepath_in)
    df['artista'] = data_file.split("-")[0]
    data = pd.concat([data, df])
    
    
pos = {
    'noun': 'sustantivo', 
    'verb': 'verbo', 
    'propn': 'nombre propio', 
    'adj': 'adjetivo', 
    'pron': 'pronombre', 
    'det': 'determinador', 
    'adv': 'adverbio', 
    'adp': 'adposición',
    'sconj': 'conj. subordinada', 
    'aux': 'auxiliar', 
    'punct': 'puntuación', 
    'conj': 'conjunción', 
    'num': 'numeral', 
    'intj': 'interjección', 
    'space': 'espacio', 
    'sym': 'símbolo',
    'part': 'partícula',
 }
data['pos'] = data['palabra'].map(pos)

data = data.reset_index().drop(columns = 'index')

filepath_out = os.path.join("..","data","processed","part_of_speech_total.csv")

data[['artista', 'pos', 'cuenta']].to_csv(filepath_out, index = False, encoding = 'utf-8')