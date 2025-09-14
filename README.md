# img-to-masm


Generador de código MASM para dibujar imágenes píxel a píxel en modo gráfico de DOS, optimizando repeticiones horizontales y creando segmentos automáticos si la imagen es grande.

## Descripción

Este proyecto toma una imagen (`img.jpg`) y genera código ensamblador MASM que dibuja la imagen en pantalla usando interrupciones de video (`int 10h`). Se incluyen optimizaciones para combinar píxeles consecutivos del mismo color en loops y reducir la cantidad de instrucciones generadas.

---

## Requisitos

Instalar las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

## Uso

1. Coloca la imagen que quieras dibujar en la carpeta del proyecto con el nombre img.jpg.

2. Ejecuta el programa:
    ```bash
    python main.py
    ```

3. Esto generará un archivo out.asm listo para ensamblar con MASM.


## Limitaciones

- Dibujar cada píxel requiere una interrupción (int 10h), por lo que el código generado puede ser muy grande y lento para imágenes grandes.

- El proyecto está diseñado como ejercicio académico para experimentar con gráficos en DOS y optimización de código ensamblador.