# create simple flsk app with a get method to return the video, the method will receive 4 parameters in body
# 1- image name
# 2- image binary
# 3- audio name
# 4- audio binary


import glob
from flask import request
from flask import Flask
from IPython.display import HTML
from base64 import b64encode

from generate import get_video

app = Flask(__name__)

@app.route('/get_talking_avatar', methods=['GET'])
def get_talking_avatar():
    test = True
    if test:
        image_name = 'happy'
        # get image binary from images folder
        image_path = 'images/{}.png'.format(image_name)
        with open(image_path, 'rb') as f:
            image_binary = f.read()
        audio_name = 'fayu'
        # get audio binary from audios folder
        audio_path = 'audios/{}.wav'.format(audio_name)
        with open(audio_path, 'rb') as f:
            audio_binary = f.read()

        video_binary = get_video(image_name, image_binary, audio_name, audio_binary, test=True)
        # show video
        video_base64 = b64encode(video_binary).decode('ascii')
        video_tag = '<video controls alt="test" src="data:video/mp4;base64,{0}">'.format(video_base64)
        return video_tag
    
    image_name = request.args.get('image_name')
    image_binary = request.args.get('image_binary')
    audio_name = request.args.get('audio_name')
    audio_binary = request.args.get('audio_binary')
    video_binary = get_video(image_name, image_binary, audio_name, audio_binary, test=True)
    return video_binary

if __name__ == '__main__':
    # run and launch in localhost:5000
    app.run(host="127.0.0.1", port=8080, debug=True)
