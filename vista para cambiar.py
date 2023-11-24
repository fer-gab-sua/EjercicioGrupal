from tkinter import *
from tkinter.ttk import Combobox,Treeview
import tkinter as tk
from tkcalendar import Calendar , DateEntry
from tkinter.colorchooser import askcolor
import webbrowser
from tkinter import simpledialog, messagebox
#import re
<<<<<<< HEAD
from modelo import MiBaseDeDatos , BaseDeDatos , Validador
from datetime import datetime

=======
from modelo import MiBaseDeDatosConnect , ModeloCategorias, ModeloParaVista, Crud, ModeloConfig , Validador
#from modeloP import MiBaseDeDatosNw
>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724


class VentanaPrincipal():

    def __init__(self,ventana1) -> None:
        #inicio Objetos de base y validador
        self.validador = Validador()
        #Base de datos general
        self.mibase = MiBaseDeDatosConnect()
        self.mibase.carga_datos_iniciales()
        #base de datos config
        self.mibase_config = ModeloConfig()
        #base de datos Crud
        self.mibase_crud = Crud()
        #base de datos Cateogorias
        self.mibase_categorias = ModeloCategorias()
        #base para las vistas
        self.mibase_vista = ModeloParaVista()


        #SOLO A MODO PRUEBA
        #self.mibaseN = MiBaseDeDatosNw()

        self.ventana1 = ventana1
        self.ventana1.title ("FACTURACIÓN")
        self.ventana1.geometry("1000x600")

        #Funcion que trae la configuracion del color 
        self.fondo = self.mibase_config.return_config('color_fondo')
        
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
        self.etiqueta_total.config(bg=self.fondo,text="Total de facturas este mes: ",font=("Arial",16,"bold"))
        self.etiqueta_total_facturas = Label(self.ventana1, text="")
<<<<<<< HEAD
        self.etiqueta_total_facturas.place (x=520,y=372)
        self.etiqueta_total_facturas.config(bg=self.fondo,text="",font=("Arial",16,"bold"),foreground="RED")
=======
        self.etiqueta_total_facturas.place (x=470,y=390)
        suma = self.mibase_vista.sumar_facturacion()
        self.etiqueta_total_facturas.config(bg=self.fondo,text=suma,font=("Arial",16,"bold"),foreground="RED")
>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724
        
        ########FECHA
        self.fecha = StringVar()
        self.etiqueta_fecha = Label(self.ventana1, text="Fecha: ", font= ("arial",13,"bold"))
        self.etiqueta_fecha.place(x=10,y=45)
        self.etiqueta_fecha.config(bg=self.fondo)
        
        self.txt_fecha = Entry (self.ventana1, width=19, textvariable=self.fecha, justify="center",state="readonly")
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
        datos = self.mibase_config.return_conceptos()
        self.lista_concepto = [tupla[1] for tupla in datos]
        #Agrego a la lista el "Agregar Nuevo"
        self.lista_concepto += ["--"*5]
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
        

        self.btn_borrar = Button(self.ventana1, text="  BORRAR  ",command= self.aux_borrar_factura)
        self.btn_borrar.place (x=220, y=540 )
    

        self.btn_actualizar_categoria = Button (self.ventana1,text="DATOS DE \n CATEGORIZACIÓN",command=lambda:self.ventana_informacion_categoria(),anchor=CENTER)
        self.btn_actualizar_categoria.place(x=790,y=190)


        self.btn_modificar_carga = Button(self.ventana1,text="MODIFICAR",command=self.auxiliar_modificar_factura)
        self.btn_modificar_carga.place(x=100, y=540)


        self.btn_guardar_modificar_carga = Button(self.ventana1,text="GUARDAR",command=self.auxiliar_guardar_modificacion)
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


