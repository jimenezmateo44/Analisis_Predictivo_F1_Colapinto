import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_lap_distribution(df):
    plt.figure(figsize=(12, 6))
    sns.set_theme(style="whitegrid")
    ax = sns.boxplot(data=df, x='GP', y='LapTime_s', hue='Driver', 
                     palette={'COL': '#0090FF', 'GAS': '#FF6600'})
    plt.title('Distribución de Ritmo de Carrera: Colapinto vs Gasly', fontsize=15)
    plt.ylabel('Tiempo de Vuelta (s)')
    return plt

def plot_race_evolution(df, gp_name): # <--- REVISÁ QUE ESTO ESTÉ IGUAL
    gp_data = df[df['GP'] == gp_name].copy()
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=gp_data, x='LapNumber', y='LapTime_s', hue='Driver', 
                 style='Driver', markers=True, dashes=False,
                 palette={'COL': '#0090FF', 'GAS': '#FF6600'})
    plt.title(f'Evolución de Ritmo de Carrera: {gp_name}', fontsize=15)
    plt.grid(True, alpha=0.3)
    return plt

def save_plot(plt_object, filename):
    folder = 'reports/figures' # Quitamos los '..' porque main.py está en la raíz
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    plt_object.savefig(path, bbox_inches='tight', dpi=300)
    print(f"✅ Gráfico guardado en: {path}")
    plt_object.close()


def calculate_performance_gap(df):
    """
    Calcula el gap porcentual entre Colapinto y Gasly por GP.
    Un valor negativo significa que Colapinto fue más rápido.
    """
    # 1. Promedio de ritmo por GP y Piloto
    averages = df.groupby(['Year', 'GP', 'Driver'])['LapTime_s'].mean().unstack()
    
    # 2. Calcular el gap relativo (%)
    # (Tiempo_COL / Tiempo_GAS - 1) * 100
    averages['Gap_%'] = (averages['COL'] / averages['GAS'] - 1) * 100
    
    return averages.reset_index()

def plot_learning_curve(gap_df):
    """Grafica la evolución de la brecha de rendimiento."""
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=gap_df, x='GP', y='Gap_%', marker='o', color='red', linewidth=2)
    
    # Línea de paridad (0%)
    plt.axhline(0, color='black', linestyle='--', alpha=0.5)
    
    plt.title('Curva de Aprendizaje: Gap Relativo Colapinto vs Gasly', fontsize=14)
    plt.ylabel('Diferencia Porcentual (%)')
    plt.xlabel('Gran Premio')
    plt.grid(True, alpha=0.2)
    
    return plt