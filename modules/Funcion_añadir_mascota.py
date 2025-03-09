import customtkinter
import os
import modules.f_json as fj
import random as rd
import modules.menu_principal as mp
#creo dos listas que va a usar la libreria customtkinter para mostar en opciones
DATA = os.path.join('data/','registros.json')
lista_genero = ["FEMENINO","MASCULINO"]
lista_vacunas = ["Tiene todas las vacunas","Tiene algunas vacunas","No tiene vacunas"]
#cuando el programa llega a esta funcion agrega todos los datos que el usuario ingreso gracias
#a la funcion añadir_mascotas, crea una variable en la que se almacenan los datos nuevo
#y los agrega al archivo .json
def oprimir_boton(ventana,nombre,especie,raza,genero,edad,dieta,residencia,vacunas):
    nombre = nombre.get("0.0","end")
    nombre = nombre.replace("\n","")
    especie = especie.get("0.0","end")
    especie = especie.replace("\n","")
    raza = raza.get("0.0","end")
    raza = raza.replace("\n","")
    genero = genero.get()
    edad = edad.get("0.0","end")
    edad = edad.replace("\n","")
    dieta = dieta.get("0.0","end")
    dieta = dieta.replace("\n","")
    residencia = residencia.get("0.0","end")
    residencia = residencia.replace("\n","")
    vacunas = vacunas.get()
    diccionario = fj.leer_json(DATA)
    id = rd.randrange(1,999999)
    if id in diccionario:
        id = rd.randrange(1,99999)
    nueva_mascota = {id:{
        "nombre":nombre,
        "especie":especie,
        "raza":raza,
        "genero":genero,
        "edad":edad,
        "dieta":dieta,
        "residencia":residencia,
        "vacunas":vacunas
    }}
    fj.actualizar_json(DATA,nueva_mascota)
    ventana.destroy()
    app = customtkinter.CTk()
    app.title("Mascota Agregada")
    app.geometry('200x140')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    datos = f"La mascota \nfue agregada con exito"
    label_nombre = customtkinter.CTkLabel(app,text_color=("white"),text=datos,font=("italic",15))
    label_nombre.grid(row=0, column=0, padx=20, pady=20)
    boton_menu_principal = customtkinter.CTkButton(app,text=("MENU PRINCIPAL"),command = lambda:volver_menu_principal(app))
    boton_menu_principal.grid(row = 1, column =0, padx= 20, pady = 20)
    app.mainloop()
#esta funcion crea el menu donde el ususario va a ingresar los datos y luego  
#los envia a la funcion llamada oprimir boton para que ingrese los datos
def añadir_mascota():
    app = customtkinter.CTk()
    app.title("Gestion de mascotas")
    app.geometry('500x820')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    label = customtkinter.CTkLabel(app,text="Ingrese el nombre de su mascota")
    label.grid(row=0, column=0, padx=0, pady=0)
    P = customtkinter.CTkTextbox(app,width=150,height=30)
    P.grid(row=1, column=0, padx=20, pady=20)
    label2 = customtkinter.CTkLabel(app,text="Ingrese la especie de su mascota")
    label2.grid(row=2, column=0, padx=0, pady=0)
    P2 = customtkinter.CTkTextbox(app,width=150,height=30)
    P2.grid(row=3, column=0, padx=20, pady=20)
    label3 = customtkinter.CTkLabel(app,text="Ingrese la raza de su mascota")
    label3.grid(row=4, column=0, padx=0, pady=0)
    P3 = customtkinter.CTkTextbox(app,width=150,height=30)
    P3.grid(row=5, column=0, padx=20, pady=20)
    label4 = customtkinter.CTkLabel(app,text="Ingrese el genero de su mascota")
    label4.grid(row=6, column=0, padx=0, pady=0)
    P4 = customtkinter.CTkOptionMenu(app,width=150,height=30,values=lista_genero)
    P4.grid(row=7, column=0, padx=20, pady=20)
    label5 = customtkinter.CTkLabel(app,text="Ingrese la edad de su mascota en años")
    label5.grid(row=8, column=0, padx=0, pady=20)
    P5 = customtkinter.CTkTextbox(app,width=150,height=30)
    P5.grid(row=9, column=0, padx=20, pady=20)
    label6 = customtkinter.CTkLabel(app,text="Ingrese nombre de la dieta de su mascota")
    label6.grid(row=0, column=1, padx=20, pady=20)
    P6 = customtkinter.CTkTextbox(app,width=150,height=30)
    P6.grid(row=1, column=1, padx=20, pady=20)
    label7 = customtkinter.CTkLabel(app,text="Ingrese el lugar de residencia de su mascota")
    label7.grid(row=2, column=1, padx=0, pady=20)
    P7 = customtkinter.CTkTextbox(app,width=150,height=30)
    P7.grid(row=3, column=1, padx=20, pady=20)
    label8 = customtkinter.CTkLabel(app,text="Ingrese si su mascota tiene las vacunas")
    label8.grid(row=4, column=1, padx=0, pady=20)
    P8 = customtkinter.CTkOptionMenu(app,width=150,height=30,values=lista_vacunas)
    P8.grid(row=5, column=1, padx=20, pady=20)
    button = customtkinter.CTkButton(app, text="aceptar", command=lambda:oprimir_boton(app,P,P2,P3,P4,P5,P6,P7,P8))
    button.grid(row=6, column=1, padx=50, pady=0)
    app.mainloop()
#esta funcion imprime un mensaje cuando no hay mascotas registradas y permite volver al menu principal
def volver_menu_principal(app):
    app.destroy()
    mp.menu_principal()