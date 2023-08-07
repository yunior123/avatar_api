

import glob
from flask import request
from flask import Flask
from IPython.display import HTML
from base64 import b64encode

from generate import gen_video

app = Flask(__name__)

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
    gen_video(image_name, image_binary, audio_name, audio_binary, test=True)
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')

# pip freeze > requirements.txt
