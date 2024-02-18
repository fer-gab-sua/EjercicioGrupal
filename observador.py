
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading



class ObservadorTarea():
    def update(self,datos):
        cuerpo = f"Se ingreso un nuevo Registro: \n Fecha: {datos[0]} \n Concepto: {datos[1]} \n Importe: {datos[2]}"
        t = threading.Thread(target=self.enviar_correo, name="enviar_correo",args=(cuerpo,))
        t.start()


    def enviar_correo(self,cuerpo):
        servidor_smtp = 'smtp.gmail.com'
        puerto_smtp = 587

        remitente = 'sistem.monotributo@gmail.com'
        contraseña = 'kzac mwtt snkm fptd'

        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = 'fer.gab.sua@gmail.com'
        mensaje['Subject'] = 'Nuevo ingreso'

        mensaje.attach(MIMEText(cuerpo, 'plain'))

        # Inicio conexion
        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()

            #me logeo
            servidor.login(remitente, contraseña)

            #envio correo
            servidor.send_message(mensaje)

        print("Correo electrónico enviado exitosamente.")

