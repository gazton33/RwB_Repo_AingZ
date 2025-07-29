# 🏛️ [RwB] GLOSARIO CODE — v1 (CORE, actualizado 2025-07-25) ✨📚🚀

> Blueprint validado e incremental: integra assets, clases y tags nuevos surgidos del ciclo iterativo. Las diferencias respecto al ciclo anterior están resaltadas en **<span style="color:#E67E22">naranja</span>** para su validación. 📋🟧🔍

---

## 🔑 REGLAS GENERALES (RULESET) ⚙️💡

Este glosario establece la normativa y los códigos de naming universal utilizados en la arquitectura RwB. Es la referencia principal para cualquier desarrollo, mapping, consolidación o migración de assets dentro del stack. 

| `CODE` | **Name**             | Descripción                                                           | Jerarquía/Relación              |
| ------ | -------------------- | --------------------------------------------------------------------- | ------------------------------- |
| `RULE` | **Ruleset**          | Framework normativo, naming y compliance universal.                   | Raíz (stack normativo)          |
| `LITW` | **LiteralWork**      | Barrido, clasificación 100% objetiva, sin interpretación.             | Hermano de RULE                 |
| `RWB`  | **RawBase**          | Ruleset propio del sistema/proyecto, triggers y mapping.              | Hijo de RULE                    |
| `RWS`  | **RwB_Specific**     | Ruleset para proyecto/cliente/contexto específico.                    | Hijo de RWB                     |
| `CFG`  | **Configuration**    | Archivo y settings para modos y compliance.                           | Transversal                     |
| <span style="color:#E67E22">`PKG`</span> | <span style="color:#E67E22">**Package**</span> | <span style="color:#E67E22">Paquete de distribución de activos/versiones (ej: onboarding, templates, releases).</span> | <span style="color:#E67E22">Hermano de CFG</span> |

---

## 🏷️ IDENTIFICADORES Y NAMING 📂🔗

| `CODE` | **Name**       | Descripción                              | Precedencia/Relación      |
| ------ | ------------- | ---------------------------------------- | ------------------------- |
| `CTX`  | **Context**   | Dataset raíz, namespace, scope principal. | Universal/Global          |
| `LYR`  | **Layer**     | Capa lógica, nivel de aplicación.         | Universal/Multicapa       |
| `DOM`  | **Domain**    | Área funcional, disciplina o expertise.   | Dominio                   |
| `USC`  | **UserScope** | Privacidad/colaboración (PR, CO, CL).     | Transversal               |
| `MOD`  | **Module**    | Subsistema, bloque de funciones.          | Sub-dominio               |
| `CAT`  | **Category**  | Macroagrupador funcional/técnico.         | Familia funcional         |
| `TSK`  | **Task**      | Acción atómica ejecutable.                | Hoja/final                |
| `VER`  | **Version**   | Versionado incremental.                   | Transversal               |
| `STA`  | **State**     | Estado operativo (WIP, FINAL, etc.).      | Transversal               |
| `ID`   | **Identifier**| Identificador único.                      | Transversal               |
| `TRG`  | **Trigger**   | Disparador asociado a Category/Task.      | Vinculado a Cat/Task      |
| `TYP`  | **Type**      | Extensión de archivo, output o dato.      | Vinculado a Cat/Task      |
| `BK`   | **Backup**    | Respaldo de estados o snapshots críticos. | Universal                 |
| <span style="color:#E67E22">`ACTV`</span> | <span style="color:#E67E22">**ActiveAsset**</span> | <span style="color:#E67E22">Activo consolidado/vivo, output RAW actual, reemplaza a FINAL/DRAFT.</span> | <span style="color:#E67E22">Hermano transversal</span> |
| <span style="color:#E67E22">`PURG`</span> | <span style="color:#E67E22">**Purgatory**</span> | <span style="color:#E67E22">Directorio/estado temporal de históricos superados.</span> | <span style="color:#E67E22">Hermano transversal</span> |

