# RwB_WF_CONSOLIDACION_FILES_ACTIVOS_V2_20250725.md — Workflow específico para consolidación y actualización de archivos activos/finales (versión actualizada)

---

## 1. Objetivo y alcance
- Estandarizar la consolidación, control de versiones y actualización de todos los archivos activos/finales del repo AingZ/ChatGPT.
- Aplicar barrido literal, checklist exhaustivo, mapping incremental y logs/versionado en cada ciclo.
- Asegurar que cada archivo consolidado esté listo para integración viva, merge, upgrades IA/documental y tuning futuro.

---

## 2. Pipeline detallado de trabajo (iterativo)

### **A. Ejecución sobre archivos en main**
1. Trabajar sobre el directorio principal (sin subcarpetas salvo indicación explícita).

### **B. Glosario y naming**
1. Validar naming, estructura y referencias de todos los archivos activos respecto al glosario y reglas RwB.

### **C. Mapping general del repo**
1. Mapear archivos activos vs. estructura total, dependencias y outputs previos para asegurar cobertura.

### **D. Nuevos archivos**
1. Crear directorio temporal para almacenar archivos nuevos/pending entre ciclos de consolidación.
2. Mantener versionado incremental hasta integración definitiva.

### **E. Changelog y trazabilidad**
1. Registrar toda modificación, consolidación, naming, división o merge en changelog incremental y logs de memoria viva.

### **F. Eliminación/purga de archivos temporales/superados**
1. Sólo tras validar cobertura, versionado y backup.
2. Documentar toda purga/eliminación en logs y changelog.

### **G. Feedback, cierre de ciclo y update del workflow**
1. Tras cada ciclo, generar feedback sobre barrido, glosario y mapping.
2. Actualizar el workflow según lessons learned, cambios o conflictos detectados.

---

## 3. Checklist operativo (por cada ciclo):
- ¿Se aplicó el pipeline a todos los activos en main?
- ¿Naming y glosario actualizados?
- ¿Mapping de dependencias y outputs actualizado?
- ¿Nuevos archivos versionados y registrados en directorio temporal?
- ¿Changelog y logs reflejan todas las acciones?
- ¿Archivos purgados sólo tras backup/validación?
- ¿Workflow actualizado según feedback/lessons?

---

## 4. Reglas clave y recomendaciones
- No borrar nada sin dejar referencia explícita (logs/versiones/backups).
- Versionar cada output/informe incrementalmente para trazabilidad absoluta.
- Entregar outputs uno por uno, en lotes pequeños o batch según preferencia del usuario.
- Modularizar archivos extensos o multifunción donde sea óptimo.

---

## 5. Ready para consolidación iterativa
- El workflow permite control estricto, reproducibilidad y tuning incremental de todos los archivos activos/finales del repo.
- Se actualiza en cada ciclo según feedback, cambios en el stack, o reglas de versionado/documentación.

---

