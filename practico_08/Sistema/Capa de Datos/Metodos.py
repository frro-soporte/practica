from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Clases import Base, Centro, Sacerdote, Penitente, Turno


class Datos():
    def __init__(self):
        engine = create_engine('sqlite:///turnosConfesiones.db')
        # Base.metadata.drop_all(engine) #Elimina todo lo que pueda tener el motor
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine) # crea todas las tablas que todavia no existen

class DatosCentros(Datos):
    def __init__(self):
        super().__init__()        

    def alta(self, cen):        
        self.session.add(cen)
        self.session.commit()
        return cen

class DatosPenitentes(Datos):
    def __init__(self):
        super().__init__()

    def alta(self,pen):
        self.session.add(pen)
        self.session.commit()
        return pen

class DatosSacerdotes(Datos):
    def __init__(self):
        super().__init__()    

    def alta(self,sac):
        self.session.add(sac)
        self.session.commit()
        return sac


class DatosTurnos(Datos):
    def __init__(self):
        super().__init__()   

    def alta(self,tur):
        self.session.add(tur)
        self.session.commit()
        return tur
   
# class DatosSacerdotesCentros(Datos):
#     def __init__(self):
#         super().__init__()      


if __name__ == '__main__':

    # Populate Centros
    dc = DatosCentros()   
    cen = Centro(nombre="Antartida", direccion="Av Estrada 145", codPostal="2000", sexoAtencion = "M")
    dc.alta(cen)

    # Populate Sacerdotes
    ds = DatosSacerdotes()
    sac = Sacerdote(dni=12345, nombreApellido='Juan Prez', mail='jp@gmail.com', celular='34123456')
    ds.alta(sac)
  
    # Populate penitentes
    dp = DatosPenitentes()
    pen = Penitente(mail='HernyG@gmail.com', nombreApellido='Hernan Gomez' , celular='1234123',estado=True, sexo='M')
    dp.alta(pen)

    # Pululate turnos
    # esto no estaria funcionando correctamente
    dt = DatosTurnos()
    tur = Turno(dni=12345,idCentro=2, mail='HernyG@gmail.com', descripcionSacerdote='None',descricpcionPenitente='None') 
    dt.alta(tur)
   