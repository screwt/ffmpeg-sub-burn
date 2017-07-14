#!/usr/bin/python
# coding: utf-8
import os 
import tkFileDialog
import subprocess
import Tkinter as tk
from pprint import pprint
from shutil import copyfile
#top = tk.Tk()
# Code to add widgets will go here...
INITIALDIR = "D:/video/anime/martin_matin"
FFMPEG_DIR = "G:/Program Files/ffmpeg-20160510-git-c8c14d0-win64-static/bin/ffmpeg.exe"

def encode(ass, mp4):
    local_ass = os.path.basename(ass)
    copyfile(ass, local_ass)
    outfile = mp4.replace(".mp4", "_subed.mp4")

    cmd = [FFMPEG_DIR,"-y", "-i", "%s"%mp4, "-vf", 'ass=%s'%(local_ass), outfile]
    pprint(cmd)
    print(" ".join(cmd))
    subprocess.call(cmd, shell=True)
    os.remove(local_ass)

def main():
    mp4 = None
    ass = tkFileDialog.askopenfile(initialdir=INITIALDIR,  mode='rb',title='Choose a subtitle file',filetypes = (("subtitle","*.ass"),))
    if ass != None:
        mp4 = tkFileDialog.askopenfile(initialdir=INITIALDIR, mode='rb',title='Choose a video file',filetypes = (("video","*.mp4"),))

    if ass != None and mp4 != None:
        encode(ass.name, mp4.name)
    



if __name__ == "__main__":
    main()
