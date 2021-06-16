import speech_recognition as sr
import yagmail
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty("rate", 178)
engine.say("Oi, eu sou sua Assistente de E-mail, como posso te ajudar?")
engine.say("Já estou te escutando")
engine.runAndWait()

recognizer= sr.Recognizer()
with sr.Microphone() as source:

    engine.setProperty("rate", 178)
    engine.say("Limpando som externo...")
    engine.runAndWait()
    print('Limpando som externo...')
    recognizer.adjust_for_ambient_noise(source,duration=1)


    engine.setProperty("rate", 178)
    engine.say("Aguardando sua mensagem...")
    engine.runAndWait()
    print("Aguardando sua mensagem...")
    recordedaudio= recognizer.listen(source)

    engine.setProperty("rate", 178)
    engine.say("Gravação realizada..!")
    engine.runAndWait()
    print('Gravação realizada..!')
try:
    print('Digitando mensagem...')
    text= recognizer.recognize_google(recordedaudio,language='pt-BR')

    print('Sua mensagem:{}'.format(text))

except Exception as ex:
    print(ex)

#Automatizando emails:
reciever='email_do_destinario'
message=text
sender=yagmail.SMTP('email_do_remetente')
sender.send(to=reciever,subject='Este é um e-mail automatizado by python',contents=message)
