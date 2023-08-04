import os
import subprocess

# Ruta de la carpeta con los archivos .whl
whl_folder = "/path/to/the/folder/of/whl"

# Obtener la lista de archivos .whl en la carpeta
whl_files = [file for file in os.listdir(whl_folder) if file.endswith(".whl")]

# Instalar cada librería desde los archivos .whl
for whl_file in whl_files:
    whl_path = os.path.join(whl_folder, whl_file)
    try:
        subprocess.check_call(["pip", "install", whl_path])
        print(f"Librería {whl_file} instalada correctamente.")
    except subprocess.CalledProcessError:
        print(f"Error al instalar la librería {whl_file}.")

print("Proceso completado.")
