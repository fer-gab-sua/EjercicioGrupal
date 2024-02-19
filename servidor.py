import socket
from modelo import ModeloCategorias
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() #Esta es la IP del servidor
puerto = 5002 #Puerto en el cual estoy escuchado 
print(host)

serversocket.bind((host, puerto)) 
serversocket.listen(3)
while True:
    #Inicia la conexión 
    clientsocket,address = serversocket.accept()
    print(type(address))
    print(address)
    # address es una tupla de dos valores
    print(0, '---', address[0])    #Dirección IP
    print(1, '---', address[1])    #Número de conexión

    print("Recibo la conexión desde: " + str(address[0]))
    #Mensaje Enviado
    mensaje = b'Hola Bienvenido a nuestro servidor' + b'\r\n'
    clientsocket.send(mensaje)
    db = ModeloCategorias()
    mensaje = db.traer_categorias()
    clientsocket.send(mensaje)
    clientsocket.close()
