# README — RwB Repo Main (v4, 2025-07-29)

> **Esta versión incorpora referencias cruzadas y mapeo directo a todos los nuevos archivos blueprint generados en la última iteración (Glosario CODE v2, Diccionario CODE\_TRIGGERS v2, DIR\_ARCH\_PLAN v4, Matrix v1).** **Arquitectura alineada a OpenAI 4.1+, dictado y workflows iterativos multi-asset.**

---

## 🔑 Navegación rápida (index de assets blueprint)

| Archivo                                            | Propósito principal                                              |
| -------------------------------------------------- | ---------------------------------------------------------------- |
| `rw_b_glosario_code_v_2_20250729.md`               | Glosario maestro: jerarquía, naming, assets, roles, features     |
| `rw_b_diccionario_code_triggers_v_2_20250729.md`   | Diccionario rápido de triggers/prompt/code, referencia IA/README |
| `rw_b_dir_arch_plan_v4_20250729.md`                | Blueprint de directorios, mapping assets, integración Matrix     |
| `rw_b_assets_classification_matrix_v1_20250729.md` | Matriz 3D de clasificación Origen×Etapa×Rol                      |
| `chglog_main_rwb_20250725_v_2.md`                  | Changelog principal del repo                                     |
| `mpln_master_plan_aingz_rw_b_v_20250725_v_2.md`    | Master plan arquitectónico y evolución de features               |
| `onbrd_welcome_onboarding_gz_rw_b_v_20250725.md`   | Onboarding, guía rápida y flujos iniciales                       |

---

## 📦 Estructura del repo (resumen actualizado)

Ver `rw_b_dir_arch_plan_v4_20250729.md` para referencia extendida.

```
/ (root)
├── WF/             # Workflows activos (bajo DIR_ARCH_PLAN v4)
├── DOC/            # Docs, blueprints, onboarding
├── KNS/            # Knowledge, learning, training, TL
├── AUDIT_LIGHT/    # Auditorías rápidas, feedback, referencias
├── SCR/            # Scripts globales y tools
├── DATA/           # Matrices y datasets
├── LOG/            # Logs y changelogs
├── BACKUP/         # Snapshots y BLN
├── PURGATORIO/     # Obsoletos/legacy
├── TMP/            # Scratchpad, temp, procesamiento previo
├── MIG/            # Outputs de migración literal
```

---

## 🗂️ Archivos clave y referencia cruzada

- **Glosario**: [Glosario CODE v2](rw_b_glosario_code_v_2_20250729.md)
- **Diccionario**: [Diccionario CODE\_TRIGGERS v2](rw_b_diccionario_code_triggers_v_2_20250729.md)
- **DirArchPlan**: [DIR\_ARCH\_PLAN v4](rw_b_dir_arch_plan_v4_20250729.md)
- **Matrix**: [Assets Classification Matrix v1](rw_b_assets_classification_matrix_v1_20250729.md)
- **Master Plan**: [MPLN MasterPlan](mpln_master_plan_aingz_rw_b_v_20250725_v_2.md)
- **Changelog**: [CHGLOG\_MAIN](chglog_main_rwb_20250725_v_2.md)
- **Onboarding**: [ONBRD\_WELCOME](onbrd_welcome_onboarding_gz_rw_b_v_20250725.md)

---

## ⚙️ Workflows y recomendaciones

- Utiliza los workflows activos definidos en `/WF` y referenciados en los blueprints.
- Para dictado por voz, tuning, training IA o feedback, comienza siempre por `/KNS/TL` o `/TMP`.
- Revisa las instrucciones y el mapping en DirArchPlan v4 antes de crear nuevos buckets, mover o consolidar assets.
- Todos los cambios relevantes (nuevos roles, buckets, procedimientos) deben registrarse en `chglog_main_rwb_20250725_v_2.md`.

---

### Firma

> Gastón Zelechower · OpenAI o3 — Ruleset RWB Universal

---

**FIN README v4**

