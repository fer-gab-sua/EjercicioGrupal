import sqlite3
import re
import tkinter as tk
from tkinter import messagebox, Toplevel,filedialog,ttk
import vista
from tkinter.colorchooser import askcolor
import pandas as pd
from tkcalendar import DateEntry
from datetime import datetime


def modificar_datos_categorizacion():
    
    patron_mod_cat = r"^\d+(\.\d+)?$"
        
    validacion_A = vista.txt_A.get()
    validacion_B = vista.txt_B.get()
    validacion_C = vista.txt_C.get()
    validacion_D = vista.txt_D.get()
    validacion_E = vista.txt_E.get()
    validacion_F = vista.txt_F.get()
    validacion_G = vista.txt_G.get()
    validacion_H = vista.txt_H.get()
    validacion_fecha = vista.txt_fecha_categoria.get()
    
    con = conexion()
    cursor = con.cursor()
    
    
    
    if re.match (patron_mod_cat,validacion_A):
        actualizar = (vista.txt_A.get(),"A")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizar)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_A.focus()
        return
    if re.match (patron_mod_cat,validacion_B):
        actualizarB = (vista.txt_B.get(),"B")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizarB)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_B.focus()
        return
    if re.match (patron_mod_cat,validacion_C):
        actualizarC = (vista.txt_C.get(),"C")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizarC)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_C.focus()
        return
    if re.match (patron_mod_cat,validacion_D):
        actualizarD = (vista.txt_D.get(),"D")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizarD)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_D.focus()
        return
    if re.match (patron_mod_cat,validacion_E):
        actualizarE = (vista.txt_E.get(),"E")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizarE)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_E.focus()
        return
    if re.match (patron_mod_cat,validacion_F):
        actualizarF = (vista.txt_F.get(),"F")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizarF)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_F.focus()
        return
    if re.match (patron_mod_cat,validacion_G):
        actualizarG = (vista.txt_G.get(),"G")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizarG)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_G.focus()
        return
    if re.match (patron_mod_cat,validacion_H):
        actualizarH = (vista.txt_H.get(),"H")
        sql="UPDATE Categorias SET Monto = ? Where Categoria=?;"
        cursor.execute(sql,actualizarH)
        con.commit()
    else:
        messagebox.showinfo("AVISO","El dato de la categoría, tiene que ser un número. Si es decimal, va separado de punto.")
        vista.txt_H.focus()
        return
    
        
    
    actualizar_fecha = (validacion_fecha,"1")
    sql="UPDATE Fecha_categoria SET Fecha = ? Where id=?;"
    cursor.execute(sql,actualizar_fecha)
    
    con.commit()
    con.close()
    
    vista.inf_categoria.grab_set()
    messagebox.showinfo("AVISO","Los datos se guardaron con éxito.")
     
def conexion():
    conexion_bd = sqlite3.connect("bd.db")
    return conexion_bd

