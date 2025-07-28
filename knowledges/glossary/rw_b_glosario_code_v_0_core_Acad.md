# [RwB] GLOSARIO CODE — v0 (CORE, Resumen Académico)

> Este blueprint sintetiza los principios y estructuras fundamentales del stack RwB, en un formato conciso diseñado para referencia rápida, consulta técnica y crecimiento modular. La información aquí se ha adaptado a un nivel de lectura universitario para estudiantes especializadas/os en arquitectura de sistemas, ingeniería de software, documentación técnica o áreas afines.

---

## Ruleset
| `CODE` | **Name**             | Descripción                                                                                           | Jerarquía/Relación              |
| ------ | -------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------- |
| `RULE` | **Ruleset**          | Marco normativo que define los lineamientos, convenciones de nomenclatura, triggers y compliance.     | Base de gobernanza (raíz)       |
| `LITW` | **LiteralWork**      | Barrido y clasificación de información sin interpretación. Clave para garantizar trazabilidad.        | Hermano de RULE                 |
| `RWB`  | **RawBase**          | Conjunto de reglas particularizadas para cada proyecto o sistema. Controla integración y naming.      | Hijo de RULE                    |
| `RWS`  | **RwB_Specific**     | Adaptación de reglas para un dominio, cliente o proyecto concreto. Permite especialización.           | Hijo de RWB                     |
| `CFG`  | **Configuration**    | Archivo y parámetros para definir modos de operación, variables de entorno y compliance técnica.      | Relación transversal            |

---

## Identificadores y Naming
| `CODE` | **Name**       | Descripción                                                                                        | Precedencia/Relación      |
| ------ | ------------- | -------------------------------------------------------------------------------------------------- | ------------------------- |
| `CTX`  | **Context**   | Espacio raíz o namespace de los datos, determina el entorno de ejecución y sus límites.            | Universal/Global          |
| `LYR`  | **Layer**     | Nivel o capa lógica dentro de la arquitectura del sistema (aplicación, datos, infraestructura).    | Universal/Multicapa       |
| `DOM`  | **Domain**    | Dominio funcional o disciplina experta, ubica los objetos y procesos en su contexto temático.      | Dominio                   |
| `USC`  | **UserScope** | Grado de acceso: privado, colaborativo, abierto. Identifica políticas de privacidad o colaboración.| Relación transversal      |
| `MOD`  | **Module**    | Subconjunto funcional o bloque lógico-técnico. Permite estructurar y escalar el sistema.           | Sub-dominio               |
| `CAT`  | **Category**  | Macrogrupo funcional. Agrupa módulos, workflows o tareas bajo una función común.                  | Familia funcional         |
| `TSK`  | **Task**      | Unidad atómica de ejecución o función individual dentro de un proceso o workflow.                  | Nodo hoja/final           |
| `VER`  | **Version**   | Identificador de release y cambios incrementales, clave para trazabilidad y control.               | Relación transversal      |
| `STA`  | **State**     | Estado de ciclo de vida (borrador, final, archivado).                                              | Relación transversal      |
| `ID`   | **Identifier**| Identificador único (global/local) para indexación y referencias cruzadas.                        | Relación transversal      |
| `TRG`  | **Trigger**   | Disparador asociado a tareas o categorías, inicia eventos o flujos según reglas definidas.        | Vinculado a Cat/Task      |
| `TYP`  | **Type**      | Tipo o formato de archivo/output. Facilita integración y parsing automatizado.                    | Vinculado a Cat/Task      |
| `BK`   | **Backup**    | Archivo de respaldo y snapshots. Esencial para recuperación y versionado seguro.                  | Universal                 |

---

## Instrucciones
| `CODE` | **Name**           | Descripción                                                                                    | Jerarquía/Relación    |
| ------ | ------------------ | ---------------------------------------------------------------------------------------------- | --------------------- |
| `INS`  | **InstructionSet** | Colección de instrucciones, lineamientos y buenas prácticas para operaciones y desarrollo.      | Raíz de ejecución     |
| `ENV`  | **EnvInstruction** | Instrucciones adaptadas a cada entorno o capa tecnológica, asegura compatibilidad.              | Hijo de INS           |
| `HIE`  | **HierInstruction**| Reglas aplicables a diferentes niveles de profundidad o jerarquía en la arquitectura.          | Hermano de ENV        |
| `PRC`  | **ProcInstruction**| Protocolos detallados para workflows, procesos o tareas repetitivas en desarrollo y gestión.   | Hermano de ENV, WF    |

---

