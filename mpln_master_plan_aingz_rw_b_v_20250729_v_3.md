# 🏗️ MPLN_MASTER_PLAN_AINGZ_RW_B — v3 (2025-07-29)
> **Blueprint arquitectónico y hoja de ruta maestra** del repo RwB.  
> Esta versión integra la reorganización por matrices, blueprint de directorios, workflows iterativos y clasificación de assets en ciclo de vida.
> **Referenciado obligatoriamente en README, DirArchPlan v4, Changelog, Glosario v2 y Matrix v1.**

---

## 🔝 Pilares de la evolución actual (v3)
1. **Alineación absoluta a blueprint de directorios**: todos los activos deben estar ubicados y nombrados según [DIR_ARCH_PLAN v4](rw_b_dir_arch_plan_v4_20250729.md).
2. **Glosario y Diccionario CODE v2**: máxima jerarquía en naming, roles, features IA y prompts.
3. **Matriz de clasificación de assets**: codificación `SRC·STG·ROLE` y rutas de consolidación.
4. **Buckets y workflows nuevos**: `/KNS/TL`, `/AUDIT_LIGHT`, `/TMP`, `/MIG`, `/PURGATORIO/LEGACY`, dictado por voz, training/tuning IA y migración literal.
5. **Feedback IA, voice dictation, training**: outputs de cada iteración se consolidan en workflows, siguiendo ciclo de vida documentado.

---

## 📅 Roadmap resumido
| Fase | Hito | Output clave | Bucket/dir destino | Fecha |
|------|------|-------------|-------------------|-------|
| 1    | Reorganización directorios y assets | Blueprint DirArchPlan v4 | `/` | 2025-07-29 |
| 2    | Glosario v2, Diccionario v2 | Naming y triggers final | `/KNS`, `/DOC` | 2025-07-29 |
| 3    | Matrix v1 | Código compuesto, QA procesos | `/KNS` | 2025-07-29 |
| 4    | Workflows dictado/auditoría/migración | Procedimientos y scripts | `/WF` | 2025-07-29 |
| 5    | Integración de training IA | Outputs TL, retroalimentación | `/KNS/TL`, `/TMP` | Q3 2025 |
| 6    | Consolidación legacy y migraciones | Nuevos ACTV migrados | `/MIG`, `/PURGATORIO` | Q3 2025 |

---

## 🗂️ Integración y dependencias
- Todos los cambios y nuevos buckets deben referenciarse en [CHGLOG_MAIN_RWB v4](chglog_main_rwb_v4_20250729.md).
- El onboarding inicial y workflows activos residen en `/DOC/ONBRD/` y `/WF/`.
- Los procedimientos de consolidación, migración y auditoría se ejecutan secuencialmente según Matrix v1.

---

## 🔄 Procedimientos clave
- **Para cada nuevo asset**: determinar `SRC·STG·ROLE` y ubicarlo según DirArchPlan v4.
- **Relevamientos**: outputs RAW en `/KNS`, análisis en `/AUDIT_LIGHT`, migración consolidada en `/MIG`.
- **Auditorías**: outputs livianos en `/AUDIT_LIGHT`, cierre y registros en `/LOG/AUDT`.
- **Entrenamiento IA / Dictado**: resultados en `/KNS/TL` y `/TMP`, ciclos de retroalimentación IA con consolidación periódica.

---

## 📝 Referencias y enlaces clave
- [Glosario CODE v2](rw_b_glosario_code_v_2_20250729.md)
- [Diccionario CODE_TRIGGERS v2](rw_b_diccionario_code_triggers_v_2_20250729.md)
- [DIR_ARCH_PLAN v4](rw_b_dir_arch_plan_v4_20250729.md)
- [Assets Classification Matrix v1](rw_b_assets_classification_matrix_v1_20250729.md)
- [CHGLOG_MAIN_RWB v4](chglog_main_rwb_v4_20250729.md)
- [ONBRD_WELCOME](onbrd_welcome_onboarding_gz_rw_b_v_20250725.md)

---

### Firma
> Gastón Zelechower · OpenAI o3 — Ruleset RWB Universal

---

**FIN MPLN_MASTER_PLAN_AINGZ_RW_B v3**

