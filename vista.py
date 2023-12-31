# v2.6.1
"""VISTA ENCARGADA DE MOSTRAR TODA LA INFORMACION CON EL USUARIO
"""

from tkinter import *
from tkinter.ttk import Combobox,Treeview
import tkinter as tk
from tkcalendar import Calendar , DateEntry
from tkinter.colorchooser import askcolor
import webbrowser
from tkinter import simpledialog, messagebox
#import re
from modelo import MiBaseDeDatosConnect , ModeloCategorias, ModeloParaVista, Crud, ModeloConfig , Validador,Estadisticas
#from modeloP import MiBaseDeDatosNw
from datetime import datetime

__author__ = "Fernando Suarez, Damian Colomb"
__mainteinter__ = "Fernando Suarez, Damian Colomb"
__email__ = "fer.gab.sua@gmail.com , colomb.damian@gmail.com"
__copyrigth__ = "Copyright 2023"
__version__ = "0.1"


class VentanaPrincipal():


    def __init__(self,ventana1) -> None:
        """
        Clase principal que define la interfaz gráfica y funcionalidades de la aplicación.

        Args:
            ventana_raiz (Tk): Ventana principal de la aplicación.
        """
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
        #Estadisticas
        self.mibase_estadistica = Estadisticas()

        #SOLO A MODO PRUEBA
        #self.mibaseN = MiBaseDeDatosNw()

        self.ventana1 = ventana1
        self.ventana1.title ("FACTURACIÓN")
        self.ventana1.geometry("1150x600")

        #Funcion que trae la configuracion del color 
        self.fondo = self.mibase_config.return_config('color_fondo')
        
        self.ventana1.config(bg=self.fondo)

        ### FRAME CATEGORÍA:
        frame_categoria = Frame(self.ventana1)
        frame_categoria.config(width=260,height=130,bg="gray50")
        frame_categoria.place(x=750,y=50)

        ###LABEL CATEGORIA
        self.etiqueta_frame = Label(self.ventana1, text="CATEGORIA: ",font= ("arial",25,"bold"))
        self.etiqueta_frame.place (x=780,y=50)
        self.etiqueta_frame.config(bg="gray50",foreground="black")
        
        self.label_categoria = Label(self.ventana1)
        self.label_categoria.place(x=840,y=90)
        self.label_categoria.config(bg="gray50",text="",font=("Arial",50,"bold"),foreground="GREEN")

        ### LABEL AÑO FISCAL
        fecha_actual = datetime.now()

        self.anio_fiscal = int(fecha_actual.year)
        self.label_anio_fiscal = Label(self.ventana1 , text=self.anio_fiscal,font= ("arial",25,"bold"),background=self.fondo)
        self.label_anio_fiscal.place(x=840 , y=0)

        ################################WIDGETS###########################################

        # ETIQUETAS:
        
        

        ############ MOSTRAR TOTALES: 
        self.etiqueta_total = Label(self.ventana1)
        self.etiqueta_total.place (x=430,y=350)
        self.etiqueta_total.config(bg=self.fondo,text="Total de facturas: ",font=("Arial",16,"bold"))
        self.etiqueta_total_facturas = Label(self.ventana1, text="")
        self.etiqueta_total_facturas.place (x=470,y=390)
        suma = self.mibase_vista.sumar_facturacion()
        self.etiqueta_total_facturas.config(bg=self.fondo,text=suma,font=("Arial",16,"bold"),foreground="RED")

        #Labels para mostrar datos:
        
        #FACTURADO MES ACTUAL:
        self.etiqueta_facturado_este_mes = Label(self.ventana1,
                                              text="FACTURADO ESTE MES: ",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_facturado_este_mes.place (x=680,y=250)
        self.etiqueta_facturado_este_mes.config(bg=self.fondo,
                                             font=("arial",12,"bold"))
        
        self.etiqueta_facturado_este_mes_rdo = Label(self.ventana1,
                                              text="",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_facturado_este_mes_rdo.place (x=940,y=250)
        self.etiqueta_facturado_este_mes_rdo.config(bg=self.fondo,
                                             font=("arial",12,"bold"))
        
        
        #PENDIENTE PARA PASAR DE CATEGORÍA:
        self.etiqueta_pendiente_pasar_categoria = Label(self.ventana1,
                                              text="FALTA PARA PASAR A: ",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_categoria.place (x=680,y=280)
        self.etiqueta_pendiente_pasar_categoria.config(bg=self.fondo,
                                             font=("arial",12,"bold"))
        
        self.etiqueta_pendiente_pasar_categoria_rdo = Label(self.ventana1,
                                              text="",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_categoria_rdo.place (x=940,y=280)
        self.etiqueta_pendiente_pasar_categoria_rdo.config(bg=self.fondo,
                                             font=("arial",12,"bold"))
        
        # PENDIENTE PARA PASAR A RESPONSABLE INSCRIPTO
        self.etiqueta_pendiente_pasar_ri = Label(self.ventana1,
                                              text="FALTA PARA RESPONSABLE INSCRIPTO:",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_ri.place (x=680,y=310)
        self.etiqueta_pendiente_pasar_ri.config(bg=self.fondo,
                                             font=("arial",12,"bold"))
        
        self.etiqueta_pendiente_pasar_ri_rdo = Label(self.ventana1,
                                              text="",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_pendiente_pasar_ri_rdo.place (x=940,y=310)
        self.etiqueta_pendiente_pasar_ri_rdo.config(bg=self.fondo,
                                             font=("arial",12,"bold"))
        
        # TOTAL FACTURADO ESTE AŃO:
        self.etiqueta_total_facturado_anual = Label(self.ventana1,
                                              text="TOTAL FACTURADO ESTE AÑO: ",
                                              foreground="White",
                                              anchor=CENTER)
        self.etiqueta_total_facturado_anual.place (x=680,y=340)
        self.etiqueta_total_facturado_anual.config(bg=self.fondo,
                                             font=("arial",12,"bold"))
        
        self.etiqueta_total_facturado_anual_rdo = Label(self.ventana1,
                                              text="$ 5000000",
                                              foreground="red",
                                              anchor=CENTER)
        self.etiqueta_total_facturado_anual_rdo.place (x=940,y=340)
        self.etiqueta_total_facturado_anual_rdo.config  (bg=self.fondo,
                                              font=("arial",12,"bold"))
        
        self.actualizar_calculos()
        self.manejo_categorias()
        
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

        #llamo al metodo para llenar la lista de conceptos.
        
        self.lista_concepto = []
                
        self.combobox_concepto = Combobox(self.ventana1,values=self.lista_concepto,state="readonly",width=19,justify="center",textvariable=self.concepto) # Readonly, lo que hace es que no se pueda escribir en el combobox.
        self.combobox_concepto.place (x=100,y=275) 
        self.carga_lista()


        #agrego la funcionalidad de agregar a la base de datos un nuevo registro
        self.combobox_concepto.bind("<<ComboboxSelected>>", lambda event: self.ab_concepto(self.concepto)) 
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
        #self.btn_ver_graficos.place(x=420,y=450) 
        

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
        menu_archivo.add_command(label="Exportar",command=lambda:self.mibase_estadistica.exportar())
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cambiar estilo", command=lambda:self.cambio_color())
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cambiar Año",command=lambda:self.cambio_anio_fiscal())
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Acerca del programa",command=self.acerca_del_programa)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=lambda:self.salir())
        menubar.add_cascade (label="Archivo",menu=menu_archivo)
        self.ventana1.config(menu=menubar)  

    def ventana_informacion_categoria(self):
        """Ventana Auxiliar de categorias
        """
        self.inf_categoria = Toplevel()
        self.inf_categoria.title("Información para categorizar")
        self.inf_categoria.geometry("600x600")
        self.inf_categoria.config(bg=self.fondo)

        #DECLARO LAS VARIABLES DE LOS ENTRY

        ########################CATEGORÍAS:
        #TRAIGO LAS CATEGORIAS ACTIVAS DE LAS BASES Y LLENO LOS ENTRY
        resultado = {}
        categorias = self.mibase_categorias.traer_categorias()
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

    def pantalla_auxiliar_concepto(self):
        """
        Crea y muestra una ventana secundaria para eliminar un concepto.
        """
        self.eli_concepto = Toplevel()
        self.eli_concepto.title("Eliminar concepto")
        self.eli_concepto.geometry("300x300")
        self.eli_concepto.config(bg=self.fondo)

        self.concepto_ab = StringVar()

        label_concepto_ab = Label(self.eli_concepto,text="Selecciones concepto a eliminar:",justify="center",font=("arial",11,"bold"),foreground="RED", background=self.fondo)
        label_concepto_ab.place(x=10, y=20)

        self.lista_conceptos_ab = Listbox(self.eli_concepto, selectmode="SINGLE")
        self.lista_conceptos_ab.place(x=10, y = 50)


                
        datos = self.mibase_config.return_conceptos()
        for tupla in datos:
            self.lista_conceptos_ab.insert("end", tupla[1])
        
        self.btn_borrar = Button(self.eli_concepto, text = "Borrar",command=lambda: self.aux_borrar_concepto())
        self.btn_borrar.place(x=140,y=250)

    def aux_borrar_concepto(self):
        """
        Maneja la eliminación de un concepto seleccionado.
        """
        indices_seleccionados = self.lista_conceptos_ab.curselection()
        if indices_seleccionados:
        # Obtener el elemento real utilizando el índice
            elemento_seleccionado = self.lista_conceptos_ab.get(indices_seleccionados[0])
            respuesta = messagebox.askquestion("Consulta",f"Estas seguro que vas a borrar el registro? {elemento_seleccionado}")
            if respuesta =="yes":
                self.mibase_config.borra_concepto(elemento_seleccionado)
                self.carga_lista()
                self.eli_concepto.destroy()
                


    def modificar_categorias_aux(self):
        """
        Habilita la modificación de categorías.
        """
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
        """
        Guarda las categorías modificadas.
        """
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

    def salir(self):
        """
        Cierra la aplicación.
        """
        self.ventana1.quit()

    def cambio_color(self):
        """
        Cambia el color de fondo de la interfaz.
        """
        color = askcolor(color="#00ff00")
        eleccion_color = color[1]
        self.mibase_config.grabar_config('color_fondo',eleccion_color)
        root.configure(bg=eleccion_color)
        self.etiqueta_concepto.config(bg=eleccion_color)
        self.etiqueta_fecha.config(bg=eleccion_color)
        self.etiqueta_monto.config(bg=eleccion_color)
        self.etiqueta_total.config(bg=eleccion_color)
        self.etiqueta_total_facturas.config(bg=eleccion_color)
        self.etiqueta_facturado_este_mes.config(bg=eleccion_color)
        self.etiqueta_facturado_este_mes_rdo.config(bg=eleccion_color)
        self.etiqueta_pendiente_pasar_categoria.config(bg=eleccion_color)
        self.etiqueta_pendiente_pasar_categoria_rdo.config(bg=eleccion_color)
        self.fondo = eleccion_color
        self.etiqueta_pendiente_pasar_ri.config(bg=eleccion_color)
        self.etiqueta_pendiente_pasar_ri_rdo.config(bg=eleccion_color)
        self.etiqueta_total_facturado_anual.config(bg=eleccion_color)
        self.etiqueta_total_facturado_anual_rdo.config(bg=eleccion_color)
        self.label_anio_fiscal.config(bg=eleccion_color)


    def ir_a_afip(self):
        """
        Abre el navegador con el enlace a la AFIP.
        """
        web = self.mibase_config.return_config('link_afip')
        webbrowser.open(web)

    def ab_concepto(self,concepto_elegido):
        """
        Maneja la lógica al elegir una opción en el menú de conceptos.

        Args:
            concepto_elegido (StringVar): Variable que almacena la opción seleccionada en el menú.
        """
        concepto_elegido = concepto_elegido.get()
        if concepto_elegido == "Agregar Nuevo":

            # configuro el mensaje
            mensaje = "Ingrese un nuevo Concepto:"

            # Mostrar la ventana emergente con un ComboBox
            seleccion = simpledialog.askstring("Conceptos", mensaje, parent=self.ventana1)

            if seleccion:
                self.mibase_config.agrega_concepto(seleccion)
                

        elif concepto_elegido == "Eliminar Concepto":
            self.pantalla_auxiliar_concepto()
            
        self.carga_lista()

    def auxiliar_carga(self):
        """
        Realiza validaciones y carga los datos de una factura.
        """
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
            formatear_fecha = datetime.strptime(self.txt_fecha.get(), '%d/%m/%Y')
            formato_fecha="%Y/%m/%d"
            fecha_formateada = formatear_fecha.strftime(formato_fecha)
            self.mibase_crud.cargar_datos(fecha_formateada,self.combobox_concepto.get(),self.txt_monto.get(),"null")

        self.fecha.set("")
        self.concepto.set("")
        self.monto.set("")

        
        self.actualizar_treeview()

    def actualizar_treeview(self):
        """
        Actualiza la vista de tabla con los datos de la base de datos.
        """
        actualizacion = self.tabla.get_children() 
        for R in actualizacion: 
            self.tabla.delete(R)
        
        #datos = self.mibaseN.actualizar_treeview()
        datos = self.mibase_vista.actualizar_treeview(str(self.anio_fiscal))
        if datos == []:
            exit
        else:
            for x in datos:
                formatear_fecha = datetime.strptime(x[1],"%Y/%m/%d")
                formato_fecha="%d/%m/%Y"
                fecha_formateada = formatear_fecha.strftime(formato_fecha) 
                self.tabla.insert("",0,text=x[0],values=(fecha_formateada,x[2],("$"+str(x[3])))) #inserto la consulta en la tabla y convierto en string la 3er columna, para poder agregar el
        self.actualizar_calculos()
        self.manejo_categorias()
        self.falta_ri_aux()
        self.facturacion_anual_aux()
        
    def actualizar_fecha(self,event):
        """
        Actualiza la fecha en la interfaz gráfica con la fecha seleccionada en el calendario.

        Parámetros:
        - event: El evento que desencadena la actualización de la fecha.
        """
        fecha = self.calendar.get_date()
        self.fecha.set(fecha)

    def aux_borrar_factura(self):
        """
        Borra la factura seleccionada en la tabla después de confirmar la acción.

        No tiene parámetros.
        """
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
    
    def auxiliar_modificar_factura(self):
        """
        Configura la interfaz gráfica para permitir la modificación de la factura seleccionada.
        Deshabilita varios botones y muestra el botón para guardar las modificaciones.

        """ 
        
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
            fecha_especifica = item['values'][0]
            self.fecha.set(fecha_especifica)
            self.calendar.selection_set(fecha_especifica)

            self.combobox_concepto.set(item['values'][1])
            con_simbolo= item['values'][2]
            sin_simbolo= con_simbolo.replace('$',"")
            self.txt_monto.insert(0,sin_simbolo)
            self.txt_monto.focus()

    def auxiliar_guardar_modificacion(self,):  
        """
        Guarda las modificaciones realizadas en una factura seleccionada y actualiza la interfaz gráfica.
        Habilita los botones previamente deshabilitados.

        """
        seleccion = self.tabla.focus()
        item=self.tabla.item(seleccion) 
        id_factura = item["text"]

        act_fecha = self.txt_fecha.get()


        formatear_fecha = datetime.strptime(self.txt_fecha.get(), '%d/%m/%Y')
        formato_fecha="%Y/%m/%d"
        act_fecha = formatear_fecha.strftime(formato_fecha)

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

    def actualizar_calculos(self):
        """
        Actualiza los cálculos y las etiquetas relacionadas con las estadísticas de facturación.
        Utiliza métodos de la clase 'mibase_estadistica'.

        """
        mes_actual = str(datetime.now().month)
        
        cantidad_facturas = self.mibase_estadistica.calculos_total_facturas(self.anio_fiscal)
        facturado_mes_actual = self.mibase_estadistica.facturado_mes_actual(mes_actual)
        
        ## labels calculados:
        self.etiqueta_total_facturas.config(text=cantidad_facturas)
        
        if facturado_mes_actual[0] == None:
            self.etiqueta_facturado_este_mes_rdo.config(text= "0")
        else:
            self.etiqueta_facturado_este_mes_rdo.config(text=f"$ {facturado_mes_actual[0]}")
    
    def manejo_categorias(self):
        """
        Maneja las categorías y actualiza la etiqueta 'label_categoria' con la categoría correspondiente.
        También actualiza otras etiquetas relacionadas con las categorías.

        """
   
        (
            self.cat_A,
            self.cat_B,
            self.cat_C,
            self.cat_D,
            self.cat_E,
            self.cat_F,
            self.cat_G,
            self.cat_H
        )   = self.mibase_estadistica.devolver_categorias()
            
         
         
         
        facturado_este_periodo = self.mibase_estadistica.total_facturado_periodo() # Traigo el total facturado del periodo
       
        
        # Valido en el caso que no hay datos en la db
        if facturado_este_periodo[0] == None:
            self.label_categoria.config(font= ("arial",12,"bold"),text="NO HAY DATOS REGISTRADOS",fg="Yellow")
            self.label_categoria.place(x=760,y=100)
            self.etiqueta_pendiente_pasar_categoria.config(text="-")
            self.etiqueta_pendiente_pasar_categoria_rdo.config(text="-")
            self.etiqueta_pendiente_pasar_ri.config(text="-")
            self.etiqueta_pendiente_pasar_ri_rdo.config(text="-")
            self.etiqueta_total_facturado_anual.config(text="-")
            self.etiqueta_total_facturado_anual_rdo.config (text = "-")
            #Cambia las etiquetas que queden todas vacias en los cálculos.
            
            return
        else:
            monto_facturado = float(facturado_este_periodo[0])

        #### En caso que haya datos: Modifico el label de la categoría    ok
            if monto_facturado < self.cat_A :
                self.label_categoria.config(text="A",font= ("arial",50,"bold"),fg="Green")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="FALTA PARA PASAR A B: ")
                falta_para_pasar = self.cat_A - monto_facturado
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text=f"$ {round(falta_para_pasar,2)}")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")


            #ok
            elif monto_facturado > self.cat_A and monto_facturado <= self.cat_B:
                self.label_categoria.config(text="B",font= ("arial",50,"bold"),fg="Green")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="FALTA PARA PASAR A C: ")
                falta_para_pasar = self.cat_B - monto_facturado
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text=f"$ {round(falta_para_pasar,2)}")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")



            elif monto_facturado > self.cat_B and monto_facturado <= self.cat_C:
                print("ACA LLEGO")
                self.label_categoria.config(text="C",font= ("arial",50,"bold"),fg="Green")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="FALTA PARA PASAR A D: ")
                falta_para_pasar = self.cat_C - monto_facturado
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text=f"$ {round(falta_para_pasar,2)}")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")
            
            elif monto_facturado > self.cat_C and monto_facturado <= self.cat_D:
                self.label_categoria.config(text="D",font= ("arial",50,"bold"),fg="Green")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="FALTA PARA PASAR A E: ")
                falta_para_pasar = self.cat_D - monto_facturado
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text=f"$ {round(falta_para_pasar,2)}")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")
            
            elif monto_facturado > self.cat_D and monto_facturado <= self.cat_E:
                self.label_categoria.config(text="E",font= ("arial",50,"bold"),fg="Green")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="FALTA PARA PASAR A F: ")
                falta_para_pasar = self.cat_E - monto_facturado
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text=f"$ {round(falta_para_pasar,2)}")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")
            
            elif monto_facturado > self.cat_E and monto_facturado <= self.cat_F:
                self.label_categoria.config(text="F",font= ("arial",50,"bold"),fg="Green")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="FALTA PARA PASAR A G: ")
                falta_para_pasar = self.cat_F - monto_facturado
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text=f"$ {round(falta_para_pasar,2)}")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")

            elif monto_facturado > self.cat_F and monto_facturado <= self.cat_G:
                self.label_categoria.config(text="G",font= ("arial",50,"bold"),fg="Green")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="FALTA PARA PASAR A H: ")
                falta_para_pasar = self.cat_G - monto_facturado
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text=f"$ {round(falta_para_pasar,2)}")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")

            elif monto_facturado > self.cat_G and monto_facturado <= self.cat_H:
                self.label_categoria.config(text="H",font= ("arial",50,"bold"),fg="Red")
                self.label_categoria.place (x=840, y= 90)
                self.etiqueta_pendiente_pasar_categoria.config(text="--")
                self.etiqueta_pendiente_pasar_ri.config(text="FALTA PARA RESPONSABLE INSCRIPTO: ")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")
                falta_para_pasar = self.cat_H - monto_facturado
                self.etiqueta_pendiente_pasar_ri_rdo.config(text=f"${round(falta_para_pasar)}")
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text="--")
            
            elif monto_facturado > self.cat_H:
                self.label_categoria.config(font= ("arial",13,"bold"),text="RESPONSABLE INSCRIPTO",fg="black")
                self.label_categoria.place(x=770,y=100)
                self.etiqueta_pendiente_pasar_categoria.config(text="- ")
                self.etiqueta_pendiente_pasar_categoria_rdo.config(text="-")
                
                self.etiqueta_pendiente_pasar_ri.config(text="-")
                self.etiqueta_total_facturado_anual.config(text="FACTURADO ESTE AÑO: ")
            
    def falta_ri_aux(self):
        """
        Muestra la falta a facturar para un responsable inscripto en la etiqueta correspondiente.

        """
        falta_ri = self.mibase_estadistica.falta_facturar_responsable_inscripto()
        
        if falta_ri is None:
            self.etiqueta_pendiente_pasar_ri_rdo.config(text="-")
        elif falta_ri =="negativo":
            self.etiqueta_pendiente_pasar_ri_rdo.config(text="-")
        else:
            self.etiqueta_pendiente_pasar_ri_rdo.config(text=f"$ {falta_ri}")

    def facturacion_anual_aux(self):
        """
        Muestra el total facturado en el año actual en la etiqueta correspondiente.

        """

        año_actual = datetime.now().year
        primer_dia_año = datetime(año_actual, 1, 1)

        
    
        facturacion_anual = self.mibase_estadistica.facturado_anual(primer_dia_año)
        
        if facturacion_anual[0] is None:
            self.etiqueta_total_facturado_anual_rdo.config (text="-")
        else:
            self.etiqueta_total_facturado_anual_rdo.config(text=f"$ {facturacion_anual[0]}")
        
    def carga_lista(self):
        """
        Carga la lista de conceptos en la interfaz gráfica.
    
        """

        self.lista_concepto = []
        datos = self.mibase_config.return_conceptos()
        self.lista_concepto = [tupla[1] for tupla in datos]
        self.lista_concepto += ["--"*5]
        self.lista_concepto += ["Agregar Nuevo"]
        self.lista_concepto += ["Eliminar Concepto"]


        self.combobox_concepto['values'] = self.lista_concepto

    def cambio_anio_fiscal(self):
        """
        Cambia el año fiscal y actualiza la interfaz gráfica.

        """
        # configuro el mensaje
        mensaje = "Ingrese el año fiscal"

        # Mostrar la ventana emergente con un ComboBox
        seleccion = simpledialog.askstring("Año Fiscal", mensaje, parent=self.ventana1)

        if seleccion:
            
            if self.validador.valida_entero(seleccion) == "ERROR":
                messagebox.showinfo ("AVISO","Tenes que ingresar un año valido.")
                self.combobox_concepto.focus()
                return
            self.anio_fiscal = seleccion
            self.label_anio_fiscal.config(text=self.anio_fiscal)
            self.actualizar_treeview()

    def acerca_del_programa(self):
        """
        Muestra información sobre la aplicación y sus desarrolladores.
    
        """
        messagebox.showinfo("INFORMACIÓN","Esta aplicación fue desarrollada por Fernando Suarez y Damián Colomb como entrega final \
                            del curso python intermedio del centro de E-Learning de la Univesidad Tecnológica Nacional.")
    

if __name__== "__main__":
    root = Tk()
    app = VentanaPrincipal(root)
    
    root.mainloop()


