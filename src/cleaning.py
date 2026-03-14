import pandas as pd
import numpy as np

def cleanRaceData(df, threshold=1.07):
    if df.empty:
        return df
    
    #1. Copia de seguridad
    df_clean = df.copy()

    #2. Convertir a LapTime a segundos (es mas facil de operar)
    #FastF1 trae LapTime como TimeDelta
    df_clean['LapTime_s'] = df_clean['LapTime'].dt.total_seconds()

    #3. Filtro de vueltas precisas.
    #Elimina automaticamente inlaps, outlaps y fallos de cronometraje
    df_clean = df_clean[df_clean['IsAccurate'] == True]

    #4. Filtro por stint y compuesto. 
    #El ritmo real depende de la goma. Calculamos la mediana por cada combinacion
    def filterOutliers(group):
        medianTime = group['LapTime_s'].median()
        #Solo nos quedamos con vueltas que no superen el % de lentitud definido
        return group[group['LapTime_s'] <= (medianTime * threshold)]
    
    #Aplicamos el filtro por GP, piloto y stint 
    df_clean = df_clean.groupby(['Year', 'GP', 'Driver', 'Stint'], group_keys=False).apply(filterOutliers).reset_index(drop=True)

    #5. Resetear indice para que quede ordenado
    df_clean = df_clean.reset_index(drop = True)

    print(f"Limpieza completada. Vueltas originales: {len(df)} | Vueltas limpias: {len(df_clean)}")

    return df_clean