import customtkinter
import os
import modules.f_json as fj
import modules.menu_principal as mp
DATA = os.path.join('data/','registros.json')
#Esta funcion crea el menu donde se muestran todas las mascotas y el usuario elige cual eliminar
def mostrar_mascota_eliminar():
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
        label_nombre = customtkinter.CTkLabel(mostrar_mascotas,text="Elija el nombre de la mascota \nque desea eliminar")
        label_nombre.grid(row=0, column=0, padx=20, pady=20)
        seleccion_mascota = customtkinter.CTkOptionMenu(mostrar_mascotas,values=mascotas)
        seleccion_mascota.grid(row=1, column=0, padx=20, pady=20)
        boton_aceptar = customtkinter.CTkButton(mostrar_mascotas,text=("Buscar"),command = lambda:eliminar_mascota(seleccion_mascota,diccionario,mostrar_mascotas))
        boton_aceptar.grid(row = 2, column =0, padx= 20, pady = 20)
        mostrar_mascotas.mainloop()
#Esta funcion elimina la mascota que se selecciono en la funcion anterior
def eliminar_mascota(mascota,diccionario,menu):
    menu.destroy()
    mascota = mascota.get()
    for key in diccionario:
        if diccionario[key]["nombre"] == mascota:
            id = key
    diccionario.pop(id)
    fj.escribir_json(DATA,diccionario)
    app = customtkinter.CTk()
    app.title("Mascota eliminada")
    app.geometry('200x140')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    datos = f"La mascota {mascota} \nfue eliminada con exito"
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