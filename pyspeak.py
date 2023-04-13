import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit


audio = sr.Recognizer() # Reconhece o audio
maquina = pyttsx3.init()

def abrir_youtube():
    with sr.Microphone() as source:
        print('O que você quer procurar no Youtube?')
        maquina.say('O que você quer procurar no Youtube?')
        maquina.runAndWait()
        audio = sr.Recognizer().record(source, duration=5)
        try:
            pesquisa = sr.Recognizer().recognize_google(audio, language='pt-BR')
            maquina.say('Ok! Procurando por ' + pesquisa)
            maquina.runAndWait()
            pywhatkit.playonyt(pesquisa)
        except:
            maquina.say('Desculpe, não entendi o que você falou.')
            maquina.runAndWait()


# Criando um bloco para retornar um erro
def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source) # para ouvir
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                maquina.runAndWait()

    except:
        print('O microfone não está funcionando...')
    
    return comando


def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'me responda' in comando:
        procurar = comando.replace('me responda', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 3)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif "abrir youtube" in comando.lower():
        abrir_youtube()


        
comando_voz_usuario()

while True:
        resposta = input("Deseja continuar? (s/n): ")
        if resposta.lower() == "n":
            break
        else:
            comando_voz_usuario()