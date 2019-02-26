from PIL import Image
import pytesseract

im = Image.open('new4.jpg')
text =pytesseract.image-to-string(im,lang='eng')
print(text)
