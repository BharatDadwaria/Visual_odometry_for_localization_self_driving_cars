import numpy as np
import pandas as pd
import cv2
import os


def count_dig(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count

def zeros(n):
    return ('0'*n)

def read_data_img(folder):
    images_= []
    for k in range(1,len(os.listdir(folder))+1):
        img=cv2.imread(os.path.join(folder,f'{zeros(6-count_dig(k))}{k}.jpg'))
        if img is not None:
            images_.append(img)
    return images_

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images