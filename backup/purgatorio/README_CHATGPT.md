# README for ChatGPT Guidance

Este documento resume la estructura y los principales lineamientos del repositorio **RwB_Repo_AingZ** para que puedas ayudarme aunque no tengas acceso directo al código desde la aplicación de PC.

## 1. Contexto general
- El repositorio sigue la metodología **RAW GOLD / RawBase**.
- La estructura se detalla en `rwb_repo_directory_plan_v_1.md` y resume las carpetas principales:
  - `AUDT/LOTE_X/Legacy_Original/` – fuentes originales por lote.
  - `AUDT/` – auditorías clasificadas por lote (`LOTE_1`, `LOTE_2`, ...).
  - `CONSOLIDADO/` – entregables finales validados.
  - `WF/` – workflows operativos.
  - `KNS/`, `SCR/`, `LOG/`, `DOC/` – knowledge base, scripts, logs y documentación.

## 2. Cómo orientarme en los siguientes pasos
1. **Consultar el plan** – Usa `rwb_repo_directory_plan_v_1.md` como guía paso a paso para mover la legacy, crear la estructura y migrar cada lote.
2. **Revisar las nomenclaturas** – El archivo `template/naming/rw_b_naming_template_v_1.md` define los prefijos y abreviaturas oficiales.
3. **Ver el análisis previo** – `proyecto_aing_z_analisis_de_repositorio.md` resume las herramientas, scripts y conclusiones de auditoría.
4. **Aplicar los workflows** – Ejecutar `WF/rw_b_wf_auditoria_legacy_v_2_20250724.md` y luego `WF/wf_migracion_final_legacy_rw_b_v_1_20250725.md` para validar y consolidar.
5. **Documentar todo** – Cada acción debe registrar logs (`LOG/`) y lecciones aprendidas (`KNS/LEARN/`).

## 3. Interacción con ChatGPT
- Cuando necesites soporte, comparte extractos de archivos o rutas específicas; ChatGPT no puede leer el repositorio directamente.
- Describe la carpeta o el lote en el que trabajas y menciona si seguiste los pasos del plan.
- Solicita indicaciones claras para scripts o comandos Bash cuando sea necesario.
- Mantén la coherencia con el glosario y las reglas de precedencia.

## 4. Próximos pasos sugeridos
1. Elegir el lote a trabajar y crear una nueva rama (`git checkout -b refactor/infra-v1`).
2. Verificar que cada lote esté ubicado bajo `AUDT/LOTE_X/Legacy_Original/` y completar la estructura faltante con el script del plan.
3. Reubicar auditorías y reclasificar scripts según las reglas de naming.
4. Actualizar enlaces en Markdown y validar con el workflow de auditoría.
5. Finalizar la migración con `wf_migracion_final_legacy_rw_b_v_1_20250725.md` y documentar resultados.

Con esta referencia, podrás indicarme los comandos y verificaciones correctas en cada etapa, incluso si solo te proveo fragmentos del repositorio.
