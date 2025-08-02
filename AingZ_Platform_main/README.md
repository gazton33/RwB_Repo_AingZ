# AingZ_Platform_main — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Bucket raíz que organiza los módulos principales de la plataforma.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `-`
- **Referencias laterales:** `[./apps/]`, `[./core/]`, `[./infra/]`, `[./legacy/]`, `[./mig/]`, `[./tmp_staging/]`, `[./BACKUP/]`, `[./backup/]`, `[./log/]`, `[./packages/]`, `[./conectors/]`
- **Buckets destino típicos:** `-`
- **Crossref central:** `[Mapa Global](../desarrollo/aingz_platform/crossref_mapping_buckets_aingz_platform_v_1_20250731.md)`
- **Flujos/Pipelines relevantes:** `-`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso / LEGACY o TMP:** `[../WF/wf_ingreso_AingZ_Platform_main.md]`
2. **Staging / MIG:** `[../WF/wf_staging_AingZ_Platform_main.md]`
3. **Consolidación / CORE:** `[../WF/wf_consolidacion_AingZ_Platform_main.md]`
4. **Backup / Eliminación:** `[../WF/wf_backup_AingZ_Platform_main.md]`

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→BACKUP`.

---

Completar todos los campos con links activos una vez creada la estructura real.

