# RwB_WF_CONSOLIDACION_FILES_ACTIVOS_V1_20250725.md — Workflow específico para consolidación y actualización de archivos activos/finales

---

## 1. Objetivo y alcance
- Estandarizar la consolidación, control de versiones y actualización de todos los archivos activos/finales del repo AingZ/ChatGPT.
- Aplicar barrido literal, checklist exhaustivo, mapping incremental y logs/versionado en cada ciclo.
- Asegurar que cada archivo consolidado esté listo para integración viva, merge, upgrades IA/documental y tuning futuro.

---

## 2. Pipeline detallado de trabajo (iterativo)

### **A. Identificación y selección**
1. Seleccionar los archivos marcados como activos, finales o prioritarios para consolidación.
2. Si existen múltiples versiones, identificar la definitiva; si hay dudas, procesar ambas y resolver el merge.

### **B. Upload y tracking incremental**
1. Subir archivos uno por vez (ó en grupos pequeños para tracking óptimo).
2. Registrar nombre, versión, prioridad y cualquier observación relevante.

### **C. Barrido literal y checklist**
1. Procesar cada archivo con barrido literal: **no omitir datos, mantener referencias, versionar y documentar cambios**.
2. Aplicar checklist:
    - ¿Es versión final?
    - ¿Validada previamente en outputs/auditoría?
    - ¿Tiene referencias cruzadas, logs y versionado?
    - ¿Debe modularizarse/dividirse por tamaño o función?
3. Documentar toda manipulación, merge, ajuste de formato, naming o contenido.

### **D. Mapping incremental y consolidación**
1. Si el archivo es parte de un macro-lote, vincularlo a outputs/modulos relevantes.
2. Entregar el archivo consolidado como output listo para merge/documentación.
3. Marcar y proponer modularización si es necesario.

### **E. Logging, memoria viva y feedback**
1. Registrar logs de cambios y lessons en memoria viva tras cada ciclo.
2. Mantener checklist y estado de avance reflejado en el canvas/documentación incremental.
3. Actualizar el workflow en cada iteración según feedback, lessons o conflictos de versiones detectados.

---

## 3. Reglas clave y recomendaciones
- No borrar nada sin dejar referencia explícita (logs/versiones/backups).
- Versionar cada output/informe incrementalmente para trazabilidad absoluta.
- Entregar outputs uno por uno, en lotes pequeños o batch según preferencia del usuario.
- Modularizar archivos extensos o multifunción donde sea óptimo.

---

## 4. Ready para consolidación iterativa
- El workflow permite control estricto, reproducibilidad y tuning incremental de todos los archivos activos/finales del repo.
- Se actualiza en cada ciclo según feedback, cambios en el stack, o reglas de versionado/documentación.

---

