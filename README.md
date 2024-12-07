# EstudioLaboralEspanya23

## Descripción
Este proyecto analiza las tasas de actividad, paro y empleo en las provincias de España utilizando datos oficiales del INE (Instituto Nacional de Estadística). A través de tres contenedores Docker, el proyecto descarga, procesa y visualiza la información en mapas de coropletas para facilitar su análisis.

## Estructura del Proyecto
El proyecto está dividido en tres máquinas virtuales:
1. **VM1_Download**: Descarga los datos en formato CSV desde la página del INE.
2. **VM2_Process**: Limpia y procesa los datos, eliminando entradas no necesarias y preparando los datos para la visualización.
3. **VM3_Visual**: Genera mapas de coropletas con las tasas de paro por provincia y género.

Además, se utiliza un directorio `outputs` para almacenar todos los archivos generados: CSV procesados y gráficos resultantes.

## Requisitos
- **Docker** y **Docker Compose** instalados.
- Python 3.9 con las siguientes librerías (si deseas ejecutar fuera de Docker):
  - `pandas`
  - `geopandas`
  - `matplotlib`
  - `requests`