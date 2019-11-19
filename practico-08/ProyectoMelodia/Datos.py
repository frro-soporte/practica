from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()


class Songs(Base):
    __tablename__ = 'Songs'

    nombre = Column(String(250), primary_key=True, nullable=False)
    autor = Column(String(50), nullable=True)
    descripcion = Column(String(250), nullable=True)
    pathAudioOriginal = Column(String(300), nullable=False)
    pathImgChroma = Column(String(300), nullable=True)
    pathAudioMelodia = Column(String(300), nullable=True)


class DatosSongs(object):

    def __init__(self):
        engine = create_engine('sqlite:///songDataBase.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        self.session = DBSession()
        Base.metadata.create_all(engine)

    def Guarda_Audio(self, nombre, autor, descripcion, path):
        """Guarda audio original en la base de datos"""
        song = Songs()
        try:
            songs = self.Get_All_Audios()
            for s in songs:
                if nombre == s[0]:
                    raise Exception("El nombre del audio está duplicado. Por favor seleccione uno nuevo.")
        except:
            pass
        song.nombre = nombre
        song.autor = autor
        song.descripcion = descripcion
        song.pathAudioOriginal = path
        try:
            self.session.add(song)
            self.session.commit()
        except:
            raise Exception("Error al guardar el audio")

    def Guarda_Analisis(self,path, chroma, nombre):
        """Guarda análisis de audio en la base de datos"""

        song = self.Get_One_Audio(nombre)
        if song != None:
            song.pathAudioMelodia = path
            song.pathImgChroma = chroma
            try:
                self.session.commit()
            except:
                raise Exception("Error al guardar los archivos de análisis")
        else:
            raise Exception("El nombre del archivo no se encuentra")

    def Get_All_Audios(self):
        """Retorna todos los audios de la base de datos"""
        try:
            songs = self.session.query(Songs).all()
        except:
            raise Exception("Error al recuperar la lista de usuarios.")
        if len(songs) == 0:
            raise Exception("No hay canciones cargadas")
        else:
            lista = []
            for s in songs:
                lista.append((s.nombre, s.descripcion, s.autor))
            return lista


    def Get_One_Audio(self, nombre):
        """Retorna un audio en particular de la base de datos"""
        try:
            audio = self.session.query(Songs).filter(Songs.nombre == nombre).first()
            lisaudio = (audio.nombre, audio.autor, audio.descripcion, audio.pathAudioOriginal, audio.pathAudioMelodia,
                        audio.pathImgChroma)
            return lisaudio
        except:
            raise Exception("Error al recuperar el usuario.")

    def Modifica_Audio(self,nombre, autor, descripcion):
        """Modifica el nombre o la descripcion de un audio"""
        song = self.session.query(Songs).filter(Songs.nombre == nombre).first()
        if song != None:
            song.autor = autor
            song.descripcion = descripcion
            try:
                self.session.commit()
            except:
                raise Exception("Error al modificar el audio")
        else:
            raise Exception("El nombre del archivo no se encuentra")

    def Elimina_Audio(self, nombre):
        """Elimina un audio y su analisis"""
        try:
            audio = self.session.query(Songs).filter(Songs.nombre == nombre).first()
            self.session.delete(audio)
            self.session.commit()
        except Exception as x:
            raise x

    def Get_One_Analisis(self,nombre):
        """Retorna el analisis de un audio"""
        return self.session.query(Songs).filter(Songs.nombre == nombre).first()



