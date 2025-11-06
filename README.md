# Modelo Supervisado de Auditoría de Prestaciones Médicas Extrahospitalarias

## Objetivo del Proyecto
Este proyecto implementa modelos de clasificación supervisada para automatizar la preselección de solicitudes de prestaciones médicas extrahospitalarias.  

El objetivo principal es optimizar el proceso de auditoría, garantizando la seguridad del paciente y la equidad en el uso de los recursos.  
Los casos con criterios claros pueden resolverse de manera automática, mientras que los casos ambiguos se destinan a supervisión profesional, manteniendo un equilibrio entre eficiencia y control.  

Desarrollado en el marco de la asignatura *Aprendizaje Automático* del *Centro Politécnico Superior Malvinas Argentinas* (2025).  

---

## Metodología
Se compararon tres modelos de clasificación:

- `DummyClassifier` (modelo base).  
- **Regresión Logística**, seleccionada por su equilibrio entre rendimiento y explicabilidad.  
- **Árbol de Decisión**, utilizado como apoyo interpretativo.  

El flujo de trabajo incluyó preprocesamiento con *Pipeline* de `scikit-learn`, división estratificada de datos, evaluación con métricas de desempeño (*accuracy*, *recall*, *f1-score*, *AUC*) y ajuste de hiperparámetros con `GridSearchCV`.

---

## Resultados Principales
El modelo de **Regresión Logística** mostró el mejor desempeño operativo, con indicadores de precisión y recall elevados, y una adecuada capacidad de generalización (*AUC = 0.89*).  

El **Árbol de Decisión** confirmó la coherencia del modelo al priorizar variables relevantes como `documentacion_completa`, `informe_social` y `derecho_a_cobertura`.

---

## Conclusión
El modelo puede funcionar como un **filtro inicial inteligente**, mejorando la eficiencia del proceso de auditoría sin comprometer la revisión médica ni la seguridad del paciente.  
Demuestra la aplicabilidad del *Machine Learning* en la gestión de prestaciones con un enfoque **ético, responsable y explicable**.

---

## Autoría
**Autora:** Nancy Julieta Cassano  
**Docente:** Nicolás Caballero  
**Institución:** Centro Politécnico Superior Malvinas Argentinas  
**Año:** 2025


