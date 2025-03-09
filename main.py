import modules.menu_principal as mp
import os
import modules.f_json as fj
#En el archivo main.py no se importa la libreria customtkinter pero el programa la usar para manejo de interfaz
#Si es necesario instalar libreria desde el terminal con el comando: pip install customtkinter
#Inicializamos tanto el nombre del archivo,como su ubicacion y se crea para evitar problemas a futuro con el docigo
DATA = os.path.join('data/','registros.json')
fj.inizializar_archivo(DATA)
mp.menu_principal()