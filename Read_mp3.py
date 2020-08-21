from playsound import playsound
import os
import multiprocessing
from flask import render_template

try:
    list3 = []
    song = ""

    def play(music):
        try:
            song = music
            playsound("mp3/" + music + '.mp3', True)

        except Exception:
            print("No File with this name")

    def stopMusic():
        p = multiprocessing.Process(target=playsound, args=("mp3/"+song+".mp3"))
        p.terminate()

    def playlist():
        music = ""
        with os.scandir('mp3/') as entries:
            for entry in entries:
                list3.append(entry.name)
            for i in range(len(list3)):
                music = music + " " + list3[i] + "\n"
            return music
except Exception as e:
    print(e)
    render_template('index.html')
