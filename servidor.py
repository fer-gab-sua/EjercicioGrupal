import socket
import pickle
from modelo import ModeloCategorias

#importo del modelo las categorias, esto tendria que ser en una base de datos que este solamente en el servidor con los datos actualizados, ahora funcionaria igual ya que estoy utilizando la misma base de datos.
base = ModeloCategorias()
datos = base.traer_categorias()

# Crear un socket del servidor
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
puerto = 5002
serversocket.bind((host, puerto))

# Escuchar conexiones entrantes
serversocket.listen(1)

print("Esperando conexión en el puerto:", puerto)

while True:
    # Aceptar conexiones
    clientsocket, addr = serversocket.accept()
    print("Conexión entrante desde:", addr)
    # Serializar los datos y enviarlos al cliente
    serialized_data = pickle.dumps(datos)
    clientsocket.send(serialized_data)
    # Cerrar la conexión con el cliente
    clientsocket.close()
