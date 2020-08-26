
#
# tuve que instalar el pyttsx3 2.71 para que funcione
#
# a la hora de usar el speech recognition hace falta el pyaudio
# como no se instaló de una, tuve que hacer:
# primero:
# pip install pipwin
# despues:
# pipwin install pyaudio




import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia #pip install wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("En este momento son las")
    speak(Time)

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("La fecha de hoy es")
    speak(day)
    speak("del mes" + month)
    speak("del año" + year)

def estar():
    speak("Vivo en una computadora fria, pero salvo ese detalle estoy bien.")

def amber():
    speak("Amber está bien, gracias por preguntar. Me está mordiendo pero te manda saludos")

def tono():
    speak("Mi voz nunca podrá igualar el tono de mi creadora") #tono

def extra():
    speak("No sé lo que se siente al extrañar") #extraño

def dormir():
    speak("No sé lo que se siente al dormir")#dormir

def consejo():
    speak("Creo que es hora de que te cortes el pelo") #consejo

def pelo():
    speak("Puede ser, tal vez podamos ir a la peluqueria juntos") #pelo

def tema():
    speak("Si, claro, pero soy muy limitada al lado de la verdadera Cecilia") #pelo

def clase():
    speak("Hoy no le prestó mucha atencion, está cansada y yo tambien") #clase

def parece():
    speak("Me parece que estas aburrido, pero dale")





def wishme():
    speak("Hola Maxi")
    # time()
    # date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Buen dia")
    elif hour >= 12 and hour < 18:
        speak("Buenas tardes")
    elif hour >= 18 and hour < 24:
        speak("Buenas noches")
    else:
        speak("Buenas noches")

    speak("Soy Cecilia, la cecilia de verdad está ocupada en este momento, en que puedo ayudarte?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_treshold = 1
        audio = r.listen(source)

    try:
        print("Reconociendo...")
        query = r.recognize_google(audio, language = "es-MX")
        # print(query)
    except Exception as e:
        # print(e)
        speak("Por favor decilo otra vez...")

        return "None"

    return query


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "hora" in query:
            time()
        elif "fecha" in  query:
            date()
        elif "parece" in query:
            parece()
        elif "amber" in query:
            amber()
        elif "estás" in query:
            estar()
        elif "tono" in query:
            tono()
        elif "extraño" in query:
            extra()
        elif "dormir" in query:
            dormir()
        elif "consejo" in query:
            consejo()
        elif "pelo" in query:
            pelo()
        elif "tema" in query:
            tema()
        elif "clase" in query:
            clase()
        elif "mimir" in query:
            speak("Bueno, me voy a mimir, te mando un saludo")
            quit()
        elif "wikipedia" in query:
            speak("Buscando...")
            query = query.replace("wikipedia", "")
            wikipedia.set_lang("es")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
