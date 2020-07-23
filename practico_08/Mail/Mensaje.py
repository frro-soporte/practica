class Mensaje():
    
    def __init__(self):
        self.subject = ""
        self.head = "<html><h2><b>Mensaje de prueba</b></h2>"
        self.body = "<p>Esto es un mensaje de prueba enviado con python</p>"
        self.tail = "<p>Hola soy el fin del mensaje  </p></html>"

    def getMensaje(self):
        return self.head + self.body + self.tail

    def agregarContenido(self, data):
        self.body = self.body + data