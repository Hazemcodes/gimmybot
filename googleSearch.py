import webbrowser
import json
from urllib.request import urlopen
from flask import render_template


try:
    def search(word):
        url = "https://www.google.com.tr/search?q={}".format(word)
        return webbrowser.get().open_new_tab(url)

    def location(place):
        url = "https://www.google.nl/maps/place/" + place + "/&amp;"
        return webbrowser.get().open_new_tab(url)

    def myip():
        url = "http://ipinfo.io/json"
        return webbrowser.get().open_new_tab(url)

    def mylocation():
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)
        location = data['loc']
        print(location)
        url = "https://www.google.nl/maps/place/" + location + "/&amp;"
        return webbrowser.get().open_new_tab(url)

except Exception as ex:
    print(ex)
    render_template('index.html')
