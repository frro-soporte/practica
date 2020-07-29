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

    def buscar_id(self, centro_id): 
        try:
            centro = self.session.query(Centro).filter(Centro.idCentro == centro_id).first()
            return centro
        except:
            print ("No se encontro el centro con id: ", centro_id)
            return None

    def buscar_nombre(self, nombre_centro): 
        try:
            centro = self.session.query(Centro).filter(Centro.idCentro == nombre_centro).first()
            return centro
        except:
            print ("No se encontro el centro con nombre: ", nombre_centro)
            return None            

    def todos(self):
        centros = self.session.query(Sacerdote).all()
        return centros

class DatosPenitentes(Datos):
    def __init__(self):
        super().__init__()

    def alta(self,pen):
        self.session.add(pen)
        self.session.commit()
        return pen
    
    def buscar_mail(self, penitente_mail): 
        try:
            penitente = self.session.query(Penitente).filter(Penitente.mail == penitente_mail).first()
            return penitente
        except:
            print ("No se encontro el penitente con mail: ", penitente_mail)
            return None            

    def todos(self):
        centros = self.session.query(Sacerdote).all()
        return centros

class DatosSacerdotes(Datos):
    def __init__(self):
        super().__init__()    

    def alta(self,sac):
        self.session.add(sac)
        self.session.commit()
        return sac

    def buscar(self, dni_sacerdote): 
        try:
            sacerdote = self.session.query(Sacerdote).filter(Sacerdote.dni == dni_sacerdote).first()
            return sacerdote
        except:
            print ("No se encontro el sacerdote: ", dni_sacerdote)
            return None

    def todos(self):
        sacerdotes = self.session.query(Sacerdote).all()
        return sacerdotes


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
    # Prueba de busqueda
    # s = ds.buscar(12345)
    # print(s.nombreApellido)

    # Populate Penitentes
    dp = DatosPenitentes()
    pen = Penitente(mail='HernyG@gmail.com', nombreApellido='Hernan Gomez' , celular='1234123',estado=True, sexo='M')
    dp.alta(pen)    

    # Pululate Turnos
    # esto no estaria funcionando correctamente, no deberia poder guardar FK que no estan creadas, 
    # si lo haces manual da el fallo esperado, pero no con esta linea de codigo
    dt = DatosTurnos()
    tur = Turno(dni=12345,idCentro=2, mail='HernyG@gmail.com', descripcionSacerdote='None',descricpcionPenitente='None') 
    dt.alta(tur)
   