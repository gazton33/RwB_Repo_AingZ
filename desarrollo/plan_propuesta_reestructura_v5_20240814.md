# PLAN DE REESTRUCTURA INICIAL — v5 (2024-08-14)

Este documento resume el análisis del estado actual del repositorio y propone una primera modificación inmediata de la estructura de directorios y del naming, tomando como referencia los assets en `desarrollo/` y el blueprint `dir_arch_plan_v_5_integracion_matrix.md`.

## 1. Estado actual del repositorio

- La raíz contiene carpetas `WF/`, `doc/`, `kns/`, `legacy/`, `desarrollo/`, `mtx/`, `scripts/`, `template/` y `tests/`. No existen aún los buckets `AUDIT_LIGHT/`, `DATA/`, `LOG/`, `BACKUP/`, `PURGATORIO/`, `TMP/` ni `MIG/` definidos en el blueprint v5【F:desarrollo/dir_arch_plan_v_5_integracion_matrix.md†L12-L33】.
- Muchos documentos en `desarrollo/` explican reglas y políticas: eliminación del purgatorio【F:desarrollo/politica_cierre_eliminacion_purgatorio.md†L1-L27】, proceso LEGACY【F:desarrollo/barrido_literal_redefinicion_legacy.md†L1-L35】 y research de arquitectura CORE【F:desarrollo/arch_research_core_rw_b_v_1.md†L1-L37】.
- El blueprint v5 amplía la Matrix de clasificación y agrega buckets como `/CORE/INT_LEG` y `/BACKUP/AI`【F:desarrollo/dir_arch_plan_v_5_integracion_matrix.md†L33-L73】.
- Tests y scripts funcionan correctamente (`pytest` pasa)【6b9c1c†L1-L4】.

## 2. Variantes analizadas

### Variante A — Aplicar Blueprint v5 literal
- Crear carpetas faltantes (`AUDIT_LIGHT`, `DATA`, `LOG`, `BACKUP`, `PURGATORIO`, `TMP`, `MIG`, `CORE`) siguiendo el árbol propuesto.【F:desarrollo/dir_arch_plan_v_5_integracion_matrix.md†L12-L33】
- Mover `legacy/` dentro de `PURGATORIO/LEGACY/`.
- Renombrar `doc/` a `DOC/` y `desarrollo/` a `DEV/` (staging temporal) para mantener mayúsculas consistentes.
- Implementar naming `SRC·STG·ROLE` en todos los nuevos archivos.

### Variante B — Arquitectura MAIN/ propuesta en research
- Crear único contenedor `MAIN/` con subcarpetas `ASSETS`, `WF`, `KNS`, `TMP`, `DATA`, `AUDIT`, `RESEARCH`, `BACKUP`, `PURG`, según el documento de research interno【F:desarrollo/arch_research_core_rw_b_v_1.md†L16-L36】.
- Fusionar `doc/` y `kns/` dentro de `MAIN/ASSETS/` o `MAIN/KNS/` según rol.
- Mantener `MIG/` para outputs de migración y consolidación.

### Variante C — Eliminación completa de PURGATORIO
- Basada en la política de cierre【F:desarrollo/politica_cierre_eliminacion_purgatorio.md†L1-L27】.
- En lugar de `PURGATORIO`, usar `BACKUP` y `MIG` para activos no consolidados. `legacy/` se movería directo a `BACKUP/INT_LEG/` o `CORE/INT_LEG/` mientras se procesa.

## 3. Análisis FODA de la reestructura

| Fortalezas | Oportunidades |
|------------|---------------|
| Integración con glosario y Matrix v1, facilitando trazabilidad. | Alinear desde ahora la semántica para IA y automatización con OpenAI/Obsidian. |
| Tests y scripts existentes ya soportan mapeo y auditoría. | Implementar desde temprano buckets `AI` para training y snapshots de contexto. |

| Debilidades | Amenazas |
|-------------|----------|
| Cambio de rutas puede romper workflows actuales si no se actualizan todos los enlaces. | Pérdida de historial si la migración de `legacy` no se registra en `registro_trazabilidad_total.md`. |
| Requiere esfuerzo inicial para mover y renombrar archivos. | Inconsistencias entre blueprint v4 y v5 podrían generar confusión si no se actualiza toda la documentación. |

## 4. Conclusiones y modelo propuesto

Se recomienda avanzar con la **Variante A** para mantener coherencia con el `dir_arch_plan_v_5_integracion_matrix.md` y la Matrix de clasificación. Esto permite una integración gradual con las políticas de cierre y la investigación de `MAIN/`, manteniendo compatibilidad con scripts y pruebas existentes. Las carpetas `PURGATORIO` y `BACKUP` se usarán como tránsito controlado mientras se consolida la política definitiva de eliminación.

### Acciones inmediatas sugeridas
1. Crear los buckets faltantes (`AUDIT_LIGHT`, `DATA`, `LOG`, `BACKUP`, `PURGATORIO`, `TMP`, `MIG`, `CORE`).
2. Mover `legacy/` a `PURGATORIO/LEGACY/` y registrar el movimiento en `registro_trazabilidad_total.md`.
3. Renombrar `doc/` → `DOC/` y `desarrollo/` → `DEV/` para uniformar mayúsculas.
4. Actualizar README y scripts de workflows con las nuevas rutas.
5. Conservar en `DEV/` los documentos de planeación y este informe para futuras iteraciones.

**FIN PLAN DE REESTRUCTURA INICIAL**
