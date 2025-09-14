import cv2
import numpy as np
from PIL import Image 


class Img():
    def __init__(self, path="img.jpg"):
        self.path = path
        self.img = cv2.imread(path)
        

    def resize(self, x, y):
        self.img = cv2.resize(self.img, dsize=(x,y), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("resized.jpg", self.img)
    
    def getPixelAtributes(self):
        im = Image.open("resized.jpg")
        pixels = list(im.getdata())

        pixelesProcesados = []

        for r, g, b in pixels:
            if r < 64 and g < 64 and b < 64:
                pixelesProcesados.append(0)   # Negro
            elif r < 64 and g < 64 and b >= 128:
                pixelesProcesados.append(1)   # Azul
            elif r < 64 and g >= 128 and b < 64:
                pixelesProcesados.append(2)   # Verde
            elif r < 64 and g >= 128 and b >= 128:
                pixelesProcesados.append(3)   # Cian
            elif r >= 128 and g < 64 and b < 64:
                pixelesProcesados.append(4)   # Rojo
            elif r >= 128 and g < 64 and b >= 128:
                pixelesProcesados.append(5)   # Magenta
            elif r >= 128 and 64 <= g < 128 and b < 64:
                pixelesProcesados.append(6)   # Marrón
            elif 128 <= r <= 192 and 128 <= g <= 192 and 128 <= b <= 192:
                pixelesProcesados.append(7)   # Gris claro
            elif 64 <= r < 128 and 64 <= g < 128 and 64 <= b < 128:
                pixelesProcesados.append(8)   # Gris oscuro
            elif 64 <= r < 128 and 64 <= g < 128 and b >= 192:
                pixelesProcesados.append(9)   # Azul claro
            elif 64 <= r < 128 and g >= 192 and 64 <= b < 128:
                pixelesProcesados.append(10)  # Verde claro
            elif r < 128 and g >= 192 and b >= 192:
                pixelesProcesados.append(11)  # Cian claro
            elif r >= 192 and 64 <= g < 128 and 64 <= b < 128:
                pixelesProcesados.append(12)  # Rojo claro
            elif r >= 192 and g < 128 and b >= 192:
                pixelesProcesados.append(13)  # Magenta claro
            elif r >= 192 and g >= 192 and b < 128:
                pixelesProcesados.append(14)  # Amarillo
            elif r >= 224 and g >= 224 and b >= 224:
                pixelesProcesados.append(15)  # Blanco
            else:
                pixelesProcesados.append(0)   # Default a negro si no encaja


        return pixelesProcesados

