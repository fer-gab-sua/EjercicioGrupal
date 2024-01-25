import os
from datetime import datetime


def log(funcion):




    def wrapper(*args, **kwargs):
        resultado = funcion(*args,**kwargs)
        nombre_archivo = 'Log.txt'
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not os.path.isfile(nombre_archivo):
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(f"Archivo de Log creado el {fecha_hora_actual}.\n")

        with open(nombre_archivo, 'a') as archivo:
            # Obtiene la información que deseas agregar al registro
            informacion = "-"*100+"\n"
            informacion += f"Inicio de la funcion {funcion.__name__} - {fecha_hora_actual}\n"
            informacion += f"    Argumentos Ingresados: {args[1:]}\n"
            informacion += f"    Resultado de la funcion {funcion.__name__}: {resultado}\n"
            informacion += f"Finalizacion de la funcion {funcion.__name__}\n"
            informacion += "-"*100+"\n"


            archivo.write(informacion)




        return resultado
    return wrapper


