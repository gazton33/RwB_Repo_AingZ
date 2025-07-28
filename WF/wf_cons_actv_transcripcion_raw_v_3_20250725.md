# WF_CONS_ACTV_TRANSCRIPCION_RAW_V3_20250725.md — Workflow para consolidación de activos con transcripción literal/incremental (v3 - 2025-07-25)

---

## 1. Objetivo y alcance
- Garantizar la consolidación de archivos activos/finales del repo bajo la filosofía RwB RAW: **transcripción literal/incremental** y conservación absoluta de aprendizajes, feedback, ejemplos y lessons learned.
- Asegurar que cada archivo “activo” resulte 100% transferible, auditable y utilizable aún tras depurar históricos, sin pérdida de contenido clave.

---

## 2. Pipeline detallado actualizado (iterativo RAW)

### A. Identificación, selección y versionado
1. Seleccionar archivos activos o prioritarios. Si hay múltiples versiones/drafts, incluirlos todos para barrido y merge incremental.
2. Registrar nombre, versión, fuente y observaciones en logs, siempre versionar outputs incrementales.

### B. Barrido literal/incremental
1. Procesar cada archivo aplicando barrido **literal**: **transcribir** (copiar/pegar RAW, no resumir ni reinterpretar) los bloques de lessons, feedback, insights, trainlog, changelog, ejemplos y checklists internos de cada ciclo/histórico.
2. Todo feedback, ejemplo, learn, idea, snapshot o tabla debe ser transcript@ literal desde el original.
3. Si un bloque es redundante o existe en varias fuentes, integrar una sola vez pero siempre manteniendo el wording literal y referencia a la fuente/ciclo.
4. Modularizar sólo si el tamaño lo exige, pero nunca omitir data clave.

### C. Integración, mapping y checklist
1. El archivo “activo” final incluye todos los bloques transcriptos RAW, versionados y organizados por ciclo/fuente/tema.
2. Checklist canvas:
    - [x] Barrido RAW completado
    - [x] Lessons, feedback, ejemplos, tablas y snapshots transcriptos
    - [x] Checklist visible y versionado
    - [x] Ready para merge, feedback y purga históricos
3. Mapping incremental y referencia cruzada en README/logs, con enlaces a versiones previas y logs de cambio.

### D. Purga y backup
1. Los archivos históricos/drafts sólo se migran a backup/PURGATORIO tras validar que todo el contenido y aprendizaje están transcriptos en el archivo activo.
2. Todo purge/documentación queda logueada y referenciada en changelog incremental.

### E. Feedback, tuning y actualización iterativa
1. Tras cada ciclo, registrar feedback de usuario/revisión y lessons en logs de memoria viva.
2. Si se detecta omisión, retroceder y reintegrar los bloques/textos detectados.
3. El workflow se actualiza ante cada nuevo feedback de lessons/tuning, documentando siempre la mejora en changelog.

---

## 3. Reglas clave y recomendaciones
- Nunca resumir, reinterpretar o compactar el contenido de los archivos activos.
- Modularizar solo si es estrictamente necesario para el uso.
- Registrar toda transcripción y mapping incremental en logs, README y changelogs.
- Checklist canvas debe ser visible, auditable y validable en cada output.

---

## 4. Ready para consolidación incremental
- Solo tras validar el barrido RAW, checklist visible y mapping, puede declararse “activo” un archivo y purgar los históricos.
- El workflow es iterativo y mejora continuamente según lessons learned, tuning o feedback incremental del ciclo.

---

