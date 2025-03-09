import customtkinter
import os
import modules.f_json as fj
import modules.menu_principal as mp
DATA = os.path.join('data/','registros.json')
#Esta funcion muestra todas las mascotas ordenadas por los nombres, el usuario elige la mascota 
#de la cual desea saber todos sus datos
def mostrar_mascotas():
    mascotas = []
    diccionario = fj.leer_json(DATA)
    for keys in diccionario:
        mascotas.append(diccionario[keys]["nombre"])
    if len(mascotas) == 0:
        sin_mascotas()
    else:
        mostrar_mascotas = customtkinter.CTk()
        mostrar_mascotas.title("Nombres de mascotas")
        mostrar_mascotas.geometry("230x200")
        label_nombre = customtkinter.CTkLabel(mostrar_mascotas,text="Elija el nombre de la mascota \nde la cual desea saber sus datos")
        label_nombre.grid(row=0, column=0, padx=20, pady=20)
        seleccion_mascota = customtkinter.CTkOptionMenu(mostrar_mascotas,values=mascotas)
        seleccion_mascota.grid(row=1, column=0, padx=20, pady=20)
        boton_aceptar = customtkinter.CTkButton(mostrar_mascotas,text=("Buscar"),command = lambda:mostrar_mascota_elegida(seleccion_mascota,diccionario,mostrar_mascotas))
        boton_aceptar.grid(row = 2, column =0, padx= 20, pady = 20)
        mostrar_mascotas.mainloop()
#Esta funcion muestra todos los datos de la mascota elegida
def mostrar_mascota_elegida(mascota,diccionario,menu):
    menu.destroy()
    mascota = mascota.get()
    datos_mascota = customtkinter.CTk()
    datos_mascota.title("INFORMACION MASCOTA")
    datos_mascota.geometry("370x180")
    for key in diccionario:
        if diccionario[key]["nombre"] == mascota:
            id = key
    datos = f"""{diccionario[id]["nombre"]} es {diccionario[id]["especie"]}
de raza {diccionario[id]["raza"]} su genero es {diccionario[id]["genero"]}
tiene {diccionario[id]["edad"]} años su dieta es {diccionario[id]["dieta"]}
su residencia es {diccionario[id]["residencia"]} y {diccionario[id]["vacunas"]}"""
    label_nombre = customtkinter.CTkLabel(datos_mascota,text_color=("white"),text=datos,font=("italic",15))
    label_nombre.grid(row=0, column=0, padx=20, pady=20)
    boton_menu_principal = customtkinter.CTkButton(datos_mascota,text=("MENU PRINCIPAL"),command = lambda:volver_menu_principal(datos_mascota))
    boton_menu_principal.grid(row = 1, column =0, padx= 20, pady = 20)
    datos_mascota.mainloop()
#Esta funcion devuelve al usuario al menu principal luego de eliminar el menu que se estaba usando antes
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