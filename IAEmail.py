import speech_recognition as sr
import yagmail
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty("rate", 178)
engine.say("Oi, eu sou sua Assistente, como posso te ajudar?")
engine.say("Já estou te escutando")

engine.runAndWait()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer= sr.Recognizer()
with sr.Microphone() as source:

    engine = pyttsx3.init()
    
    engine.setProperty("rate", 178)
    engine.say("Limpando som externo...")
    engine.runAndWait()
    print('Limpando som externo...')

    recognizer.adjust_for_ambient_noise(source,duration=1)
    engine.say("Aguardando sua mensagem...")
    print("Aguardando sua mensagem...")
    recordedaudio= recognizer.listen(source)
    engine.say("Gravação realizada..!")
    print('Gravação realizada..!')
try:
    print('Digitando mensagem...')
    text= recognizer.recognize_google(recordedaudio,language='pt-BR')

    print('Sua mensagem:{}'.format(text))

except Exception as ex:
    print(ex)

#Automatizando emails:

reciever='donacareta@gmail.com'
message=text
sender=yagmail.SMTP('keziacamposcs@gmail.com')
sender.send(to=reciever,subject='Este é um e-mail automatizado by python',contents=message)
