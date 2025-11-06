# Modelo Supervisado de Auditoría de Prestaciones Médicas Extrahospitalarias

## Objetivo del Proyecto
Este proyecto aplica modelos de clasificación supervisada para automatizar la preselección de solicitudes de prestaciones médicas extrahospitalarias.  
El objetivo es optimizar el proceso de auditoría, garantizando la seguridad del paciente y reduciendo los falsos negativos (denegaciones injustificadas).  
Desarrollado en el marco de la asignatura **Aprendizaje Automático** del **Centro Politécnico Superior Malvinas Argentinas (2025)**.

## Metodología
Se implementaron y compararon tres modelos:
- **DummyClassifier** (modelo base).
- **Regresión Logística**, seleccionada por su equilibrio entre rendimiento y explicabilidad.
- **Árbol de Decisión**, utilizado como apoyo interpretativo.

Flujo de trabajo:
1. Preprocesamiento mediante `Pipeline` de scikit-learn (imputación, codificación One-Hot).
2. División estratificada en entrenamiento y prueba para preservar el equilibrio de clases.
3. Evaluación con métricas de clasificación (accuracy, recall, f1-score, AUC).
4. Búsqueda de hiperparámetros con `GridSearchCV`.

## Resultados Principales
El modelo de **Regresión Logística** (sin balanceo de clases) obtuvo el mejor desempeño operativo.

- **AUC:** 0.9019  
- **Recall (clase “Autorizado”):** 0.9909  
- **F1-score (clase “Autorizado”):** 0.9587  

Estos resultados reflejan una alta capacidad para detectar correctamente las solicitudes que deben ser autorizadas, minimizando los falsos negativos.  
El Árbol de Decisión confirmó la coherencia del modelo al priorizar variables como *documentación completa*, *informe social* y *derecho a cobertura*.

## Conclusión
El modelo de Regresión Logística puede funcionar como filtro inicial, autorizando automáticamente los casos claros y derivando los intermedios a auditoría humana.  
Esto reduce la carga administrativa sin comprometer la seguridad del paciente.  
El proyecto demuestra la aplicabilidad del Machine Learning en auditoría médica con enfoque ético y explicable.

## Próximos Pasos
- Validación cruzada k-fold.  
- Incorporación de modelos de ensamble (Random Forest, Gradient Boosting).  
- Implementación de técnicas de explicabilidad avanzadas (SHAP, LIME).

## Autoría
**Autora:** Nancy Julieta Cassano  
**Docente:** Nicolás Caballero  
**Institución:** Centro Politécnico Superior Malvinas Argentinas  
**Año:** 2025
