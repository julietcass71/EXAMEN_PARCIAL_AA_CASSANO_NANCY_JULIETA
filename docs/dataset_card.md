# Dataset Card — Prestaciones Extrahospitalarias (TDF) 2025 — v1

**Tamaño:** 1 200 filas · 21 columnas (20 features + target `autorizar`)  
**Target:** `autorizar` (0/1) con ≈ 91 % autorizadas.  
**Periodo:** 2025-01-01 → 2025-09-30 (con algunas fechas fuera de rango para control).  
**Origen:** Sintético, basado en el flujo real del proceso de auditoría de prestaciones
extrahospitalarias de la Dirección de Prestaciones Médicas y Programas Sociales (TDF).  
**Generación:** Octubre 2025 – para uso académico en la materia *Aprendizaje Automático*.  

### Calidad intencional
Se incluyeron irregularidades para practicar EDA:
- Nulos (~7 %) en `estado_civil`, `ocupacion`, `ingresos_mensuales`, `egresos_mensuales`, `vehiculos_cantidad`.  
- Valores booleanos mezclados (`0/1`, `S/N`, `True/False`, vacío).  
- Tipos inconsistentes en categóricas (`zona`, `vivienda_tipo`).  
- Ingresos negativos (~0,5 %) y fechas fuera de rango.

### Ética · Privacidad
- Sin datos personales reales ni identificadores (PII).  
- Uso exclusivo con fines didácticos.

### Licencia de datos
CC0 1.0 Universal — Dominio Público.  
Ver archivo `docs/DATA_LICENSE.txt`.
