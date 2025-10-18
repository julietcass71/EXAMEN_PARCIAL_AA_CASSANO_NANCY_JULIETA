# ML Auditoría de Prestaciones Extrahospitalarias (TDF)

# EXAMEN PARCIAL – Aprendizaje Automático  
### Entrega 2 · Descripción del Dataset y Origen  
**Estudiante:** Nancy Julieta Cassano  
**Proyecto:** Auditoría de Prestaciones Extrahospitalarias con Aprendizaje Automático  
**Institución:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial – Centro Politécnico Superior Malvinas Argentinas  
**Docente:** Nicolás Caballero  
**Año:** 2025  

# 1 · Contexto del proyecto

Este trabajo continúa la **Entrega 1**, donde se formuló el objetivo general de desarrollar un modelo de aprendizaje automático supervisado que prediga la decisión de **autorización o no autorización** de una prestación médica extrahospitalaria, utilizando variables administrativas, médicas y socioeconómicas.  
El propósito es asistir a la **Dirección de Prestaciones Médicas y Programas Sociales del Ministerio de Salud de Tierra del Fuego** en el proceso de auditoría, buscando mayor eficiencia, transparencia y trazabilidad en las decisiones.

Esta **Entrega 2** se centra en la descripción detallada del **dataset** que será utilizado en la etapa de entrenamiento y validación de los modelos.

# 2 · Origen de los datos

El dataset no proviene de registros reales, sino que fue **generado sintéticamente** siguiendo las **reglas de negocio reales** aplicadas por la Dirección de Prestaciones Médicas de Tierra del Fuego en el proceso de auditoría de solicitudes.

Se simularon **1.200 solicitudes de prestaciones médicas** correspondientes al período **enero – septiembre de 2025**, manteniendo proporciones reales entre casos aprobados y no aprobados.  
El dataset busca reflejar fielmente los criterios utilizados durante la auditoría, incluyendo:

- Residencia provincial y documentación vigente.  
- Ausencia o presencia de cobertura social.  
- Situación socioeconómica familiar.  
- Existencia de Certificado Único de Discapacidad (CUD).  
- Informe social validado por el servicio hospitalario.  
- Completitud de la documentación presentada.  

Se adoptó un **balance realista**, con aproximadamente **91 % de casos autorizados** y **9 % no autorizados**, en línea con los valores observados en la práctica institucional.

# 3 · Estructura del dataset

- **Nombre del archivo:** `dataset_prestaciones_extrahospitalarias_2025_realista_v1.csv`  
- **Ubicación:** [`data/raw/`](data/raw/dataset_prestaciones_extrahospitalarias_2025_realista_v1.csv)  
- **Cantidad de instancias:** 1.200  
- **Cantidad de variables:** 21 (20 predictoras + 1 target `autorizar`)  
- **Variable objetivo:** `autorizar` (1 = autorizar · 0 = no autorizar)  
- **Formato:** CSV UTF-8 con encabezado  

# Principales variables incluidas

| Tipo | Ejemplo de columnas |
|------|----------------------|
| **Numéricas** | `edad`, `ingresos_mensuales`, `egresos_mensuales`, `vehiculos_cantidad`, `grupo_familiar_a_cargo` |
| **Categóricas** | `zona`, `hospital_origen`, `estado_civil`, `ocupacion`, `vivienda_tipo` |
| **Booleanas** | `dni_domicilio_tdf`, `disponible_en_red_publica`, `tiene_cobertura_inicial`, `derecho_cobertura_dir`, `informe_social_ok`, `documentacion_completa`, `cud` |
| **Fecha** | `fecha_solicitud` (ISO YYYY-MM-DD) |

> Se incluyeron **inconsistencias intencionales** (valores nulos, fechas fuera de rango, errores de carga) para realizar un **EDA completo** durante la Entrega 3.

# 4 · Propósito del dataset

Este conjunto de datos será la base para el desarrollo de modelos de **aprendizaje supervisado**, específicamente:

1. **Regresión Logística** – para estimar la probabilidad de autorización.  
2. **Árbol de Decisión** – para interpretar reglas y criterios de decisión.  

Las siguientes etapas del proyecto incluirán:
- **Entrega 3:** Análisis exploratorio y limpieza de datos.  
- **Entrega 4:** Entrenamiento y validación de modelos.  
- **Entrega Final:** Interpretación de resultados y conclusiones institucionales.

# 5 · Licencias y atribución

- **Licencia del código:** MIT License  
- **Licencia de los datos:** CC0 1.0 Universal (Dominio Público) – ver [`docs/DATA_LICENSE.txt`](docs/DATA_LICENSE.txt)  
- **Autora:** Nancy Julieta Cassano (2025)  
- **Repositorio:** [EXAMEN_PARCIAL_AA_CASSANO_NANCY_JULIETA](https://github.com/julietcass71/EXAMEN_PARCIAL_AA_CASSANO_NANCY_JULIETA)

# 6 · Estructura del proyecto (Cookiecutter Data Science)


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
