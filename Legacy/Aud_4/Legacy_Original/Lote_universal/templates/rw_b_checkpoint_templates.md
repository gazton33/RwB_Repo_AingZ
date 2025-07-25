# [RwB] CHECKPOINT TEMPLATES — Auditoría, Migración y Cierre

> Plantillas para generar todos los archivos y outputs requeridos para un cierre/auditoría completa, migración a purgatorio, y aseguramiento de trazabilidad, según estándar RwB-RAWBASE.

---

## 1. Template de documento de cierre/ciclo

**Título:**

```
[RwB] CHECKPOINT CIERRE — [Ciclo/Proyecto/Fecha]
```

**Contenido mínimo:**

- Objetivo y alcance del cierre.
- Fecha, responsables, prompts base y ciclo de origen.
- Listado de TODOS los archivos generados, migrados o auditados (nombre legacy, nombre RwB, categoría, contexto, dominio, ubicación).
- Mapping (tabla csv o markdown): nombre y ruta legacy → nombre y ruta nueva.
- Principales aprendizajes, feedback, reglas y coverage.
- Referencias a glosario, macroplan, changelog, logs y matrices relevantes.
- Pendientes y recomendaciones para integración.

---

## 2. Template de inventario y mapping de archivos

**Ejemplo CSV o Markdown:**

| Archivo Legacy                     | Archivo RwB universal                                      | Categoría | Contexto | Dominio   | Ubicación final               |
| ---------------------------------- | ---------------------------------------------------------- | --------- | -------- | --------- | ----------------------------- |
| legacy/knowledge/knowledge1.md     | RwB\_PR\_DataAIEng\_KNS\_v1d1\_WIP\_knowledge1.md          | KNS       | PR       | DataAIEng | /purgatorio/PR/DataAIEng/KNS/ |
| legacy/scripts/auto\_backup.py     | RwB\_PR\_DataAIEng\_SCR\_v1d1\_WIP\_auto\_backup.py        | SCR       | PR       | DataAIEng | /purgatorio/PR/DataAIEng/SCR/ |
| legacy/docs/readme\_integracion.md | RwB\_PR\_DataAIEng\_DOC\_v1d1\_WIP\_readme\_integracion.md | DOC       | PR       | DataAIEng | /purgatorio/PR/DataAIEng/DOC/ |

---

## 3. Template de README o archivo de revisión para carpeta de purgatorio

```
# [RwB] REVISION PENDIENTE — [Fecha, Contexto, Dominio, Ciclo]
- Grupo/Equipo: [si aplica]
- Fuente (repo, ciclo, chat): [indicar]
- Fecha de migración: [YYYY-MM-DD HH:MM]

**IMPORTANTE:** Todos los archivos de esta carpeta requieren análisis, clasificación y adaptación final.
- Revisar mapping, actualizar referencias y ubicar outputs definitivos en la infraestructura funcional.
- Ver log de migración y mapping legacy→RwB.
- Pendientes:
    - [ ] ¿Está todo inventariado?
    - [ ] ¿Hay duplicados a fusionar?
    - [ ] ¿Se actualizaron todos los nombres en sistemas/documentos externos?
    - [ ] ¿Hay archivos con información cruzada entre proyectos/contextos?
    - [ ] ¿Se integraron todos los aprendizajes relevantes al knowledge base global?
```

---

## 4. Template de log/changelog para auditoría

```
# [RwB] CHANGELOG / LOG DE MIGRACION
- Fecha: [YYYY-MM-DD HH:MM]
- Ejecutado por: [usuario/script]
- Resumen:
    - Archivos migrados:
    - Duplicados encontrados:
    - Errores:
    - Mapping legacy→RwB:
- Observaciones/pending feedback:
    - ...
```

---

> Usar y versionar estos templates en cada ciclo/hilo/proyecto relevante. Adjuntar como outputs de auditoría y migración en `/purgatorio/`. Siempre referenciar el glosario y macroplan vigente.

