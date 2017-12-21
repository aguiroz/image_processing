#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 00:23:24 2017

@author: aguiroz
"""

from PIL import Image
from sys import argv
import os


def get_prewitt(array):
    
    mask = [[-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]]
    
    red = get_red(array, mask)
    green = get_red(array, mask)
    blue = get_blue(array, mask)
    
    return (red, green, blue)


def get_red(array, mask):
    
    red = 0
    
    for i in xrange(0, len(array)):
        for j in xrange(0, len(array)):
            
            red += array[i][j][0] * mask[i][j]
            
    return red * (red >= 0)

def get_green(array, mask):
    
    green = 0
    
    for i in xrange(0, len(array)):
        for j in xrange(0, len(array)):
            
            green = array[i][j][1] * mask[i][j]
            
        return green * (green >= 0)


def get_blue(array, mask):
    
    blue = 0
    
    for i in xrange(0, len(array)):
        for j in xrange(0, len(array)):
            
            blue += array[i][j][2] * mask[i][j]
            
    return blue * (blue >= 0)


file = argv[1]
img = Image.open(file)

px = img.load()

for i in xrange(1, img.size[0]-1):
    for j in xrange(1, img.size[1]-1):
        
        array = [[px[i-1,j-1], px[i,j-1], px[i+1,j-1]],
                 [px[i-1,j],   px[i,j],   px[i+1,j]],
                 [px[i-1,j+1], px[i,j+1], px[i+1,j+1]]]
        
        
        px[i,j] = get_prewitt(array)

fn, fxt = os.path.splitext(file)

img.save('{}_prewitt_height{}'.format(fn, fxt))