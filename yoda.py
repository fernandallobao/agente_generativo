import pyttsx3
import speech_recognition as sr
# import pyaudio vai internamente com essas outras bibliotecas

ouvido = sr.Recognizer()

voz = pyttsx3.init()

def falar(texto):
    print(f'Assistente: {texto}')
    voz.say(texto)
    voz.runAndWait()

def ouvir():
    with sr.Microphone() as mic:
        print('Ouvindo...')
        audio = ouvido.listen(mic)
        try:
            comando = ouvido.recognize_google(audio, lenguage = "pt-BR")
            print(f"você disse:{comando}")
            return comando.lower()
        except sr.UnknownValueError:
            falar('Desculpe não entendi!')
            return ''
        except sr.RequestError:
            falar('Não consegui abrir o sistema de audio!')
            return ''
        

# falar('Ola me chamo Lulu Cabelo Azul')
ouvir()
