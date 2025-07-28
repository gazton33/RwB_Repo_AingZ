# README_CONSOLIDADO_AINGZ_MAIN_20250725_v2.md — Archivo raíz consolidado (AingZ, v2 - 2025-07-25)

---

## 1. Propósito y contexto
Este README centraliza las referencias, estructura, reglas y logs para operar el repo AingZ bajo estándar RwB v2+. Enlaza bitácoras, changelogs y documentación activa para asegurar trazabilidad total.

---

## 2. Estructura general del repositorio (RawBase 2025)
- **WF/** – Workflows activos, logs y bitácora de versiones (`CHG_LOG_WF_PURGATORIO_20250725.md`)
- **knowledges/** – Glosario, contextos, KNS, lessons learned, changelogs (`rw_b_glosario_code_v_1_core.md`, logs KNS)
- **Learn/** – Memoria viva incremental
- **template/** – Plantillas de naming, prompts, README
- **AUDT/** – Auditorías legacy, logs y bitácoras (`CHG_LOG_AUDITORIA_20250725.md`)
- **CONSOLIDADO/** – Outputs finales y entregables listos para uso
- **KNS/** – Knowledge base modular (glosarios, memorias, lessons, logs KNS)
- **DOC/** – Documentación formal, blueprints, master-plans, logs DOC
- **SCR/** – Scripts globales, de integración, ETL
- **LOG/** – Logs globales, changelogs, audit-logs (`CHG_LOG_MAIN_AINGZ_20250725.md`)
- **PURGATORIO/** – Staging temporal/backup previo a integración

---

## 3. Reglas y metodología de operación
- Seguir siempre el glosario core (`knowledges/rw_b_glosario_code_v_1_core.md`) y plantilla de naming (`template/naming/rw_b_naming_template_v_1.md`).
- Usar el plan de directorio (`rwb_repo_directory_plan_v_1.md`), workflows (`WF/`), logs y bitácoras como referencia operativa.
- Toda acción (movimiento, auditoría, integración) debe registrar logs en carpeta/log correspondiente y actualizar el changelog maestro.
- Checklist de cobertura, versionado y referenciación cruzada antes de cada merge, integración o purga.
- Nunca borrar outputs legacy sin respaldo y registro en logs.

---

## 4. Onboarding, logs y changelogs
- La guía de bienvenida (`ONBRD_WELCOME_ONBOARDING_GZ_RW_B_v_20250725.md`) es la referencia inicial para cualquier usuario o IA.
- Logs y changelogs incrementales se mantienen por subcarpeta y se unifican en `CHG_LOG_MAIN_AINGZ_20250725.md`.
- Cada carpeta relevante debe incluir su bitácora/log (WF, AUDT, KNS, DOC, ONBRD, MPLN).
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

