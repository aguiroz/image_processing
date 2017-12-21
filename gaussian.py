#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:36:59 2017

@author: aguiroz
"""

from PIL import Image
from sys import argv
import os

def get_gaussian(mask):
    
    gaussian_mask = [[1, 2, 1],
                     [2, 4, 2],
                     [1, 2, 1]]
    
    red = get_red(mask, gaussian_mask)
    green = get_green(mask, gaussian_mask)
    blue = get_blue(mask, gaussian_mask)
    
    return (red, green, blue)


def get_red(mask, gaussian_mask):
    
    red = 0
    
    for i in xrange(0, len(mask)-1):
        for j in xrange(0, len(mask)-1):
            red += mask[i][j][0] * gaussian_mask[i][j]
        
    return red / 16

def get_green(mask, gaussian_mask):
    
    green = 0
    
    for i in xrange(0, len(mask)-1):
        for j in xrange(0, len(mask)-1):
            green += mask[i][j][1] * gaussian_mask[i][j]
        
    return green / 16


def get_blue(mask, gaussian_mask):
    
    blue = 0
    
    for i in xrange(0, len(mask)-1):
        for j in xrange(0, len(mask)-1):
            blue += mask[i][j][2] * gaussian_mask[i][j]
        
    return blue / 16


file = 'noise.jpeg' #argv[1]
img = Image.open(file)
px = img.load()

for i in xrange(1, img.size[0]-1):
    for j in xrange(1, img.size[1]-1):
        array = [[px[i-1,j-1], px[i,j-1], px[i+1,j-1]],
                 [px[i-1,j],   px[i,j],   px[i+1,j]],
                 [px[i-1,j+1], px[i,j+1], px[i+1,j+1]]]
        
        px[i,j] = get_gaussian(array)
        
fn, fxt = os.path.splitext(file)

img.save('{}_gaussian{}'.format(fn, fxt))
        
        
        
        
        
        
        
        
        
        
        
        