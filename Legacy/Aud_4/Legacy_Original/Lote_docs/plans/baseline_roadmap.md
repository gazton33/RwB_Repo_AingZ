# Línea de Base y Roadmap – Reorganización Universal

Esta línea de base consolida los avances detectados en todos los archivos Legacy y resume cómo construir un repositorio online dinámico conectado a OpenAI bajo el estándar **RawBase (RwB)**.

## Línea de base actual
- Todo el material histórico reside en `Legacy/` y conserva versiones previas de glosarios, reglas y planes.
- `universal/` contiene la estructura activa (carpetas vacías de feedback, knowledge, onboarding, projects y templates).
- Se creó `backup/` para archivar archivos superados una vez migrados.
- Los archivos `.rar` se convirtieron a `.zip` y se resguardan en `backup/`.
- Documentos clave ya validados: `README.md`, `RwB_Glosario_vFinal.md` y `docs/rules/README_reglas_raw_base.md`.
- Existen roadmap y planes de implementación en `Legacy/` (`rw_b_baseline_y_roadmap_v1.md`, `rw_b_plan_implementacion_v_3.md`).

## Roadmap de consolidación
1. **Clasificación de documentación**
   - Crear directorio `docs/` con subcarpetas `rules/`, `plans/`, `checklists/` y `glosario/`.
   - Mover aquí las versiones finales de reglas, planes y glosario.
- Consultar `docs/checklists/checklist_clases_archivos.md` para las categorías de archivos a migrar.
2. **Depuración de Legacy**
   - Revisar cada README, checklist y plan en `Legacy/`.
   - Tras integrar su contenido en `docs/` o `universal/`, mover el archivo original a `backup/`.
3. **Poblado de `universal/`**
   - Consolidar en `universal/templates/` las plantillas aprobadas (migradas desde `Legacy/RwB_Templates`).
   - Completar guías en `universal/onboarding/` y registrar retroalimentación en `universal/feedback/`.
4. **Automatización y scripts**
   - Desarrollar utilidades, como `scripts/mapping.py`, para generar mapping de archivos legacy→RwB y registrar los logs en `registro_trazabilidad_total.md`.
    - Generar un checklist global con `scripts/generate_globalchecklist_main.py` y guardar el resultado en `Legacy_RwB_Cons/globalchecklist_main.md`.
   - Configurar la integración continua con la API de OpenAI para un funcionamiento en línea.

   - Permitir que ChatGPT (Codex) edite el repositorio de forma dinámica mediante Pull Requests en GitHub.

5. **Pruebas y validación**
   - Implementar un juego mínimo de tests que verifique naming y existencia de logs/mappings.
   - Actualizar `docs/changelog.md` y `checklist_incongruencias.md` en cada iteración.
6. **Cierre de la migración**
   - Una vez trasladada la documentación definitiva a `docs/` y `universal/`, limpiar `Legacy/` dejando solo respaldos en `backup/`.
   - Publicar un resumen final en `README.md` con enlaces a glosario, reglas y roadmap.
- Comprimir el directorio `backup/` y retirarlo del repositorio, conservando la copia en un almacenamiento de respaldo.

Este roadmap deberá revisarse y ampliarse tras cada fase. Cualquier archivo completamente integrado se moverá a `backup/` dejando constancia en los registros de trazabilidad.
