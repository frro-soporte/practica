from sqlalchemy import create_engine, asc, and_
from sqlalchemy.orm import sessionmaker
from Clases import Base, Centro, Sacerdote, Penitente, Turno, Ciudad, Disponibilidad
from datetime import datetime, timedelta, time, date



class Datos():
    def __init__(self):
        engine = create_engine('mysql+pymysql://u448809972_gregorioSamsa:rosarioCentral119@185.201.11.149:3306/u448809972_turnosDB')
        #Base.metadata.reflect(engine=engine) #Prepara las clases en la metadata para un reinicio

        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine) # crea todas las tablas que todavia no existen
    
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
            centro = self.session.query(Centro).filter(Centro.nombre == nombre_centro).first()
            return centro
        except:
            print ("No se encontro el centro con nombre: ", nombre_centro)
            return None 

    def GetOne(self, idCentro):
        return  self.session.query(Centro).filter(Centro.idCentro == idCentro).first()

    def GetAll(self):
        centros = self.session.query(Centro).order_by(asc(Centro.nombre)).all()
        return centros

    def GetAllxSacerdote(self,idSacerdote):
        dd = DatosDisponibilidad()
        disponibilidades = dd.GetCentrosxSacerdote(idSacerdote)
        centros = []
        for d in disponibilidades:
            centro = self.GetOne(d.idCentro) 
            if centro not in centros:
                centros.append(centro)
        return centros

    def GetSacerdotesyHorarios(self,centro):
        ds = DatosSacerdotes()
        dd = DatosDisponibilidad()
        sacerdotes = ds.GetAllxCentro(centro.idCentro)
        horarios = []
        sacerdotesyDisponibilidad = []
        for s in sacerdotes:
            horarios=[]
            disponibilidades =  dd.GetAllxCentroySacerdote(centro.idCentro,s.id)
            for d in disponibilidades:
                horarios.append([d.diaNombre,d.horaInicioAtencion,d.horaFinAtencion])
            sacerdotesyDisponibilidad.append([s,horarios])
        return sacerdotesyDisponibilidad
    


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

    def GetOne(self, idSacerdote): 
        try:
            sacerdote = self.session.query(Sacerdote).filter(Sacerdote.id == idSacerdote).first()
            return sacerdote
        except:
            print ("No se encontro el sacerdote: ", idSacerdote)
            return None

    def GetAll(self):
        sacerdotes = self.session.query(Sacerdote).order_by(asc(Sacerdote.apellidoNombre)).all()      
        return sacerdotes
    
    def GetAllxCentro(self,idCentro):
        dd = DatosDisponibilidad()
        disponibilidades = dd.GetSacerdotesxidCentro(idCentro)
        sacerdotes = []
        for d in disponibilidades:
            sacerdote = self.GetOne(d.idSacerdote) 
            if sacerdote not in sacerdotes:
                sacerdotes.append(sacerdote)
        return sacerdotes

    def GetCentrosyHorarios(self,sacerdote):
        dc = DatosCentros()
        dd= DatosDisponibilidad()
        centros = dc.GetAllxSacerdote(sacerdote.id)
        horarios = []
        centrosyDisponibilidad = []
        for c in centros:
            horarios=[]
            disponibilidades =  dd.GetAllxCentroySacerdote(c.idCentro,sacerdote.id)
            for d in disponibilidades:
                horarios.append([d.diaNombre,d.horaInicioAtencion,d.horaFinAtencion])
            centrosyDisponibilidad.append([c,horarios])
        return centrosyDisponibilidad

    def GetOneMail(self, mail): 
        try:
            sacerdote = self.session.query(Sacerdote).filter(Sacerdote.mail == mail).first()
            return sacerdote
        except:
            print ("No se encontro el sacerdote con mail: ", mail)
            return None


