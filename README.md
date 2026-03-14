# 🏎️ Telemetry Analysis: Colapinto vs Gasly (F1 2026)

[![Python](https://img.shields.io/badge/Python-3.11-blue)]
[![FastF1](https://img.shields.io/badge/Data-FastF1-red)]
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)]
[![License](https://img.shields.io/badge/License-MIT-green)]

Análisis de telemetría de **Franco Colapinto** vs **Pierre Gasly** durante la temporada 2026 de Fórmula 1 utilizando técnicas de **Ciencia de Datos, series temporales y simulación estocástica** para predecir la posición final en el campeonato.

---

# 📊 1. Resumen

Este proyecto analiza datos de **telemetría de alta frecuencia** para comparar el rendimiento entre **Franco Colapinto** y **Pierre Gasly** dentro del mismo equipo.

El objetivo es estimar la **posición final en el campeonato 2026** mediante modelos predictivos basados en:

- Análisis de micro-sectores
- Modelos de degradación de neumáticos
- Simulación de escenarios mediante **Monte Carlo**

El estudio intenta aislar el **ritmo puro del piloto** eliminando factores externos como estrategia, tráfico o incidentes.

---

# 📖 2. Introducción

## Problemática

Evaluar el rendimiento real de un piloto de Fórmula 1 es complejo debido a múltiples variables externas:

- Estrategias de pit stop
- Fiabilidad mecánica
- Tráfico en pista
- Safety Cars
- Diferencias estratégicas entre pilotos del mismo equipo

Estas variables pueden **distorsionar la tabla de puntos**, ocultando diferencias reales de rendimiento.

---

## Hipótesis de Investigación

El análisis de **micro-sectores de telemetría** permite detectar ventajas competitivas de **Franco Colapinto** sobre **Pierre Gasly** que no se reflejan directamente en los resultados oficiales.

---

## Objetivo General

Desarrollar un **modelo predictivo basado en datos de telemetría** que permita proyectar el desempeño de Franco Colapinto hacia el final de la temporada 2026.

---

## Objetivos Específicos

- Extraer datos de telemetría usando **FastF1**
- Analizar degradación de neumáticos
- Comparar rendimiento en micro-sectores
- Modelar rendimiento mediante **machine learning**
- Simular escenarios de campeonato usando **Monte Carlo**

---

## Antecedentes

Históricamente, la Fórmula 1 dependía en gran medida de la **intuición y experiencia de los ingenieros**.

Con el aumento del volumen de datos de sensores, el deporte evolucionó hacia un enfoque **data-driven**, donde:

- Se analizan millones de puntos de datos por carrera
- Se optimizan estrategias mediante modelos predictivos
- La ciencia de datos se convirtió en una herramienta central para la toma de decisiones.

---

# ⚙️ 3. Metodología

## Stack Tecnológico

El proyecto se desarrolló utilizando el siguiente stack:

- **Python**
- **FastF1** para adquisición de telemetría
- **Scikit-learn** para modelos de Machine Learning
- **Pandas / NumPy** para manipulación de datos
- **Matplotlib / Seaborn** para visualización

---

## Justificación del Dataset

Se utilizan datos de la **temporada 2026** para realizar una comparación interna dentro del equipo **Alpine**, lo que permite reducir variables externas como:

- Diferencias entre autos
- Estrategias entre equipos
- Performance del paquete aerodinámico

---

# 🏁 4. El Ecosistema de la Fórmula 1 (Caso de Estudio)

## Alpine A126

El análisis se centra en el **Alpine A126**, monoplaza utilizado durante la temporada 2026.

Aspectos relevantes:

- Unidad de potencia híbrida
- Sistema ERS
- Sensores de alta frecuencia en múltiples componentes del vehículo

---

## Flujo de Datos en un Gran Premio

Durante un Gran Premio se capturan datos de múltiples sensores:

- Velocidad
- RPM
- Posición del acelerador
- Presión de frenado
- Temperatura de neumáticos
- Energía recuperada (ERS)

Estos datos generan **telemetría de alta resolución** utilizada posteriormente para análisis.

---

## Sistema de Competencia

El modelo considera el sistema de puntuación oficial de Fórmula 1:

| Posición | Puntos |
|--------|--------|
| 1 | 25 |
| 2 | 18 |
| 3 | 15 |
| 4 | 12 |
| 5 | 10 |
| 6 | 8 |
| 7 | 6 |
| 8 | 4 |
| 9 | 2 |
| 10 | 1 |

---

# 📈 5. Técnicas de Ciencia de Datos Aplicadas

## Adquisición de Datos

Los datos se obtienen mediante:

- API **FastF1**
- Base histórica **Ergast**

Esto permite acceder a:

- tiempos de vuelta
- telemetría por sector
- datos de stint

---

## Procesamiento de Series Temporales

Los datos de telemetría se modelan como **series temporales dependientes de distancia o tiempo**, permitiendo analizar:

- evolución del ritmo
- degradación de neumáticos
- cambios durante el stint

---

## Análisis Exploratorio (EDA)

Se utilizan diferentes visualizaciones:

- **Boxplots** para distribución de tiempos de vuelta
- **Gráficos de líneas** para evolución del stint
- Comparaciones sector por sector

---

## Modelado Predictivo

Se aplican diferentes técnicas:

- Regresión
- Modelos probabilísticos
- **Simulación Monte Carlo** para proyectar escenarios de campeonato

---

# 🧪 6. Desarrollo Experimental

## Materiales y Entorno

- **VS Code**
- **Python 3.x**
- **GitHub**
- Librerías de análisis científico

---

## Adquisición y Limpieza de Datos

Durante el procesamiento se eliminan vueltas afectadas por:

- Safety Car
- Virtual Safety Car
- tráfico extremo
- pit in / pit out

Esto permite aislar vueltas representativas del **ritmo real del piloto**.

---

## Análisis Univariado

Se analizan distribuciones de variables individuales:

- velocidad máxima
- tiempo de vuelta
- tiempo por sector

---

## Análisis Multivariado

Se estudian relaciones entre múltiples variables:

- temperatura de pista vs degradación
- carga aerodinámica vs velocidad
- consumo energético vs ritmo de carrera

---

## Implementación del Modelo

El modelo final estima:

- ritmo medio esperado
- degradación por stint
- probabilidad de terminar en cada posición

Estas métricas alimentan una **simulación Monte Carlo** para estimar el resultado final del campeonato.

---

# 📊 7. Resultados y Discusión

Los resultados del modelo permiten estimar:

- **Posición final probable de Franco Colapinto**
- Diferencias de rendimiento con Pierre Gasly
- Ventajas en frenada, tracción y gestión de neumáticos

El análisis sugiere que las diferencias en **micro-sectores técnicos** pueden generar ventajas acumulativas a lo largo de la temporada.

---

# 🧾 8. Conclusiones

Los resultados permiten evaluar la hipótesis inicial:

> El análisis de telemetría puede revelar ventajas competitivas que no se reflejan directamente en la tabla de puntos.

El estudio sugiere que **Franco Colapinto presenta ventajas en ritmo puro**, particularmente en sectores de alta carga aerodinámica y gestión de neumáticos.

---

# 📂 Estructura del Proyecto
