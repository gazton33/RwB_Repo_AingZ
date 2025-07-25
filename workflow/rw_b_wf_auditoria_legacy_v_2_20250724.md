# RwB_WF_AUDITORIA_LEGACY_v2_20250724.md — Workflow de auditoría legacy (versión 2, post-feedback ciclo lote 1)

---

## 1. Propósito
Implementar las lecciones aprendidas del ciclo piloto y asegurar una auditoría legacy expansiva, estructurada y trazable, adaptada a futuras migraciones y consolidaciones globales.

---

## 2. Principios
- Priorizar outputs estructurales/plantillas en las fases intermedias, manteniendo referencias vivas y trazabilidad a todos los datos originales.
- Agregar snapshots visuales o extractos literales solo cuando la estructura legacy lo justifique (matrices/tablas/diagramas complejos).
- Modularizar la auditoría por lotes, versionando los backups y outputs en carpetas separadas.
- Dejar registro detallado de lessons learned, feedback y tuning en memoria viva tras cada lote.

---

## 3. Pasos del procedimiento

1. **Barrido selectivo y mapeo estructural**
   - Extraer bloques, reglas y referencias clave.
   - Si corresponde, agregar “snapshot visual” o ejemplo literal de matriz/tablas.
   - Mapear cada ítem a glosario, estructura, tipología y carpeta sugerida.

2. **Auditoría y consolidación estructural**
   - Generar outputs guía con estructura, checklist y referencias cruzadas.
   - Si hay redundancia entre archivos legacy, consolidar en un único output.
   - Guardar todos los archivos originales y de auditoría en carpetas distintas.

3. **Feedback, lessons learned y memoria viva**
   - Registrar cada mejora en LEARN/INSI/TRNLOG/CHGLOG.
   - Enriquecer cada output con feedback inmediato, lessons learned y rutas de referencia para integración futura.

4. **Preparación para integración global**
   - Marcar, en cada consolidado, los bloques/cruces que requieren validación directa con legacy para la migración final.
   - Listar en la sección de referencias todos los archivos y lotes relacionados.

---

## 4. Checklist de cumplimiento (v2)
- Barrido selectivo ejecutado
- Snapshot visual/literal cuando corresponda
- Checklist y referencias cruzadas completas
- Lessons learned y feedback registrados
- Outputs, auditorías y legacy en carpetas separadas
- Actualización de memoria viva tras cada lote

---

## 5. Ejemplo de estructura de carpetas sugerida
- LEGACY/ORIGINAL/
- AUDITORIAS/
- CONSOLIDADOS/
- LEGACY/ARCHIVE/ (cuando corresponda)

---

## 6. Observaciones finales
- No eliminar ni comprimir legacy original hasta la migración global final.
- El workflow v2 debe adaptarse y enriquecerse en cada ciclo de retroalimentación.
- Registrar lessons learned globales en KNS_CTX al cierre del hilo.

---