def crear_bd():
    con = conexion()
    mi_cursor = con.cursor() 
    sql0 = "CREATE TABLE IF NOT EXISTS Facturacion (id INTEGER, Fecha TEXT, Concepto TEXT, Monto NUMERIC, PRIMARY KEY(id AUTOINCREMENT))"
    mi_cursor.execute(sql0)
    sql01 = "CREATE TABLE IF NOT EXISTS Fondo (id INTEGER, Color TEXT, PRIMARY KEY(id AUTOINCREMENT))"
    mi_cursor.execute (sql01)
    sql02 = "INSERT INTO Fondo (Color) SELECT '#004080' WHERE NOT EXISTS (SELECT 1 FROM Fondo WHERE id = '1')"
    mi_cursor.execute(sql02)
    sql03 = "CREATE TABLE IF NOT EXISTS Fecha_categoria(id INTEGER, Fecha TEXT, PRIMARY KEY (id AUTOINCREMENT))"
    mi_cursor.execute(sql03)
    
    sql04 = "INSERT INTO Fecha_categoria (Fecha) SELECT '2023/01/01' WHERE NOT EXISTS (SELECT 1 FROM Fecha_categoria WHERE id = '1')"
    mi_cursor.execute(sql04)
    sql05 = "CREATE TABLE IF NOT EXISTS categorias(Categoria TEXT, Monto NUMERIC)"
    mi_cursor.execute(sql05)
    sql06 = "INSERT INTO categorias (Categoria,Monto) SELECT 'A', 1414762.58 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'A')"
    mi_cursor.execute (sql06)
    sql07 = "INSERT INTO categorias (Categoria,Monto) SELECT 'B', 2103025.45 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'B')"
    mi_cursor.execute(sql07)
    sql08 = "INSERT INTO categorias (Categoria,Monto) SELECT 'C', 2944235.6 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'C')"
    mi_cursor.execute(sql08)
    sql09 ="INSERT INTO categorias (Categoria,Monto) SELECT 'D', 3656604.33 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'D')"
    mi_cursor.execute(sql09)
    sql10 = "INSERT INTO categorias (Categoria,Monto) SELECT 'E', 4305799.15 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'E')"
    mi_cursor.execute(sql10)
    sql11 ="INSERT INTO categorias (Categoria,Monto) SELECT 'F', 5382248.94 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'F')"
    mi_cursor.execute(sql11)
    sql12 = "INSERT INTO categorias (Categoria,Monto) SELECT 'G', 6458698.71 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'G')"
    mi_cursor.execute(sql12)
    sql13="INSERT INTO categorias (Categoria,Monto) SELECT 'H', 7996484.12 WHERE NOT EXISTS (SELECT 1 FROM categorias WHERE categoria = 'H')"
    mi_cursor.execute(sql13)
    con.commit()
    con.close()

def actualizar_fondo():
    
    con = conexion()
    cursor = con.cursor()
    sql1 = "SELECT * FROM Fondo where Id=1 ;"
    cursor.execute(sql1)
    
    rows= cursor.fetchall()
    for x in rows:
        fondo = x[1]  
    con.close()
    return fondo

def cambiar_fondo():
    color = askcolor(color="#00ff00")
    eleccion_color = color[1]
    
    con = conexion()
    cursor = con.cursor()
    actualizar = (eleccion_color,"1")
     
    sql="UPDATE Fondo SET Color = ? Where id=?;"
    cursor.execute(sql,actualizar)
    con.commit()
    con.close()
    
    vista.root.configure(bg=eleccion_color)
    vista.etiqueta_concepto.config(bg=eleccion_color)
    vista.etiqueta_fecha.config(bg=eleccion_color)
    vista.etiqueta_monto.config(bg=eleccion_color)
    vista.etiqueta_total.config(bg=eleccion_color)
    
    vista.etiqueta_total_facturas.config(bg=eleccion_color)
    actualizar_fondo()
    actualizar_categoria()
    
def sumar_facturas():
    actualizar_fondo()
    
    con = conexion()
    cursor_facturas = con.cursor()
    
    sql_total_facturas="SELECT count(id) FROM facturacion;"
    cursor_facturas.execute(sql_total_facturas)
        
    total_facturas=cursor_facturas.fetchone()
    concatenar = str(total_facturas[0])
    con.close
    return concatenar

