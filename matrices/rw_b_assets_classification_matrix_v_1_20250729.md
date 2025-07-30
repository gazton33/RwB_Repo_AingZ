# 🧮 [RwB] ASSETS\_CLASSIFICATION\_MATRIX — v1 (2025‑07‑29)

> **Propósito:** Matriz 3‑D *Origen × Etapa × Rol Funcional* para clasificar cualquier asset del repo y determinar el procedimiento adecuado (Relevamiento, Auditoría, Consolidado, Migración). Complementa **CONCEPTOS CICLO DE VIDA v1.1**.

---

## 0 · Dimensiones clave

1. **Origen (SRC)** — Fuente del asset (interno, legacy, externo‑oficial, externo‑comunidad, IA, etc.).
2. **Etapa (STG)** — Estado dentro del ciclo de vida (Draft, Activo, Backup, Purgatorio, Legacy, Auditoría, Training‑Learning).
3. **Rol Funcional (ROLE)** — Función operacional principal (Core, Training/Learning, Referencia, Blueprint, etc.).

Formato de código compuesto final: `SRC·STG·ROLE` (ej. `INT·DR·TL`).

---

## 1 · Tabla de Origen (SRC)

| SRC ID  | Fuente            | Descripción |
| ------- | ----------------- | ----------- |
| INT     | Interno‑Nuevo     |             |
| INT‑LEG | Interno‑Legacy    |             |
| EXT‑OFF | Externo‑Oficial   |             |
| EXT‑COM | Externo‑Comunidad |             |
| AI      | Generado‑IA       |             |

## 2 · Tabla de Etapas (STG)

| STG ID | CODE         | State |
| ------ | ------------ | ----- |
| DR     | DRAFT        |       |
| AC     | ACTV         |       |
| BK     | BK/BLN       |       |
| PG     | PURG         |       |
| LG     | LEGACY       |       |
| AU     | AUDT         |       |
| TL     | TRAIN\_LEARN |       |

## 3 · Tabla de Roles Funcionales (ROLE)

| ROLE ID | Nombre            | Descripción                    |
| ------- | ----------------- | ------------------------------ |
| CORE    | Core Activo       | Parte del producto final       |
| TL      | Training/Learning | Resultados de feedback, tuning |
| REF     | Referencia        | Fuente de consulta             |
| BLUE    | Blueprint         | Plan/diagrama maestro          |

---

## 4 · Matriz combinada (extracto)

| SRC \ STG \ ROLE | CORE            | TL        | REF            | BLUE        |
| ---------------- | --------------- | --------- | -------------- | ----------- |
| **INT · DR**     | INT·DR·CORE     | INT·DR·TL | INT·DR·REF     | INT·DR·BLUE |
| **INT · AC**     | INT·AC·CORE     | INT·AC·TL | INT·AC·REF     | INT·AC·BLUE |
| **INT‑LEG · PG** | INT‑LEG·PG·CORE | ‑         | INT‑LEG·PG·REF | ‑           |
| **EXT‑OFF · DR** | EXT‑OFF·DR·CORE | ‑         | EXT‑OFF·DR·REF | ‑           |
| **EXT‑OFF · AC** | EXT‑OFF·AC·CORE | EXT‑OFF·AC·TL | EXT‑OFF·AC·REF | EXT‑OFF·AC·BLUE |
| **INT · BK**     | INT·BK·CORE     | ‑         | INT·BK·REF     | ‑ |
| **INT · PG**     | INT·PG·CORE     | ‑         | INT·PG·REF     | ‑ |
| **INT · AU**     | INT·AU·CORE     | INT·AU·TL | INT·AU·REF     | ‑ |
| **INT · TL**     | ‑               | INT·TL·TL | ‑              | ‑ |
| **INT‑LEG · BK** | INT‑LEG·BK·CORE | ‑         | INT‑LEG·BK·REF | ‑ |
| **INT‑LEG · LG** | INT‑LEG·LG·CORE | ‑         | INT‑LEG·LG·REF | ‑ |
| **EXT‑OFF · BK** | EXT‑OFF·BK·CORE | ‑         | EXT‑OFF·BK·REF | ‑ |
| **EXT‑OFF · PG** | EXT‑OFF·PG·CORE | ‑         | EXT‑OFF·PG·REF | ‑ |
| **EXT‑COM · DR** | EXT‑COM·DR·CORE | ‑         | EXT‑COM·DR·REF | ‑ |
| **EXT‑COM · AC** | EXT‑COM·AC·CORE | EXT‑COM·AC·TL | EXT‑COM·AC·REF | EXT‑COM·AC·BLUE |
| **EXT‑COM · PG** | EXT‑COM·PG·CORE | ‑         | EXT‑COM·PG·REF | ‑ |
| **AI · DR**      | ‑               | AI·DR·TL  | ‑              | ‑ |
| **AI · AC**      | ‑               | AI·AC·TL  | ‑              | ‑ |
| **AI · TL**      | ‑               | AI·TL·TL  | ‑              | ‑ |

*(Completar según necesidades; combinaciones vacías implican flujo no usual.)*

---

## 5 · Procedimiento por Código Compuesto (plantilla)

```markdown
### INT·DR·TL — Draft interno de Training/Learning
1. Crear en `/TRAIN_LEARN/INT/` con sufijo `_draft.md`.
2. Etiquetar `STA=WIP` y registrar en BIT.
3. WF aplicado: `WF_TUNE_FEEDBACK` → genera resultado.
4. Auditoría semanal `WF_AUDIT_TL` decide consolidación a ACTV.
```

### INT·AC·CORE — Activo interno principal
1. Ubicar en `/CORE/INT/`.
2. Registrar snapshot BLN y log en BIT.
3. Auditar mensual `WF_AUDIT_CORE`.
```
### EXT‑OFF·AC·REF — Referencia externa oficial activa
1. Colocar en `/DOC/EXT_OFF/`.
2. Verificar licencias y registrar en BIT.
3. Auditoría trimestral `WF_AUDIT_EXT_OFF`.

### INT·BK·REF — Respaldo interno de referencia
1. Guardar en `/BACKUP/INT/`.
2. Etiquetar `STA=BCK` y registrar en BIT.
3. Auditoría semestral `WF_AUDIT_BACKUP`.

### EXT‑OFF·BK·CORE — Respaldo externo oficial
1. Almacenar en `/BACKUP/EXT_OFF/` con checksum.
2. Revisar licencias antes de archivarlo.
3. Auditoría anual `WF_AUDIT_EXT_OFF`.

### EXT‑COM·AC·TL — Activos comunitarios de Training
1. Guardar en `/KNS/TL/EXT_COM/`.
2. Validar integridad y origen.
3. Ejecutar `WF_TRAIN_EXT_COM` para integrar feedback.

### AI·DR·TL — Draft IA para entrenamiento
1. Crear en `/TMP/AI/` con prefijo `draft_`.
2. Revisar coherencia antes de mover a `/KNS/TL`.
3. Auditoría rápida `WF_AUDIT_TL`.


Añadir subsecciones similares para cada combinación relevante.

---

## 6 · Próximos pasos

1. Completar la matriz y las secciones de procedimiento.
2. Crear triggers `TRG_AUDIT_TL`, `TRG_CONSOLIDATE_TL`.
3. Sincronizar con `DIR_ARCH_PLAN` (posible carpeta `/TRAIN_LEARN/`).
4. Actualizar Glosario con nuevos ROLE codes si procede.

---

### Firma

> Gastón Zelechower · OpenAI o3 — Ruleset RWB Universal

---

**FIN — ASSETS\_CLASSIFICATION\_MATRIX v1**

