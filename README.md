# ML Auditoría de Prestaciones Extrahospitalarias (TDF)
### EXAMEN PARCIAL – Aprendizaje Automático  
**Entrega 2**  
**Estudiante:** Nancy Julieta Cassano  
**Docente:** Nicolás Caballero · **Año:** 2025  
**Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial – CPS Malvinas Argentinas**

## 1. Contexto del proyecto
El trabajo continúa la Entrega 1, cuyo objetivo general es desarrollar un modelo de **aprendizaje automático supervisado** que prediga la decisión de **autorizar / no autorizar** una prestación médica extrahospitalaria.

El propósito es asistir a la **Dirección de Prestaciones Médicas y Programas Sociales del Ministerio de Salud de Tierra del Fuego**, fortaleciendo la **eficiencia, transparencia y trazabilidad** en las decisiones de auditoría.

Esta **Entrega 2** incluye:
- Descripción y origen del dataset sintético.
- Estructura y principales variables.
- Resultados del Análisis Exploratorio de Datos (EDA).

## 2. Origen y características del dataset
- **Generación sintética:** 19/10/2025, a partir de reglas de negocio reales.  
- **Periodo simulado:** enero – septiembre 2025.  
- **Observaciones:** 1.200 · **Variables:** 21 (20 predictoras + target).  
- **Distribución del target:** 91 % autorizadas / 9 % no autorizadas.  
- **Archivo:** `data/raw/dataset_prestaciones_extrahospitalarias_2025_realista_v1.csv`  
- **Semilla:** 2025 · **MD5:** `c3f985a546faedf456a37d197c3f8502`  

Los datos fueron generados con fines académicos, garantizando **confidencialidad y reproducibilidad**.  
El script generador se encuentra documentado en `src/data/make_dataset.py`.

## 3. Variables principales
| Variable | Tipo | Descripción breve |
|-----------|------|-------------------|
| `edad` | numérica | Edad del paciente |
| `zona` | categórica | Zona geográfica (norte / sur) |
| `hospital_origen` | categórica | Hospital o CAPS que inicia el trámite |
| `ingresos_mensuales`, `egresos_mensuales` | numéricas | Variables económicas del hogar |
| `dni_domicilio_tdf` | booleana | Domicilio en Tierra del Fuego |
| `disponible_en_red_publica` | booleana | Prestación disponible en red pública provincial |
| `tiene_cobertura_inicial` | booleana | Posee obra social o prepaga activa |
| `derecho_cobertura_dir`, `verificacion_cobertura_dir` | booleanas | Flags de cobertura y derecho verificados por la Dirección |
| `informe_social_ok`, `documentacion_completa` | booleanas | Validaciones administrativas y sociales |
| `autorizar` | binaria | Variable objetivo (1 = autoriza · 0 = no autoriza) |

> Se incorporaron **valores nulos y ruido controlado** para practicar técnicas de limpieza e imputación en la próxima entrega.

## 4. Resultados del EDA
- 1.200 registros y 21 variables. Sin duplicados relevantes.  
- 488 nulos concentrados en 84 filas con los mismos campos faltantes.  
- Target desbalanceado (91 % / 9 %).  
- Outliers esperables en `ingresos_mensuales` (4 %).  
- Correlaciones bajas a moderadas, sin multicolinealidad crítica.  
- Señal fuerte en variables administrativas: `disponible_en_red_publica`, `verificacion_cobertura_dir` y `derecho_cobertura_dir`.  
- Se detectaron autorizaciones residuales en combinaciones que deberían descartarse (p. ej., con cobertura activa o domicilio fuera de TDF), probablemente por ruido sintético o reglas conjuntas. Esto se documenta y se analizará con un árbol de decisión.

## 5. Archivos de la Entrega 2
- 📘 Informe descriptivo del dataset (PDF): [`reports/PARCIAL_AA_ENTREGA2_CASSANO_JULIETA.pdf`](reports/PARCIAL_AA_ENTREGA2_CASSANO_JULIETA.pdf)
- 📓 Notebook: [`notebooks/EXAMEN_PARCIAL_AA_CASSANO_NANCY_JULIETA_ENTREGA2_EDA.ipynb`](notebooks/EXAMEN_PARCIAL_AA_CASSANO_NANCY_JULIETA_ENTREGA2_EDA.ipynb)
El informe interpretativo se encuentra incluido dentro de la notebook, en formato Markdown, con las explicaciones y conclusiones completas del análisis exploratorio.

## 6. Licencias y atribución
- **Código:** MIT License  
- **Datos:** CC0 1.0 Universal (Dominio Público)  
- **Autora:** Nancy Julieta Cassano (2025)  
- **Repositorio:** `EXAMEN_PARCIAL_AA_CASSANO_NANCY_JULIETA`

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
