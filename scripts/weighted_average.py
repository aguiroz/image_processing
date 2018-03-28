#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:15:05 2017

@author: aguiroz
"""

from PIL import Image
import os


def get_weighted_average(mask):
    
    weighted_mask = [[1,1,1],
                     [1,2,1],
                     [1,1,1]]

    red = get_red(mask, weighted_mask)
    green = get_green(mask, weighted_mask)
    blue = get_blue(mask, weighted_mask)
    return (red, green, blue)

def get_red(mask, weighted_mask):
    red = 0
    for i in xrange(0, len(mask)-1):
        for j in xrange(0, len(mask)-1):
           red += mask[i][j][0] * weighted_mask[i][j] 

    return red / 10

def get_green(mask, weighted_mask):
    green = 0;
    for i in xrange(0, len(mask)-1):
        for j in xrange(0, len(mask)-1):
            green += mask[i][j][1] * weighted_mask[i][j]
    return green / 10

def get_blue(mask, weighted_mask):
    blue = 0
    for i in xrange(0, len(mask)-1):
        for j in xrange(0, len(mask)-1):
            blue += mask[i][j][2] * weighted_mask[i][j]
    return blue / 10

if __name__ == "__main__":

  try:
    file = argv[1]
  except IndexError:
    print "\nusage:\n  weighted_average.py\n"
    exit(0)

  img = Image.open(file)

  px = img.load()

  for i in xrange(1, img.size[0]-1):
    for j in xrange(1, img.size[1]-1):
        array = [[px[i-1,j-1], px[i,j-1], px[i+1,j-1]],
                 [px[i-1,j],   px[i,j],   px[i+1,j]],
                 [px[i-1,j+1], px[i,j+1], px[i+1,j+1]]]
        px[i,j] = get_weighted_average(array)

  fn, fxt = os.path.splitext(file)
  img.save('{}_weighted_average{}'.format(fn, fxt))