def actualizar_categoria():
    actualizar_fondo()

    ##Categorias:
    con = conexion()
    cursor = con.cursor()
    sqlA = "SELECT * FROM Categorias where categoria='A';"
    cursor.execute(sqlA)
    rows = cursor.fetchall()
    for x in rows:
        categoriaA=x[1]
    
    global A
    A = categoriaA
    
    sqlB = "SELECT * FROM Categorias where categoria='B';"
    cursor.execute(sqlB)
    rows = cursor.fetchall()
    for x in rows:
        categoriaB=x[1]
    global B
    B = categoriaB
    
    sqlC = "SELECT * FROM Categorias where categoria='C';"
    cursor.execute(sqlC)
    rows = cursor.fetchall()
    for x in rows:
        categoriaC=x[1]
    global C
    C = categoriaC
    
    sqlD = "SELECT * FROM Categorias where categoria='D';"
    cursor.execute(sqlD)
    rows = cursor.fetchall()
    for x in rows:
        categoriaD=x[1]
    global D
    D = categoriaD
    
    sqlE = "SELECT * FROM Categorias where categoria='E';"
    cursor.execute(sqlE)
    rows = cursor.fetchall()
    for x in rows:
        categoriaE=x[1]
    global E
    E = categoriaE
    
    sqlF = "SELECT * FROM Categorias where categoria='F';"
    cursor.execute(sqlF)
    rows = cursor.fetchall()
    for x in rows:
        categoriaF=x[1]
    global F
    F = categoriaF
    
    sqlG = "SELECT * FROM Categorias where categoria='G';"
    cursor.execute(sqlG)
    rows = cursor.fetchall()
    for x in rows:
        categoriaG=x[1]
    global G
    G = categoriaG
    
    sqlH = "SELECT * FROM Categorias where categoria='H';"
    cursor.execute(sqlH)
    rows = cursor.fetchall()
    for x in rows:
        categoriaH=x[1]
    global H
    H = categoriaH
    
    con = conexion()
    cursor= con.cursor()
   
    sql0 = "SELECT Fecha FROM Fecha_categoria WHERE id = 1 "
    cursor.execute(sql0)
    
    global fecha_categoria
    fecha_categoria = cursor.fetchone()

    sql = "SELECT sum (Monto) FROM Facturacion WHERE Fecha >= ?;"
    
    cursor.execute(sql,fecha_categoria)   
    total_facturado = cursor.fetchone()


    if  total_facturado[0] == None:
        color = "Gold3"
        actualizar_categoria = "No hay datos para\n calcular la categoría."
        tamaño = 14
        return actualizar_categoria, color,tamaño
    
    elif total_facturado[0] <= A:
        color = "GREEN"
        actualizar_categoria= "            A"
        tamaño = 20   
        return actualizar_categoria, color, tamaño
        
    elif total_facturado[0] > A and total_facturado[0] <= B : 
        color = "GREEN"
        actualizar_categoria= "            B"
        tamaño = 20
        return actualizar_categoria, color,tamaño
        
    elif total_facturado[0] > B and total_facturado[0] <= C : 
        color = "GREEN"
        actualizar_categoria= "            C"
        tamaño = 20
        return actualizar_categoria, color, tamaño
        
    elif total_facturado[0] > C and total_facturado[0] <= D : 
        color = "GREEN"
        actualizar_categoria= "            D"
        tamaño = 20
        return actualizar_categoria, color, tamaño
        
    elif total_facturado[0] > D and total_facturado[0] <= E : 
        color = "GREEN"
        actualizar_categoria= "            E"
        tamaño = 20
        return actualizar_categoria, color, tamaño
    elif total_facturado[0] > E and total_facturado[0] <= F : 
        color = "GREEN"
        actualizar_categoria= "            F"
        tamaño = 20
        return actualizar_categoria, color, tamaño
        
    elif total_facturado[0] > F and total_facturado[0] <= G : 
        color = "GREEN"
        actualizar_categoria= "            G"
        tamaño = 20
        return actualizar_categoria, color, tamaño
        
    elif total_facturado[0] > G and total_facturado[0] <= H : 
        color = "RED4"
        actualizar_categoria= "OJO, H\n No te pases"
        tamaño = 14
        return actualizar_categoria, color, tamaño
        
    elif total_facturado[0]> H:
        color = "RED4"
        actualizar_categoria= "Te pasaste a\n responsable inscripto\n"
        tamaño = 14
        return actualizar_categoria, color, tamaño
    con.close()  

