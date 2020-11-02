## primer intento

"""
Funciones resumen:
muestra_secreto(secreto:str,key:str)->str:
muestra_secreto(secreto:str,key:str)->str:

oculta_columna(tabla:pd.DataFrame,columna:str,key:str):
dmuestra_columna(tabla:pd.DataFrame,columna:str,key:str):
"""

import pandas as pd
from pathlib import Path
from cryptography.fernet import Fernet

folder=r'/home/sem/Documents/secretTab'
arq='Datos_red.csv'
llave="master.key"

def read_key(rawFile):
    with open(rawFile,"r") as key_file:
        k=key_file.read()
    return k 

def oculta_secreto(secreto:str,key:str)->str:
    '''Encrypta texto del argumento'''
    codificado=secreto.encode()
    f=Fernet(key)
    return f.encrypt(codificado)

def muestra_secreto(secreto:str,key:str)->str:
    """Decripta argumento"""
    f=Fernet(key)
    return f.decrypt(secreto).decode()
    

def oculta_columna(tabla:pd.DataFrame,columna:str,key:str):
    tabla[columna]=tabla.apply(lambda x: oculta_secreto(x[columna],key),axis=1)
    
def muestra_columna(tabla:pd.DataFrame,columna:str,key:str):
    tabla[columna]=tabla.apply(lambda x: muestra_secreto(x[columna],key),axis=1)

def test_()
    key=read_key(Path(folder,llave))
    tabla=pd.read_csv(Path(folder,arq))
    
    print(key)
    print(tabla)
    oculta_columna(tabla,"Value",key)
    breakpoint()
    #tabla.to_csv(Path(folder,"protected_data.csv"))

if __name__=='__main__':
    test()