---

## 🧩 INSTRUCCIONES Y CLASES DE PROCEDIMIENTO 📜🔑

| `CODE` | **Name**           | Descripción                                  | Jerarquía/Relación    |
| ------ | ------------------ | --------------------------------------------- | --------------------- |
| `INS`  | **InstructionSet** | Conjunto de instrucciones y buenas prácticas. | Raíz de ejecución     |
| `ENV`  | **EnvInstruction** | Instrucciones por entorno o capa.             | Hijo de INS           |
| `HIE`  | **HierInstruction**| Por jerarquía, capa o nivel.                  | Hermano de ENV        |
| `PRC`  | **ProcInstruction**| Para procesos, workflows y tareas.            | Hermano de ENV, WF    |
| <span style="color:#E67E22">`WK`</span> | <span style="color:#E67E22">**WorkflowKnowledge**</span> | <span style="color:#E67E22">Macro-workflow de aprendizaje, integración, logging y consolidación incremental.</span> | <span style="color:#E67E22">Hermano de WF</span> |

---

## 🛠️ WORKFLOW, PIPELINES Y CHECKLISTS 🔄🗂️

| `CODE`  | **Name**              | Descripción                                         | Precedencia/Relación    |
| ------- | --------------------- | --------------------------------------------------- | ----------------------- |
| `WF`    | **Workflow**          | Macro-pipeline, ciclo maestro transversal.          | Raíz/Padre             |
| `MPLN`  | **MasterPlan**        | Planificación maestra, blueprint global.            | Padre (bajo WF)        |
| `PLN`   | **Plan**              | Plan específico, cronograma, scheduling.            | Hijo de MPLN           |
| `RMAP`  | **Roadmap**           | Roadmap estratégico, milestones y etapas.           | Hijo de PLN/MPLN       |
| `CHK`   | **Checklist**         | Validación estructurada de pasos.                   | Hijo de PLN/RMAP       |
| `CHKP`  | **Checkpoint**        | Punto de control, cierre parcial, snapshot.         | Hijo de CHK/RMAP       |
| `REVP`  | **ReviewPending**     | Revisión manual, feedback iterativo.                | Hijo de CHK/RMAP       |
| `AUDT`  | **Audit**             | Auditoría integral, revisión y cierre.              | Hermano de CHK/RMAP    |
| `TMPLG` | **TemplateGenerator** | Generador automático de outputs o estructuras.      | Secundario, en WF      |
| `TUNG`  | **Tuning**            | Ajuste iterativo, mejoras y evolución.              | Secundario, transversal|
| `LSWP`  | **LiteralSweep**      | Barrido literal, sin interpretación.                | Secundario, cierre WF  |
| `VALD`  | **Validation**        | Validación técnica/final, testing lógico.           | Secundario, cierre     |
| `MIG`   | **Migration**         | Proceso/archivo de migración legacy/actualización.  | Hijo de WF             |
| `MAP`   | **Mapping**           | Mapeo, correspondencias, equivalencias.             | Secundario, en MIG     |
| `CLSS`  | **Classification**    | Organización por naming o familias.                 | Secundario, cierre     |
| `FBCK`  | **FeedbackEval**      | Evaluación/feedback estructurado.                   | Hermano de REVP        |
| `EVLS`  | **Evaluation**        | Evaluación global de outputs o performance.         | Hermano de AUDT        |
| `ONBG`  | **Onboarding**        | Inicialización del sistema o ciclo.                 | WF especial            |
| `TAGX`  | **ExtendedTag**       | Subtag específico (ej: IMG_DIAGRAM).                | Decorador transversal  |
| `RPT`   | **Report**            | Informe de resultados, salida consolidada.          | Hijo de cualquier WF   |
| `TST`   | **Test**              | Script/matriz de pruebas, validación automatizada.  | Output de VALD         |
| `QRY`   | **Query**             | Consulta declarativa, búsqueda avanzada.            | Proceso en MAP/MIG/WF  |
| `BLPR`  | **Blueprint**         | Blueprint estructural o diagrama de referencia.     | Hermano de MPLN, RMAP  |

