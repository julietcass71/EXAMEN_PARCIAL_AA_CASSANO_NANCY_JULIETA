# ML Auditoría de Prestaciones Extrahospitalarias (TDF)
**EXAMEN PARCIAL – Aprendizaje Automático**  
**Entrega 2 · Descripción del Dataset y Origen**  

**Estudiante:** Nancy Julieta Cassano  
**Proyecto:** Auditoría de Prestaciones Extrahospitalarias con Aprendizaje Automático  
**Institución:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial – Centro Politécnico Superior Malvinas Argentinas  
**Docente:** Nicolás Caballero  
**Año:** 2025  

## 1 · Contexto del proyecto
Este trabajo continúa la **Entrega 1**, donde se formuló el objetivo general de desarrollar un modelo de **aprendizaje automático supervisado** que prediga la decisión de **autorización o no autorización** de una prestación médica extrahospitalaria, utilizando variables **administrativas, médicas y socioeconómicas**.

El propósito es asistir a la **Dirección de Prestaciones Médicas y Programas Sociales del Ministerio de Salud de Tierra del Fuego** en el proceso de auditoría, buscando **mayor eficiencia, transparencia y trazabilidad** en las decisiones.

Esta **Entrega 2** se centra en la descripción detallada del **dataset** que será utilizado en la etapa de entrenamiento y validación de los modelos.

## 2 · Origen de los datos
El dataset fue **generado sintéticamente** por la autora a partir de reglas de negocio reales aplicadas por la Dirección de Prestaciones Médicas de Tierra del Fuego, con el objetivo de **proteger la confidencialidad de los pacientes** y evitar el uso de información sensible.

- **Fecha de generación:** 17/10/2025
- **Herramienta / script:** `src/data/make_dataset.py`  
- **Semilla aleatoria (reproducibilidad):** 2025  
- **Periodo simulado:** enero – septiembre de 2025  
- **Balance de clases:** 91 % autorizadas / 9 % no autorizadas  
- **Conteos:** 1.092 “autorizar = 1” y 108 “autorizar = 0” (sobre 1.200 instancias) 

**Criterios simulados:**
- Residencia provincial y documentación vigente.  
- Ausencia o presencia de cobertura social.  
- Situación socioeconómica familiar.  
- Existencia de Certificado Único de Discapacidad (CUD).  
- Informe social validado por el servicio hospitalario.  
- Completitud de la documentación presentada.  

> La decisión de utilizar datos sintéticos responde a **razones éticas y regulatorias**, garantizando el cumplimiento de los principios de confidencialidad y trazabilidad institucional.  
> El código generador y las reglas de simulación se encuentran documentadas para asegurar **reproducibilidad y transparencia**.

## 3 · Estructura del dataset
- **Archivo:** `data/raw/dataset_prestaciones_extrahospitalarias_2025_realista_v1.csv`  
- **Versión:** v1.0  
- **Instancias (filas):** 1.200  
- **Variables (columnas):** 21 (20 predictoras + 1 target `autorizar`)  
- **Formato:** CSV UTF-8 con encabezado (separador `,`)  
- **Variable objetivo:** `autorizar` (1 = autorizar · 0 = no autorizar)  
- **Calidad de datos intencional:** se incorporaron valores nulos, fechas fuera de rango y errores de carga simulados para aplicar técnicas de limpieza y validación durante la Entrega 3.  

### Detalles técnicos del dataset
**Fecha de generación:** 17/10/2025  
**Semilla aleatoria:** 2025  
**Hash (MD5):** c3f985a546faedf456a37d197c3f8502  
**Instancias (filas):** 1.200  
**Variables (columnas):** 21  
**Distribución del target `autorizar`:** 1 = 1.092 · 0 = 108

### 3.1 · Diccionario de datos (resumen)

| Variable | Tipo | Descripción | Dominio / Ejemplos |
|-----------|------|--------------|--------------------|
| `fecha_solicitud` | fecha (YYYY-MM-DD) | Fecha en que se ingresó la solicitud | 2025-03-17 |
| `edad` | numérica (entera) | Edad del/la paciente | 0–99 |
| `zona` | categórica | Zona geográfica | norte / sur |
| `hospital_origen` | categórica | Establecimiento que inicia el trámite | HRU / HRC / CAPS_x |
| `estado_civil` | categórica | Estado civil del responsable | soltero / casado / divorciado / viudo |
| `ocupacion` | categórica | Ocupación u oficio | empleado / autónomo / desocupado / estudiante |
| `vivienda_tipo` | categórica | Tipo de vivienda | propia / alquilada / prestada |
| `ingresos_mensuales` | numérica | Ingresos netos del hogar (ARS) | ≥0 |
| `egresos_mensuales` | numérica | Egresos mensuales del hogar (ARS) | ≥0 |
| `grupo_familiar_a_cargo` | numérica (entera) | Cantidad de dependientes | 0–10 |
| `vehiculos_cantidad` | numérica (entera) | Vehículos a nombre del hogar | 0–4 |
| `dni_domicilio_tdf` | booleana | DNI con domicilio en Tierra del Fuego | True / False |
| `disponible_en_red_publica` | booleana | Prestación disponible en red pública provincial | True / False |
| `tiene_cobertura_inicial` | booleana | Posee obra social/prepaga activa | True / False |
| `derecho_cobertura_dir` | booleana | Derecho derivado (por cónyuge/progenitor) | True / False |
| `cud` | booleana | Posee CUD vigente | True / False |
| `informe_social_ok` | booleana | Informe social validado | True / False |
| `documentacion_completa` | booleana | Documentación requerida completa | True / False |
| `zona_riesgo_sanitario` | booleana | Indicador de riesgo sanitario local | True / False |
| `tipo_prestacion` | categórica | Tipo de prestación médica | diagnóstico / tratamiento / cirugía |
| `autorizar` | binaria (**target**) | Resultado de la auditoría | 1 / 0 |

## 4 · Propósito del dataset
Este conjunto de datos será la base para el desarrollo de **modelos de aprendizaje supervisado**, específicamente:

- **Regresión Logística** para estimar la probabilidad de autorización.  
- **Árbol de Decisión** para interpretar reglas y criterios de decisión.

En etapas posteriores se incluirá la comparación con modelos **K-NN** y **SVM** para evaluar desempeño.

## 5 · Licencias y atribución
- **Licencia del código:** MIT License  
- **Licencia de los datos:** CC0 1.0 Universal (Dominio Público) – ver `docs/DATA_LICENSE.txt`  
- **Autora:** Nancy Julieta Cassano (2025)  
- **Repositorio:** `EXAMEN_PARCIAL_AA_CASSANO_NANCY_JULIETA`

## 6 · Estructura del proyecto (Cookiecutter Data Science)

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
