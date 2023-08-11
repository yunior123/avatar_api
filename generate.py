import ipywidgets as widgets
import glob
import matplotlib.pyplot as plt
from IPython.display import display
import torch
from argparse import Namespace
import ssl
import asyncio
import inference as inf
ssl._create_default_https_context = ssl._create_unverified_context

from IPython.display import HTML
from base64 import b64encode
import os, sys


def get_parser(img_path, audio_path):
    try:
        config = Namespace(
            driven_audio=audio_path,
            source_image=img_path,
            ref_eyeblink=None,
            ref_pose=None,
            checkpoint_dir='./checkpoints',
            result_dir='./results',
            pose_style=0,
            batch_size=2,
            size=256,
            expression_scale=1.,
            input_yaw=None,
            input_pitch=None,
            input_roll=None,
            enhancer="gfpgan",
            background="white",
            background_enhancer=None,
            cpu=False,
            face3dvis=False,
            still=False,
            preprocess='full',
            verbose=False,
            old_version=False,
            net_recon='resnet50',
            init_path=None,
            use_last_fc=False,
            bfm_folder='./checkpoints/BFM_Fitting/',
            bfm_model='BFM_model_front.mat',
            focal=1015.,
            center=112.,
            camera_d=10.,
            z_near=5.,
            z_far=15.,
            
            )
   
   
    except SystemExit as e:
        print("Please check the input format")
        sys.exit(1)

    return config





def gen_video(image_name, image_binary, audio_name, audio_binary, test=False):
  
    img_path = './images/{}.png'.format(image_name)
    with open(img_path, 'wb') as f:
        f.write(image_binary)

    print(img_path)

    audio_path = './audios/{}.wav'.format(audio_name)
    with open(audio_path, 'wb') as f:
        f.write(audio_binary)

    print(audio_path)
    
    args = get_parser(img_path=img_path, audio_path=audio_path)
    
    if torch.cuda.is_available() and not args.cpu:
        args.device = "cuda"
    else:
        args.device = "cpu"
    
    inf.main(args)


    



    # if test:
    #     # return any video from results folder
    #     video_path = glob.glob('results/*.mp4')[-1]
    #     print(video_path)
    #     with open(video_path, 'rb') as f:
    #         video_binary = f.read()
    #     return video_binary




        # config = parser.parse_args()