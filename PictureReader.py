from pytesseract import pytesseract, image_to_string
from PIL.ImageGrab import grabclipboard as readImage
from pyperclip import paste as readText
WARNING = '\033[93m'
OKGREEN = '\033[92m'
pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def scanImage():
    img = readImage()
    if img:
        string = image_to_string(img)
        string = string.replace("\n", "")
        string = string.replace("¢", "c")
        string = string.replace("€", "e")
        string = string.replace("&", "e")
        string = string.replace("£", "f")
        return string.split(" ")
    return []

def genHex(string):
    for i in range(0, len(string), 2):
        yield string[i:i+2]
        # Look up itertools.batched

def parse(string):
    original = ""
    decoded = ""
    for val in genHex(string):
        try:
            d = bytes.fromhex(val).decode("ascii")
        except (UnicodeDecodeError, ValueError):
            original += WARNING + val
            decoded += WARNING + "?"
        else:
            original += OKGREEN + val
            decoded += OKGREEN + d            
    return original, decoded

def main():
    strings = scanImage()
    for string in strings:
            print("\n".join(parse(string)))
    print("\n".join(parse(readText())))

if __name__ == "__main__":
    main()