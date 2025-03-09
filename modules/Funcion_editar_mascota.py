import customtkinter
import os
import modules.f_json as fj
import modules.menu_principal as mp
#creo dos listas que va a usar la libreria customtkinter para mostar en opciones
DATA = os.path.join('data/','registros.json')
lista_genero = ["FEMENINO","MASCULINO"]
lista_vacunas = ["Tiene todas las vacunas","Tiene algunas vacunas","No tiene vacunas"]
#Esta funcion es parecida al mostrar mascotas,solo que el boton de aceptar envia a la funcion necesaria 
#para editar la informacion de la mascota seleccionada
def mostrar_mascota_editar():
    mascotas = []
    diccionario = fj.leer_json(DATA)
    for keys in diccionario:
        mascotas.append(diccionario[keys]["nombre"])
    if len(mascotas) == 0:
        sin_mascotas()
    else:
        mostrar_mascotas = customtkinter.CTk()
        mostrar_mascotas.title("Nombres de mascotas")
        mostrar_mascotas.geometry("260x200")
        label_nombre = customtkinter.CTkLabel(mostrar_mascotas,text="Elija el nombre de la mascota \nde la cual desea saber editar sus datos")
        label_nombre.grid(row=0, column=0, padx=20, pady=20)
        seleccion_mascota = customtkinter.CTkOptionMenu(mostrar_mascotas,values=mascotas)
        seleccion_mascota.grid(row=1, column=0, padx=20, pady=20)
        boton_aceptar = customtkinter.CTkButton(mostrar_mascotas,text=("Buscar"),command = lambda:editar_mascota(seleccion_mascota,diccionario,mostrar_mascotas))
        boton_aceptar.grid(row = 2, column =0, padx= 20, pady = 20)
        mostrar_mascotas.mainloop()
#Esta funcion muestra el mismo menu que añadir mascota pero en las celdas de texto muestra
#la informacion ya almacenada de la mascota seleccionada y luego edita el archivo json
#se hizo de esta manera para que se pueda editar toda la info de la mascota en un solo proceso
def editar_mascota(mascota,diccionario,menu):
    menu.destroy()
    mascota = mascota.get()
    for key in diccionario:
        if diccionario[key]["nombre"] == mascota:
            id = key
    app = customtkinter.CTk()
    app.title("Editor de mascotas")
    app.geometry('500x820')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    label = customtkinter.CTkLabel(app,text="Ingrese el nombre de su mascota")
    label.grid(row=0, column=0, padx=0, pady=0)
    P = customtkinter.CTkTextbox(app,width=150,height=30)
    P.grid(row=1, column=0, padx=20, pady=20)
    P.insert("0.0",diccionario[id]["nombre"])
    label2 = customtkinter.CTkLabel(app,text="Ingrese la especie de su mascota")
    label2.grid(row=2, column=0, padx=0, pady=0)
    P2 = customtkinter.CTkTextbox(app,width=150,height=30)
    P2.grid(row=3, column=0, padx=20, pady=20)
    P2.insert("0.0",diccionario[id]["especie"])
    label3 = customtkinter.CTkLabel(app,text="Ingrese la raza de su mascota")
    label3.grid(row=4, column=0, padx=0, pady=0)
    P3 = customtkinter.CTkTextbox(app,width=150,height=30)
    P3.grid(row=5, column=0, padx=20, pady=20)
    P3.insert("0.0",diccionario[id]["raza"])
    label4 = customtkinter.CTkLabel(app,text="Ingrese el genero de su mascota")
    label4.grid(row=6, column=0, padx=0, pady=0)
    P4 = customtkinter.CTkOptionMenu(app,width=150,height=30,values=lista_genero)
    P4.grid(row=7, column=0, padx=20, pady=20)
    label5 = customtkinter.CTkLabel(app,text="Ingrese la edad de su mascota en años")
    label5.grid(row=8, column=0, padx=0, pady=20)
    P5 = customtkinter.CTkTextbox(app,width=150,height=30)
    P5.grid(row=9, column=0, padx=20, pady=20)
    P5.insert("0.0",diccionario[id]["edad"])
    label6 = customtkinter.CTkLabel(app,text="Ingrese nombre de la dieta de su mascota")
    label6.grid(row=0, column=1, padx=20, pady=20)
    P6 = customtkinter.CTkTextbox(app,width=150,height=30)
    P6.grid(row=1, column=1, padx=20, pady=20)
    P6.insert("0.0",diccionario[id]["dieta"])
    label7 = customtkinter.CTkLabel(app,text="Ingrese el lugar de residencia de su mascota")
    label7.grid(row=2, column=1, padx=0, pady=20)
    P7 = customtkinter.CTkTextbox(app,width=150,height=30)
    P7.grid(row=3, column=1, padx=20, pady=20)
    P7.insert("0.0",diccionario[id]["residencia"])
    label8 = customtkinter.CTkLabel(app,text="Ingrese si su mascota tiene las vacunas")
    label8.grid(row=4, column=1, padx=0, pady=20)
    P8 = customtkinter.CTkOptionMenu(app,width=150,height=30,values=lista_vacunas)
    P8.grid(row=5, column=1, padx=20, pady=20)
    button = customtkinter.CTkButton(app, text="aceptar", command=lambda:editar_documento(app,P,P2,P3,P4,P5,P6,P7,P8,id))
    button.grid(row=6, column=1, padx=50, pady=0)
    app.mainloop()
#Esta funcion esta conectada con el editar_mascota y se encarga de sacar todos los datos que ingreso
#el usuario y modificar todo
def editar_documento(app,nombre,especie,raza,genero,edad,dieta,residencia,vacunas,id):
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
    app.destroy()
    diccionario = fj.leer_json(DATA)
    diccionario[id]["nombre"] = nombre
    diccionario[id]["especie"] = especie
    diccionario[id]["raza"] = raza
    diccionario[id]["genero"] = genero
    diccionario[id]["edad"] = edad
    diccionario[id]["dieta"] = dieta
    diccionario[id]["residencia"] = residencia
    diccionario[id]["vacunas"] = vacunas
    fj.escribir_json(DATA,diccionario)
    app = customtkinter.CTk()
    app.title("Mascota editada")
    app.geometry('200x140')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    datos = f"La mascota {nombre} \nfue editada con exito"
    label_nombre = customtkinter.CTkLabel(app,text_color=("white"),text=datos,font=("italic",15))
    label_nombre.grid(row=0, column=0, padx=20, pady=20)
    boton_menu_principal = customtkinter.CTkButton(app,text=("MENU PRINCIPAL"),command = lambda:volver_menu_principal(app))
    boton_menu_principal.grid(row = 1, column =0, padx= 20, pady = 20)
    app.mainloop()
#Esta funcion se usa para volver al menu principal
def volver_menu_principal(app):
    app.destroy()
    mp.menu_principal()
#esta funcion imprime un mensaje cuando no hay mascotas registradas y permite volver al menu principal
def sin_mascotas():
    app = customtkinter.CTk()
    app.title("Mascota editada")
    app.geometry('270x140')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    datos = f"No existe ninguna mascota registrada"
    label_nombre = customtkinter.CTkLabel(app,text_color=("white"),text=datos,font=("italic",15))
    label_nombre.grid(row=0, column=0, padx=20, pady=20)
    boton_menu_principal = customtkinter.CTkButton(app,text=("MENU PRINCIPAL"),command = lambda:volver_menu_principal(app))
    boton_menu_principal.grid(row = 1, column =0, padx= 20, pady = 20)
    app.mainloop()