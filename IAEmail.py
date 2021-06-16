import speech_recognition as sr
import yagmail

recognizer= sr.Recognizer()
with sr.Microphone() as source:
    print('Limpando som externo...')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Aguardando sua mensagem...")
    recordedaudio= recognizer.listen(source)
    print('Gravação realizada..!')
try:
    print('Digitando mensagem...')
    text= recognizer.recognize_google(recordedaudio,language='pt-BR')

    print('Sua mensagem:{}'.format(text))

except Exception as ex:
    print(ex)

#Automatizando emails:

reciever='email_do_destinário'
message=text
sender=yagmail.SMTP('email_do_remetente')
sender.send(to=reciever,subject='Este é um e-mail automatizado by python',contents=message)
