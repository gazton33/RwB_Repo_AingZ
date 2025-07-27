# README_Legacy_RwB_v1_20250725.md — Manual e instrucciones para auditoría y consolidación de Legacy (AingZ/ChatGPT)

---

## 1. Propósito y alcance
Este README guía el proceso de relevamiento, auditoría y consolidación de la carpeta **Legacy** del proyecto AingZ/ChatGPT, integrando outputs de auditoría, mapping y legacy original.
Incluye instrucciones, referencias, reglas y rutinas recomendadas para trabajo manual o automatizado (Codex, LLM, scripts).

---

## 2. Estructura de la carpeta Legacy
- **/legacy/original/**: Archivos originales sin modificar
- **/legacy/auditoria/**: Outputs de auditoría, mapping, lessons, checklists
- **/legacy/resumenes/**: Mappings globales, insights, matrices de coverage y dependencias
- **/legacy/consolidado/**: Outputs finales para merge, upgrades o integración en el stack vivo

---

## 3. Instrucciones generales de uso

### A. Relevamiento inicial
- Leer y mapear el 100% de los archivos legacy y outputs de auditoría disponibles.
- Usar el **workflow RwB_WF_AUDITORIA_LEGACY_V3** como blueprint obligatorio (ver instrucciones adjuntas).

### B. Auditoría y análisis incremental
- Procesar cada archivo legacy aplicando el workflow v3: checklist de cobertura, mapping a outputs existentes, comparación contra legacy original.
- Generar y registrar insights, dependencias, gaps y lessons learned por cada macro-lote o tema.
- Mantener versiones y logs automáticos en cada ciclo.

### C. Consolidación y organización
- Organizar outputs y archivos por tema/familia (workflows, matrices, templates, KNS, inventarios, perfiles, blueprints).
- Usar matrices de dependencias para documentar relaciones y coverage, asegurando trazabilidad y reproducibilidad total.

### D. Backup y seguridad
- No borrar legacy original ni outputs históricos hasta la validación completa del mapping y consolidación.
- Mantener backups y logs de eventos críticos en memoria viva o sistema seguro.

---

## 4. Referencias y rutinas Codex/IA
- Referenciar siempre el workflow actualizado, mapping global y matrices de coverage en cada ciclo de auditoría.
- Relevar insights importantes y resumen de cada archivo de auditoría, generando un índice temático y reporte incremental de lessons learned.
- Para modelos Codex/LLM: procesar por bloques, priorizar outputs de mapping y resúmenes, validar insights y dependencias antes de merge o integración masiva.

---

## 5. Checklist visual-friendly para cada archivo
- ¿Está versionado y registrado el mapping/insight del archivo?
- ¿Existe cobertura y mapping contra legacy original?
- ¿Quedaron documentadas dependencias y relaciones en matrices globales?
- ¿El output es reproducible, modular y autoexplicativo?
- ¿Se actualizaron logs/lessons/feedback para trazabilidad y tuning IA?

---

## 6. Ready para consolidación incremental
El README y el workflow v3 permiten analizar, mapear, organizar y consolidar toda la carpeta Legacy para futuras integraciones, upgrades o migraciones IA/documental.

---

## 7. Archivos de auditoría y mapping
Los reportes generados por Codex se encuentran en la raíz de `AUDT`:

- `audit_mapping.csv` – tabla con la categoría del glosario y título de cada auditoría.
- `audit_insights.json` – listado de insights clave por archivo.
- `audit_summary.json` – índice resumido con la misma información.
- `auditoria_consolidacion_propuesta_20250725.md` – propuesta de consolidación y árbol de directorios.

Todos estos archivos fueron movidos desde el directorio principal a `AUDT/` para mantener centralizada la documentación de auditoría.

