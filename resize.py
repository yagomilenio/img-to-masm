import cv2
import numpy as np
from PIL import Image 
from pixel import Pixel


class Img():
    def __init__(self, path="img.jpg"):
        self.path = path
        self.img = cv2.imread(path)
        

    def resize(self, x, y):
        self.img = cv2.resize(self.img, dsize=(x,y), interpolation=cv2.INTER_CUBIC)
        self.x=x
        self.y=y
        cv2.imwrite("resized.jpg", self.img)
    
    def getPixelAtributes(self):
        rgb_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_img)
        pixels = pil_img.load()

        pixelesProcesados = []

        for y in range(self.y):
            for x in range(self.x):
                r, g, b = pixels[x, y]

                if r < 64 and g < 64 and b < 64:
                    color = 0 # Negro
                elif r < 64 and g < 64 and b >= 128:
                    color=1   # Azul
                elif r < 64 and g >= 128 and b < 64:
                    color=2   # Verde
                elif r < 64 and g >= 128 and b >= 128:
                    color=3   # Cian
                elif r >= 128 and g < 64 and b < 64:
                    color=4   # Rojo
                elif r >= 128 and g < 64 and b >= 128:
                    color=5   # Magenta
                elif r >= 128 and 64 <= g < 128 and b < 64:
                    color=6   # Marrón
                elif 128 <= r <= 192 and 128 <= g <= 192 and 128 <= b <= 192:
                    color=7   # Gris claro
                elif 64 <= r < 128 and 64 <= g < 128 and 64 <= b < 128:
                    color=8   # Gris oscuro
                elif 64 <= r < 128 and 64 <= g < 128 and b >= 192:
                    color=9   # Azul claro
                elif 64 <= r < 128 and g >= 192 and 64 <= b < 128:
                    color=10  # Verde claro
                elif r < 128 and g >= 192 and b >= 192:
                    color=11  # Cian claro
                elif r >= 192 and 64 <= g < 128 and 64 <= b < 128:
                    color=12  # Rojo claro
                elif r >= 192 and g < 128 and b >= 192:
                    color=13  # Magenta claro
                elif r >= 192 and g >= 192 and b < 128:
                    color=14  # Amarillo
                elif r >= 224 and g >= 224 and b >= 224:
                    color=15  # Blanco
                else:
                    color=0 # Negro por defecto

                pixelesProcesados.append(Pixel(color, x, y))   

        return pixelesProcesados

