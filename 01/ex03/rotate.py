import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def transpose_image(img: np.ndarray) -> np.ndarray:
    """Manually transposes a 3D image array of shape (H, W, 1)

    into a 2D array of shape (W, H).
    """
    # Eliminar la dimensión del canal para tener un array 2D (400, 400)
    img_2d = np.squeeze(img)
    height, width = img_2d.shape
    
    # Crear una nueva matriz vacía con las dimensiones invertidas
    transposed = np.zeros((width, height), dtype=img_2d.dtype)
    
    # Transposición manual mediante bucles anidados
    for i in range(height):
        for j in range(width):
            transposed[j, i] = img_2d[i, j]
            
    return transposed

def main():
    # 1. Cargar y recortar la imagen usando el módulo previo
    img = ft_load("../ex02/IMG_0311.jpeg")
    if img is None:
        return
        
    # 2. Realizar la transposición
    rotated_img = transpose_image(img)
    
    # 3. Imprimir la nueva forma y el contenido de la matriz transpuesta
    print(f"New shape after Transpose: {rotated_img.shape}")
    print(rotated_img)
    
    # 4. Mostrar la imagen final en pantalla con sus escalas visibles
    plt.imshow(rotated_img, cmap="gray")
    plt.axis("on")
    plt.title("Transposed Image")
    plt.show()
    plt.savefig("mapache_grey.png")

if __name__ == "__main__":
    main()
