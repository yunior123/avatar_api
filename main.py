

import glob
from flask import request
from flask import Flask
from IPython.display import HTML
from base64 import b64encode

from generate import get_video

app = Flask(__name__)

# CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/get_talking_avatar', methods=['POST'])
def get_talking_avatar():
    form = request.form
    image_name = form.get('image_name')
    audio_name = form.get('audio_name')
    image_binary = request.files['image_binary'].read()
    audio_binary = request.files['audio_binary'].read()
    video_binary = get_video(image_name, image_binary, audio_name, audio_binary, test=True)
    return video_binary

if __name__ == '__main__':

    app.run(debug=True, port=5000, host='0.0.0.0')



# host = '
    # test = True
    # if test:
    #     image_name = 'happy'
    #     # get image binary from images folder
    #     image_path = 'images/{}.png'.format(image_name)
    #     with open(image_path, 'rb') as f:
    #         image_binary = f.read()
    #     audio_name = 'fayu'
    #     # get audio binary from audios folder
    #     audio_path = 'audios/{}.wav'.format(audio_name)
    #     with open(audio_path, 'rb') as f:
    #         audio_binary = f.read()

    #     video_binary = get_video(image_name, image_binary, audio_name, audio_binary, test=True)
    #     # show video
    #     video_base64 = b64encode(video_binary).decode('ascii')
    #     video_tag = '<video controls alt="test" src="data:video/mp4;base64,{0}">'.format(video_base64)
    #     return video_tag