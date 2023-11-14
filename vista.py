from tkinter import *
from tkcalendar import DateEntry
from tkinter.ttk import Combobox,Treeview
import Base.modelo as modelo
import tkinter as tk
from tkcalendar import Calendar

class VentanaPrincipal():

    def __init__(self,ventana1) -> None:
    
    
        ventana1.title ("FACTURACIÓN")
        ventana1.geometry("1000x600")
        global fondo
        fondo = "blue4"
        ventana1.config(bg=fondo)

        


        ### FRAME CATEGORÍA:
        frame_categoria = Frame(ventana1)
        frame_categoria.config(width=230,height=130,bg="gray50")
        frame_categoria.place(x=750,y=50)



        ################################WIDGETS###########################################

        # ETIQUETAS:

    

    

        

        etiqueta_categoria = Label(ventana1, text="CATEGORIA: ",font= ("arial",15,"bold"))
        etiqueta_categoria.place (x=795,y=50)
        etiqueta_categoria.config(bg="gray50",foreground="black")


        global etiqueta_categoria_rdo_nulo
        etiqueta_categoria_rdo_nulo = Label(ventana1, text="",foreground="green",anchor=CENTER)
        etiqueta_categoria_rdo_nulo.place (x=760,y=90)
        etiqueta_categoria_rdo_nulo.config(bg="gray50", font=("arial",14,"bold"))

        ############ MOSTRAR TOTALES: 
        
        etiqueta_total = Label(ventana1)
        etiqueta_total.place (x=430,y=350)
        etiqueta_total.config(bg=fondo,text="Total de facturas: ",font=("Arial",16,"bold"))

        global etiqueta_total_facturas
        
        etiqueta_total_facturas = Label(ventana1, text="")
        etiqueta_total_facturas.place (x=470,y=370)
        etiqueta_total_facturas.config(bg=fondo,text="prueba",font=("Arial",16,"bold"),foreground="RED")


        
        
        
        ########FECHA
        global fecha
        fecha = StringVar()
        
        etiqueta_fecha = Label(ventana1, text="Fecha: ", font= ("arial",13,"bold"))
        etiqueta_fecha.place (x=10,y=45)
        etiqueta_fecha.config(bg=fondo)
        
        global txt_fecha
        txt_fecha = Entry (ventana1, width=19, textvariable=fecha, justify="center")
        txt_fecha.place(x=83,y=45)
        txt_fecha.config(state="readonly")
        
        calendar= Calendar(ventana1, selectmode="day", date_pattern="dd/MM/yyyy")
        calendar.place(x=60,y=85)
        


    ######## Concepto
        etiqueta_concepto = Label(ventana1, text="Concepto: ",font= ("arial",13,"bold"))
        etiqueta_concepto.place (x=10,y=255)
        etiqueta_concepto.config(bg=fondo)
    
        global concepto
        concepto = StringVar()
        lista_concepto = ["Colegio médico","Hospital","Intecnus","Particular"]
        global combobox_concepto
        combobox_concepto = Combobox(ventana1,values=lista_concepto,state="readonly",width=19,justify="center",textvariable=concepto) # Readonly, lo que hace es que no se pueda escribir en el combobox.
        combobox_concepto.place (x=83,y=255) 

        ###########MONTO:
        etiqueta_monto = Label(ventana1, text="Monto:",font= ("arial",13,"bold"))
        etiqueta_monto.place (x=10,y=11)
        etiqueta_monto.config(bg=fondo)
        
        global monto
        monto = StringVar()
        global txt_monto
        txt_monto = Entry(ventana1, width=19, textvariable=monto, justify="center")
        txt_monto.place(x=83, y=10)


        # TABLA:
        global tabla
        tabla = Treeview(ventana1,) 
        tabla.tag_configure('negrita',font=("TkDefaultFont",15,"bold"))
        tabla.place(x=10,y=300) 
        tabla["columns"] = ("Fecha","Concepto","Monto") 
        tabla.heading("#0", text="Id") 
        tabla.heading("Fecha", text="Fecha",)
        tabla.heading("Concepto",text="Concepto")
        tabla.heading("Monto",text="Monto")
        tabla.column("#0",width=0,minwidth=0,anchor=CENTER) 
        tabla.column("Fecha",width=100,minwidth=100,anchor=CENTER)
        tabla.column("Concepto",width=150,minwidth=80,anchor=CENTER)
        tabla.column("Monto",width=150,minwidth=80,anchor=CENTER)
        


    # BOTONES:
        
        global btn_cargar
        btn_cargar = Button(ventana1, text="CARGAR",command="") 
        btn_cargar.place (x=320,y=260)
        
        global btn_ver_graficos
        btn_ver_graficos = Button(ventana1, text="VISUALIZAR\n DATOS",command="")
        btn_ver_graficos.place(x=420,y=450)
        
        global btn_borrar
        btn_borrar = Button(ventana1, text="  BORRAR  ",command= "")
        btn_borrar.place (x=220, y=520 )
    
        global btn_actualizar_categoria
        btn_actualizar_categoria = Button (ventana1,text="DATOS DE \n CATEGORIZACIÓN",command="",anchor=CENTER)
        btn_actualizar_categoria.place(x=790,y=190)

        global btn_modificar_carga 
        btn_modificar_carga = Button(ventana1,text="MODIFICAR",command="")
        btn_modificar_carga.place(x=100, y=520)

        global btn_guardar_modificar_carga 
        btn_guardar_modificar_carga = Button(ventana1,text="GUARDAR",command="")
        btn_guardar_modificar_carga.pack_forget()


        menubar = Menu(ventana1)
        menu_archivo = Menu(menubar,tearoff=0)
        menu_archivo.add_command(label="Exportar",command="")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cambiar estilo", command="")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=ventana1.quit)
        menubar.add_cascade (label="Archivo",menu=menu_archivo)
        menu_ayuda = Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca del programa",command="")
        menubar.add_cascade(label="Información",menu=menu_ayuda)
        ventana1.config(menu=menubar)   
    
   
