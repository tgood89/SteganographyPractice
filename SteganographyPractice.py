import cv2
import numpy
from pathlib import Path
from PIL import Image

#Encode
#Translates secret message into unicode numbers
def char_generator(secret_message):
    for c in secret_message:
        yield ord(c)

#Gets Image and converts to a matrix
def get_image(image_location):
    img = cv2.imread(image_location)
    return img

#Get GCD of the image array
def getGCD(x,y):
    while(y):
        x,y=y,x%y

    return x

#Hides secret message in image
def encode_image(image_location, msg):
  img = get_image(image_location)
  msg_gen = char_generator(msg)
  pattern = getGCD(len(img), len(img[0]))
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i+1 * j+1) % pattern == 0:
        try:
          img[i-1][j-1][0] = next(msg_gen)
        except StopIteration:
          img[i-1][j-1][0] = 0
          return img

#Decodes secret message from image
def decode_image(img_loc):
  img = get_image(img_loc)
  pattern = getGCD(len(img), len(img[0]))
  message = ''
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i-1 * j-1) % pattern == 0:
        if img[i-1][j-1][0] != 0:
          message = message + chr(img[i-1][j-1][0])
        else:
          return message

#Gets the RGB array data of an image
def getPixels(filename):
    img = Image.open(filename, 'r')
    w, h = img.size
    pix = list(img.getdata())
    return [pix[n:n+w] for n in range(0, w*h, w)]

#Compares RGB array data of two images to check for alteration
def imageCompare(known_original, file_to_compare):
    if(getPixels(known_original) == getPixels(file_to_compare)):
       print("File has not been altered.")
    else:
        print("File has been altered.")