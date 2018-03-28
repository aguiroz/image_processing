#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:45:38 2017

@author: aguiroz
"""

from PIL import Image
from sys import argv
import os


def filter(mask):
    
    red = get_red(mask)
    green = get_green(mask)
    blue = get_blue(mask)
        
    new_px = (red, green, blue)

    return new_px

def get_red(mask):
    
    total = 0
    
    for i in mask:
        
        total += i[0]
        
    return total / 9

def get_green(mask):
    
    total = 0
    
    for i in mask:
        total += i[1]

    return total / 9


def get_blue(mask):
    
    total = 0
    
    for i in mask:
        total += i[2]
    
    return total /9


if __name__ == "__main__":

  try:
    file =  argv[1]
  except IndexError:
    print "\nusage:\n  average.py <IMAGE>\n"
    exit(0)
  img = Image.open(file)
  px = img.load()
  mask = []

  for i in xrange(1,img.size[0]-1):
      for j in xrange(1,img.size[1]-1):
         mask = [px[i-1,j-1], px[i,j-1], px[i+1,j-1],
                 px[i-1,j],   px[i,j],   px[i+1,j],
                 px[i-1,j+1], px[i,j+1], px[i+1,j+1]]
         px[i,j] = filter(mask)

  fn, fxt = os.path.splitext(argv[1])
  img.save('{}_average{}'.format(fn,fxt))
