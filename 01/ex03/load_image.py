import sys
import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    """Loads an image, converts it to grayscale, crops a 400x400 square,

    prints its format, and returns the slice as a numpy array.
    """
    try:
        # 1. Cargar la imagen original
        img_pil = Image.open(path)
        
        # 2. Convertir a escala de grises para coincidir con el formato de 1 canal del ejercicio
        img_gray = img_pil.convert("L")
        img = np.asarray(img_gray)
        
        # 3. Recortar la sección de 400x400 (ajusta las coordenadas según tu animal.jpeg)
        # Tomamos un cuadrado de 400x400 desde el inicio o el centro
        sliced_img = img[100:500, 100:500]
        
        # Expandir dimensiones para tener la forma (400, 400, 1) requerida por el output
        sliced_img = np.expand_dims(sliced_img, axis=2)
        
        # 4. Imprimir la forma inicial y el contenido de la matriz
        print(f"The shape of image is: {sliced_img.shape}")
        print(sliced_img)
        
        return sliced_img

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
