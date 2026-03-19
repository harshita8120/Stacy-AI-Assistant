import speech_recognition as sr
import webbrowser
import musicLibrary
import client
import news
import speech

recognizer = sr.Recognizer()


def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open pinterest" in c.lower():
        webbrowser.open("https://pinterest.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] #"Play song" command is split by space and the word at index 1 (song name) is assigned to the variable song
        songLink = musicLibrary.music[song]
        webbrowser.open(songLink)
    elif "news" in c.lower():
        news.newsHeadline()
        
    elif any(w in c.lower() for w in ["thanks", "thank you", "helpful", "useful", "thank"]) :
        speech.speak("My pleasure! Let me know if you need any other help.")

    else:
        #Further requests to be handled by Google Gemini
        output = client.geminiResponse(c)
        print(output)
        speech.speak(output)

     
if __name__ == "__main__" :
    speech.speak("Initialising Stacy ...")
    while True:
        #Listen for the wake word "Stacy" (gets activated whenever it hears "Stacy")
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1) #noise calibration
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
                #timeout is for how long user can speak, phrase_time_out is for how long user can take pause

            word = r.recognize_google(audio)
            print("Stacy heard: " + word)

            if any(w in word.lower() for w in ["stacy", "stasie", "stasy", "hey stacy"]):
                speech.speak("Hello, how can I help you?")

                #Listen for command

                with sr.Microphone() as source:
                    print("Stacy is active...")
                    
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


      
        except Exception as e:
            print("ERROR {0}".format(e))