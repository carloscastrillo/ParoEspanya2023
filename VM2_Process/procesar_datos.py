#### DICCIONRIO CON EL NOMBRE DE LAS PROVINCIAS CORRECTAMENTE


diccionario_provincias = {
    "01 Araba/Álava": "Araba/Álava",
    "02 Albacete": "Albacete",
    "03 Alicante/Alacant": "Alicante/Alacant",
    "04 Almería": "Almería",
    "05 Ávila": "Ávila",
    "06 Badajoz": "Badajoz",
    "07 Balears, Illes": "Islas Baleares",
    "08 Barcelona": "Barcelona",
    "09 Burgos": "Burgos",
    "10 Cáceres": "Cáceres",
    "11 Cádiz": "Cádiz",
    "12 Castellón/Castelló": "Castellon",
    "13 Ciudad Real": "Ciudad Real",
    "14 Córdoba": "Córdoba",
    "15 Coruña, A": "A Coruña",
    "16 Cuenca": "Cuenca",
    "17 Girona": "Gerona",
    "18 Granada": "Granada",
    "19 Guadalajara": "Guadalajara",
    "20 Gipuzkoa": "Guipúzcoa",
    "21 Huelva": "Huelva",
    "22 Huesca": "Huesca",
    "23 Jaén": "Jaén",
    "24 León": "León",
    "25 Lleida": "Lérida",
    "26 Rioja, La": "La Rioja",
    "27 Lugo": "Lugo",
    "28 Madrid": "Madrid",
    "29 Málaga": "Málaga",
    "30 Murcia": "Murcia",
    "31 Navarra": "Navarra",
    "32 Ourense": "Orense",
    "33 Asturias": "Asturias",
    "34 Palencia": "Palencia",
    "35 Palmas, Las": "Las Palmas",
    "36 Pontevedra": "Pontevedra",
    "37 Salamanca": "Salamanca",
    "38 Santa Cruz de Tenerife": "Santa Cruz de Tenerife",
    "39 Cantabria": "Cantabria",
    "40 Segovia": "Segovia",
    "41 Sevilla": "Sevilla",
    "42 Soria": "Soria",
    "43 Tarragona": "Tarragona",
    "44 Teruel": "Teruel",
    "45 Toledo": "Toledo",
    "46 Valencia/València": "Valencia/València",
    "47 Valladolid": "Valladolid",
    "48 Bizkaia": "Vizcaya",
    "49 Zamora": "Zamora",
    "50 Zaragoza": "Zaragoza",
    "51 Ceuta": "Ceuta",
    "52 Melilla": "Melilla",
    "Total Nacional": "España"  
}


import pandas as pd
import os

# Ruta de entrada y salida
input_file = "/app/outputs/datos_tasas.csv"
output_file = "/app/outputs/datos_tasas_procesados.csv"

print(f"Leyendo los datos desde {input_file}...")
try:
    datos = pd.read_csv(input_file, sep=";", encoding="utf-8-sig")
    
    datos["Provincias"] = datos["Provincias"].map(diccionario_provincias)
    datos = datos[datos["Provincias"] != "España"]
    # Convertir la columna "Total" a formato numérico
    datos["Total"] = datos["Total"].str.replace(",", ".").astype(float)
    #############################################################################################################
    ################################################# PROCESADO #################################################
    #############################################################################################################

    # Gráfico 1 y 2: Paro medio en hombres y mujeres 2023 por provincia
    hombres_2023 = datos[(datos["Sexo"] == "Hombres") & (datos["Tasas"] == "Tasa de paro de la población") & (datos["Periodo"].str.contains("2023"))]
    mujeres_2023 = datos[(datos["Sexo"] == "Mujeres") & (datos["Tasas"] == "Tasa de paro de la población") & (datos["Periodo"].str.contains("2023"))]

    hombres_2023_prom = hombres_2023.groupby("Provincias")["Total"].mean().reset_index()
    mujeres_2023_prom = mujeres_2023.groupby("Provincias")["Total"].mean().reset_index()

    # Gráfico 3-6: Paro ambos sexos por trimestre 2023 por provincias
    paro_t1 = datos[(datos["Sexo"] == "Ambos sexos") & (datos["Tasas"] == "Tasa de paro de la población") & (datos["Periodo"] == "2023T1")]
    paro_t2 = datos[(datos["Sexo"] == "Ambos sexos") & (datos["Tasas"] == "Tasa de paro de la población") & (datos["Periodo"] == "2023T2")]
    paro_t3 = datos[(datos["Sexo"] == "Ambos sexos") & (datos["Tasas"] == "Tasa de paro de la población") & (datos["Periodo"] == "2023T3")]
    paro_t4 = datos[(datos["Sexo"] == "Ambos sexos") & (datos["Tasas"] == "Tasa de paro de la población") & (datos["Periodo"] == "2023T4")]

    # Guardar los datos limpios en un archivo
    datos_procesados = {
        "hombres_2023_prom.csv": hombres_2023_prom,
        "mujeres_2023_prom.csv": mujeres_2023_prom,
        "paro_t1.csv": paro_t1,
        "paro_t2.csv": paro_t2,
        "paro_t3.csv": paro_t3,
        "paro_t4.csv": paro_t4
    }

    for filename, df in datos_procesados.items():
        output_path = os.path.join("/app/outputs", filename)
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"Archivo generado: {output_path}")

    print("Procesado de datos completado")


except Exception as e:
    print(f"Error durante la limpieza: {e}")
