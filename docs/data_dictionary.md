# Data Dictionary

| Variable | Tipo | Descripción |
|-----------|------|--------------|
| id_solicitud | string | Identificador único de la solicitud. |
| fecha_solicitud | date (YYYY-MM-DD) | Fecha de ingreso. |
| zona | categórica | Norte / Sur (procedencia administrativa). |
| hospital_origen | categórica | HRU, HRRG, CAPS u otro. |
| edad | int | Años cumplidos del paciente. |
| estado_civil | categórica | Soltero, casado, etc. |
| dni_domicilio_tdf | bool | DNI vigente con domicilio en Tierra del Fuego. |
| disponible_en_red_publica | bool | Si la prestación existe en la red pública provincial. |
| tiene_cobertura_inicial | bool | Si posee cobertura declarada. |
| verificacion_cobertura_dir | bool | Rechequeo por la Dirección. |
| derecho_cobertura_dir | bool | Derecho indirecto (cónyuge, progenitor, etc.). |
| grupo_familiar_a_cargo | int | Cantidad de familiares a cargo. |
| ingresos_mensuales | float (ARS) | Ingreso declarado total del hogar. |
| egresos_mensuales | float (ARS) | Egreso declarado total del hogar. |
| ocupacion | categórica | Profesión, oficio u ocupación principal. |
| cud | bool | Posee Certificado Único de Discapacidad. |
| vivienda_tipo | categórica | Propia, alquilada, prestada, etc. |
| vehiculos_cantidad | int | Cantidad de vehículos propios. |
| informe_social_ok | bool | Informe social completo y validado. |
| documentacion_completa | bool | Orden médica, DNI, informes y estudios adjuntos. |
| autorizar | bool (target) | Decisión de autorización simulada (1 = sí, 0 = no). |
