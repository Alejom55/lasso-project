import os
import random
import ctypes

def change_wallpaper(folder_path):
    # Lista de archivos en la carpeta especificada
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Selecciona una imagen aleatoria
    random_image = random.choice(image_files)
    
    # Ruta completa de la imagen seleccionada
    image_path = os.path.join(folder_path, random_image)
    
    # Cambia el fondo de pantalla en Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)

# Ruta de la carpeta del script actual
script_folder = os.path.dirname(os.path.abspath(__file__))

# Ruta de la carpeta que contiene las imágenes
image_folder = os.path.join(script_folder, "images")

# Cambia el fondo de pantalla usando las imágenes en la carpeta "imagenes"
change_wallpaper(image_folder)
