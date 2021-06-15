import speech_recognition as sr
import yagmail

recognizer = sr.Recognizer()
with sr.Microphone() as souce:
  print('Limpando o som externo...')
  recognizer.adjust_for_ambient_noise(source,duration=1)
  print("Aguardando sua mensagem...")
  recordedaudio = recognizer.listen(source)
  print('Gravação realizada!')
try:
  print('Digitando sua mensagem...')
  text = recognizer.recognize_google(recordeaudio, laguage ='pt-BR')
  
  print('Sua mensagem:{}'.format(text))
  
except Exception as ex:
  print(ex)
  
#Automatizando e-mail
reciever = 'donacareta@gmail.com'
message = text
sender = yagmail.SMTP('keziacamposcs@gmail.com')
sender.send(to=reciever, subject = 'Email automatizado por voz', contents = message)
