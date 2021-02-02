import pandas as pd
import requests
import json

def cargarSonidos():
    url = 'http://138.100.100.143:3001/sonidos/'
    df = pd.read_csv('/Users/marcosgamazo/Downloads/muestras_mayo.csv', sep=",", usecols=['ID','lnk_snd'])
    df.columns = ["_id","Ruta"]  
    data = df.to_dict("records") #Formato del json a añadir {"_id":"Fuenlabrada....","Ruta":"/home/...."}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    for key in data:
        #Realizamos el Post a través de la API
        r=requests.post(url,json.dumps(key),headers=headers)
        print(r.status_code)
    return


def cargarEcos():
    url = 'http://138.100.100.143:3001/ecos/'
    df = pd.read_csv('/Users/marcosgamazo/Downloads/muestras_mayo.csv', sep=",", usecols=['ID','DATE','STATION','DURATION'])
    df.columns = ["_id","Fecha","Id_Estacion","Duracion"]
    df["id_estacion"] = df["id_estacion"].map({'fuenlabrada':1})
    data = df.to_dict("records") #Formato del json a añadir {"_id":"Fuenlabrada....","Ruta":"/home/...."}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    for key in data:
        #Realizamos el Post a través de la API
        r=requests.post(url,json.dumps(key),headers=headers)
        print(r.status_code)
    return


def cargarEspectrogramas():
    url = 'http://138.100.100.143:3001/espectrogramas/'
    df = pd.read_csv('/Users/marcosgamazo/Downloads/muestras_mayo.csv', sep=",", usecols=['ID','STATION','lnk_votsp','lnk_spec','lnk_csvsp'])
    df.columns = ["_id","id_estacion","Votable","Imagen","Csv"]
    df["id_estacion"] = df["id_estacion"].map({'fuenlabrada':1})
    data = df.to_dict("records") #Formato del json a añadir {"_id":"Fuenlabrada....","Ruta":"/home/...."}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    for key in data:
        #Realizamos el Post a través de la API
        r=requests.post(url,json.dumps(key),headers=headers)
        print(r.status_code)
    return

def cargarCurvasDeLuz():
    url = 'http://138.100.100.143:3001/curvasdeluz/'
    df = pd.read_csv('/Users/marcosgamazo/Downloads/muestras_mayo.csv', sep=",", usecols=['ID','STATION','lnk_votlc','lnk_lc','lnk_csvlc'])
    df.columns = ["_id","id_estacion","Votable","Imagen","Csv"]
    df["id_estacion"] = df["id_estacion"].map({'fuenlabrada':1})
    data = df.to_dict("records") #Formato del json a añadir {"_id":"Fuenlabrada....","Ruta":"/home/...."}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    for key in data:
        #Realizamos el Post a través de la API
        r=requests.post(url,json.dumps(key),headers=headers)
        print(r.status_code)
    return

if __name__ == '__main__':
    cargarEcos()
    cargarSonidos()
    cargarEspectrogramas()
    cargarCurvasDeLuz()