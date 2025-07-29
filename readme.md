# README_CONSOLIDADO_AINGZ_MAIN_20250725_v2.md — Archivo raíz consolidado (AingZ, v2 - 2025-07-25)

---

## 1. Propósito y contexto
Este README centraliza las referencias, estructura, reglas y logs para operar el repo AingZ bajo estándar RwB v2+. Enlaza bitácoras, changelogs y documentación activa para asegurar trazabilidad total.

---

## 2. Estructura general del repositorio (RawBase 2025)
- **WF/** – Workflows activos, logs y bitácora de versiones (`chg_log_wf_purgatorio_20250725.md`)
- **knowledges/** – Glosario, contextos y lessons learned (`rw_b_glosario_code_v_1_core_20250725.md`)
- **Learn/** – Memoria viva incremental
- **template/** – Plantillas de naming y README
- **AUDT/** – Auditorías legacy y bitácoras (`CHG_LOG_AUDITORIA_20250725.md`)
- **doc/** – Documentación formal y master-plans
- **scripts/** – Utilidades y ETL
- **matrices/** – Matrices de precedencia y trazabilidad
- **backup/** – Respaldo y purgatorio (`backup/purgatorio/`)

---

## 3. Reglas y metodología de operación
- Seguir siempre el glosario core (`knowledges/rw_b_glosario_code_v_1_core.md`) y plantilla de naming (`template/naming/rw_b_naming_template_v_1.md`).
- Usar el plan de directorio (`rwb_repo_directory_plan_v_1.md`), workflows (`WF/`), logs y bitácoras como referencia operativa.
- Toda acción (movimiento, auditoría, integración) debe registrar logs en el archivo o carpeta correspondiente y actualizar el changelog maestro.
- Checklist de cobertura, versionado y referenciación cruzada antes de cada merge, integración o purga.
- Nunca borrar outputs legacy sin respaldo y registro en logs.

---

## 4. Onboarding, logs y changelogs
- La guía de bienvenida (`ONBRD_WELCOME_ONBOARDING_GZ_RW_B_v_20250725.md`) es la referencia inicial para cualquier usuario o IA.
- Logs y changelogs incrementales se mantienen por subcarpeta y se unifican en `CHG_LOG_MAIN_AINGZ_20250725.md`.
- Cada carpeta relevante debe incluir su bitácora o log (WF, AUDT, knowledges, doc). Las guías de onboarding y el master plan se mantienen en archivos raíz.
- Toda actualización mayor debe reflejarse en este README y el changelog principal.

---

## 5. Próximos pasos y automatización
- Para migrar, auditar o refactorizar cualquier lote, seguir el directorio plan + workflows y logs asociados.
- Validar toda estructura y outputs con scripts/checklists y documentar cada acción incrementalmente en logs/changelogs.
- Mantener el changelog maestro como pivote de revisión y onboarding.

---

## 6. Estado y versionado
- Este README v2 consolida y actualiza la documentación raíz al 25-07-2025.
- Toda versión previa se archiva en backup/PURGATORIO tras validar cobertura y migración.

---


## 7. Ejecución de pruebas
Las pruebas unitarias están en la carpeta `tests/`. Para correrlas se utiliza `pytest`:

```bash
pip install pytest  # si no está instalado
pytest
```
