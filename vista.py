from tkinter import *
from tkinter.ttk import Combobox,Treeview
import tkinter as tk
from tkcalendar import Calendar , DateEntry
from tkinter.colorchooser import askcolor
import webbrowser
from tkinter import simpledialog, messagebox
import re
from modelo import MiBaseDeDatos , BaseDeDatos

###HOL
### ESCRIBO COSAS
### ESCRIBO MAS COSAS....
#BLA BLCAS DKD

###QUE TAL

class VentanaPrincipal():

    def __init__(self,ventana1) -> None:

        self.mibase = MiBaseDeDatos()
        self.objeto_modelo_bd = BaseDeDatos() #BASE DAMIAN

        self.ventana1 = ventana1
        self.ventana1.title ("FACTURACIÓN")
        self.ventana1.geometry("1000x600")

        #Funcion que trae la configuracion del color 
        self.fondo = self.mibase.return_config('color_fondo')
        
        self.ventana1.config(bg=self.fondo)

        ### FRAME CATEGORÍA:
        frame_categoria = Frame(self.ventana1)
        frame_categoria.config(width=230,height=130,bg="gray50")
        frame_categoria.place(x=750,y=50)

        ################################WIDGETS###########################################

        # ETIQUETAS:
        self.etiqueta_categoria = Label(self.ventana1, text="CATEGORIA: ",font= ("arial",15,"bold"))
        self.etiqueta_categoria.place (x=795,y=50)
        self.etiqueta_categoria.config(bg="gray50",foreground="black")
        self.etiqueta_categoria_rdo_nulo = Label(self.ventana1, text="",foreground="green",anchor=CENTER)
        self.etiqueta_categoria_rdo_nulo.place (x=760,y=90)
        self.etiqueta_categoria_rdo_nulo.config(bg="gray50", font=("arial",14,"bold"))

        ############ MOSTRAR TOTALES: 
        self.etiqueta_total = Label(self.ventana1)
        self.etiqueta_total.place (x=430,y=350)
        self.etiqueta_total.config(bg=self.fondo,text="Total de facturas: ",font=("Arial",16,"bold"))
        self.etiqueta_total_facturas = Label(self.ventana1, text="")
        self.etiqueta_total_facturas.place (x=470,y=370)
        self.etiqueta_total_facturas.config(bg=self.fondo,text="prueba",font=("Arial",16,"bold"),foreground="RED")
        
        ########FECHA
        self.fecha = StringVar()
        self.etiqueta_fecha = Label(self.ventana1, text="Fecha: ", font= ("arial",13,"bold"))
        self.etiqueta_fecha.place(x=10,y=45)
        self.etiqueta_fecha.config(bg=self.fondo)
        
        self.txt_fecha = Entry (self.ventana1, width=19, textvariable=self.fecha, justify="center")
        self.txt_fecha.place(x=83,y=45)
        #self.txt_fecha.config(state="readonly")
        
        self.calendar= Calendar(self.ventana1, selectmode="day", date_pattern="dd/MM/yyyy")
        self.calendar.bind("<<CalendarSelected>>", self.actualizar_fecha)
        self.calendar.place(x=60,y=85)

    ######## Concepto
        self.etiqueta_concepto = Label(self.ventana1, text="Concepto: ",font= ("arial",13,"bold"))
        self.etiqueta_concepto.place (x=10,y=275)
        self.etiqueta_concepto.config(bg=self.fondo)
    
        self.concepto = StringVar()

        #cargo la lista llamando al modelo 
        self.lista_concepto = []
        datos = self.mibase.trae_conceptos()
        self.lista_concepto = [tupla[1] for tupla in datos]
        #Agrego a la lista el "Agregar Nuevo"
        self.lista_concepto += ["Agregar Nuevo"]
        
        
        self.combobox_concepto = Combobox(self.ventana1,values=self.lista_concepto,state="readonly",width=19,justify="center",textvariable=self.concepto) # Readonly, lo que hace es que no se pueda escribir en el combobox.
        self.combobox_concepto.place (x=100,y=275) 

        #agrego la funcionalidad de agregar a la base de datos un nuevo registro
        self.combobox_concepto.bind("<<ComboboxSelected>>", lambda event: self.agregar_concepto(self.concepto)) 
        ###########MONTO:
        self.etiqueta_monto = Label(self.ventana1, text="Monto:",font= ("arial",13,"bold"))
        self.etiqueta_monto.place (x=10,y=11)
        self.etiqueta_monto.config(bg=self.fondo)
        

        self.monto = StringVar()
        self.txt_monto = Entry(self.ventana1, width=19, textvariable=self.monto, justify="center")
        self.txt_monto.place(x=83, y=10)

        # TABLA:
        self.tabla = Treeview(self.ventana1,) 
        self.tabla.tag_configure('negrita',font=("TkDefaultFont",15,"bold"))
        self.tabla.place(x=10,y=300) 
        self.tabla["columns"] = ("Fecha","Concepto","Monto") 
        self.tabla.heading("#0", text="Id") 
        self.tabla.heading("Fecha", text="Fecha",)
        self.tabla.heading("Concepto",text="Concepto")
        self.tabla.heading("Monto",text="Monto")
        self.tabla.column("#0",width=0,minwidth=0,anchor=CENTER) 
        self.tabla.column("Fecha",width=100,minwidth=100,anchor=CENTER)
        self.tabla.column("Concepto",width=150,minwidth=80,anchor=CENTER)
        self.tabla.column("Monto",width=150,minwidth=80,anchor=CENTER)
        
        self.actualizar_treeview()

    # BOTONES:
        

        self.btn_cargar = Button(self.ventana1, text="CARGAR",command=self.auxiliar_carga) 
        self.btn_cargar.place (x=320,y=270)
        

        self.btn_ver_graficos = Button(self.ventana1, text="VISUALIZAR\n DATOS",command="")
        self.btn_ver_graficos.place(x=420,y=450)
        

        self.btn_borrar = Button(self.ventana1, text="  BORRAR  ",command= "")
        self.btn_borrar.place (x=220, y=540 )
    

        self.btn_actualizar_categoria = Button (self.ventana1,text="DATOS DE \n CATEGORIZACIÓN",command=lambda:self.ventana_informacion_categoria(),anchor=CENTER)
        self.btn_actualizar_categoria.place(x=790,y=190)


        self.btn_modificar_carga = Button(self.ventana1,text="MODIFICAR",command="")
        self.btn_modificar_carga.place(x=100, y=540)


        self.btn_guardar_modificar_carga = Button(self.ventana1,text="GUARDAR",command="")
        self.btn_guardar_modificar_carga.pack_forget()


        menubar = Menu(self.ventana1)
        menu_archivo = Menu(menubar,tearoff=0)
        menu_archivo.add_command(label="Exportar",command="")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cambiar estilo", command=lambda:self.cambio_color())
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=lambda:self.salir())
        menubar.add_cascade (label="Archivo",menu=menu_archivo)
        menu_ayuda = Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca del programa",command="")
        menubar.add_cascade(label="Información",menu=menu_ayuda)
        self.ventana1.config(menu=menubar)   
    
    def ventana_informacion_categoria(self):
        inf_categoria = Toplevel()
        inf_categoria.title("Información para categorizar")
        inf_categoria.geometry("600x600")
        inf_categoria.config(bg=self.fondo)

        
        
        
        ########################CATEGORÍAS:
        
        et_categorias = Label(inf_categoria,text="CATEGORIAS",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_categorias.place (x=27,y=20)
        et_categorias.config(bg=self.fondo)
        
        et_montos = Label(inf_categoria,text="MONTOS",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_montos.place (x=180,y=20)
        et_montos.config(bg=self.fondo)
        
        et_fecha = Label(inf_categoria,text=" FECHA PARA\nCATEGORIZACION",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_fecha.place (x=400,y=100)
        et_fecha.config(bg=self.fondo)
        
        
        global txt_fecha_sqlite
        txt_fecha_sqlite = StringVar()
        txt_fecha_sqlite= "2023/01/01"
        
        global txt_fecha_categoria
        txt_fecha_categoria = DateEntry(inf_categoria,date_pattern="yyyy/mm/dd", width=15,justify="center",textvariable=txt_fecha_sqlite)
        txt_fecha_categoria.place(x=420,y=150)
        txt_fecha_categoria.config(state="readonly")
        txt_fecha_categoria.set_date(txt_fecha_sqlite)
        
    
        btn_modificar_datos = Button(inf_categoria,text="MODIFICAR DATOS",command="")
        btn_modificar_datos.place(x=160,y=300)
        
        btn_ir_afip = Button(inf_categoria,text="Ir a Afip",command=lambda:self.ir_a_afip())
        btn_ir_afip.place(x=190,y=340)
        
        
        et_A = Label(inf_categoria,text="CATEGORIA A: ",justify="center",font=("arial",11,"bold"))
        et_A.place(x=20,y=50)
        et_A.config(bg=self.fondo)
        
        global var_A,txt_A
        var_A = StringVar()
        var_A.set("")
        
        txt_A = Entry(inf_categoria, width=20, textvariable=var_A, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_A.place(x=135, y=52)
        txt_A.config(bg=self.fondo)
        
        et_B = Label(inf_categoria,text="CATEGORIA B: ",justify="center",font=("arial",11,"bold"))
        et_B.place(x=20,y=80)
        et_B.config(bg=self.fondo)
        
        global var_B,txt_B
        var_B = StringVar()
        var_B.set("")
        txt_B = Entry(inf_categoria, width=20, textvariable=var_B, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_B.place(x=135, y=82)
        txt_B.config(bg=self.fondo)
        
        et_C = Label(inf_categoria,text="CATEGORIA C: ",justify="center",font=("arial",11,"bold"))
        et_C.place(x=20,y=110)
        et_C.config(bg=self.fondo)
        
        global var_C,txt_C
        var_C = StringVar()
        var_C.set("")
        txt_C = Entry(inf_categoria, width=20, textvariable=var_C, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_C.place(x=135, y=112)
        txt_C.config(bg=self.fondo)
        
        et_D = Label(inf_categoria,text="CATEGORIA D: ",justify="center",font=("arial",11,"bold"))
        et_D.place(x=20,y=140)
        et_D.config(bg=self.fondo)
        
        global var_D,txt_D
        var_D = StringVar()
        var_D.set("")
        txt_D = Entry(inf_categoria, width=20, textvariable=var_D, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_D.place(x=135, y=142)
        txt_D.config(bg=self.fondo)
        
        et_E = Label(inf_categoria,text="CATEGORIA E: ",justify="center",font=("arial",11,"bold"))
        et_E.place(x=20,y=170)
        et_E.config(bg=self.fondo)
        
        global var_E,txt_E
        var_E = StringVar()
        var_E.set("")
        txt_E = Entry(inf_categoria, width=20, textvariable=var_E, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_E.place(x=135, y=172)
        txt_E.config(bg=self.fondo)
        
        et_F = Label(inf_categoria,text="CATEGORIA F: ",justify="center",font=("arial",11,"bold"))
        et_F.place(x=20,y=200)
        et_F.config(bg=self.fondo)
        
        global var_F,txt_F
        var_F = StringVar()
        var_F.set("")
        txt_F = Entry(inf_categoria, width=20, textvariable=var_F, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_F.place(x=135, y=202)
        txt_F.config(bg=self.fondo)
        
        et_G = Label(inf_categoria,text="CATEGORIA G: ",justify="center",font=("arial",11,"bold"))
        et_G.place(x=20,y=230)
        et_G.config(bg=self.fondo)
        
        global var_G,txt_G
        var_G = StringVar()
        var_G.set("")
        txt_G = Entry(inf_categoria, width=20, textvariable=var_G, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_G.place(x=135, y=232)
        txt_G.config(bg=self.fondo)
        
        et_H = Label(inf_categoria,text="CATEGORIA H: ",justify="center",font=("arial",11,"bold"))
        et_H.place(x=20,y=260)
        et_H.config(bg=self.fondo)
        
        global var_H,txt_H
        var_H = StringVar()
        var_H.set("")
        txt_H = Entry(inf_categoria, width=20, textvariable=var_H, justify="center",font=("arial",11,"bold"),foreground="white")
        txt_H.place(x=135, y=262)
        txt_H.config(bg=self.fondo)

    def salir(self):
        self.mibase.desconectar()
        self.ventana1.quit()

    def cambio_color(self):
        color = askcolor(color="#00ff00")
        eleccion_color = color[1]
        self.mibase.grabar_config('color_fondo',eleccion_color)
        root.configure(bg=eleccion_color)
        self.etiqueta_concepto.config(bg=eleccion_color)
        self.etiqueta_fecha.config(bg=eleccion_color)
        self.etiqueta_monto.config(bg=eleccion_color)
        self.etiqueta_total.config(bg=eleccion_color)
        self.etiqueta_total_facturas.config(bg=eleccion_color)
        self.fondo= eleccion_color

    def ir_a_afip(self):
        web = self.mibase.return_config('link_afip')
        webbrowser.open(web)

    def agregar_concepto(self,concepto_elegido):
        concepto_elegido = concepto_elegido.get()
        if concepto_elegido == "Agregar Nuevo":

            # configuro el mensaje
            mensaje = "Ingrese un nuevo Concepto:"

            # Mostrar la ventana emergente con un ComboBox
            seleccion = simpledialog.askstring("Mensaje", mensaje, parent=self.ventana1)

            if seleccion:
                self.mibase.agrega_concepto(seleccion)
        
            self.lista_concepto = []
            datos = self.mibase.trae_conceptos()
            self.lista_concepto = [tupla[1] for tupla in datos]
            #Agrego a la lista el "Agregar Nuevo"
            self.lista_concepto += ["Agregar Nuevo"]
            self.combobox_concepto['values'] = self.lista_concepto

    def auxiliar_carga(self):
    ### VALIDACIONES DE LOS 3 campos de entrada Fecha, concepto y monto
    
        patron = r"^\d+(\.\d+)?$" #Valida numeros enteros y decimales.
        cadena =  self.txt_monto.get()
        if re.match (patron,cadena):
            pass
        else:
            messagebox.showinfo("AVISO","Para cargar una facturación tenes que completar un monto, pueden ser solo números. Si es decimal, va separado de punto.")
            self.txt_monto.focus()
            return
        
        validacion_concepto= self.concepto.get()
        if validacion_concepto == "":
            messagebox.showinfo ("AVISO","Tenes que ingresar el concepto de la factura.")
            self.combobox_concepto.focus()
            return
            
        else:
            self.objeto_modelo_bd.cargar_datos(self.txt_fecha.get(),self.combobox_concepto.get(),self.txt_monto.get())

        self.fecha.set("")
        self.concepto.set("")
        self.monto.set("")
        print ("Los registros fueron guardados con éxito.")
        
        self.actualizar_treeview()

    def actualizar_treeview(self):
        datos = self.objeto_modelo_bd.actualizar_treeview() 
        if datos == []:
            exit
        else:
            for x in datos:
                self.tabla.insert("",0,text=x[0],values=(x[1],x[2],("$"+str(x[3]))))
    
    def actualizar_fecha(self,event):
        fecha = self.calendar.get_date()
        self.fecha.set(fecha)
        print(fecha)








if __name__== "__main__":
    root = Tk()
    app = VentanaPrincipal(root)
    
    #ventana = VentanaInformacionCategoria(root)
    root.mainloop()


