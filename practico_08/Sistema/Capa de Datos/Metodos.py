from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Clases import Base, Sacerdote, Penitente, Centro

class Datos():
    def __init__(self):
        engine = create_engine('sqlite:///turnosConfesiones.db')
        # Base.metadata.drop_all(engine) #Elimina todo lo que pueda tener el motor
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine) #crea todas las tablas que todavia no existen
        

class DatosPenitentes(Datos):
    pass
class DatosSacerdotes(Datos):
    pass
class DatosCursos(Datos):
    pass
class DatosTurnos(Datos):
    pass
class DatosSacerdotesCentros(Datos):
    pass

if __name__ == '__main__':
    datos = Datos()    
    
    cen = Centro(nombre="Antartida", direccion="Av Estrada 145", codPostal="2000", sexoAtencion = "M")
    datos.session.add(cen)

   

    # pen = Penitente("lucas@gmail.com", "Lucas Gervasoni", "341234567", True, "M" )
    # datos.session.add(pen)

    # horario1=Crono(dia='lunes',hora_inicio="7:00 am", hora_fin='8:00')
    # session.add(horario1)
    # horario1.curso_hora=Course(nombrec='Quimica')
    # horario1.curso_profe=Maestro(nombrep='Vicente',apellidop='  Huidobro')


    # print(horario1.curso_profe)
    # print(session.query(Course).filter(Maestro.profe_curso.any()).all())
    # print(session.query(Crono).filter(Maestro.profe_curso.any()).all())

    # session.commit()