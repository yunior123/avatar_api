

import glob
from flask import request
from flask import Flask
from IPython.display import HTML
from base64 import b64encode
from threading import Thread
import time

from generate import gen_video

app = Flask(__name__)


class Compute(Thread):
    def __init__(self, image_name, image_binary, audio_name, audio_binary):
        Thread.__init__(self)
        self.image_name = image_name
        self.image_binary = image_binary
        self.audio_name = audio_name
        self.audio_binary = audio_binary

    def run(self):
        print("start")
        time.sleep(5)
        try:
            gen_video(self.image_name, self.image_binary, self.audio_name, self.audio_binary)
        except Exception as e:
            print(e)
        print("done")

# CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/gen_talking_avatar', methods=['POST'])
def gen_talking_avatar():
    form = request.form
    image_name = form.get('image_name')
    audio_name = form.get('audio_name')
    image_binary = request.files['image_binary'].read()
    audio_binary = request.files['audio_binary'].read()
    thread_a = Compute(image_name, image_binary, audio_name, audio_binary)
    thread_a.start()
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

# pip freeze > requirements.txt
