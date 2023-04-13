import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser

# Cria uma instância do reconhecedor de fala
r = sr.Recognizer()

# Cria uma instância do engine para falar
engine = pyttsx3.init()

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        engine.say(summary)
        engine.runAndWait()
    except wikipedia.exceptions.DisambiguationError as e:
        engine.say("Houve um erro na pesquisa. Por favor, tente novamente.")
        engine.runAndWait()
    except wikipedia.exceptions.PageError as e:
        engine.say("Não foi possível encontrar o que você procurou. Por favor, tente novamente.")
        engine.runAndWait()

def search_youtube():
    engine.say("O que você gostaria de ver?")
    engine.runAndWait()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            search_term = r.recognize_google(audio, language='pt-BR')
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            engine.say(f"Aqui está o resultado para {search_term}.")
            engine.runAndWait()
        except sr.UnknownValueError:
            engine.say("Desculpe, não consegui entender o que você disse.")
            engine.runAndWait()
        except sr.RequestError as e:
            engine.say("Houve um erro na conexão. Por favor, tente novamente.")
            engine.runAndWait()

# Usa o microfone como fonte de entrada
with sr.Microphone() as source:

    # Ajusta o ruído de fundo
    r.adjust_for_ambient_noise(source)

    # Exibe mensagem para indicar que está ouvindo
    print("Diga algo!")

    # Grava o áudio do microfone
    audio = r.listen(source)

    try:
        # Usa o Google Speech Recognition para transcrever a fala
        text = r.recognize_google(audio, language='pt-BR')
        print("Você disse: {}".format(text))

        # Condicional para checar se o usuário pediu as horas
        if "que horas são" in text:
            now = datetime.datetime.now()
            hora_atual = now.strftime("Agora são %H horas e %M minutos.")
            engine.say(hora_atual)
            engine.runAndWait()

        # Condicional para checar se o usuário pediu para pesquisar na Wikipedia
        elif "pesquisar na wikipedia" in text:
            query = text.replace("pesquisar na wikipedia", "")
            search_wikipedia(query)

        # Condicional para checar se o usuário pediu para procurar no Youtube
        elif "procurar no youtube" in text:
            search_youtube()

    except sr.UnknownValueError:
        # Caso a fala não seja compreendida
        print("Não entendi o que você disse")
    except sr.RequestError as e:
        # Caso ocorra um erro de conexão
        print("Erro ao realizar a transcrição; {0}".format(e))