def actualizar_treeview(tabla):  
    con = conexion()
    mi_cursor = con.cursor()
    sql1 = "SELECT* FROM facturacion ORDER BY Fecha ASC"
    mi_cursor.execute(sql1)
    datos = mi_cursor.fetchall()
    
    if datos == []:
        exit
    else:    
        sql2 = "SELECT* FROM facturacion ORDER BY Fecha ASC"
        mi_cursor.execute(sql2)
        datos = mi_cursor.fetchall()
        fecha=datos[0][1]
        formatear_fecha = datetime.strptime(fecha,"%Y/%m/%d")
        formato_fecha="%d/%m/%Y"
        fecha_formateada = formatear_fecha.strftime(formato_fecha)
    
    for x in datos:
        formatear_fecha = datetime.strptime(x[1],"%Y/%m/%d")
        formato_fecha="%d/%m/%Y"
        fecha_formateada = formatear_fecha.strftime(formato_fecha) 
        vista.tabla.insert("",0,text=x[0],values=(fecha_formateada,x[2],("$"+str(x[3])))) #inserto la consulta en la tabla y convierto en string la 3er columna, para poder agregar el $
    con.close()
    
def cargar_datos(fecha,concepto,monto):
    con = conexion() 
    mi_cursor = con.cursor() 
    global patron
    patron = r"^\d+(\.\d+)?$" #Valida numeros enteros y decimales.
    cadena = vista.txt_monto.get()
    if re.match (patron,cadena):
        pass
    else:
        messagebox.showinfo("AVISO","Para cargar una facturación tenes que completar un monto, pueden ser solo números. Si es decimal, va separado de punto.")
        vista.txt_monto.focus()
        return
    valido_concepto = vista.concepto.get()
    valido_fecha = vista.txt_fecha.get()
    if valido_fecha == "":
        messagebox.showinfo ("AVISO","Tenes que ingresar la fecha de la factura.")
        vista.txt_fecha.focus()
        return
    
    if valido_concepto== "":
        messagebox.showinfo ("AVISO","Tenes que ingresar el concepto de la factura.")
        vista.combobox_concepto.focus()
        return
    else:
        ###Doy formato a la fecha para poder trabajar luego con sqlite YYYY
        traer_fecha = vista.fecha.get()
        formatear_fecha = datetime.strptime(traer_fecha, '%d/%m/%Y')
        formato_fecha="%Y/%m/%d"
        fecha_formateada = formatear_fecha.strftime(formato_fecha)
        ###
        
        datos = (fecha_formateada,concepto.get(),monto.get()) 
        sql1 = "INSERT INTO facturacion VALUES (NULL,?,?,?)" 
        mi_cursor.execute (sql1,datos) 
        con.commit() 
        monto.set("")
        concepto.set("")
        fecha.set("")

        records = vista.tabla.get_children()
        for R in records:
            vista.tabla.delete(R)     
        con.close()
        actualizar_treeview(vista.tabla)
        vista.concatenar=sumar_facturas()
        vista.etiqueta_total_facturas.config(bg=vista.fondo,text=vista.concatenar,font=("Arial",16,"bold"),foreground="RED")
        
        actualizar_categoria()
        vista.actualizar_categoria, vista.color,vista.tamaño = actualizar_categoria()
        vista.etiqueta_categoria_rdo_nulo.config(text=vista.actualizar_categoria,foreground=vista.color,font=("arial",vista.tamaño,"bold"))

