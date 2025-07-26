# RwB_LEARN_v1.md — Lecciones Aprendidas (Draft)

---

## 2025-07-24 — Barrido literal completo y reproducibilidad en auditorías legacy
- **Origen:** Ciclo de auditoría legacy, feedback GZ, Chat 2025-07-24
- **Lección:** Todo output de auditoría debe incluir el barrido literal completo del archivo legacy, salvo bloques extremadamente extensos (en cuyo caso se debe listar encabezados y marcar “no auto-reproducible”).
- **Impacto:** Se actualiza workflow oficial RwB_AUDITORIA_LEGACY a v1.1 y se implementa checklist de barrido literal en cada output.
- **Trigger:** Cada ciclo de auditoría deberá validar y referenciar este requisito.
- **Relacionado:** RwB_WF_AUDITORIA_LEGACY_v1.1, RwB_KNS_CTX_v0_lswp.md

---

## 2025-07-24 — Cumplimiento de lista de objetivos antes de avanzar
- **Origen:** Feedback GZ, ciclo training/auditoría, Chat 2025-07-24
- **Lección:** Cuando se plantee una lista de objetivos (o sub-objetivos), no avanzar a nuevas tareas/etapas hasta cumplir 100% todos los puntos salvo feedback o cambio de prioridad explícito.
- **Impacto:** Incluir auto-review de objetivos/tareas abiertas en el workflow y checklist de outputs.
- **Trigger:** Revisar historial y objetivos pendientes cada X tokens/mensajes.
- **Relacionado:** RwB_WF_AUDITORIA_LEGACY_v1.1

---

## 2025-07-24 — Workflow dictado por voz y batch
- **Origen:** Feedback dictado móvil, Chat 2025-07-24
- **Lección:** En modo dictado por voz (mobile/PC), aplicar triggers: no responder entre mensajes, acusar recibido, insight antes de análisis, outputs en texto plano si está en móvil, y registrar plataforma usada.
- **Impacto:** Generar y versionar archivo RwB_WF_DICTADO_v1.md, agregar checklist por plataforma, registrar en memoria viva.
- **Trigger:** Detectar modo dictado por feedback, formato o contexto.
- **Relacionado:** RwB_WF_DICTADO_v1.md, RwB_CHGLOG_v1.md

---


### Última actualización
Actualizado tras auditoría de naming y enlaces (commit ec010c1). Ver changelog.
