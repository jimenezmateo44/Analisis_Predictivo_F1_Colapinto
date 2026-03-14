# main.py
import pandas as pd
from src.analysis import (plot_lap_distribution, 
                        plot_race_evolution, 
                        calculate_performance_gap, 
                        plot_learning_curve, 
                        save_plot
)

from src.prediction import predict_future_gap, plot_prediction

def ejecutar_reportes():
    # Cargar los datos que ya procesamos y guardamos antes
    df_clean = pd.read_csv('data/raw/dataset_estudio_piloto.csv')
    
    # 1. Gráfico de consistencia total
    fig1 = plot_lap_distribution(df_clean)
    save_plot(fig1, '01_consistencia_total.png')

    # 2. Evolución en Brasil
    fig2 = plot_race_evolution(df_clean, 'São Paulo Grand Prix')
    save_plot(fig2, '02_evolucion_brasil_2025.png')

    # 3. Evolución en Abu Dhabi
    fig3 = plot_race_evolution(df_clean, 'Abu Dhabi Grand Prix')
    save_plot(fig3, '03_evolucion_abudhabi_2025.png')

    # 4. Análisis de Brecha (Gap)
    gap_data = calculate_performance_gap(df_clean)
    print("\n--- Tabla de Gap Relativo (%) ---")
    print(gap_data[['GP', 'Gap_%']])

    fig4 = plot_learning_curve(gap_data)
    save_plot(fig4, '04_curva_aprendizaje.png')

    # 5. Predicción de tendencia futura
    # Aquí llamamos a las funciones del nuevo archivo src/prediction.py
    model, future, preds = predict_future_gap(gap_data)
    
    fig5 = plot_prediction(gap_data, future, preds)
    save_plot(fig5, '05_prediccion_tendencia.png')

    # Imprimimos la métrica para tu Word
    print(f"\n🚀 Coeficiente de mejora: {model.coef_[0]:.4f}")

if __name__ == "__main__":
    ejecutar_reportes()