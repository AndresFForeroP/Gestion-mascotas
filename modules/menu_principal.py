import customtkinter
import modules.Funcion_añadir_mascota as am
import modules.Funcion_buscar_mascota as bm
import modules.Funcion_editar_mascota as em
import modules.Funcion_eliminar_mascota as dm
#como mencione en el main ya desde este modulo se comienza a usar la libreria customtkinter
def editar_mascota(app):
    app.destroy()
    em.mostrar_mascota_editar()
def añadir_mascota(app):
    app.destroy()
    am.añadir_mascota()
def eliminar_mascota(app):
    app.destroy()
    dm.mostrar_mascota_eliminar()
def buscar_mascota(app):
    app.destroy()
    bm.mostrar_mascotas()
def salir(app):
    app.destroy()
#en el menu principal se usa la libreria para crear el menu con intrerfaz y segun el boton que oprima el usuario 
#se envie a la funcion deseada que esta en su debido modulo
def menu_principal():
    app = customtkinter.CTk()
    app.title("Gestion de mascotas")
    app.geometry('240x350')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    button = customtkinter.CTkButton(app, text="1.Añadir mascota", command=lambda:añadir_mascota(app))
    button.grid(row=1, column=0, padx=50, pady=20, columnspan=2)
    boton_2 = customtkinter.CTkButton(app,text="2.Editar mascota",command=lambda:editar_mascota(app))
    boton_2.grid(row=2,column= 0,padx=50,pady=20, columnspan=2)
    boton_3 = customtkinter.CTkButton(app,text="3.Eliminar mascota",command=lambda:eliminar_mascota(app))
    boton_3.grid(row=3,column= 0,padx=50,pady=20, columnspan=2)
    boton_4 = customtkinter.CTkButton(app,text="4.Buscar mascotas",command=lambda:buscar_mascota(app))
    boton_4.grid(row=4,column= 0,padx=50,pady=20, columnspan=2)
    boton_5 = customtkinter.CTkButton(app,text="9.Salir",command=lambda:salir(app))
    boton_5.grid(row=5,column= 0,padx=50,pady=20, columnspan=2)
    app.mainloop()