# README — RwB Repo Main (v5, 2025-07-30)

> **STATUS:** `ACTIVO`
>
> Consolidado a partir de *README\_CONSOLIDADO\_AINGZ\_MAIN\_20250725\_v2.md* y *README — RwB Repo Main v4 (2025-07-29)*. Integra todas las secciones operativas (instalación, pruebas, mapeo), referencias blueprint y matrices actualizadas al día.

---

## 🔑 Navegación rápida (Blueprint Assets)

| Archivo                                               | Propósito                                                            |
| ----------------------------------------------------- | -------------------------------------------------------------------- |
| `rw_b_glosario_code_v_2_20250729.md`                  | Glosario maestro: jerarquía, naming, roles, features                 |
| `rw_b_diccionario_code_triggers_v_2_20250729.md`      | Diccionario rápido triggers/prompt/code                              |
| `rw_b_dir_arch_plan_v4_20250729.md`                   | Blueprint de directorios & mapping                                   |
| `rw_b_assets_classification_matrix_v1_20250729.md`    | Matriz 3D Origen×Etapa×Rol                                           |
| `chglog_main_rwb_v5_20250730_ACTIVO.md`               | Changelog principal consolidado (histórico completo, auto-contenido) |
| `mpln_master_plan_aingz_rw_b_v_20250730_v4_ACTIVO.md` | MasterPlan arquitectónico ACTIVO                                     |
| `onbrd_welcome_onboarding_gz_rw_b_v_20250725.md`      | Onboarding & flujos iniciales                                        |

---

## 📦 Estructura del repo (resumen DIR\_ARCH\_PLAN v4)

> **Referencia extendida**: ver `rw_b_dir_arch_plan_v4_20250729.md`.

```
/ (root)
├── WF/             # Workflows activos
├── DOC/            # Docs, blueprints, onboarding
├── KNS/            # Knowledge, learning, training, TL
├── AUDIT_LIGHT/    # Auditorías rápidas
├── SCR/            # Scripts globales y tools
├── DATA/           # Matrices y datasets
├── LOG/            # Logs y changelogs
├── BACKUP/         # Snapshots y BLN
├── PURGATORIO/     # Históricos/legacy
├── TMP/            # Scratchpad temporal
├── MIG/            # Outputs de migración literal
```

---

## 1. Propósito y contexto

Centraliza referencias, reglas y logs para operar el repo RwB bajo estándar **RwB v2+** con arquitectura blueprint **v4**.

## 2. Reglas y metodología de operación *(heredadas de v2)*

- Seguir glosario core y plantilla de naming.
- Utilizar DirArchPlan v4 y workflows activos.
- Registrar **todo** movimiento en changelog y logs de carpeta.
- Aplicar checklist de cobertura y QA antes de integrar.
- No borrar outputs legacy sin respaldo y log.

## 3. Instalación (sección preservada)

```bash
pip install -r requirements.txt
```

Paquetes opcionales: `py-cpuinfo`, `GPUtil`, `wmi`, `pywin32`.

## 4. Ejecución de pruebas

```bash
pip install pytest
pytest
```

## 5. Generar mapeo legacy

```bash
python scripts/mapping.py
```

## 6. Control inicial del repositorio

Revisa `WF_INICIO_REPO_CHECK` antes de cada sesión.

---

## ⚙️ Workflows y recomendaciones clave

- Dictado por voz, tuning y training IA → `/KNS/TL` o `/TMP`.
- Validar rutas con DirArchPlan v4 antes de mover/consolidar.
- Mantener changelog maestro (`chglog_main_rwb_v5_20250730_ACTIVO.md`) actualizado.

---

### Firma

> Gastón Zelechower · OpenAI o3 — Ruleset RWB Universal

---

**FIN README v5 ACTIVO**

