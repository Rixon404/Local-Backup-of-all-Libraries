import os
import subprocess
import shutil

# Ejecutar el comando 'pip list' y capturar la salida
pip_list_output = subprocess.check_output(["pip", "list"]).decode("utf-8")

# Divide la salida en líneas y omite las primeras 2 líneas (encabezados)
pip_list_lines = pip_list_output.strip().split("\n")[2:]

# Crear una carpeta de respaldo si no existe
backup_folder = "/path/to/the/folder/of/whl"
os.makedirs(backup_folder, exist_ok=True)

# Recorre las líneas de la lista y obtiene los nombres y versiones de las librerías
for line in pip_list_lines:
    package, version = line.split(maxsplit=1)
    
    # Generar el nombre del archivo .whl
    whl_file = f"{package}-{version}.whl"
    
    try:
        # Copiar el archivo .whl a la carpeta de respaldo
        subprocess.check_call(["pip", "download", "--dest", backup_folder, package])
        print(f"Archivo {whl_file} copiado a la carpeta de respaldo.")
    except subprocess.CalledProcessError:
        print(f"Error al copiar el archivo {whl_file}.")

print("Proceso completado.")