---

## 🧠 CONOCIMIENTO Y MEMORIA VIVA 🔎📒

| `CODE`  | **Name**          | Descripción                             | Precedencia/Relación          |
| ------- | ----------------- | --------------------------------------- | ----------------------------- |
| `KNS`   | **Knowledge**     | Recopilación y síntesis de saberes.     | Raíz/Padre                    |
| `MEM`   | **ContextMemory** | Memoria viva/contextual.                | Hijo directo de KNS           |
| `NOTE`  | **Note**          | Notas rápidas, apuntes técnicos.        | Hermano de MEM, hijo de KNS   |
| `GLOS`  | **Glossary**      | Diccionario o glosario interno.         | Hermano de MEM/NOTE, hijo KNS |
| `PREF`  | **Preferences**   | Preferencias y configuraciones propias. | Hermano de MEM/NOTE/GLOS      |
| `LEARN` | **Learning**      | Aprendizajes y lecciones clave.         | Hermano de KNS, procesos      |
| `INSI`  | **Insight**       | Hallazgos o observaciones estratégicas. | Asociado a LEARN/KNS          |
| <span style="color:#E67E22">`BRAIN`</span> | <span style="color:#E67E22">**Brainstorm**</span> | <span style="color:#E67E22">Brainstorming registrado, baseline de ideas y experimentos.</span> | <span style="color:#E67E22">Hermano de INSI</span> |
| <span style="color:#E67E22">`IDEA`</span> | <span style="color:#E67E22">**IdeaDraft**</span> | <span style="color:#E67E22">Registro incremental de drafts de ideas, propuestas, prompts, experimentos de relevamiento.</span> | <span style="color:#E67E22">Hermano de INSI/BRAIN</span> |

---

## 📝 LOGS, TRAZABILIDAD Y AUDITORÍA 📈🧾

| `CODE` | **Name**        | Descripción                               | Precedencia/Relación       |
| ------ | -------------- | ----------------------------------------- | -------------------------- |
| `LOG`  | **Log**        | Registro cronológico de eventos y outputs.| Raíz/Padre                |
| `BIT`  | **Logbook**    | Bitácora extendida, registro detallado.   | Hijo de LOG               |
| `CHG`  | **Changelog**  | Historial de cambios/versiones.           | Hermano de LOG            |
| `TRC`  | **Trace**      | Trazabilidad, referencias cruzadas.       | Hermano de LOG/CHG        |
| `XRF`  | **CrossRef**   | Referencias cruzadas entre módulos.       | Hijo de TRC               |
| `ADT`  | **AuditLog**   | Auditoría como log estructural.           | Hermano de LOG/CHG        |

---

## 📖 DOCUMENTACIÓN Y ASSETS DE REFERENCIA 💾🗃️

