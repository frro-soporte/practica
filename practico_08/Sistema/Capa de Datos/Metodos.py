from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from Clases import Base, Centro, Sacerdote, Penitente, Turno, Ciudad, Disponibilidad



class Datos():
    def __init__(self):
        engine = create_engine('mysql+pymysql://u448809972_gregorioSamsa:rosarioCentral119@185.201.11.149:3306/u448809972_turnosDB')
        #Base.metadata.reflect(engine=engine) #Prepara las clases en la metadata para un reinicio

        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine) # crea todas las tablas que todavia no existen
        self.connection = engine.connect()
        #Base.metadata.drop_all(engine)  #Elimina todo lo que pueda tener el motor
        #Base.metadata.clear() #Borra las clases anteriores

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

    def GetAll(self):
        centros = self.session.query(Centro).order_by(asc(Centro.nombre)).all()
        return centros

    def GetAllxSacerdote(self,dniSacerdote):
        dd = DatosDisponibilidad()
        idcentros = dd.GetidCentrosxdni(dniSacerdote)
        centros = []
        for i in idcentros:
            centros.append(dd.GetOne(i,dniSacerdote))
        return centros
    


class DatosPenitentes(Datos):
    def __init__(self):
        super().__init__()

    def add(self,pen):
        self.session.add(pen)   
        self.session.commit()
        return pen
    
    def searchByEmail(self, penitente_mail): 
        try:
            penitente = self.session.query(Penitente).filter(Penitente.mail == penitente_mail).first()
            return penitente
        except:
            print ("No se encontro el penitente con mail: ", penitente_mail)
            return None            

    def all(self):
        centros = self.session.query(Sacerdote).all()
        return centros

class DatosSacerdotes(Datos):
    def __init__(self):
        super().__init__()    

    def Add(self,sac):
        self.session.add(sac)
        self.session.commit()
        return sac

    def search(self, dni_sacerdote): 
        try:
            sacerdote = self.session.query(Sacerdote).filter(Sacerdote.dni == dni_sacerdote).first()
            return sacerdote
        except:
            print ("No se encontro el sacerdote: ", dni_sacerdote)
            return None

    def GetAll(self):
        sacerdotes = self.session.query(Sacerdote).order_by(asc(Sacerdote.apellidoNombre)).all()      
        return sacerdotes

    def GetCentrosyHorarios(self,sacerdote):
        dc = DatosCentros()
        dd= DatosDisponibilidad()
        centros = dc.GetAllxSacerdote(sacerdote.dni)
        horarios = []
        for c in centros:
          disponibilidad =  dd.GetOne(c.idCentro,sacerdote.dni)
          horarios.append([disponibilidad.horaInicioAtencion,disponibilidad.horaFinAtencion])
        sacerdote.centrosyDisponibilidad = [centros,horarios]
        return sacerdote.centrosyDisponibilidad


class DatosTurnos(Datos):
    def __init__(self):
        super().__init__()   

    def add(self,tur):
        self.session.add(tur)
        self.session.commit()
        return tur
   
class DatosDisponibilidad(Datos):
    def __init__(self):
        super().__init__() 

    def GetidCentrosxdni(self, dniSacerdote):
        return self.session.query(Disponibilidad).filter_by(dni = dniSacerdote).all()
    
    def GetOne(self, idCentro, dniSacerdote):
        return self.session.query(Disponibilidad).filter_by(idCentro = idCentro, dni = dniSacerdote).one()

class DatosCiudades(Datos):
    def __init__(self):
         super().__init__() 

    def getAll(self):
        ciudades= self.session.query(Ciudad).all()
        return ciudades

    def getOne(self, id):
        return self.Session.query.filter_by(idCiudad=id).first()
         



if __name__ == '__main__':
    ds = DatosSacerdotes()
    sacerdotes = ds.GetAll()
    for s in sacerdotes:
        s.centrosyDisponibilidad = ds.GetCentrosyHorarios(s)
        for  i in s.centrosyDisponibilidad[0]:
            print("centro: ", i)
        for j in s.centrosyDisponibilidad[1]:
            print("hora inicio: ", j[1] , "hora fin: ", j[2])
