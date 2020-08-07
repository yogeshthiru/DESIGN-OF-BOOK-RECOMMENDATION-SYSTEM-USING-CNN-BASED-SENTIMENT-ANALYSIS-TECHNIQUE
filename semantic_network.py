# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:40:45 2020

@author: TPR
"""
import glob, os
from PIL import Image
count='501'

PATH_TO_TEST_IMAGES_DIR = "C:/Users/TPR/Desktop/datasets/pics/pics-book"
searchstr = os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.jfif')
list_of_images = glob.glob(searchstr)
for i in list_of_images:
    img = Image.open(i)
    #a='C:/Users/TPR/Desktop/pic/res/''"'+i+'"''.jpg'
    img.save('C:/Users/TPR/Desktop/pic/res/'+str(count)+'.jpg')
    print('success')
    e = int(count)
    e=e+1
    count=str(e)
    