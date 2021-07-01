import cv2
import numpy
from pathlib import Path

#Encode
#Translates secret message into unicode numbers
secret_message = "Hola Amigos and Amigas"
def char_generator(secret_message):
    for c in secret_message:
        yield ord(c)

#Gets Image and converts to a matrix
#image_location = Path("C:/Users/tsgoo/source/repos/school/SteganographyPractice/Stevie.jpg")
image_location = "Stevie.jpg"
def get_image(image_location):
    img = cv2.imread(image_location)
    return img

#Get GCD of the image array
def getGCD(x,y):
    while(y):
        x,y=y,x%y
    return x

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

encoded_image = encode_image(image_location, secret_message)
cv2.imwrite ("EncodedImage.png", encoded_image)
print("Works")

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









