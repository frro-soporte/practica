import smtplib
# python3 -m smtpd -c DebuggingServer -n localhost:1025

smtp = smtplib.SMTP('localhost',1025)
body = 'Reporte de Periodo'
subject = 'Prueba de correo'
message = f'Subject: {subject}\n\n{body}'
smtp.sendmail('ariasramirox@gmail.com','ariasramirox@gmail.com',message)