class DatosTurnos(Datos):
    def __init__(self):
        super().__init__()   

    def InsertFiltrado(self,turno):
        if (self.GetOnexSacerdoteCentroyFechayHora(turno.idSacerdote, turno.idCentro, turno.fechayHoraTurno) == []):
            self.session.add(turno)
            self.session.commit()
            return True
        return False

    def GetOnexSacerdoteCentroyFechayHora(self, idSacerdote, idCentro, fechayHora):
        turnosAll = self.session.query(Turno).all()
        turnosFiltrados = []
        for t in turnosAll:
            if(t.idSacerdote == idSacerdote and t.idCentro == idCentro and t.fechayHoraTurno == fechayHora):
                turnosFiltrados.append(t)
        return turnosFiltrados


    def GetAllxSacerdoteyCentro(self, idSacerdote, idCentro):
        turnosAll = self.session.query(Turno).all()
        turnosFiltrados = []
        for t in turnosAll:
            if(t.idSacerdote == idSacerdote and t.idCentro == idCentro):
                turnosFiltrados.append(t)
        return turnosFiltrados

    def GetAllxSacerdoteCentroyDia(self, idSacerdote, idCentro, dia):
        turnosAll = self.session.query(Turno).all()
        turnosFiltrados = []
        for t in turnosAll:
            if(t.idSacerdote == idSacerdote and t.idCentro == idCentro and t.fechayHoraTurno.date() == dia.date()):
                turnosFiltrados.append(t)
        return turnosFiltrados

    def GetDiasDisponiblesxSacerdoteyCentro(self,idSacerdote,idCentro):
        dd = DatosDisponibilidad()
        disps = dd.GetAllxCentroySacerdote(idCentro, idSacerdote)
        turnos = self.GetAllxSacerdoteyCentro(idSacerdote, idCentro)
        diasDisponibles = []
        for incremento in range(0,7):
            cantTurnosDia = 0
            diaActual = datetime.today() + timedelta(incremento)
            for t in turnos:
                if (t.fechayHoraTurno.date() == diaActual):
                    cantTurnosDia = cantTurnosDia + 1
            cantTurnosDisponibles = 0
            for d in disps:
                if (d.diaAtencion ==  diaActual.weekday()):
                    minutos = (d.horaFinAtencion.hour - d.horaInicioAtencion.hour)*60 + d.horaFinAtencion.minute
                    if ((d.horaFinAtencion.hour - d.horaInicioAtencion.hour) != 0):
                        minutos = minutos + (60 - d.horaFinAtencion.minute)
                    cantTurnosDisponibles = cantTurnosDisponibles + minutos / 20
                    desc = d.diaNombre + " " + str(diaActual.day)
            if(cantTurnosDisponibles > cantTurnosDia):
                diasDisponibles.append((diaActual,desc))

        return  diasDisponibles

    def GetPeriodosDisponiblesxSacerdoteCentroyDia(self, idSacerdote, idCentro, diaFormat):
        turnos = self.GetAllxSacerdoteCentroyDia(idSacerdote, idCentro, diaFormat)
        dd = DatosDisponibilidad()
        disps =  dd.GetAllxSacerdoteCentroyDia(idSacerdote, idCentro, diaFormat)
        periodosDisponibles = []
        for d in disps:
            minutos = (d.horaFinAtencion.hour - d.horaInicioAtencion.hour)*60 + d.horaFinAtencion.minute
            cantPeriodos = int(minutos/ 20)
            for numPeriodo in range(0,cantPeriodos):
                bandera = True
                fechayHoraActual = datetime(diaFormat.year,diaFormat.month, diaFormat.day, d.horaInicioAtencion.hour, d.horaInicioAtencion.minute) + timedelta(minutes = (20 * numPeriodo))
                for t in turnos:
                    if (fechayHoraActual.time() == t.fechayHoraTurno.time()):
                        bandera = False
                if (bandera):
                    fechayHora = datetime.strftime(fechayHoraActual, '%d-%m-%Y %H:%M:%S')
                    desc =str(fechayHoraActual.time())[:5] + '-' + str((fechayHoraActual + timedelta(minutes=20)).time())[:5] 
                    periodosDisponibles.append((fechayHora, desc))
        return periodosDisponibles
    
    def GetOne(self, idTurno):
        try:
            turno = self.session.query(Turno).filter(Turno.idTurno == idTurno).first()
            return turno
        except:
            print ("No se encontro el turno: ", idTurno)
            return None


    # obtener datos de un turno
    def datosDeTurno(self, idTurno):
        turno = self.GetOne(idTurno)

        dc = DatosCentros()
        centro = dc.GetOne(turno.idCentro)

        ds = DatosSacerdotes()
        sacerdote = ds.GetOne(turno.idSacerdote)

        fechayHora = turno.fechayHoraTurno

        return centro.nombre, sacerdote.apellidoNombre, fechayHora


class DatosDisponibilidad(Datos):
    def __init__(self):
        super().__init__() 

    def GetCentrosxSacerdote(self, idSacerdote):
        return self.session.query(Disponibilidad).filter(Disponibilidad.idSacerdote == idSacerdote).all()
    
    def GetSacerdotesxidCentro(self, idCentro):
        return self.session.query(Disponibilidad).filter(Disponibilidad.idCentro == idCentro).all()

    def GetAllxCentroySacerdote(self, idCentro, idSacerdote):
        disponibilidadesAll = self.session.query(Disponibilidad).all()
        disponibilidadesFiltradas = []
        for d in disponibilidadesAll:
            if (d.idCentro == idCentro and d.idSacerdote == idSacerdote):
                disponibilidadesFiltradas.append(d)
        return disponibilidadesFiltradas

    def GetAllxSacerdoteCentroyDia(self,idSacerdote , idCentro, dia):
        disponibilidadesAll = self.session.query(Disponibilidad).all()
        disponibilidadesFiltradas = []
        for d in disponibilidadesAll:
            if (d.idCentro == idCentro and d.idSacerdote == idSacerdote and d.diaAtencion == dia.weekday()):
                disponibilidadesFiltradas.append(d)
        return disponibilidadesFiltradas
    
   



class DatosCiudades(Datos):
    def __init__(self):
         super().__init__() 

    def getAll(self):
        ciudades= self.session.query(Ciudad).all()
        return ciudades

    def getOne(self, id):
        return self.Session.query.filter_by(idCiudad=id).first()
         



if __name__ == '__main__':
    dt = DatosTurnos()
    turno = Turno(idTurno = 1, idSacerdote = 1, idCentro = 1, mail = "@")
    print(dt.InsertFiltrado(turno))
