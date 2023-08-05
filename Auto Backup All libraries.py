import subprocess
import os

# Ruta de la carpeta de respaldo de .whl
backup_folder = "/ruta/del/respaldo/de/librerias"

# Obtener la lista de librerías instaladas
completed_process = subprocess.run(["pip", "list"], capture_output=True, text=True)
installed_libraries = [line.split()[0] for line in completed_process.stdout.splitlines()[2:]]

# Obtener la lista de archivos .whl en la carpeta de respaldo
existing_whl_files = [filename for filename in os.listdir(backup_folder) if filename.endswith(".whl")]

# Crear respaldo solo de librerías no presentes en la carpeta de respaldo
for library in installed_libraries:
    library_name = library.split()[0]
    if not any(library_name in filename for filename in existing_whl_files):
        try:
            subprocess.run(["pip", "download", "--no-deps", "-d", backup_folder, library_name])
            print(f"Respaldo de {library_name} creado correctamente.")
        except subprocess.CalledProcessError:
            print(f"Error al crear el respaldo de {library_name}.")

print("Proceso de respaldo completado.")
