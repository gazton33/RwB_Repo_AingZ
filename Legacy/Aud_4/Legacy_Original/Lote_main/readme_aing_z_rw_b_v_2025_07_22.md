# Repositorio AingZ — Infraestructura RwB

Este repositorio centraliza la reorganización de todos los archivos históricos bajo el estándar **RawBase (RwB)**. La carpeta `Legacy/` conserva el material original y `universal/` es el entorno activo para pruebas y workflows.

---

## Directorios principales

- `Legacy/` — Histórico completo pendiente de depuración y migración incremental (no debe borrarse ni sobrescribirse durante ningún proceso).
- `universal/` — Entorno unificado para ejemplos, templates y conocimiento.
- `backup/` — Almacén temporal de archivos migrados desde `Legacy/` (referenciado siempre en los logs de registro incremental).
- `docs/` — Documentación central (reglas, planes, glosario y checklists). Consultar `docs/checklists/checklist_clases_archivos.md` para categorías y definición de clases.
- `Legacy_RwB_Cons/` — **Nuevo** staging/documental de outputs RAW incrementales (consolidados de logs, changelogs, registros de trazabilidad, checklists y actas de ciclo). Aquí se almacenan **todos los bloques de registro incremental** antes de su consolidación manual.

---

## Documentación y registros clave

- [Glosario y naming universal](docs/glosario/RwB_Glosario_vFinal.md)
- [Reglas RawBase y trazabilidad](docs/rules/README_reglas_raw_base.md)
- [Registro de trazabilidad total (incremental)](Legacy_RwB_Cons/registro_trazabilidad_total.md)
- [Changelog incremental](Legacy_RwB_Cons/changelog.md)
- [Checklist de incongruencias incremental](Legacy_RwB_Cons/checklist_incongruencias.md)
- [Roadmap y línea de base](docs/plans/baseline_roadmap.md)
- [Procedimiento de migración y depuración](docs/procedimiento_migracion.md)

**Todos los registros incrementales generados por procesos de migración deben integrarse manualmente al registro histórico principal cuando se decida el cierre total.**

---

## Instrucciones para consolidación y auditoría (usando ChatGPT/Codex y scripts)

### 1. Procedimiento general de migración y auditoría

- La **migración incremental** se realiza por clase de archivo (ver checklist de clases). Para cada ciclo:
  1. Ejecutar un barrido literal de la clase en Legacy/ usando el checklist como referencia.
  2. Registrar mapeo y cambios como bloque RAW incremental (nunca reemplazar ni sobrescribir históricos).
  3. Mover los archivos migrados a backup/ solo tras documentar el ciclo en los registros.
  4. Agregar la entrada correspondiente en los registros incrementales (trazabilidad, changelog, checklist).
  5. Sumar los archivos RAW incrementales a Legacy\_RwB\_Cons/ hasta la consolidación global manual.

### 2. Auditoría profunda de Legacy/

- Para una **auditoría detallada y exhaustiva** con Codex o ChatGPT:
  - Recorrer el 100% de los archivos y subcarpetas de Legacy/.
  - Clasificar cada archivo según las clases y criterios de `checklist_clases_archivos.md`.
  - Verificar duplicidades, inconsistencias, archivos huérfanos o pendientes de ciclo.
  - Registrar cada hallazgo como bloque incremental en Legacy\_RwB\_Cons/.
  - Producir un **nuevo checklist global actualizado**, con todos los archivos clasificados y pendientes de analizar, que pueda ser utilizado para nuevas migraciones iterativas o para consulta rápida en auditorías.
  - El checklist generado debe incluir: nombre, ruta, clase, status (migrado/pending/obsoleto/duplicado/etc.), observaciones y referencia cruzada a los registros incrementales.

---

## Recomendaciones de uso y control

- Nunca sobrescribir, borrar o fusionar registros históricos automáticamente.
- Sumar siempre los bloques RAW incrementales como nuevos documentos o secciones en Legacy\_RwB\_Cons/.
- Solo consolidar los registros y logs globalmente al cierre final de la migración/auditoría.
- Cualquier acción debe dejar referencia cruzada en todos los registros relevantes (trazabilidad, changelog, checklist, actas de ciclo, outputs de clase, etc.).

---

## Scripts y automatización

- Usar `scripts/mapping.py` para generar tablas de correspondencia entre Legacy/ y destino, y para alimentar los registros incrementales:
  ```bash
  python scripts/mapping.py [carpeta] --output Legacy_RwB_Cons/registro_trazabilidad_total.md
  ```
- Para nuevos ciclos, repetir el workflow para cada clase siguiendo el checklist, y sumar el output a Legacy\_RwB\_Cons/ antes de consolidar.
- Ejecutar `scripts/generate_globalchecklist_main.py` tras cada ciclo para actualizar `Legacy_RwB_Cons/globalchecklist_main.md`.

---

## Ejemplo de entrada en checklist global generado por auditoría

| Archivo        | Ruta Legacy                           | Clase | Status    | Observaciones                | Referencia Registro |
| -------------- | ------------------------------------- | ----- | --------- | ---------------------------- | ------------------- |
| logs\_demo.log | Legacy/PR/projects/DataAIEng/logs/    | LOG   | Migrado   | Consolidado                  | LOG\_v1d1\_RAW\.md  |
| class\_scan.py | Legacy/PR/projects/DataAIEng/scripts/ | SCR   | Eliminado | Superado por versión en main | changelog.md        |
| ...            | ...                                   | ...   | ...       | ...                          | ...                 |

---

## Licencia

Este proyecto se publica bajo la licencia [MIT](LICENSE).

