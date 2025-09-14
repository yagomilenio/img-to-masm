from translateToMasm import TranslateToMasm
from resize import Img

imagen = Img("img.jpg")
imagen.resize(160, 120)
pixeles = imagen.getPixelAtributes()

translate = TranslateToMasm("out.asm")
pixelesOptimizados = translate.optimize(pixeles)
cuarto = len(pixelesOptimizados) // 16 
primer_cuarto = pixelesOptimizados[:cuarto]
translate.translate(pixelesOptimizados)
translate.finish()
