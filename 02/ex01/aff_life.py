import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

def plot_country_evolution(df: pd.DataFrame, country_name: str):
    """Filtra el dataset para un país específico y grafica la evolución

    de su esperanza de vida a lo largo de los años.
    """
    # 1. Buscar el país de forma exacta en la columna 'country'
    country_data = df[df['country'].str.lower() == country_name.capitalize()]
    
    # Validación por si el usuario escribe mal el nombre
    if country_data.empty:
        print(f"Error: El país '{country_name}' no se encuentra en el dataset.")
        return

    # 2. Preparar los ejes X e Y
    # El eje X serán los años (los nombres de las columnas desde la segunda posición en adelante)
    years = country_data.columns[1:]
    
    # El eje Y serán los valores de esperanza de vida para ese país (.values[0][1:] extrae la fila limpia)
    values = country_data.values[0][1:]

    # Convertir los datos del eje X a enteros para que Matplotlib ordene el eje del tiempo limpiamente
    years = years.astype(int)

    # 3. Construir y estilizar el gráfico en Matplotlib
    plt.figure(figsize=(12, 6))
    
    # Trazar la línea principal con marcadores sutiles cada cierto tiempo
    plt.plot(years, values, label=country_data['country'].values[0], color='#2ecc71', linewidth=2.5)
    
    # Configuración de textos y etiquetas
    plt.title(f"Evolución de la Esperanza de Vida: {country_data['country'].values[0]}", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Años", fontsize=11)
    plt.ylabel("Esperanza de Vida (Años)", fontsize=11)
    
    # Activar cuadrícula estética de fondo
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc="upper left")
    
    # Desplegar la ventana gráfica
    plt.show()
    plt.savefig("???.png")

# === PRUEBA DE EJECUCIÓN ===
if __name__ == "__main__":
    # Cargar los datos usando tu función nativa
    df_dataset = load("life_expectancy_years.csv")
    plot_country_evolution(df_dataset, "Afghanistan")
