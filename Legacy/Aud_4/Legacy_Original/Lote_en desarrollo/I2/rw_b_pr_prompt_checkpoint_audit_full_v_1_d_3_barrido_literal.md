# [RwB] PROMPT UNIVERSAL PARA CHECKPOINT, AUDITORÍA Y BARRIDO LITERAL (v1d3 WIP)

> **Este prompt ejecuta barridos, auditorías, checkpoints y relevamientos literales según la infraestructura RwB. Todo output debe estar marcado como `BARRIDO_LITERAL` y registrar alertas `REVISION_PENDING` para análisis profundo futuro. NO se interpreta, omite ni resume datos bajo ningún concepto.**

---

## 1. Instrucciones de uso (barrido literal RwB)

1. Adjunta o referencia todos los archivos, logs, outputs, prompts, templates, registros, y especialmente:
   - Archivos visibles en canvas actual
   - Archivos adjuntos históricos o en hilos de chat
   - Docs, workflows, scripts, logs, knowledge, imágenes, feedback, backups, templates, mapeos, changelogs
2. Selecciona el tipo de proceso RwB a ejecutar (Barrido Literal / Checkpoint / Auditoría / Relevamiento / Update / Cierre / Migración / Otro).
3. El sistema procederá a:
   - Auditar y listar literal todos los archivos/outputs sin interpretación
   - Validar naming y triggers (incluyendo `BARRIDO_LITERAL` por defecto)
   - Inventariar outputs y mapping legacy→RwB, marcando con `REVISION_PENDING` cualquier alerta de revisión profunda
   - Checklist y cobertura literal (sin análisis)
   - Logs, changelogs y referencias cruzadas
   - Dejar explícita la consigna “sin análisis, omisión ni interpretación” en cada output
4. Se generará un acta markdown conforme al template RwB, con todo mapeado, checklist y alertas detalladas.
5. NO omite ni resume nada salvo orden del responsable.

---

## 2. Preguntas previas al barrido literal

- ¿Tipo de procedimiento? (Barrido Literal / Checkpoint / Auditoría / ...)
- ¿Contexto (PR / CO / CL)?
- ¿Dominio, proyecto, hilo/ciclo?
- ¿Responsable/revisor?
- ¿Dónde se ubicará el mapping y acta generada?
- ¿Todos los outputs y archivos están adjuntos/referenciados (canvas, adjuntos, histórico)?
- ¿Se detectan archivos/ciclos a marcar para revisión especial? (detalle motivo y referencia)
- ¿Requiere notas adicionales para el análisis posterior?

---

## 3. Output generado

- Acta markdown literal usando el template oficial, con naming/tag `BARRIDO_LITERAL` y sección de alertas `REVISION_PENDING` si aplica
- Mapping legacy→RwB exhaustivo
- Checklist y cobertura literal, sin interpretación
- Logs, referencias cruzadas, changelogs
- Listado completo de outputs, y alerta/flag de todo pendiente de análisis profundo

---

## 4. Instrucciones y advertencias

- Este prompt NO interpreta, omite ni resume datos salvo orden expresa
- Todo output/ciclo que requiera análisis posterior debe quedar marcado y justificado como `REVISION_PENDING`
- El responsable debe aprobar el pase a feedback y la integración final
- Actualiza este prompt a cada cambio en naming, triggers o procedimientos

---

> Usa este prompt en cada ciclo/hilo/legacy que requiera barrido literal, checkpoint o auditoría. Es la base para la etapa de feedback iterativo posterior. Toda excepción o interpretación debe estar documentada y autorizada explícitamente.

