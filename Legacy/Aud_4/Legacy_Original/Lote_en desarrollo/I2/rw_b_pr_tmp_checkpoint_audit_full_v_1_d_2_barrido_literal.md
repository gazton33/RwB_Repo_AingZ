# [RwB] TEMPLATE UNIVERSAL DE CHECKPOINT, AUDITORÍA, RELEVAMIENTO Y CIERRE — BARRIDO LITERAL (v1d2 WIP)

> **Este template se utiliza en cada ciclo de barrido, checkpoint, auditoría o relevamiento literal RwB. Cada instancia es literal, exhaustiva y sin interpretación, debe estar marcada con `BARRIDO_LITERAL` en naming y acta. Toda alerta para revisión profunda se documenta como `REVISION_PENDING`. No se elimina, omite ni resume nada salvo autorización expresa.**

---

## 1. Metadatos del ciclo/procedimiento
- **Nombre RwB (full naming, con tag):**
- **Tipo de procedimiento:** Barrido Literal / Checkpoint / Auditoría / Relevamiento / Update / Cierre / Migración
- **Tag RwB obligatorio:** BARRIDO_LITERAL
- **¿Algún ciclo/archivo marcado para revisión?:** (Sí/No, detallar)
- **Fecha y hora:**
- **Responsable:**
- **Contexto:** PR / CO / CL
- **Dominio, proyecto, hilo:**
- **Trigger/proceso disparador:** CP / AUD / MIG / REV / TMP / BARRIDO_LITERAL

---

## 2. Objetivo, alcance y descripción literal
- **Descripción literal del ciclo, chat, hilo o integración (sin interpretación):**
- **Objetivo concreto:** (Qué se releva, cierre o audita)
- **Alcance:** (archivos, features, procesos, áreas cubiertas)
- **Notas contextuales:** (Dependencias, feedback previo, relación con infra, etc)

---

## 3. Inventario y mapping legacy → RwB
- **Tabla mapping literal:**

| Archivo Legacy           | Archivo RwB universal (con tag)                | Categoría | Contexto | Dominio   | Ubicación final           | Status         | Tag revisión  |
| ------------------------ | ---------------------------------------------- | --------- | -------- | --------- | ------------------------- | -------------- | ------------- |
| legacy/knowledge1.md     | RwB_PR_DataAIEng_ProjA_ThreadX_KNS_v1d1_WIP_knowledge1_BARRIDO_LITERAL.md | KNS       | PR       | DataAIEng | /purgatorio/PR/DataAIEng/KNS/ | AUDITADO       |               |
| legacy/scripts/auto.py   | RwB_PR_DataAIEng_ProjA_ThreadX_SCR_v1_FIN_auto_BARRIDO_LITERAL.py         | SCR       | PR       | DataAIEng | /purgatorio/PR/DataAIEng/SCR/ | REVISION_PENDING| Falta análisis sobre dependencias|

- **Referencias cruzadas y logs:** (chats, templates, scripts, logs, changelogs, feedback, README, etc)

---

## 4. Checklist de cobertura literal (sin interpretación)
  - [ ] Mapping legacy→RwB realizado y versionado
  - [ ] Naming universal con tag BARRIDO_LITERAL validado
  - [ ] Outputs ubicados en infra extendida
  - [ ] Logs y changelogs adjuntos
  - [ ] Pendientes/revisión documentados (REVISION_PENDING)
  - [ ] Referencias cruzadas completas (features, glosario, plan, infra, scripts)
  - [ ] Integración/cierre pendiente de análisis posterior

---

## 5. Alerta de revisión (si aplica)
- **¿Hay archivos, outputs o ciclos marcados para revisión profunda?**
  - [ ] Sí (detalle a continuación)
  - [ ] No
- **Detalle literal y referencia de outputs/ciclos a revisar (REVISION_PENDING):**

---

## 6. Instrucciones finales de barrido literal RwB
- No eliminar ni resumir ningún dato/archivo hasta cerrar ciclo de feedback y análisis.
- Mantener mapping legacy→RwB y logs visibles hasta integración final.
- Señalar todo output que requiera revisión posterior con el tag REVISION_PENDING.
- Versionar y registrar este acta/checkpoint junto al resto de outputs del ciclo.
- El responsable debe aprobar el cierre y el pase a etapa de análisis.

---

> **Este template debe usarse en toda auditoría, barrido o checkpoint literal RwB. La consigna es NO OMITIR, NO INTERPRETAR ni eliminar datos hasta cerrar el análisis posterior (etapa de feedback iterativo). Actualizar template a cada nuevo trigger, feature o regla del sistema.**

