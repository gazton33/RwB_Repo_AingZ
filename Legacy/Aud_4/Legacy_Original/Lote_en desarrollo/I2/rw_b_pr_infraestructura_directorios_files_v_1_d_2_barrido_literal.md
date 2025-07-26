# [RwB] INFRAESTRUCTURA, DIRECTORIOS, FILES Y REFERENCIAS CRUZADAS — BARRIDO LITERAL (v1d2 WIP)

---

## 1. Esquema General de Infraestructura (Versión Barrido Literal)

```plaintext
/
├── README.md (main global)
├── RwB_PR_GLOSARIO_NAMING_PROC_*.md (tag BARRIDO_LITERAL)
├── RwB_README_Templates.md
├── RwB_TEMPLATES_INDEX.md
├── purgatorio/
│    └── [CTX]/[GRP]/[DOMINIO]/[PROJ]/[THREAD]/[CAT]/
├── PR/
│    ├── README.md
│    ├── changelog.md
│    ├── knowledge/
│    ├── templates/
│    ├── onboarding/
│    ├── feedback/
│    └── projects/
│         └── [Dominio]/[Proyecto]/[Thread]/[CAT]/
├── CO/ ...
├── CL/ ...
├── scripts_global/
├── feedback/
├── knowledge/
├── config/
├── onboarding/
├── docs/
```

**Cada ciclo, barrido o checkpoint literal debe estar marcado explícitamente en el naming y README con **``**.**

---

## 2. Tipos de archivos y referencia cruzada (con tags de barrido y revisión)

| Tipo/Categoría | Sigla | Ubicación típica | Glosario/ref | Tag obligatorio  | Features principales            |
| -------------- | ----- | ---------------- | ------------ | ---------------- | ------------------------------- |
| Matriz         | MTR   | .../[CAT]/MTR/   | MTR          | BARRIDO\_LITERAL | Tracking, dashboards            |
| Script         | SCR   | .../[CAT]/SCR/   | SCR          | BARRIDO\_LITERAL | Automatización, migrador, IA    |
| Workflow       | WF    | .../[CAT]/WF/    | WF           | BARRIDO\_LITERAL | Pipelines, integración          |
| Log            | LOG   | .../[CAT]/LOG/   | LOG          | BARRIDO\_LITERAL | Auditing, changelog, version    |
| Documentación  | DOC   | .../[CAT]/DOC/   | DOC          | BARRIDO\_LITERAL | Manuales, decisiones, guías     |
| Knowledge      | KNS   | .../[CAT]/KNS/   | KNS          | BARRIDO\_LITERAL | Aprendizajes, jurisprudencia    |
| Backup         | BK    | .../[CAT]/BK/    | BK           | BARRIDO\_LITERAL | Snapshots, respaldo histórico   |
| Notebook       | NB    | .../[CAT]/NB/    | NB           | BARRIDO\_LITERAL | Prototipos, exploración IA      |
| Configuración  | CFG   | .../[CAT]/CFG/   | CFG          | BARRIDO\_LITERAL | Settings, params, secrets       |
| Template       | TMP   | .../[CAT]/TMP/   | TMP          | BARRIDO\_LITERAL | Modelos de cierre/ciclo         |
| Checklist      | CHK   | .../[CAT]/CHK/   | CHK          | BARRIDO\_LITERAL | Coverage, integridad, QA        |
| Imagen         | IMG   | .../[CAT]/IMG/   | IMG          | BARRIDO\_LITERAL | Visualización, diagrama         |
| Plan           | PLN   | .../[CAT]/PLN/   | PLN          | BARRIDO\_LITERAL | Roadmap, milestones, estrategia |

*(Marcar outputs/ciclos de revisión profunda con tag **`REVISION_PENDING`** en columna adicional)*

---

## 3. Procedimientos, triggers y tags de control

| Proceso/Feature    | Trigger | Tag obligatorio   | Archivo/template asociado        |
| ------------------ | ------- | ----------------- | -------------------------------- |
| Barrido literal    | MIG/CP  | BARRIDO\_LITERAL  | checkpoint\_template, logs       |
| Revisión pendiente | REV     | REVISION\_PENDING | checklist, changelog, feedback   |
| Auditoría          | AUD     | BARRIDO\_LITERAL  | checklist, changelog, infra      |
| Template gen       | TMP     | BARRIDO\_LITERAL  | checkpoint\_template, otros TMPs |

---

## 4. Ciclo de integración (barrido literal)

1. Ejecuta barrido/adquisición/adjunto de outputs legacy, backups y archivos usando template/prompt RwB (`BARRIDO_LITERAL`)
2. Inventaría y versiona outputs en estructura extendida
3. Marca todo ciclo/output pendiente de análisis profundo como `REVISION_PENDING`, con referencia y motivo
4. Documenta logs y changelogs en ciclo/infra
5. Prepara todo para revisión iterativa y feedback

---

## 5. Control y versionado

- Toda actualización de carpeta/infra/README debe estar marcada con fecha, versión y responsable
- Outputs de barrido literal no pueden ser eliminados ni resumidos hasta revisión final y feedback iterativo
- Mantén tags, triggers y logs sincronizados con glosario y templates RwB

---

> Usa esta estructura y tabla como guía en cada ciclo de barrido literal, migración, checkpoint o auditoría. Versiona y registra toda evolución o excepción hasta el cierre definitivo.

