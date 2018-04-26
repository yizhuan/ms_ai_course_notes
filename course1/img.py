# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:59:54 2018

@author: yizhuan
"""

#%matplotlib inline
from matplotlib.pyplot import imshow
from PIL import Image
import numpy as np
import skimage.color as sc
import curl

#!curl -o img.jpg https://www.google.ie/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F67636%2Frose-blue-flower-rose-blooms-67636.jpeg%3Fcs%3Dsrgb%26dl%3Dblue-plant-wet-67636.jpg%26fm%3Djpg&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fflower%2F&docid=5UbOpOqf9qM23M&tbnid=A6JJqffgz3xzlM%3A&vet=10ahUKEwignJrfmtjaAhVHL8AKHVHiCVEQMwiuASgAMAA..i&w=4928&h=3264&bih=989&biw=1826&q=images&ved=0ahUKEwignJrfmtjaAhVHL8AKHVHiCVEQMwiuASgAMAA&iact=mrc&uact=8
i = np.array(Image.open('img.jpg'))
imshow(i)


i_mono = sc.rgb2gray(i)
imshow(i_mono,cmap = 'gray')

#i_mono.shape
