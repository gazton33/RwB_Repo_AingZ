# BACKUP — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Repositorio definitivo de backups consolidados.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]`
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]`

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** [../apps/], [../backup/], [../conectors/], [../core/], [../infra/], [../legacy/], [../log/], [../mig/], [../packages/], [../scripts/], [../tmp_staging/]
- **Buckets destino típicos:** `[../PURGATORIO/]`, `[../CORE/]`
- **Crossref central:** `[Mapa Global](../DOC/MPLN/crossref_global.md)`
- **Flujos/Pipelines relevantes:** `[../WF/pipeline_backup.md]`, `[../PIPELINES/pipeline_backup.md]`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
└── BACKUP/
```

## 4.1 Procedencia en el Árbol de Directorios
```text
BACKUP/
├── AI/
├── EXT/
└── INT/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
1. **Ingreso / LEGACY o TMP:** `[../WF/wf_ingreso_backup.md]`
2. **Staging / MIG:** `[../WF/wf_staging_backup.md]`
3. **Consolidación / CORE:** `[../WF/wf_consolidacion_backup.md]`
4. **Backup / Eliminación:** `[../WF/wf_backup_backup.md]`

---
Completar todos los campos con links activos una vez creada la estructura real.

