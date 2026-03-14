import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def predict_future_gap(gap_df):
    """
    Usa una regresión lineal para predecir la evolución del gap.
    """
    # Convertimos los GPs a números (1, 2, 3...) para que el modelo pueda operar
    gap_df = gap_df.copy()
    gap_df['Race_Number'] = range(1, len(gap_df) + 1)
    
    X = gap_df[['Race_Number']].values
    y = gap_df['Gap_%'].values
    
    # Entrenamos el modelo
    model = LinearRegression()
    model.fit(X, y)
    
    # Predecimos para las próximas 5 carreras
    future_races = np.array([[i] for i in range(len(gap_df) + 1, len(gap_df) + 6)])
    predictions = model.predict(future_races)
    
    return model, future_races, predictions

def plot_prediction(gap_df, future_races, predictions):
    plt.figure(figsize=(10, 5))
    
    # Datos actuales
    plt.scatter(range(1, len(gap_df) + 1), gap_df['Gap_%'], color='blue', label='Datos Reales')
    
    # Línea de tendencia y predicción
    all_races = np.concatenate([np.arange(1, len(gap_df) + 1), future_races.flatten()])
    # Unimos los datos para graficar la línea completa
    # (Esto es simplificado para el gráfico)
    
    plt.plot(future_races, predictions, '--o', color='red', label='Predicción (Próximas 5)')
    plt.axhline(0, color='black', linestyle='-', alpha=0.3)
    
    plt.title('Proyección de Rendimiento: ¿Cuándo dominará Colapinto?', fontsize=14)
    plt.xlabel('Número de Carrera (Secuencia)')
    plt.ylabel('Gap Relativo (%)')
    plt.legend()
    plt.grid(True, alpha=0.2)
    
    return plt