# MIG — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Procesos y scripts de migración.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../legacy/], [../tmp_staging/]`
- **Referencias laterales:** [../core/], [../BACKUP/]
- **Buckets destino típicos:** [../core/], [../BACKUP/]
- **Crossref central:** `[Mapa Global](../../desarrollo/aingz_platform/crossref_mapping_buckets_aingz_platform_v_1_20250731.md)`
- **Flujos/Pipelines relevantes:** `-`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
└── mig/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso / LEGACY o TMP:** `[../WF/wf_ingreso_mig.md]`
2. **Staging / MIG:** `[../WF/wf_staging_mig.md]`
3. **Consolidación / CORE:** `[../WF/wf_consolidacion_mig.md]`
4. **Backup / Eliminación:** `[../WF/wf_backup_mig.md]`

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→BACKUP`.

---

Completar todos los campos con links activos una vez creada la estructura real.