## Workflow
| `CODE`  | **Name**              | Descripción                                                                                        | Precedencia/Relación    |
| ------- | --------------------- | -------------------------------------------------------------------------------------------------- | ----------------------- |
| `WF`    | **Workflow**          | Macroproceso o pipeline que coordina tareas y outputs a lo largo de distintas capas y módulos.     | Raíz/Padre             |
| `MPLN`  | **MasterPlan**        | Planificación estratégica que fija hoja de ruta, releases y visión global del sistema.             | Padre (bajo WF)        |
| `PLN`   | **Plan**              | Cronograma o plan operativo que define metas, entregables y responsables en ciclos específicos.    | Hijo de MPLN           |
| `RMAP`  | **Roadmap**           | Itinerario estratégico de etapas, dependencias y revisiones para despliegue iterativo.            | Hijo de PLN/MPLN       |
| `CHK`   | **Checklist**         | Listado de pasos o criterios de validación para releases, QA y cierre de ciclos.                  | Hijo de PLN/RMAP       |
| `CHKP`  | **Checkpoint**        | Punto de control para corte, revisión o rollback en flujos y releases complejos.                  | Hijo de CHK/RMAP       |
| `REVP`  | **ReviewPending**     | Ciclo de revisión y feedback iterativo, esencial para asegurar calidad y aprendizaje continuo.     | Hijo de CHK/RMAP       |
| `AUDT`  | **Audit**             | Auditoría y validación cruzada de procesos, resultados y cumplimiento de reglas.                  | Hermano de CHK/RMAP    |
| `TMPLG` | **TemplateGenerator** | Automatiza la generación de outputs, documentos y configuraciones, favorece estandarización.      | Secundario, en WF      |
| `TUNG`  | **Tuning**            | Ajuste iterativo y mejoras incrementales sobre módulos o workflows. Potencia agilidad y calidad.  | Secundario, transversal|
| `LSWP`  | **LiteralSweep**      | Recopilación literal de datos/outputs, sin interpretación, ideal para auditorías o migraciones.   | Secundario, cierre WF  |
| `VALD`  | **Validation**        | Validación lógica y técnica de outputs y releases antes de integrarlos en entornos productivos.    | Secundario, cierre     |
| `MIG`   | **Migration**         | Migración, actualización o refactorización de archivos, datos o workflows.                        | Hijo de WF             |
| `MAP`   | **Mapping**           | Definición y documentación de correspondencias y relaciones entre objetos, módulos o datos.       | Secundario, en MIG     |
| `CLSS`  | **Classification**    | Organización lógica por familias, tags o atributos. Optimiza búsquedas y reporting.               | Secundario, cierre     |
| `FBCK`  | **FeedbackEval**      | Evaluación y feedback formal sobre outputs, orientado a aprendizaje y mejora iterativa.           | Hermano de REVP        |
| `EVLS`  | **Evaluation**        | Evaluación global de procesos, sistemas y entregables. Facilita análisis crítico y evolución.     | Hermano de AUDT        |
| `ONBG`  | **Onboarding**        | Proceso de inducción y configuración para nuevos usuarios, equipos o sistemas.                    | WF especial            |
| `TAGX`  | **ExtendedTag**       | Etiquetas extendidas para outputs específicos (ej: diagramas, tests unitarios, visualizaciones).  | Decorador transversal  |
| `RPT`   | **Report**            | Informe técnico consolidado de resultados, métricas o validaciones realizadas.                    | Hijo de cualquier WF   |
| `TST`   | **Test**              | Script o matriz de pruebas automatizadas. Control de calidad previo a integración o release.      | Output de VALD         |
| `QRY`   | **Query**             | Consulta avanzada para extracción, análisis o integración de datos y outputs.                     | Proceso en MAP/MIG/WF  |
| `BLPR`  | **Blueprint**         | Documento/diseño estructural reutilizable como patrón para arquitectura, procesos o soluciones.   | Hermano de MPLN, RMAP  |

---

## Knowledge
| `CODE`  | **Name**          | Descripción                                                                                                    | Precedencia/Relación          |
| ------- | ----------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `KNS`   | **Knowledge**     | Repositorio de saberes, contexto, memoria e insights para consulta y mejora de sistemas.                       | Raíz/Padre                    |
| `MEM`   | **ContextMemory** | Registro de contexto activo y resultados relevantes, clave para aprendizaje organizacional.                    | Hijo directo de KNS           |
| `NOTE`  | **Note**          | Apuntes, datos y observaciones técnicas rápidas. Facilitan captura de información no formalizada.             | Hermano de MEM, hijo de KNS   |
| `GLOS`  | **Glossary**      | Diccionario técnico de términos, códigos y triggers del sistema. Permite uniformidad en naming y taxonomía.   | Hermano de MEM/NOTE, hijo KNS |
| `PREF`  | **Preferences**   | Configuraciones, decisiones y personalizaciones almacenadas para adaptar el sistema al contexto.              | Hermano de MEM/NOTE/GLOS      |
| `LEARN` | **Learning**      | Lecciones aprendidas, síntesis y buenas prácticas derivadas de auditorías y validaciones.                     | Hermano de KNS, procesos      |
| `INSI`  | **Insight**       | Observaciones estratégicas, patrones detectados y oportunidades de optimización en el ciclo de vida.         | Asociado a LEARN/KNS          |

---

