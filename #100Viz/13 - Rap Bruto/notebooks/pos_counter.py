# la meta de este script es tomar un archivo de texto limpio y contar las 100 palabras mas usadas.
# Las barras de progreso son completamente decorativas y no sirven ninguna función.

import os
import sys
try:
    from tqdm import tqdm
except ImportError:
        os.system("pip install tqdm")
        from tqdm import tqdm


try:
    import spacy
except ImportError:
        os.system("conda install -c conda-forge spacy -y")
        import spacy

from spacy.attrs import ORTH
from collections import Counter

try:
    nlp = spacy.load('es')
except OSError:
    os.system("python -m spacy download es")
    nlp = spacy.load('es')

# importamos el texto

def contador(filepath: str = sys.argv[1], numero: int = 100):
    """
    Esta funcion limpia y cuenta la frecuencia de cada palabra dicha en el archivo de texto que recibe.
    """
    
    # extraemos el texto
    with open(filepath, "r", encoding = "utf-8") as file:
        texto = file.read()
        
    # creamos el documento tokenizado con spacy
    doc = nlp(texto)
        
    # definimos parametros 
    etiquetas_de_ruido = [] 
    minimo_de_caracteres = 2

    # 
    def esRuido(token):
        """
        Esta función define si una palabra (o token) es ruido o no.
        """
        es_ruido = False
        if token.pos_ in etiquetas_de_ruido:
            es_ruido = True 
        elif token.is_stop == True:
            es_ruido = True
        elif len(token.string) <= minimo_de_caracteres:
            es_ruido = True
        return es_ruido 
    def limpiador(token, minuscula = True):
        if minuscula:
           token = token.lower()
        return token.strip()

    # contador
    cuenta_limpia = [limpiador(palabra.pos_) for palabra in doc if not esRuido(palabra)]

    top_100 = Counter(cuenta_limpia).most_common(numero)
    
    # salvar el archivo limpio    
    path, filename = os.path.split(filepath)
    parent_dir, data_dir = os.path.split(path)
    filename, extension = os.path.splitext(filename)
    if "-" in filename:
        filename = filename.split("-")[0]
    filepath_out = os.path.join(parent_dir, "processed", f"{filename}-POS.csv")

    with open(filepath_out, "w", encoding = "utf-8",) as file:
        file.write("palabra,cuenta\n")
        for i in range(len(top_100)):
            file.write(f"{top_100[i][0]},{top_100[i][1]}\n")
        
    return filepath_out, filename


if __name__ == "__main__":
    
    filepath_out, filename = contador(filepath = sys.argv[1],)
    
    print("#"*70)
    print("_"*70)
    print(f"Limpiando el archivo {filename}")
    for i in tqdm(range(5_000_000)):
        pass
    print("_"*70)
    print(f"Guardando el archivo {filepath_out}")
    for i in tqdm(range(5_000_000)):
        pass
    print("#"*70)