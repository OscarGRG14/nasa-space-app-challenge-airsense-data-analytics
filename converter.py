from PIL import Image
import numpy as np
import os

def load_tif_image(file_path):
    """
    Carga una imagen .tif y la convierte en un array NumPy.
    """
    try:
        image = Image.open(file_path)
        image_array = np.array(image.convert('L'))  # Convertir a escala de grises
        return image_array / 255.0  # Normalizar valores
    except Exception as e:
        print(f"Error al cargar la imagen {file_path}: {e}")
        return None

def get_tif_files(upload_dir):
    """
    Obtiene una lista de todas las imágenes .tif en el directorio 'upload'.
    """
    return [f for f in os.listdir(upload_dir) if f.endswith('.tif')]
