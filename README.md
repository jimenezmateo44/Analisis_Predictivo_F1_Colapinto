# 🏎️ Análisis Predictivo: Colapinto vs Gasly (F1 2026)

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![FastF1](https://img.shields.io/badge/Data-FastF1-red.svg)](https://docs.fastf1.dev/)
[![Scikit-Learn](https://img.shields.io/badge/Model-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

Este proyecto de **Ciencia de Datos** analiza la telemetría y el rendimiento comparativo entre **Franco Colapinto** y **Pierre Gasly** dentro de la escudería Alpine. El objetivo es modelar la curva de aprendizaje del piloto argentino y predecir su competitividad para la temporada 2026.

---

## 📊 1. Resumen
El estudio utiliza datos de telemetría de alta frecuencia para aislar el ritmo puro del piloto, eliminando ruidos externos como Safety Cars, estrategias de boxes y tráfico. Mediante modelos de **Regresión Lineal**, se proyecta el punto de convergencia técnica entre ambos pilotos.

## 📖 2. Hipótesis de Investigación
> *"El análisis de micro-sectores y ritmo limpio permite detectar una tasa de mejora constante en Franco Colapinto, sugiriendo que superará la base de rendimiento de Pierre Gasly durante el primer tercio de la temporada 2026."*

## ⚙️ 3. Metodología y Stack Tecnológico
El proyecto sigue una arquitectura modular para garantizar la reproducibilidad y escalabilidad del análisis:
* **Adquisición:** `FastF1 API` para datos de telemetría y tiempos de vuelta.
* **Procesamiento:** `Pandas` y `NumPy` para limpieza y normalización.
* **Visualización:** `Seaborn` y `Matplotlib` para el análisis exploratorio (EDA).
* **Modelado:** `Scikit-learn` para la implementación de la regresión predictiva.

---

## 📂 Estructura del Proyecto
```text
/Analisis_Predictivo_F1_Colapinto
├── data/               # Datasets extraídos y procesados
│   ├── raw/            # CSVs originales de la extracción
│   └── processed/      # Datos limpios listos para modelado
├── src/                # Motor del proyecto (Archivos .py)
│   ├── extraction.py   # ETL y conexión con API
│   ├── cleaning.py     # Filtros estadísticos y outliers
│   ├── analysis.py     # Métricas de gap y visualización
│   └── prediction.py   # Regresión lineal y proyecciones
├── notebooks/          # Experimentación y prototipado
├── reports/            # Output de la investigación
│   └── figures/        # Gráficos de alta resolución (300 DPI)
├── main.py             # Script principal de ejecución
└── requirements.txt    # Dependencias del entorno
```

## 4. Desarrollo Experimental

### 4.1 Materiales y Entorno
El proyecto se desarrolló bajo un entorno de **Ciencia de Datos** profesional, utilizando:
* **Lenguaje:** Python 3.12.
* **IDE:** Visual Studio Code.
* **Gestión de Versiones:** Git y GitHub.
* **Entorno Virtual:** `.venv` para el aislamiento de dependencias.

### 4.2 Algoritmo de Adquisición y Limpieza
Se desarrolló un módulo de extracción (`src/extraction.py`) que interactúa con la API de **FastF1**. Para garantizar la integridad de los datos, se implementó una lógica de limpieza en `src/cleaning.py` basada en los siguientes criterios:
1. **Eliminación de Sesgo de Boxes:** Descarte automático de *In-laps* y *Out-laps*.
2. **Filtrado de Contingencias:** Eliminación de vueltas bajo Safety Car y Virtual Safety Car.
3. **Tratamiento de Atípicos (Outliers):** Aplicación de un umbral del 7% sobre la mediana de tiempo por stint para eliminar ruidos por tráfico o errores de pilotaje.

---

## 5. Resultados y Discusión

### 5.1 Análisis de Consistencia (EDA)
Mediante el análisis de distribución (Boxplots), se determinó que **Pierre Gasly** mantiene una desviación estándar promedio menor ($std \approx 0.7s$), reflejando su experiencia. No obstante, **Franco Colapinto** mostró una reducción progresiva de su variabilidad, alcanzando niveles de consistencia comparables hacia el cierre de la muestra.

### 5.2 Análisis de la Brecha (Gap Analysis)
Se calculó el **Gap Porcentual Relativo** para normalizar el rendimiento entre circuitos. 
* **Hallazgo clave:** En el GP de São Paulo, Colapinto registró un gap de **-0.05%**, superando por primera vez el ritmo promedio de Gasly en condiciones de carrera limpia.

---

## 6. Modelado Predictivo

### 6.1 Implementación de Regresión Lineal
Se utilizó la librería `scikit-learn` para entrenar un modelo de regresión lineal sobre la serie temporal de los gaps obtenidos. La función de transferencia del modelo se define como:



### 6.2 Proyecciones 2026
El modelo arrojó un **Coeficiente de Mejora ($\beta_1$)** negativo y constante. La proyección indica que:
1. La paridad técnica absoluta se consolida al inicio de la temporada 2026.
2. Para la **carrera 8 de 2026**, se predice una ventaja competitiva de Colapinto superior al **0.35%** sobre el tiempo base de referencia.

Estos resultados sugieren que la curva de aprendizaje del piloto argentino no ha llegado a su techo, presentando una tasa de optimización superior a la media de pilotos debutantes en la categoría.

