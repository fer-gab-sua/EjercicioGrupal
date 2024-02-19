import socket
import pickle

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'DESKTOP-PP1EQCP'
puerto = 5002

# Conectar al servidor
clientsocket.connect((host, puerto))

# Recibir los datos del servidor
serialized_data = clientsocket.recv(4096)
datos_recibidos = pickle.loads(serialized_data)

# Imprimir los datos recibidos
print("Datos recibidos del servidor:")
print(datos_recibidos)


# Cerrar la conexión con el servidor
clientsocket.close()