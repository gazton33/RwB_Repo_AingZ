# [RwB] Macro Plan de Migración v2

Este documento resume las fases clave para migrar y normalizar todos los archivos legacy siguiendo la arquitectura RawBase. Se complementa con el `rw_b_plan_implementacion_v_3.md` y los archivos de auditoría INTEGRA.

## Fases principales
1. **Barrido y catálogo inicial**
   - Identificar y registrar todos los archivos legacy por contexto y dominio.
2. **Conversión al naming universal**
   - Aplicar la convención `RwB_[CTX][_GRP]_PRJ_[PROJECT]_[THREAD]_CAT_VER_STA_TAG.ext`.
3. **Migración a purgatorio**
   - Mover los archivos convertidos a `/purgatorio/` con log y tabla de correspondencia legacy→RwB.
4. **Revisión y ajuste**
   - Usar los templates de checkpoint y feedback para validar cobertura y reglas.
5. **Integración definitiva**
   - Tras la auditoría, mover los archivos a su carpeta final en `PR/`, `CO/` o `CL/` y actualizar los READMEs.

---
Este plan se irá actualizando conforme avance la implementación y se apliquen los aprendizajes del repositorio.