| `CODE`  | **Name**         | Descripción                                         | Tipo de flujo         | Origen   | Precedencia/Relación             |
| ------- | ---------------- | --------------------------------------------------- | --------------------- | -------- | -------------------------------- |
| `DOC`   | **Documentation**| Documento técnico o referencia clave.               | -                     | Macro    | Invocable por cualquier WF/KNS   |
| `RDM`   | **Readme**       | Archivo principal para humanos y sistemas.           | Output/Template       | Oficial  | Enlaza RDM_H y RDM_AI            |
| `RDM_H` | **ReadmeHuman**  | README visual, onboarding y uso humano.              | Output/Template       | Oficial  | Anexo a RDM                      |
| `RDM_AI`| **ReadmeAI**     | Prompt/reglas para AI: triggers, taxonomía, meta.    | Input/Output/Template | Oficial  | Anexo a RDM                      |
| `TXT`   | **TextDoc**      | Documento textual, guía o especificación.            | Input/Output          | Oficial  | Base de integración              |
| `IMG`   | **ImageDoc**     | Imagen, diagrama o screenshot técnico.               | Input/Output          | Oficial  | Complemento visual               |
| `VID`   | **VideoDoc**     | Video, grabación o registro audiovisual.             | Input/Output          | Oficial  | Output o demo                    |
| `AUD`   | **AudioDoc**     | Audio, grabación o nota de voz.                      | Input/Output          | Oficial  | Output o feedback                |
| `LIB`   | **LibraryRef**   | Biblioteca oficial, manual o libro técnico.          | Input                 | Externa  | Fuente de consulta               |
| `PAP`   | **Paper/Article**| Paper científico o artículo técnico.                 | Input                 | Externa  | Referencia, cita                 |
| `OWN`   | **OwnDoc**       | Documento creado internamente (propio).              | Output                | Propio   | Puede migrar Output > Input      |
| `DRAFT` | **DraftDoc**     | Documento en desarrollo, editable.                   | Output                | Propio   | Flujo iterativo                  |
| `FINAL` | **FinalDoc**     | Documento final, validado y aprobado.                | Output/Input          | Propio   | Puede migrar Output > Input      |
| `NB`    | **Notebook**     | Documento interactivo (Jupyter, Colab, etc.).        | Output/Tool           | Propio   | Output/herramienta enriquecida   |
| `MD`    | **Markdown**     | Documento estructurado, legible por humanos.         | Input/Output/Template | Oficial  | Plantilla/output principal       |
| <span style="color:#E67E22">`RDM_P`</span> | <span style="color:#E67E22">**ReadmeProject**</span> | <span style="color:#E67E22">README específico de paquete/proyecto, onboarding externo, release, setup.</span> | <span style="color:#E67E22">Output/Template</span> | <span style="color:#E67E22">Oficial</span> | <span style="color:#E67E22">Enlaza RDM, glosario, assets externos</span> |

---

## 🖥️ SCRIPTS Y AUTOMATIZACIÓN 🔌📝

| `CODE` | **Name**              | Descripción                             | Subcategorías/Ejemplos     |
| ------ | --------------------- | --------------------------------------- | -------------------------- |
| `SCR`  | **Script**            | Archivo ejecutable o interpretable.     | Raíz de scripts            |
| `PIPE` | **PipelineScript**    | Script para pipelines de datos, ETL.    | Hijo de SCR                |
| `TSTSC`| **TestScript**        | Script de pruebas/unit test.            | Hermano de PIPE            |
| `INTG` | **IntegrationScript** | Script de integración y automatización. | Hermano de PIPE            |
| `PRCSC`| **ProcessingScript**  | Script de procesamiento de datos.       | Hermano de PIPE            |
| `CMD`  | **CommandScript**     | Script de comandos/shell.               | Hermano de PIPE            |

---

## 🟧 MATRICES, TABLAS Y ESTRUCTURAS TABULARES 📊🧮

| `CODE` | **Name**            | Descripción                                   | Subcategorías/Ejemplos     |
| ------ | ------------------- | --------------------------------------------- | -------------------------- |
| `MTR`  | **Matrix**          | Estructura tabular, DataFrame, tabla.         | Raíz de matrices           |
| `MAPX` | **MappingMatrix**   | Matriz de correspondencias/mappings.          | Hijo de MTR                |
| `REL`  | **RelationMatrix**  | Matriz de relaciones o correlaciones.         | Hermano de MAPX            |
| `INM`  | **InputMatrix**     | Matriz de entrada/datos.                      | Hermano de MAPX/REL        |
| `OUTM` | **OutputMatrix**    | Matriz de salida/resultados.                  | Hermano de MAPX/REL/INM    |
| `VALM` | **ValidationMatrix**| Matriz de validación o QA.                    | Hermano de MAPX/REL        |
| `VRS`  | **VersusMatrix**    | Matriz comparativa tipo “versus

