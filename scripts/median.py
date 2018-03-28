#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:26:35 2017

@author: aguiroz
"""

from PIL import Image
from sys import argv
import os



def get_median(mask):
    red = get_red(mask)
    green = get_green(mask)
    blue = get_blue(mask)
    
    new_px = (red, green, blue)
    
    return new_px

def get_red(mask):
    array = []
    
    for i in mask:
        array.append(i[0])
        
    array.sort()
    return array[4]
    
def get_green(mask):
    array = []
    
    for i in mask:
        array.append(i[1])
    
    array.sort()
    return array[4]
    
    
def get_blue(mask):
    array = []
    
    for i in mask:
        array.append(i[2])
    
    array.sort()
    return array[4]
    
    
if __name__ == "__main__":
  try:
    file = argv[1]
  except IndexError:
    print "\nusage:\n  median.py <IMAGE>"
    exit(0)
  img = Image.open(file)

  px = img.load()

  for i in xrange(1,img.size[0]-1):
     for j in xrange(1,img.size[1]-1):
        mask = [px[i-1,j-1], px[i,j-1], px[i+1,j-1],
                px[i-1,j],   px[i,j],   px[i+1,j],
                px[i-1,j+1], px[i,j+1], px[i+1,j+1]]
        px[i,j] = get_median(mask)
    fn, fxt = os.path.splitext(file)

  img.save('{}_median{}'.format(fn,fxt))
