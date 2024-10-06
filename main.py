import os
import json
from converter import load_tif_image, get_tif_files
from generator import analyze_image

# Directorios
upload_dir = 'upload'
output_dir = 'output'

# Asegurarse de que el directorio de salida existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def process_images():
    """
    Procesa todas las imágenes .tif en el directorio 'upload', las analiza y guarda los resultados en JSON.
    """
    try:
        # Obtener todas las imágenes .tif
        tif_files = get_tif_files(upload_dir)

        for tif_file in tif_files:
            file_path = os.path.join(upload_dir, tif_file)
            
            # Cargar la imagen
            image_array = load_tif_image(file_path)
            
            if image_array is not None:
                # Analizar la imagen
                result = analyze_image(image_array)
                
                if result:
                    # Guardar el resultado en JSON
                    output_file = os.path.join(output_dir, f"{os.path.splitext(tif_file)[0]}.json")
                    with open(output_file, 'w') as json_file:
                        json.dump(result, json_file, indent=4)
                    print(f"Resultados guardados en: {output_file}")
            else:
                print(f"Error al procesar la imagen: {tif_file}")
    except Exception as e:
        print(f"Error en el procesamiento de imágenes: {e}")

if __name__ == "__main__":
    process_images()
