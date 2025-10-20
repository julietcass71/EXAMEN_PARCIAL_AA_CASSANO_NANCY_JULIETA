# Data Dictionary – Dataset de Auditoría de Prestaciones Extrahospitalarias (TDF)

**Archivo fuente:** data/raw/dataset_prestaciones_extrahospitalarias_2025_realista_v1.csv  
**Versión:** v1.0  
**Cantidad de registros (filas):** 1.200  
**Cantidad de variables (columnas):** 21  
**Variable objetivo:** autorizar (1 = autorizar, 0 = no autorizar)  
**Semilla aleatoria:** 2025  
**Fecha de generación:** 19/10/2025  
**Hash (MD5):** c3f985a546faedf456a37d197c3f8502

## 1. Descripción general

El dataset fue generado de forma sintética siguiendo las **reglas de negocio reales** aplicadas por la Dirección de Prestaciones Médicas de Tierra del Fuego, con el objetivo de **simular solicitudes de prestaciones médicas extrahospitalarias** y su decisión de **autorización o no autorización**.

Incluye variables **administrativas**, **socioeconómicas** y **médicas** que reflejan los criterios institucionales vigentes para el análisis de cobertura.

## 2. Estructura del dataset

| Nº | Variable | Tipo de dato | Descripción | Valores / Rango posible |
|----|-----------|--------------|--------------|--------------------------|
| 1 | `fecha_solicitud` | Fecha (YYYY-MM-DD) | Fecha de ingreso de la solicitud | 2025-01-01 a 2025-09-30 |
| 2 | `edad` | Numérica (entera) | Edad del/la paciente | 0 – 99 |
| 3 | `zona` | Categórica | Zona geográfica provincial | `norte`, `sur` |
| 4 | `hospital_origen` | Categórica | Establecimiento que origina la solicitud | `HRU`, `HRC`, `CAPS_x` |
| 5 | `estado_civil` | Categórica | Estado civil del responsable | `soltero`, `casado`, `divorciado`, `viudo` |
| 6 | `ocupacion` | Categórica | Ocupación principal | `empleado`, `autónomo`, `desocupado`, `estudiante` |
| 7 | `vivienda_tipo` | Categórica | Tipo de vivienda declarada | `propia`, `alquilada`, `prestada` |
| 8 | `ingresos_mensuales` | Numérica (float) | Ingresos mensuales del hogar (ARS) | ≥ 0 |
| 9 | `egresos_mensuales` | Numérica (float) | Egresos mensuales del hogar (ARS) | ≥ 0 |
| 10 | `grupo_familiar_a_cargo` | Numérica (entera) | Cantidad de familiares a cargo | 0 – 10 |
| 11 | `vehiculos_cantidad` | Numérica (entera) | Cantidad de vehículos declarados | 0 – 4 |
| 12 | `dni_domicilio_tdf` | Booleana | DNI con domicilio en Tierra del Fuego | `True`, `False` |
| 13 | `disponible_en_red_publica` | Booleana | Prestación disponible en red pública provincial | `True`, `False` |
| 14 | `tiene_cobertura_inicial` | Booleana | Posee obra social o prepaga activa | `True`, `False` |
| 15 | `derecho_cobertura_dir` | Booleana | Tiene derecho derivado a cobertura (por cónyuge/progenitor) | `True`, `False` |
| 16 | `cud` | Booleana | Posee Certificado Único de Discapacidad (CUD) | `True`, `False` |
| 17 | `informe_social_ok` | Booleana | Informe social validado por el hospital/CAPS | `True`, `False` |
| 18 | `documentacion_completa` | Booleana | Documentación requerida completa y vigente | `True`, `False` |
| 19 | `zona_riesgo_sanitario` | Booleana | Indicador de riesgo sanitario en zona de residencia | `True`, `False` |
| 20 | `tipo_prestacion` | Categórica | Tipo de prestación médica solicitada | `diagnóstico`, `tratamiento`, `cirugía` |
| 21 | `autorizar` | Binaria (objetivo) | Resultado de la auditoría (target) | `1 = autorizar`, `0 = no autorizar` |

## 3. Notas sobre calidad de datos
- Se incluyeron **valores faltantes y errores intencionales** para practicar limpieza y validación en la próxima entrega.  
- Las variables numéricas fueron generadas dentro de rangos plausibles, con variabilidad realista.  
- No existen identificadores personales ni datos sensibles.  
- La proporción de clases (`autorizar`) refleja valores observados en la práctica real (~91 % aprobadas).  

## 4. Licencia y uso
- **Licencia de los datos:** CC0 1.0 Universal (Dominio Público).  
- Los datos pueden ser utilizados libremente con fines educativos y de investigación, citando a la autora.  

**Versión:** v1.0  
**Última actualización:** {19/10/2025}  
**Autora:** Nancy Julieta Cassano  
**Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial – CPS Malvinas Argentinas**