def ventana_informacion_categoria():
        
        global inf_categoria
        inf_categoria = Toplevel()
        inf_categoria.title("Información para categorizar")
        inf_categoria.geometry("600x600")
        
        inf_categoria.config(bg="")
        
        
        ########################CATEGORÍAS:
        
        et_categorias = Label(inf_categoria,text="CATEGORIAS",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_categorias.place (x=27,y=20)
        et_categorias.config(bg=fondo)
        
        et_montos = Label(inf_categoria,text="MONTOS",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_montos.place (x=180,y=20)
        et_montos.config(bg=fondo)
        
        et_fecha = Label(inf_categoria,text=" FECHA PARA\nCATEGORIZACION",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_fecha.place (x=400,y=100)
        et_fecha.config(bg=fondo)
        
        
        global txt_fecha_sqlite
        txt_fecha_sqlite = StringVar()
        txt_fecha_sqlite= ""
        
        global txt_fecha_categoria
        txt_fecha_categoria = DateEntry(inf_categoria,date_pattern="yyyy/mm/dd", width=15,justify="center",textvariable=txt_fecha_sqlite)
        txt_fecha_categoria.place(x=420,y=150)
        txt_fecha_categoria.config(state="readonly")
        txt_fecha_categoria.set_date(txt_fecha_sqlite)
        
    
        btn_modificar_datos = Button(inf_categoria,text="MODIFICAR DATOS",command="")
        btn_modificar_datos.place(x=160,y=300)
        
        
        
        et_A = Label(inf_categoria,text="CATEGORIA A: ",justify="center",font=("arial",11,"bold"))
        et_A.place(x=20,y=50)
        et_A.config(bg=fondo)
        
        global var_A,txt_A
        var_A = StringVar()
        var_A.set("")
        
        txt_A = Entry(inf_categoria, width=20, textvariable=var_A, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_A.place(x=135, y=52)
        txt_A.config(bg=fondo)
        
        et_B = Label(inf_categoria,text="CATEGORIA B: ",justify="center",font=("arial",11,"bold"))
        et_B.place(x=20,y=80)
        et_B.config(bg=fondo)
        
        global var_B,txt_B
        var_B = StringVar()
        var_B.set("")
        txt_B = Entry(inf_categoria, width=20, textvariable=var_B, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_B.place(x=135, y=82)
        txt_B.config(bg=fondo)
        
        et_C = Label(inf_categoria,text="CATEGORIA C: ",justify="center",font=("arial",11,"bold"))
        et_C.place(x=20,y=110)
        et_C.config(bg=fondo)
        
        global var_C,txt_C
        var_C = StringVar()
        var_C.set("")
        txt_C = Entry(inf_categoria, width=20, textvariable=var_C, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_C.place(x=135, y=112)
        txt_C.config(bg=fondo)
        
        et_D = Label(inf_categoria,text="CATEGORIA D: ",justify="center",font=("arial",11,"bold"))
        et_D.place(x=20,y=140)
        et_D.config(bg=fondo)
        
        global var_D,txt_D
        var_D = StringVar()
        var_D.set("")
        txt_D = Entry(inf_categoria, width=20, textvariable=var_D, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_D.place(x=135, y=142)
        txt_D.config(bg=fondo)
        
        et_E = Label(inf_categoria,text="CATEGORIA E: ",justify="center",font=("arial",11,"bold"))
        et_E.place(x=20,y=170)
        et_E.config(bg=fondo)
        
        global var_E,txt_E
        var_E = StringVar()
        var_E.set("")
        txt_E = Entry(inf_categoria, width=20, textvariable=var_E, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_E.place(x=135, y=172)
        txt_E.config(bg=fondo)
        
        et_F = Label(inf_categoria,text="CATEGORIA F: ",justify="center",font=("arial",11,"bold"))
        et_F.place(x=20,y=200)
        et_F.config(bg=fondo)
        
        global var_F,txt_F
        var_F = StringVar()
        var_F.set("")
        txt_F = Entry(inf_categoria, width=20, textvariable=var_F, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_F.place(x=135, y=202)
        txt_F.config(bg=fondo)
        
        et_G = Label(inf_categoria,text="CATEGORIA G: ",justify="center",font=("arial",11,"bold"))
        et_G.place(x=20,y=230)
        et_G.config(bg=fondo)
        
        global var_G,txt_G
        var_G = StringVar()
        var_G.set("")
        txt_G = Entry(inf_categoria, width=20, textvariable=var_G, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_G.place(x=135, y=232)
        txt_G.config(bg=fondo)
        
        et_H = Label(inf_categoria,text="CATEGORIA H: ",justify="center",font=("arial",11,"bold"))
        et_H.place(x=20,y=260)
        et_H.config(bg=fondo)
        
        global var_H,txt_H
        var_H = StringVar()
        var_H.set("")
        txt_H = Entry(inf_categoria, width=20, textvariable=var_H, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_H.place(x=135, y=262)
        txt_H.config(bg="")

def aux_modificar_datos_categorizacion(var_A):
        modelo.modificar_datos_categorizacion(var_A)

if __name__== "__main__":
    root = Tk()
    app = VentanaPrincipal(root)

    root.mainloop()
