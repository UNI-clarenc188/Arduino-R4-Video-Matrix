import cv2
import math
import pyautogui # file picker high definition
import re
import ntpath
from tkinter.filedialog import askopenfilename
import numpy as np

def dround(x):
     frac = x - math.floor(x)
     if frac < 0.5: return math.floor(x)
     return math.ceil(x)

def rescale_frame(frame_input):
    # let's downscale the image using new  width and height
     fixedH = 8
     fixedW = 12
     ar = float(frame_input.shape[1])/float(frame_input.shape[0])
     width = round(fixedH * ar)
     down_points = (width, fixedH)
     resized_down = cv2.resize(frame_input, down_points, interpolation=cv2.INTER_AREA)
     # thresholding 
     grayImage = cv2.cvtColor(resized_down, cv2.COLOR_BGR2GRAY)
     (thresh, bnw) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_OTSU)
     bnw = (255-bnw)
     bnw[bnw == 255] = 1
     # fit in fixedW x fixedH
     if bnw.shape[1] < fixedW:
          bnw = cv2.hconcat([bnw, np.zeros((fixedH,fixedW-bnw.shape[1],1), dtype=np.uint8)])

     if bnw.shape[1] > fixedW:
          exceed = float(bnw.shape[1] - fixedW) / 2.0
          bnw = bnw[::, int(exceed):bnw.shape[1] - dround(exceed)]
     
     return bnw

def getHexValues(frame):
     conc = ''.join([''.join(''.join([str(elem)]) for elem in row) for row in frame])
     return [hex(int(conc[i:i+32], 2)) for i in range(0, len(conc), 32)]

def getFile(name, frames, fps):
     delta = int(1000 / fps)
     with open(name + '.h', 'w') as f:
          f.write('const uint32_t animation[][4] = {\n')
          for frame in frames:
               f.write(
                    '{'+ 
                    f'{frame[0]},{frame[1]},{frame[2]},{delta}'+
                    '},\n'
               )
          f.write('};')
          
def pickFile():
     return askopenfilename( 
          initialdir = "~/Desktop", 
          title = "Select a File", 
          filetypes = (("all files", "*.*"),) 
     )

def validName(name):
     return name[0 : re.search(r'\W+', name).start()]

name = pickFile()
cap = cv2.VideoCapture(name)
print(cap.get(cv2.CAP_PROP_FPS))

if cap.isOpened():
     ret, frame = cap.read()
     frames = [getHexValues(rescale_frame(frame))]
    
else:
    print("Camera is not opened")
    exit()

while cap.isOpened():
     ret, frame = cap.read()
     if not ret:
        break
     frames.append(getHexValues(rescale_frame(frame)))
getFile(validName(ntpath.split(name)[1]), frames, cap.get(cv2.CAP_PROP_FPS))
cap.release()

