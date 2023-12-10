from jvdb_connector import *
import subprocess


basededatos = 'empresa2'
collection = 'clientes2'
nombrearchivo = 'cliente2'
contenido = {'Datos':'datos'}

my_connector = JVDBClient()
# my_connector.insert(basededatos, collection, nombrearchivo, contenido)
# my_connector.select_file(basededatos, collection, nombrearchivo)
my_connector.select_collection(basededatos, collection)