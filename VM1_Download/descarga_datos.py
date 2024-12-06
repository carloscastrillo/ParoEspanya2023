import requests
import os

# URL del archivo CSV del INE de Tasas de actividad, paro y empleo por provincia y sexo
url = "https://ine.es/jaxiT3/files/t/es/csv_bdsc/3996.csv?nocab=1"
nombre_archivo = "datos_tasas.csv"

# Ruta de salida a outputs
output_dir = "/app/outputs"
ruta_salida = os.path.join(output_dir, nombre_archivo)

print(f"Descargando datos desde {url}...")

try:
    response = requests.get(url)
    response.raise_for_status()  # Verificado
    with open(ruta_salida, "wb") as archivo:
        archivo.write(response.content)
    print(f"Datos descargados y guardados en {ruta_salida}.")
except requests.exceptions.RequestException as e:
    print(f"Error al descargar los datos: {e}")