<<<<<<< HEAD
        #Labels para mostrar datos:

        #Facturado el mes actual:

        self.etiqueta_facturado_este_mes = Label(self.ventana1,
                                              text="FACTURADO ESTE MES: ",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_facturado_este_mes.place (x=680,y=250)
        self.etiqueta_facturado_este_mes.config(bg=self.fondo,
                                             font=("arial",14,"bold"))
        
        self.etiqueta_facturado_este_mes_rdo = Label(self.ventana1,
                                              text="$ 1000000",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_facturado_este_mes_rdo.place (x=910,y=250)
        self.etiqueta_facturado_este_mes_rdo.config(bg=self.fondo,
                                             font=("arial",14,"bold"))
        
        #PENDIENTE PARA PASAR DE CATEGORÍA:
        self.etiqueta_pendiente_pasar_categoria = Label(self.ventana1,
                                              text="FALTA PARA PASAR A: ",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_categoria.place (x=680,y=270)
        self.etiqueta_pendiente_pasar_categoria.config(bg=self.fondo,
                                             font=("arial",14,"bold"))
        
        self.etiqueta_pendiente_pasar_categoria_rdo = Label(self.ventana1,
                                              text="$ 100....",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_categoria_rdo.place (x=910,y=270)
        self.etiqueta_pendiente_pasar_categoria_rdo.config(bg=self.fondo,
                                             font=("arial",14,"bold"))
        
        # PENDIENTE PARA PASAR A RESPONSABLE INSCRIPTO
        self.etiqueta_pendiente_pasar_ri = Label(self.ventana1,
                                              text="FALTA PARA R.I: ",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_ri.place (x=680,y=290)
        self.etiqueta_pendiente_pasar_ri.config(bg=self.fondo,
                                             font=("arial",14,"bold"))
        
        self.etiqueta_pendiente_pasar_ri_rdo = Label(self.ventana1,
                                              text="$ 10.00000",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_ri_rdo.place (x=910,y=290)
        self.etiqueta_pendiente_pasar_ri_rdo.config(bg=self.fondo,
                                             font=("arial",14,"bold"))
        
        # TOTAL FACTURADO ESTE AŃO:
        self.etiqueta_total_facturado_anual = Label(self.ventana1,
                                              text="TOTAL FACTURADO ESTE AÑO: ",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_total_facturado_anual.place (x=680,y=310)
        self.etiqueta_total_facturado_anual.config(bg=self.fondo,
                                             font=("arial",14,"bold"))
        
        self.etiqueta_total_facturado_anual_rdo = Label(self.ventana1,
                                              text="$ 5000000",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_total_facturado_anual_rdo.place (x=910,y=310)
        self.etiqueta_total_facturado_anual_rdo.config  (bg=self.fondo,
                                                        font=("arial",14,"bold"))
        
        self.actualizar_calculos()
        

    
=======
>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724
    def ventana_informacion_categoria(self):
        
        self.inf_categoria = Toplevel()
        self.inf_categoria.title("Información para categorizar")
        self.inf_categoria.geometry("600x600")
        self.inf_categoria.config(bg=self.fondo)

        #DECLARO LAS VARIABLES DE LOS ENTRY

        ########################CATEGORÍAS:
        #TRAIGO LAS CATEGORIAS ACTIVAS DE LAS BASES Y LLENO LOS ENTRY
        resultado = {}
        categorias = self.mibase.return_categorias()
        for dato in categorias:
            letra = dato[1]
            importe = dato[2]
            resultado[letra] = importe

        self.var_A = StringVar()
        self.var_B = StringVar()
        self.var_C = StringVar()
        self.var_D = StringVar()
        self.var_E = StringVar()
        self.var_F = StringVar()
        self.var_G = StringVar()
        self.var_H = StringVar()

        self.var_A.set(resultado['A'])
        self.var_B.set(resultado['B'])
        self.var_C.set(resultado['C'])
        self.var_D.set(resultado['D'])
        self.var_E.set(resultado['E'])
        self.var_F.set(resultado['F'])
        self.var_G.set(resultado['G'])
        self.var_H.set(resultado['H'])


        et_categorias = Label(self.inf_categoria,text="CATEGORIAS",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_categorias.place (x=27,y=20)
        et_categorias.config(bg=self.fondo)
        
        et_montos = Label(self.inf_categoria,text="MONTOS",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_montos.place (x=180,y=20)
        et_montos.config(bg=self.fondo)
        
        et_fecha = Label(self.inf_categoria,text=" FECHA PARA\nCATEGORIZACION",justify="center",font=("arial",11,"bold"),foreground="RED")
        et_fecha.place (x=400,y=100)
        et_fecha.config(bg=self.fondo)
        
        
        
        self.txt_fecha_sqlite = StringVar()
        self.txt_fecha_sqlite= "2023/01/01"
        
        self.txt_fecha_categoria = DateEntry(self.inf_categoria,date_pattern="yyyy/mm/dd", width=15,justify="center",textvariable=self.txt_fecha_sqlite)
        self.txt_fecha_categoria.place(x=420,y=150)
        self.txt_fecha_categoria.config(state="readonly")
        self.txt_fecha_categoria.set_date(self.txt_fecha_sqlite)
        
    
        self.btn_modificar_datos = Button(self.inf_categoria,text="MODIFICAR DATOS",command=lambda:self.modificar_categorias_aux())
        self.btn_modificar_datos.place(x=160,y=300)
        
        btn_ir_afip = Button(self.inf_categoria,text="Ir a Afip",command=lambda:self.ir_a_afip())
        btn_ir_afip.place(x=190,y=340)
        
        
        et_A = Label(self.inf_categoria,text="CATEGORIA A: ",justify="center",font=("arial",11,"bold"))
        et_A.place(x=20,y=50)
        et_A.config(bg=self.fondo)
        
        self.txt_A = Entry(self.inf_categoria, width=20, textvariable=self.var_A, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_A.place(x=135, y=52)
        self.txt_A.config(bg=self.fondo)
        
        et_B = Label(self.inf_categoria,text="CATEGORIA B: ",justify="center",font=("arial",11,"bold"))
        et_B.place(x=20,y=80)
        et_B.config(bg=self.fondo)
        
        self.txt_B = Entry(self.inf_categoria, width=20, textvariable=self.var_B, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_B.place(x=135, y=82)
        self.txt_B.config(bg=self.fondo)
        
        et_C = Label(self.inf_categoria,text="CATEGORIA C: ",justify="center",font=("arial",11,"bold"))
        et_C.place(x=20,y=110)
        et_C.config(bg=self.fondo)
        
        self.txt_C = Entry(self.inf_categoria, width=20, textvariable=self.var_C, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_C.place(x=135, y=112)
        self.txt_C.config(bg=self.fondo)
        
        et_D = Label(self.inf_categoria,text="CATEGORIA D: ",justify="center",font=("arial",11,"bold"))
        et_D.place(x=20,y=140)
        et_D.config(bg=self.fondo)
        
        self.txt_D = Entry(self.inf_categoria, width=20, textvariable=self.var_D, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_D.place(x=135, y=142)
        self.txt_D.config(bg=self.fondo)
        
        et_E = Label(self.inf_categoria,text="CATEGORIA E: ",justify="center",font=("arial",11,"bold"))
        et_E.place(x=20,y=170)
        et_E.config(bg=self.fondo)

        self.txt_E = Entry(self.inf_categoria, width=20, textvariable=self.var_E, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_E.place(x=135, y=172)
        self.txt_E.config(bg=self.fondo)
        
        et_F = Label(self.inf_categoria,text="CATEGORIA F: ",justify="center",font=("arial",11,"bold"))
        et_F.place(x=20,y=200)
        et_F.config(bg=self.fondo)
        
        self.txt_F = Entry(self.inf_categoria, width=20, textvariable=self.var_F, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_F.place(x=135, y=202)
        self.txt_F.config(bg=self.fondo)
        
        et_G = Label(self.inf_categoria,text="CATEGORIA G: ",justify="center",font=("arial",11,"bold"))
        et_G.place(x=20,y=230)
        et_G.config(bg=self.fondo)
        
        self.txt_G = Entry(self.inf_categoria, width=20, textvariable=self.var_G, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_G.place(x=135, y=232)
        self.txt_G.config(bg=self.fondo)
        
        et_H = Label(self.inf_categoria,text="CATEGORIA H: ",justify="center",font=("arial",11,"bold"))
        et_H.place(x=20,y=260)
        et_H.config(bg=self.fondo)
        
        self.txt_H = Entry(self.inf_categoria, width=20, textvariable=self.var_H, justify="center",font=("arial",11,"bold"),foreground="white",state="disabled")
        self.txt_H.place(x=135, y=262)
        self.txt_H.config(bg=self.fondo)

    def modificar_categorias_aux(self):
        self.txt_A.config(state="normal")
        self.txt_B.config(state="normal")
        self.txt_C.config(state="normal")
        self.txt_D.config(state="normal")
        self.txt_E.config(state="normal")
        self.txt_F.config(state="normal")
        self.txt_G.config(state="normal")
        self.txt_H.config(state="normal")
        self.btn_modificar_datos.config(text="GUARDAR DATOS",command=lambda:self.guardar_categorias_aux())

    def guardar_categorias_aux(self):

        fecha_corte = self.txt_fecha_categoria.get()
        a = ["A",self.var_A.get(),fecha_corte]
        b = ["B",self.var_B.get(),fecha_corte]
        c = ["C",self.var_C.get(),fecha_corte]
        d = ["D",self.var_D.get(),fecha_corte]
        e = ["E",self.var_E.get(),fecha_corte]
        f = ["F",self.var_F.get(),fecha_corte]
        g = ["G",self.var_G.get(),fecha_corte]
        h = ["H",self.var_H.get(),fecha_corte]
        bloque_categorias = a,b,c,d,e,f,g,h

<<<<<<< HEAD
=======
        mostrar_advertencia = False

        for categoria in bloque_categorias:
            letra, valor, fecha = categoria
            if self.validador.valida_monto(valor) == "ERROR":
                mostrar_advertencia = True
                self.inf_categoria.title("Información para categorizar - ¡Error!")
        
        if mostrar_advertencia:
            messagebox.showwarning ("AVISO","Para cargar una categoria tenes que completar un monto, pueden ser solo números. Si es decimal, va separado de punto.")
            self.txt_A.focus()
        else:
            self.mibase_categorias.cambiar_categorias(bloque_categorias)
            self.btn_modificar_datos.config(text="MODIFICAR DATOS",command=lambda:self.modificar_categorias_aux())
            self.txt_A.config(state="disabled")
            self.txt_B.config(state="disabled")
            self.txt_C.config(state="disabled")
            self.txt_D.config(state="disabled")
            self.txt_E.config(state="disabled")
            self.txt_F.config(state="disabled")
            self.txt_G.config(state="disabled")
            self.txt_H.config(state="disabled")

>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724
    def salir(self):
        self.ventana1.quit()

    def cambio_color(self):
        color = askcolor(color="#00ff00")
        eleccion_color = color[1]
        self.mibase_config.grabar_config('color_fondo',eleccion_color)
        root.configure(bg=eleccion_color)
        self.etiqueta_concepto.config(bg=eleccion_color)
        self.etiqueta_fecha.config(bg=eleccion_color)
        self.etiqueta_monto.config(bg=eleccion_color)
        self.etiqueta_total.config(bg=eleccion_color)
        self.etiqueta_total_facturas.config(bg=eleccion_color)
        self.fondo= eleccion_color

    def ir_a_afip(self):
        web = self.mibase_config.return_config('link_afip')
        webbrowser.open(web)

    def agregar_concepto(self,concepto_elegido):
        concepto_elegido = concepto_elegido.get()
        if concepto_elegido == "Agregar Nuevo":

            # configuro el mensaje
            mensaje = "Ingrese un nuevo Concepto:"

            # Mostrar la ventana emergente con un ComboBox
            seleccion = simpledialog.askstring("Mensaje", mensaje, parent=self.ventana1)

            if seleccion:
                self.mibase_config.agrega_concepto(seleccion)
        
            self.lista_concepto = []
            datos = self.mibase_config.return_conceptos()
            self.lista_concepto = [tupla[1] for tupla in datos]
            #Agrego a la lista el "Agregar Nuevo"
            self.lista_concepto += ["Agregar Nuevo"]
            self.combobox_concepto['values'] = self.lista_concepto

    def auxiliar_carga(self):
    ### VALIDACIONES DE LOS 3 campos de entrada Fecha, concepto y monto
        valido_monto = self.txt_monto.get()
        
        
        if self.validador.valida_monto(valido_monto) == "OK":
            pass
        else:
            messagebox.showwarning ("AVISO","Para cargar una facturación tenes que completar un monto, pueden ser solo números. Si es decimal, va separado de punto.")
            return
        
        validacion_concepto= self.concepto.get()

        if self.validador.valida_concepto(validacion_concepto) == "ERROR":
            messagebox.showinfo ("AVISO","Tenes que ingresar el concepto de la factura.")
            self.combobox_concepto.focus()
            return
        
        valido_fecha = self.txt_fecha.get()
        if self.validador.valida_fecha (valido_fecha) == "ERROR":
            messagebox.showinfo("AVISO","Tenes que llenar la fecha para cargar la factura.")
            self.txt_fecha.focus()
            return
        
        else:
            self.mibase_crud.cargar_datos(self.txt_fecha.get(),self.combobox_concepto.get(),self.txt_monto.get(),"null")

        self.fecha.set("")
        self.concepto.set("")
        self.monto.set("")

        
        self.actualizar_treeview()
        self.actualizar_calculos()

    def actualizar_treeview(self):
        actualizacion = self.tabla.get_children() 
        for R in actualizacion: 
            self.tabla.delete(R)
        
<<<<<<< HEAD
        datos = self.objeto_modelo_bd.actualizar_treeview()
        print (datos)
        
=======
        #datos = self.mibaseN.actualizar_treeview()
        datos = self.mibase_vista.actualizar_treeview()
>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724
        if datos == []:
            exit
        else:
            for x in datos:
                formatear_fecha = datetime.strptime(x[1],"%Y/%m/%d")
                formato_fecha="%d/%m/%Y"
                fecha_formateada = formatear_fecha.strftime(formato_fecha) 
                self.tabla.insert("",0,text=x[0],values=(fecha_formateada,x[2],("$"+str(x[3])))) #inserto la consulta en la tabla y convierto en string la 3er columna, para poder agregar el
                   
    def actualizar_fecha(self,event):
        fecha = self.calendar.get_date()
        self.fecha.set(fecha)


    def aux_borrar_factura(self):
        seleccion= self.tabla.focus() 
        if seleccion ==(""):
            messagebox.showwarning("AVISO","Tenes que seleccionar el registro que queres borrar.")
            exit
        else:
            respuesta = messagebox.askquestion("Consulta","Estas seguro que vas a borrar el registro?")
            if respuesta =="yes":
                item=self.tabla.item(seleccion) 
                borrar =(item.get("text"),) 
                self.mibase_crud.borrar_datos(borrar)
                self.actualizar_treeview() 
            else:
                exit      
    
<<<<<<< HEAD
    def auxiliar_modificar_factura(self):
=======
    def auxiliar_modificar_factura(self):#VER TEMA VALIDACIONES CUANDO SE MODIFICA

        
>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724
        seleccion= self.tabla.focus() 
        if seleccion ==(""):
            messagebox.showwarning("AVISO","Tenes que seleccionar el registro que queres modificar.")
            exit
        else:
            self.btn_actualizar_categoria.config(state="disabled")
            self.btn_borrar.config(state="disabled")
            self.btn_cargar.config(state="disabled")
            self.btn_ver_graficos.config(state="disabled")
            self.btn_modificar_carga.config(state="disabled")
            self.btn_guardar_modificar_carga.place(x=420, y=270)
            
            seleccion = self.tabla.focus()
            item=self.tabla.item(seleccion)

            print (item)
            print (item ["values"][0])
           
        
            self.txt_fecha.insert(0,item['values'][0])
            self.combobox_concepto.set(item['values'][1])
            con_simbolo= item['values'][2]
            sin_simbolo= con_simbolo.replace('$',"")
            self.txt_monto.insert(0,sin_simbolo)
            self.txt_monto.focus()

<<<<<<< HEAD
    def auxiliar_guardar_modificacion(self,): 
=======
    def auxiliar_guardar_modificacion(self,):  
>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724
        seleccion = self.tabla.focus()
        item=self.tabla.item(seleccion) 
        id_factura = item["text"]

        act_fecha = self.txt_fecha.get()
        act_concepto = self.combobox_concepto.get()
        act_monto = self.txt_monto.get()
        
        self.mibase_crud.actualizar_datos(act_fecha,act_concepto,act_monto,id_factura)

        
        self.actualizar_treeview()
        

        self.btn_actualizar_categoria.config(state="active")
        self.btn_borrar.config(state="active")
        self.btn_cargar.config(state="active")
        self.btn_ver_graficos.config(state="active")
        self.btn_modificar_carga.config(state="active")
        self.btn_guardar_modificar_carga.place_forget()
        
        self.fecha.set("")
        self.concepto.set("")
        self.monto.set("")
        messagebox.showinfo ("AVISO", "Los datos se modificaron con éxito.")
<<<<<<< HEAD
            
    def actualizar_calculos(self):
        cantidad_facturas = self.objeto_modelo_bd.calculos_total_facturas()
        self.etiqueta_total_facturas.config(text=cantidad_facturas)

        

            
            
    
=======
>>>>>>> 24d481671cac1ab59bd838b9d3dedc222867f724



if __name__== "__main__":
    root = Tk()
    app = VentanaPrincipal(root)
    
    #ventana = VentanaInformacionCategoria(root)
    root.mainloop()

