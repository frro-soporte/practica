import pyaudio
import wave
import os
import vamp
import librosa
import numpy as np
import matplotlib.pyplot as plt
import math as m
from librosa import display as d
from melosynth import melosynth
from Datos import DatosSongs


class AbrirNegocio(object):

    def __init__(self):
        self.datos = DatosSongs()

    def GeneraAudioMelodia(self,nombre):
        try:
            path = ".\\CapaDatos\\Songs\\{0}.wav".format(nombre)

            audio, sr = librosa.load(path, sr=44100, mono = True)

            params = {"minfqr": 25.0, "maxfqr": 2000.0, "voicing": 0.2, "minpeaksalience": 0.0}
            data = vamp.collect(audio, sr, "mtg-melodia:melodia", parameters = params)
            hop, melody = data['vector']
            timestamps = 8 * 128/44100.0 + np.arange(len(melody)) * (128/44100.0)

            nombreMel = nombre + ".txt"
            archivo = open(nombreMel, "w")
            for i in range(len(timestamps)):
                time = str(timestamps[i])
                if not m.isnan(melody[i]):
                    archivo.write(time)
                    archivo.write('\t')
                    archivo.write(str(melody[i]))
                    archivo.write('\n')
                else:
                    archivo.write(str(timestamps[i]))
                    archivo.write('\t')
                    archivo.write(str(-220))
                    archivo.write('\n')
            archivo.close()
            filename = '.\\CapaDatos\\Songs\\{0}_Mel.wav'.format(nombre)
            melosynth(nombreMel, outputfile=filename ,fs= 44100, nHarmonics= 1, square= False, useneg=False)
            os.remove(".\\{0}.txt".format(nombre))
        except:
            raise Exception("Error al generar el archivo de audio de la melodía")


    def GeneraChromagrama(self, nombre):
        try:
            path = '.\\CapaDatos\\Songs\\{0}_Mel.wav'.format(nombre)
            audio, sr = librosa.load(path , sr = 44100 , mono = True)

            chroma = librosa.feature.chroma_cqt(y = audio, sr = sr)

            plt.figure(figsize=(10, 4))
            d.specshow(chroma, y_axis='chroma', x_axis='time')
            plt.colorbar()
            plt.title('Chromagram')
            plt.tight_layout()
            filename: str ='.\\CapaDatos\\Graphics\\{0}_Chroma'.format(nombre)
            plt.savefig(filename)
        except:
            raise Exception("Error al generar el Chromagrama")


    def GuardaAudio(self, nombre, autor, desc):
        try:
            path = ".\\CapaDatos\\Songs\\{0}.wav".format(nombre)
            self.datos.Guarda_Audio(nombre, autor, desc, path)
            os.rename(".\\TKinter.wav", ".\\CapaDatos\\Songs\\{0}.wav".format(nombre))
        except Exception as Ex:
            raise Ex


    def Lista_Audios(self):
        """Pide audios de la BD y los devuelve a la Interfaz"""
        try:
            lista = self.datos.Get_All_Audios()
            return lista
        except Exception as Ex:
            raise Ex

    def Eliminar(self, nombre):
        try:
            self.datos.Elimina_Audio(nombre)
            os.remove(".\\CapaDatos\\Songs\\{0}.wav".format(nombre))
            if os.path.exists(".\\CapaDatos\\Songs\\{0}_Mel.wav".format(nombre)):
                os.remove(".\\CapaDatos\\Songs\\{0}_Mel.wav".format(nombre))
                os.remove(".\\CapaDatos\\Graphics\\{0}_Chroma.png".format(nombre))
        except Exception as Ex:
            raise Ex

    def Modifica(self, nombre, autor, desc):
        try:
            self.datos.Modifica_Audio(nombre,autor,desc)
        except Exception as x:
            raise x

    def Grabar(self, seconds):
        p = pyaudio.PyAudio()  # Crea una interfaz a PortAudio

        chunk = 1024  # Graba en 24 trozos de 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits por sample
        channels = 1
        fs = 44100  # Graba 44100 samples por segundo
        frames = []

        stream = p.open(format=sample_format,
                             channels=channels,
                             rate=fs,
                             frames_per_buffer=chunk,
                             input=True)
        stream.start_stream()

        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        filename = "TKinter.wav"

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()


    def Reproducir_Analisis_Mel(self, nombre):
        try:
            path = ".\\CapaDatos\\Songs\\{0}_Mel.wav".format(nombre)
            p = pyaudio.PyAudio()
            wf = wave.open(path, 'rb')

            stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(),
                        rate = wf.getframerate(),
                        output = True)

            data = wf.readframes(1024)

            while str(data) != "b''":
                stream.write(data)
                data = wf.readframes(1024)

            stream.close()
            p.terminate()
        except Exception as Ex:
            raise Ex

    def Abrir_Reproducir(self, nombre):
        """Pide Item de la BD y busca el path y lo reproduce"""
        try:
            if nombre=="TKinter.wav":
                path = ".\\TKinter.wav"
            else:
                audio = self.datos.Get_One_Audio(nombre)
                path = audio[3]

            p = pyaudio.PyAudio()
            wf = wave.open(path, 'rb')

            stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(),
                        rate = wf.getframerate(),
                        output = True)

            data = wf.readframes(1024)

            while str(data) != "b''":
                stream.write(data)
                data = wf.readframes(1024)

            stream.close()
            p.terminate()
        except Exception as Ex:
            raise Ex

