# Stenography Example

## Background

This is a Python project created in Visual Studio that does 3 things:
1. Encodes a message in a file
2. Decodes that message
3. Checks to see if a file has been altered by comparing the RGB matricies of the data

## How to use

**This is how I run it:**
- Clone project from GitHub
- Open project in Visual Studio
- Open Python interactive console
- Set environment in Python interactive console to SteganographyPractice
- Follow prompts below
- Have fun!

**Encoding**
import SteganographyPractice, cv2
file_location = "{your image location}"
secret_message = "{your message}"
encoded_image = SteganographyPractice.encode_image(file_location, secret_message)
cv2.imwrite("EncodedImage.jpg", encoded_image)

**Decoding**
encoded_img = "EncodedImage.jpg"
SteganographyPractice.decode_image(encoded_img)

**Checking an image against a known original to see if it is altered**
known_original = "{your image location}"
file_to_compare = "{your other image location}"
SteganographyPractice.imageCompare(known_original, file_to_compare)
