import smtplib
from Mensaje import Mensaje
import json


class ManejoMail(object):

	def __init__(self):

		self.destinatarios = []
		self.parametros = json.load(open('practico_08/config.json', "r"))


	def enviarCorreo(self):		

		message = "Reporte de Periodo"
		subject = 'Prueba de correo'

		message = 'Subject: {}\n\n{}'.format(subject, message)

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login('turnosconfesiones@gmail.com', 'sgdpv2020')	

		for destino in self.destinatarios:
			print ("Enviando correo a ",destino)		
			server.sendmail('turnosconfesiones@gmail.com', destino, message)	

		server.quit() 