import ipywidgets as widgets
import glob
import matplotlib.pyplot as plt
from IPython.display import display
import torch
from argparse import ArgumentParser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from IPython.display import HTML
from base64 import b64encode
import os, sys

import SadTalker.src as src


def get_video(image_name, image_binary, audio_name, audio_binary, test=False):

    if test:
        # return any video from results folder
        video_path = glob.glob('results/*.mp4')[-1]
        print(video_path)
        with open(video_path, 'rb') as f:
            video_binary = f.read()
        return video_binary


    img_path = 'images/{}.png'.format(image_name)
    with open(img_path, 'wb') as f:
        f.write(image_binary)

    print(img_path)

    audio_path = 'audios/{}.wav'.format(audio_name)
    with open(audio_path, 'wb') as f:
        f.write(audio_binary)

    print(audio_path)
    
    args = get_parser(img_path=img_path, audio_path=audio_path).parse_args()
    
    if torch.cuda.is_available() and not args.cpu:
        args.device = "cuda"
    else:
        args.device = "cpu"
    
    src.inference.main(args)

    video_path = glob.glob('results/*.mp4')[-1]
    print(video_path)
    with open(video_path, 'rb') as f:
        video_binary = f.read()

    return video_binary

    



def get_parser(img_path, audio_path):
    parser = ArgumentParser()  
    parser.add_argument("--driven_audio", default=audio_path, help='')
    parser.add_argument("--source_image", default=img_path, help='')
    parser.add_argument("--ref_eyeblink", default=None, help="path to reference video providing eye blinking")
    parser.add_argument("--ref_pose", default=None, help="path to reference video providing pose")
    parser.add_argument("--checkpoint_dir", default='./checkpoints', help="path to output")
    parser.add_argument("--result_dir", default='./results', help="path to output")
    parser.add_argument("--pose_style", type=int, default=0,  help="input pose style from [0, 46)")
    parser.add_argument("--batch_size", type=int, default=2,  help="the batch size of facerender")
    parser.add_argument("--size", type=int, default=256,  help="the image size of the facerender")
    parser.add_argument("--expression_scale", type=float, default=1.,  help="the batch size of facerender")
    parser.add_argument('--input_yaw', nargs='+', type=int, default=None, help="the input yaw degree of the user ")
    parser.add_argument('--input_pitch', nargs='+', type=int, default=None, help="the input pitch degree of the user")
    parser.add_argument('--input_roll', nargs='+', type=int, default=None, help="the input roll degree of the user")
    parser.add_argument('--enhancer',  type=str, default="gfpgan", help="gfpgan")
    parser.add_argument('--background',  type=str, default="white", help="background color, [white, black]")
    parser.add_argument('--background_enhancer',  type=str, default=None, help="background enhancer, [realesrgan]")
    parser.add_argument("--cpu", dest="cpu", action="store_true") 
    parser.add_argument("--face3dvis", action="store_true", help="generate 3d face and 3d landmarks") 
    parser.add_argument("--still", action="store_true", help="can crop back to the original videos for the full body aniamtion") 
    parser.add_argument("--preprocess", default='full', choices=['crop', 'extcrop', 'resize', 'full', 'extfull'], help="how to preprocess the images" ) 
    parser.add_argument("--verbose",action="store_true", help="saving the intermedia output or not" ) 
    parser.add_argument("--old_version",action="store_true", help="use the pth other than safetensor version" ) 
    
    
        # net structure and parameters
    parser.add_argument('--net_recon', type=str, default='resnet50', choices=['resnet18', 'resnet34', 'resnet50'], help='useless')
    parser.add_argument('--init_path', type=str, default=None, help='Useless')
    parser.add_argument('--use_last_fc',default=False, help='zero initialize the last fc')
    parser.add_argument('--bfm_folder', type=str, default='./checkpoints/BFM_Fitting/')
    parser.add_argument('--bfm_model', type=str, default='BFM_model_front.mat', help='bfm model')
    
        # default renderer parameters
    parser.add_argument('--focal', type=float, default=1015.)
    parser.add_argument('--center', type=float, default=112.)
    parser.add_argument('--camera_d', type=float, default=10.)
    parser.add_argument('--z_near', type=float, default=5.)
    parser.add_argument('--z_far', type=float, default=15.)

    return parser