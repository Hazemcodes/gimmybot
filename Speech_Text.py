import speech_recognition as sr
from time import ctime
import os
from gtts import gTTS
import webbrowser

def speak(audioString):
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")

# Record Audio
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        data = ''
    try:
        data = r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)
    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        # location = data[2]
        location = "london"
        speak("Hold on , I will show you where " + location + " is.")
        url = "https://www.google.nl/maps/place/" + location + "/&amp;"
        return webbrowser.open_new_tab(url)

#
# # initialization
# time.sleep(2)
# speak("Hi, what can I do for you?")
# while 1:
#
#     data = recordAudio()
#     jarvis(data)
if __name__ == '__main__':
    jarvis("where is")