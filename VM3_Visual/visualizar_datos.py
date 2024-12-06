import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

input_folder = "/app/outputs/"
output_folder = "/app/outputs/"

files = {
    "hombres_2023": "hombres_2023_prom.csv",
    "mujeres_2023": "mujeres_2023_prom.csv",
    "paro_t1": "paro_t1.csv",
    "paro_t2": "paro_t2.csv",
    "paro_t3": "paro_t3.csv",
    "paro_t4": "paro_t4.csv",
}

provincias_shp = gpd.read_file("https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/spain-provinces.geojson")

def generar_cloropleta(data_file, title, output_file):
    print(f"Leyendo {data_file}...")
    df = pd.read_csv(input_folder + data_file)
    
    provincias_shp["Provincia"] = provincias_shp["name"].str.strip()
    df["Provincias"] = df["Provincias"].str.strip()
    merged = provincias_shp.merge(df, left_on="Provincia", right_on="Provincias", how="left")
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    merged.plot(column="Total", cmap="coolwarm", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True)
    ax.set_title(title, fontdict={"fontsize": 15}, loc="center")
    plt.axis("off")
    
    plt.savefig(output_folder + output_file, dpi=300)
    plt.close()
    print(f"Gráfico guardado en {output_folder + output_file}")

generar_cloropleta(files["hombres_2023"], "Paro medio en hombres 2023", "paro_hombres_2023.png")
generar_cloropleta(files["mujeres_2023"], "Paro medio en mujeres 2023", "paro_mujeres_2023.png")
generar_cloropleta(files["paro_t1"], "Paro en T1 2023", "paro_t1_2023.png")
generar_cloropleta(files["paro_t2"], "Paro en T2 2023", "paro_t2_2023.png")
generar_cloropleta(files["paro_t3"], "Paro en T3 2023", "paro_t3_2023.png")
generar_cloropleta(files["paro_t4"], "Paro en T4 2023", "paro_t4_2023.png")

print("Visualización completada.")