def eliminar_datos():
    
    seleccion= vista.tabla.focus() 
    if seleccion ==(""):
        messagebox.showwarning("AVISO","Tenes que seleccionar el registro que queres borrar.")
        exit
    else:
        respuesta = messagebox.askquestion("Consulta","Estas seguro que vas a borrar el registro?")
        if respuesta =="yes":
            item=vista.tabla.item(seleccion) 
            borrar =(item.get("text"),) 
            con = conexion () 
            cursor=con.cursor() 
            sql = "DELETE FROM facturacion WHERE id = ?;" 
            cursor.execute(sql,borrar) 
            con.commit() 
            actualizacion = vista.tabla.get_children() 
            for R in actualizacion: 
                vista.tabla.delete(R) 
            actualizar_treeview(vista.tabla) 
            
            vista.concatenar=sumar_facturas()
            vista.etiqueta_total_facturas.config(bg=vista.fondo,text=vista.concatenar,font=("Arial",16,"bold"),foreground="RED")         
            
            vista.actualizar_categoria, vista.color, vista.tamaño = actualizar_categoria()
            vista.etiqueta_categoria_rdo_nulo.config(text=vista.actualizar_categoria,foreground=vista.color,font=("arial",vista.tamaño,"bold"))
            con.close()
        else:
            exit      

def informacion():
    messagebox.showinfo ("A cerca del programa.",\
    "Este programa fue desarrollado por Damián Colomb.\nSe realizó en python con la interfaz gráfica tkinter.")
    
def exportar():
    con = conexion()
    sql = "SELECT * FROM  Facturacion"
    exportar = pd.read_sql_query(sql,con)
    ruta = filedialog.asksaveasfilename(defaultextension='.xlsx')
    exportar.to_excel(ruta,index=False)
    con.close()
    messagebox.showinfo("AVISO","La exportación de datos fué realizada con éxito.")
    
def modificar_carga():
    seleccion= vista.tabla.focus() 
    if seleccion ==(""):
        messagebox.showwarning("AVISO","Tenes que seleccionar el registro que queres modificar.")
        exit
    else:
        vista.btn_actualizar_categoria.config(state="disabled")
        vista.btn_borrar.config(state="disabled")
        vista.btn_cargar.config(state="disabled")
        vista.btn_ver_graficos.config(state="disabled")
        vista.btn_modificar_carga.config(state="disabled")
        vista.btn_guardar_modificar_carga.place(x=500, y=190)
        
        seleccion = vista.tabla.focus()
        item=vista.tabla.item(seleccion)
        vista.txt_fecha.set_date(item['values'][0])
        vista.combobox_concepto.set(item['values'][1])
        
        con_simbolo= item['values'][2]
        sin_simbolo= con_simbolo.replace('$',"")
    
        vista.txt_monto.insert(0,sin_simbolo)
        vista.txt_monto.focus()
         
def guardar_modificacion():
    
    vista.btn_actualizar_categoria.config(state="active")
    vista.btn_borrar.config(state="active")
    vista.btn_cargar.config(state="active")
    vista.btn_ver_graficos.config(state="active")
    vista.btn_modificar_carga.config(state="active")
    vista.btn_guardar_modificar_carga.place_forget()
    
    seleccion = vista.tabla.focus()
    item=vista.tabla.item(seleccion) 
    
    borrar =(item.get("text"),) 
    con = conexion () 
    cursor=con.cursor() 
    sql = "DELETE FROM facturacion WHERE id = ?;" 
    cursor.execute(sql,borrar) 
    con.commit() 
    actualizacion = vista.tabla.get_children() 
    for R in actualizacion: 
        vista.tabla.delete(R) 
        actualizar_treeview(vista.tabla)
    cargar_datos(vista.fecha,vista.concepto,vista.monto)
    vista.concatenar=sumar_facturas()
    vista.etiqueta_total_facturas.config(bg=vista.fondo,text=vista.concatenar,font=("Arial",16,"bold"),foreground="RED")              
    
    vista.actualizar_categoria, vista.color, vista.tamaño = actualizar_categoria()
    vista.etiqueta_categoria_rdo_nulo.config(text=vista.actualizar_categoria,foreground=vista.color,font=("arial",vista.tamaño,"bold"))
    con.close()