from flask import Flask, request,render_template
from rivescript import RiveScript
import os
from gtts import gTTS

app = Flask(__name__)

file = os.path.dirname(__file__)
brain = os.path.join(file,'brain')

bot = RiveScript()
bot.load_directory(brain)
bot.sort_replies()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/callChat')
def callchat():
    return render_template('chat.html')

@app.route('/callTalk')
def calltalk():
    return render_template('talk.html')

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        user = request.form['nm']
        msg1 = user
        while True:
            if msg1 == 'bye':
                return "<h1 style='color:blue;'>Gimmy: GoodBye </h1>"

            else:
                message = ('Gimmy: ' + bot.reply('localuser', msg1))

                return render_template('chat.html', message = message)


@app.route('/talk', methods=['POST', 'GET'])
def talk():
    if request.method == 'POST':
        user = request.form['record']
        while True:
            if user == 'bye':
                return "<h1 style='color:blue;'>Gimmy: GoodBye </h1>"

            else:
                result = ('Gimmy: ' + bot.reply('localuser', user))
                print(result)
                result = result.replace('Gimmy', '')
                speak(result)
                return render_template('talk.html')


def speak(audioString):
    tts = gTTS(text=audioString, lang='en')

    tts.save("static/audio/audio.mp3")
    os.remove("static/audio/audio.mp3")
    tts.save("static/audio/audio.mp3")

if __name__ == '__main__':
   app.run(debug=True)
