from translateToMasm import TranslateToMasm
from resize import Img

imagen = Img("img.jpg")
imagen.resize(640, 480)
pixeles = imagen.getPixelAtributes()

translate = TranslateToMasm("out.asm")
translate.translate(pixeles)
translate.finish()