## Log
| `CODE` | **Name**        | Descripción                                                                                                    | Precedencia/Relación       |
| ------ | -------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `LOG`  | **Log**        | Registro cronológico de eventos y outputs validados. Base para auditoría y trazabilidad de proyectos.          | Raíz/Padre                |
| `BIT`  | **Logbook**    | Bitácora extendida con contexto, justificación de cambios y referencias para rollback o auditoría técnica.      | Hijo de LOG               |
| `CHG`  | **Changelog**  | Historial estructurado de versiones, cambios y mejoras de releases y entregables.                             | Hermano de LOG            |
| `TRC`  | **Trace**      | Mapeo de relaciones y dependencias entre outputs, entradas y procesos críticos.                               | Hermano de LOG/CHG        |
| `XRF`  | **CrossRef**   | Enlaces y referencias cruzadas que garantizan unicidad e integración modular de componentes.                  | Hijo de TRC               |
| `ADT`  | **AuditLog**   | Registro detallado de acciones clave y compliance. Permite asegurar cumplimiento normativo y técnico.         | Hermano de LOG/CHG        |

---

## Documentation
| `CODE`  | **Name**         | Descripción                                                                                                   | Tipo de flujo         | Origen   | Precedencia/Relación             |
| ------- | ---------------- | ------------------------------------------------------------------------------------------------------------- | --------------------- | -------- | -------------------------------- |
| `DOC`   | **Documentation**| Archivo técnico o de referencia clave para integración, procesos y reporting.                                 | -                     | Macro    | Invocable por cualquier WF/KNS   |
| `RDM`   | **Readme**       | Documento principal de onboarding y referencia, accesible por humanos y sistemas.                             | Output/Template       | Oficial  | Enlaza RDM_H y RDM_AI            |
| `RDM_H` | **ReadmeHuman**  | README visual y ampliado para usuarios humanos, facilita comprensión y adopción del stack.                    | Output/Template       | Oficial  | Anexo a RDM                      |
| `RDM_AI`| **ReadmeAI**     | Prompt o bloque de instrucciones para IA. Incluye triggers, taxonomía y guías para integración automática.     | Input/Output/Template | Oficial  | Anexo a RDM                      |
| `TXT`   | **TextDoc**      | Guía, instructivo o resumen técnico. Integración y consulta rápida.                                           | Input/Output          | Oficial  | Base de integración              |
| `IMG`   | **ImageDoc**     | Imagen técnica, diagrama o screenshot utilizado para visualizar estructuras o procesos complejos.             | Input/Output          | Oficial  | Complemento visual               |
| `VID`   | **VideoDoc**     | Registro audiovisual, video de procesos, demos o workflows relevantes.                                        | Input/Output          | Oficial  | Output o demo                    |
| `AUD`   | **AudioDoc**     | Grabación de audio, feedback o explicaciones rápidas documentadas para consulta posterior.                    | Input/Output          | Oficial  | Output o feedback                |
| `LIB`   | **LibraryRef**   | Manual, libro, dataset o recurso oficial externo utilizado como fuente primaria de integración.               | Input                 | Externa  | Fuente de consulta               |
| `PAP`   | **Paper/Article**| Paper o artículo científico de referencia para desarrollo, diseño o validación de procesos.                   | Input                 | Externa  | Referencia, cita                 |
| `OWN`   | **OwnDoc**       | Documento interno propio, evoluciona iterativamente y puede ser input/output en múltiples ciclos.             | Output                | Propio   | Puede migrar Output > Input      |
| `DRAFT` | **DraftDoc**     | Documento en desarrollo y revisión iterativa hasta alcanzar release o integración final.                       | Output                | Propio   | Flujo iterativo                  |
| `FINAL` | **FinalDoc**     | Documento validado, aprobado, listo para integración o referencia definitiva.                                 | Output/Input          | Propio   | Puede migrar Output > Input      |
| `NB`    | **Notebook**     | Documento interactivo (Jupyter, Colab) para experimentación, documentación viva y pruebas.                    | Output/Tool           | Propio   | Output/herramienta enriquecida   |
| `MD`    | **Markdown**     | Documento estructurado, base para outputs y reporting legible por humanos y sistemas.                         | Input/Output/Template | Oficial  | Plantilla/output principal       |

---

## Script
| `CODE` | **Name**              | Descripción                                                                                        | Subcategorías/Ejemplos     |
| ------ | --------------------- | -------------------------------------------------------------------------------------------------- | -------------------------- |
| `SCR`  | **Script**            | Archivo ejecutable para automatización de tareas, integración de datos o procesos repetibles.      | Raíz de scripts            |
| `PIPE` | **PipelineScript**    | Script especializado en pipelines de datos, ETL y orquestación.                                    | Hijo de SCR                |
| `TSTSC`| **TestScript**        | Script de testing automatizado, validación de módulos y outputs antes de releases o despliegue.     | Hermano de PIPE            |
| `INTG` | **IntegrationScript** | Script para integración continua, despliegue y automatización avanzada en sistemas complejos.       | Hermano de PIPE            |
| `PRCSC`| **ProcessingScript**  | Script para procesamiento, limpieza o transformación de datos.                                     | Hermano de PIPE            |
| `CMD`  | **CommandScript**     | Script de comandos o shell para administración, monitoreo y mantenimiento del sistema.             | Hermano de PIPE            |

