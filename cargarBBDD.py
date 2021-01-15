import pandas as pd
import json
from pymongo import MongoClient
from bson import ObjectId
import binascii

client = MongoClient('localhost', 27017)  # Punto de acceso
db = client['SonidosDelCielo']  # Base de datos

def main():
    loadEchoes(path='/Users/marcosgamazo/Downloads/meteoros_1604918784.csv')
    loadSpectrogram(path='/Users/marcosgamazo/Downloads/meteoros_1604918784.csv')
    loadLightCurve(path='/Users/marcosgamazo/Downloads/meteoros_1604918784.csv')


def getIdEstacionByLocation(locations):
    collection = db['Estacion']
    for location in locations:
        id = collection.find_one({"Localizacion": location})
        if id is None:
            raise Exception()
    client.close()
    return id


def loadEchoes(path):
    '''
    :param path: ruta o url donde se encuentra el fichero csv
    :return:
    '''

    df = pd.read_csv(path, sep=',', usecols=["ID", "DATE", "STATION", "DURATION"])
    df.columns = ['_id', 'Fecha', 'Id_Estacion', 'Duracion']
    df['Id_Estacion'] = df['Id_Estacion'].str.capitalize()
    location = df['Id_Estacion'].drop_duplicates()
    location = getIdEstacionByLocation(location)  # De momento solo existe 1 -> Fuenlabrada
    df['Id_Estacion'].replace("Fuenlabrada", location['_id'], inplace=True)  # Hardcoded, Not Pretty but it works
    data = df.to_dict('records')
    collection = db['Eco']
    collection.insert_many(data)
    client.close()


def loadSpectrogram(path):
    '''
    :param path: ruta o url donde se encuentra el fichero csv
    :return:
    '''

    df = pd.read_csv(path, sep=',', usecols=["ID", "lnk_votsp", "lnk_csvsp", "STATION", "lnk_spec"])
    df.columns = ['_id', 'Id_Estacion', 'Votable', 'Imagen', 'Csv']
    df['Id_Estacion'] = df['Id_Estacion'].str.capitalize()
    location = df['Id_Estacion'].drop_duplicates()
    location = getIdEstacionByLocation(location)  # De momento solo existe 1 -> Fuenlabrada
    df['Id_Estacion'].replace("Fuenlabrada", location['_id'], inplace=True)  # Hardcoded, Not Pretty but it works
    data = df.to_dict('records')
    collection = db['Espectrograma']
    collection.insert_many(data)
    client.close()


def loadLightCurve(path):
    '''
    :param path: ruta o url donde se encuentra el fichero csv
    :return:
    '''

    df = pd.read_csv(path, sep=',', usecols=["ID", "lnk_votlc", "lnk_csvlc", "lnk_lc", "STATION"])
    df.columns = ['_id', 'Id_Estacion', 'Votable', 'Imagen', 'Csv']
    df['Id_Estacion'] = df['Id_Estacion'].str.capitalize()
    location = df['Id_Estacion'].drop_duplicates()
    location = getIdEstacionByLocation(location)  # De momento solo existe 1 -> Fuenlabrada
    df['Id_Estacion'].replace("Fuenlabrada", location['_id'], inplace=True)  # Hardcoded, Not Pretty but it works
    data = df.to_dict('records')
    collection = db['Curva Luz']
    collection.insert_many(data)
    client.close()


def usersToDB():
    collection = db['Usuario']
    url = 'https://raw.githubusercontent.com/redflaggpl/catman/master/usuarios.csv'
    df = pd.read_csv(url, delimiter=';', names=["Name", "Last Name", "DNI", "mail"], encoding='latin1', header=None)

    df.to_json(
        r'/Users/marcosgamazo/Downloads/pruebas_series.json', indent=True, orient='records',
        force_ascii=False)  # Funciona

    with open('/Users/marcosgamazo/Downloads/pruebas_series.json') as file:
        file_data = json.load(file)

    collection.insert_many(file_data)
    client.close()


if __name__ == '__main__':
    main()
