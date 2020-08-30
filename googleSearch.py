import json
from urllib.request import urlopen
from flask import render_template


try:
    def mylocation():
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)
        location = data['loc']
        return location

except Exception as ex:
    print(ex)
    render_template('index.html')
