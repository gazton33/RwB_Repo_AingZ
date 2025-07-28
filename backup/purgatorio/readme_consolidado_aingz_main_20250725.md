# README_CONSOLIDADO_AINGZ_MAIN_20250725.md — Archivo raíz consolidado para AingZ (v2025-07-25)

---

## 1. Propósito y contexto
Este README reemplaza y consolida la información clave de los archivos `README.md`, `README_CHATGPT.md` y la guía onboarding previa, centralizando referencias, estructura y reglas para operar sobre el repo AingZ bajo estándar RwB v2+.

---

## 2. Estructura general del repositorio (RawBase 2025)
- **WF/** – Workflows operativos versionados y validados
- **knowledges/** – Glosarios, contextos, KNS, lessons learned y changelogs
- **Learn/** – Memoria viva incremental
- **template/** – Plantillas de naming, prompts y README
- **AUDT/** – Auditorías legacy por lote (ver directorio plan)
- **CONSOLIDADO/** – Outputs finales y entregables listos para uso
- **KNS/** – Knowledge base modular (glosarios, memorias, lessons)
- **DOC/** – Documentación formal, blueprints, master-plans
- **SCR/** – Scripts globales, de integración, ETL
- **LOG/** – Logs globales, changelogs, audit-logs
- **PURGATORIO/** – Staging temporal previo a integración

---

## 3. Reglas y metodología de operación
- Seguir siempre el glosario core (`knowledges/glossary/rw_b_glosario_code_v_0_core.md`) y la **plantilla de naming** (`template/naming/rw_b_naming_template_v_1.md`).
- Usar el plan de directorio (`rwb_repo_directory_plan_v_1.md`) como guía estructural y el workflow de auditoría (`WF/rw_b_wf_auditoria_legacy_v_2_20250724.md` + `WF/wf_migracion_final_legacy_rw_b_v_1_20250725.md`).
- Toda acción (movimiento, auditoría, integración) debe registrar logs (`LOG/`), lessons learned (`KNS/LEARN/`), y actualizar el changelog.
- Aplicar checklist de cobertura, versionado y referenciación cruzada antes de cada merge, integración o purga.
- Nunca borrar outputs legacy sin respaldo y referencia explícita en logs.

---

## 4. Onboarding y colaboración
- La guía de bienvenida (`welcome_onboarding_gz.md`) se mantiene como contacto rápido y referencia para nuevos colaboradores. Todas las instrucciones iniciales deben centralizarse en este README consolidado.
- Enlaces útiles, documentación ampliada y blueprints se gestionan bajo `DOC/` y `DOC/BLPR/`.

---

## 5. Próximos pasos y automatización
- Para migrar, auditar o refactorizar cualquier lote, seguir el directorio plan + workflows asociados.
- Validar toda estructura y outputs con scripts de checklist (`generate_legacy_checklist.py`, etc.).
- Documentar cada acción incrementalmente y mantener trazabilidad absoluta en logs/changelogs.

---

## 6. Estado y versionado
- Este README se irá actualizando conforme avance la consolidación.
- Todos los archivos legacy previos se mueven a backup/`PURGATORIO` una vez verificado que la cobertura está garantizada por los outputs nuevos.

---

