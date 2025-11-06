# Modelo Supervisado de Auditoría de Prestaciones Médicas Extrahospitalarias

## Objetivo del Proyecto
Este proyecto aplica modelos de clasificación supervisada para automatizar la preselección de solicitudes de prestaciones médicas extrahospitalarias.  

El objetivo principal es optimizar el proceso de auditoría, **garantizando la seguridad del paciente y la equidad en el uso de los recursos**, mediante la **reducción de falsos positivos** (autorizaciones indebidas).  
Los casos grises o ambiguos se derivan a **supervisión humana**, manteniendo un equilibrio entre automatización y control profesional.  

Desarrollado en el marco de la asignatura *Aprendizaje Automático* del *Centro Politécnico Superior Malvinas Argentinas* (2025).  

---

## Metodología
Se implementaron y compararon tres modelos:

- `DummyClassifier` (modelo base).  
- **Regresión Logística**, seleccionada por su equilibrio entre rendimiento y explicabilidad.  
- **Árbol de Decisión**, utilizado como apoyo interpretativo.  

### Flujo de trabajo
1. Preprocesamiento mediante *Pipeline* de `scikit-learn` (imputación, codificación One Hot).  
2. División estratificada en entrenamiento y prueba para preservar el equilibrio de clases.  
3. Evaluación con métricas de clasificación (*accuracy*, *recall*, *f1-score*, *AUC*).  
4. Búsqueda de hiperparámetros con `GridSearchCV`.  

---

## Resultados Principales
El modelo de **Regresión Logística** (sin balanceo de clases) obtuvo el mejor desempeño operativo.

- **AUC:** 0.8919  
- **Recall (clase “Autorizado”):** 0.9690  
- **Precision (clase “Autorizado”):** 0.9157  

Estos indicadores reflejan una alta capacidad para **detectar correctamente las solicitudes válidas** y un control adecuado de **autorizaciones erróneas** (*falsos positivos*).  
El **Árbol de Decisión** confirmó la coherencia del modelo al priorizar variables como `documentacion_completa`, `informe_social` y `derecho_a_cobertura`.  

---

## Conclusión
El modelo de **Regresión Logística** puede funcionar como un **filtro inicial**, autorizando automáticamente los casos claros y derivados, mientras reserva los casos dudosos para **revisión por auditoría médica**.  

Este enfoque contribuye a una auditoría más eficiente y transparente, sin comprometer la seguridad del paciente.  
El proyecto demuestra la aplicabilidad del *Machine Learning* en auditoría médica con un enfoque **ético, responsable y explicable**.  

---

## Próximos Pasos
- Validación cruzada *k-fold*.  
- Incorporación de modelos de ensamble (*Random Forest*, *Gradient Boosting*).  
- Implementación de técnicas de explicabilidad avanzada (*SHAP*, *LIME*).  

---

## Autoría
**Autora:** Nancy Julieta Cassano  
**Docente:** Nicolás Caballero  
**Institución:** Centro Politécnico Superior Malvinas Argentinas  
**Año:** 2025  

