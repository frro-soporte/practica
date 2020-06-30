'''import smtplib

message = 'Hola, esto es un mensaje desde Python'
subject = 'Prueba de correo'

message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('turnosconfesiones@gmail.com', 'sgdpv2020')

server.sendmail('turnosconfesiones@gmail.com','ariasramirox@gmail.com',message)

server.quit()'''

from ManejoMail import ManejoMail

mMail = ManejoMail()

mMail.destinatarios.append("ariasramirox@gmail.com")

mMail.enviarCorreo()

