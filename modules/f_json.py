import json
import os
#permite leer el archivo.json y ingresarlo en una variable como un diccionario
#si el archivo esta vacio devuelve la estructura base de un diccionario
def leer_json(archivo):
    try:
        with open(archivo,"r",encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        return {}
#permite sobreescrivir el archivo
def escribir_json(archivo,diccionario):
    with open(archivo,"w",encoding='utf-8') as file:
        json.dump(diccionario,file,indent=4,ensure_ascii=False)
#esta funcion permite agregar informacion al diccionario y luego al archivo.json
def actualizar_json(archivo,msg):
    diccionario = leer_json(archivo)
    diccionario.update(msg)
    escribir_json(archivo,diccionario)
#se inicializa el archivo completamente vacio si no esta creado
def inizializar_archivo(archivo):
    if not os.path.isfile(archivo):
        escribir_json(archivo,{})