# [RwB] README — REGLAS RAWBASE Y TRAZABILIDAD UNIVERSAL

> Compendio de las reglas esenciales de la infraestructura, foco en trazabilidad, control de cambios y cumplimiento del estándar RwB-RAWBASE.

---

## 1. Fundamento RawBase
- El RawBase es la fuente de verdad: toda integración, migración, archivo, template, workflow o log debe adherir 100% a la convención universal (naming, estructura, status, logs, mapping).
- Ningún archivo, integración ni template fuera del estándar podrá considerarse "definitivo" ni migrar a PR/CO/CL sin pasar por revisión en purgatorio.

---

## 2. Reglas esenciales
- Todo ciclo de trabajo (migración, cierre, integración, upgrade) debe dejar un mapping de correspondencia entre archivos legacy y archivos RwB (ruta, nombre, status).
- El naming universal es OBLIGATORIO y auditable por script, checklist y logs.
- Ninguna migración puede borrar, sobreescribir ni fusionar archivos legacy sin mapping validado.
- Los logs, changelogs y mapping deben versionarse y adjuntarse en cada cierre/auditoría.
- El onboarding, glosario y templates deben estar siempre actualizados y referenciados en README_MAIN.
- TODO lo que requiera revisión, adaptación, integración cruzada o contiene info de múltiples proyectos/contextos debe marcarse y quedarse en purgatorio hasta resolución.

---

## 3. Trazabilidad total
- El tracking legacy→RwB es la piedra angular: debe poder auditarse cualquier archivo, ciclo o integración desde cualquier punto.
- La tabla mapping y logs de migración son la fuente oficial para actualizar referencias en otros sistemas, docs o históricos.
- Los scripts y templates RwB deben auditar que la trazabilidad se mantenga tras cada cambio.

---

> Toda excepción, adaptación o innovación debe documentarse aquí, con fecha y justificación. La trazabilidad y el RawBase no son negociables.

