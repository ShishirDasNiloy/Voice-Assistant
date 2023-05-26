import pyttsx3  # convert text to speect
import speech_recognition as sr  # voice recognising module
import datetime
import wikipedia
import webbrowser
import datetime
import pyjokes
import wolframalpha

# Shishir Das Niloy
# sapi5 - this is microsoft sprrech api
# using female voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print(voices)

# setting up the specific browser
# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
#     "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
# browser = webbrowser.get('chrome')

# default browser
browser = webbrowser


def speak(audio):
    engine.say(audio)  # this convert text to speech
    engine.runAndWait()  # make speech audible


def dotalk():  # starting speeches
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello. I am Nili your personal voice assistant. I am here to help you. What can I do for you?")


def listenMe():  # takes input from mic and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uk')
        print(f"User: {query}\n")

    except Exception as e:
        print("I can't understand. Please say that again?")
        return "None"
    return query


if __name__ == "__main__":
    dotalk()
    while True:  # infinity loop
        query = listenMe().lower()  # convert the speech in lower case for better result

        # using wikipia module finding information
        if "tell me about" in query:
            query = query.replace("tell me about", "")
            speak(f'Searching {query}')
            print(f"User: Searching {query}\n")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak(results)
        # opening website or programes
        elif 'open youtube' in query:
            speak("opening youtube")
            browser.open("https://www.youtube.com/")

        elif 'open wikipedia' in query:
            speak("opening wikipedia")
            browser.open("https://www.wikipedia.org/")

        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            browser.open("https://stackoverflow.com/")

        elif 'open github' in query:
            speak("opening giyhub")
            browser.open("https://github.com/")

        elif 'open w3school' in query:
            speak("opening w3school")
            browser.open("https://www.w3schools.com/python/default.asp")

        # quiting
        elif 'exit' in query:
            speak('Ok bye. Please ask for help if you need me. See you later!')
            quit()

        # searching somthing wikipedia on browser
        elif 'search wikipedia about' in query:
            query = query.replace("search wikipedia about ", "")
            print(f"User: {query}\n")
            speak('Searching Wikipedia...')
            browser.open(f"https://www.wikipedia.org/wiki/{query}")

        elif 'search youtube' in query:
            query = query.replace("search youtube", "")
            print(f"User: {query}\n")
            speak('Searching youtube...')
            browser.open(
                f"https://www.youtube.com/results?search_query={query}")

        # speak time
        elif 'the time' in query:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(str(now))
            speak(f"The time is {now}")

        # finding location on google map
        elif "find location of" in query:
            query = query.replace("find location of", "")
            location = query
            speak("Searcing"+location+"")
            browser.open("https://www.google.nl/maps/place/"+location+"")

        # writing notes replace the previous note
        elif "write a note" in query:
            speak("What should i write in the note?")
            note = listenMe()
            file = open('shishir.txt', 'w')
            speak("Should i include date and time")
            snfm = listenMe()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":- ")
                file.write(note)
            else:
                file.write(note)

         # show the last saveed note
        elif "open note" in query:
            speak("Showing Notes")
            file = open("shishir.txt", "r")
            print(file.read())
            speak(file.read(6))

        # pyjokes module telling jokes
        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        # basic chatting
        elif 'how are you' in query:
            speak("I am fine. How are you?")

        elif 'fine' in query or "good" in query:
            speak("It's great to know that your fine")

        elif 'your name' in query:
            speak("My name is Nili")

        elif 'nice name' in query:
            speak("Thaks, that's so nice to hear")

        elif "who are you" in query:
            speak("I am your voice assistant Nili")

        # wolframakpha module
        elif "what is" in query or "who is" in query:
            app_id = "3Q69KP-Y542R4GWQ4"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
