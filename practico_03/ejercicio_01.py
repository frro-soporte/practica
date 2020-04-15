# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="soporte"
)
mycursor = mydb.cursor()

def crear_tabla():
  try:
    mycursor.execute("CREATE TABLE `Persona` ( `IdPersona` INT NOT NULL AUTO_INCREMENT , `Nombre` CHAR(30) NOT NULL , `FechaNacimiento` DATE NOT NULL , `DNI` INT NOT NULL , `Altura` INT NOT NULL , PRIMARY KEY (`IdPersona`))")
  except mysql.connector.Error as error:
        print("Error al crear tabla Persona: {}".format(error))

crear_tabla()
