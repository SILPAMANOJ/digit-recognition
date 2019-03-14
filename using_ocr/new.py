try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

im = Image.open('new4.jpg')
text =pytesseract.image-to-string(im,lang='eng')
print(text)
