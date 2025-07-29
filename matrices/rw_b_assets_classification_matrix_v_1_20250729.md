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
| **INT‑LEG · PG** | INT‑LEG·PG·CORE | ‑         | INT‑LEG·PG·REF | ‑           |
| **EXT‑OFF · DR** | EXT‑OFF·DR·CORE | ‑         | EXT‑OFF·DR·REF | ‑           |
| **AI · TL**      | ‑               | AI·TL·TL  | ‑              | ‑           |

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

