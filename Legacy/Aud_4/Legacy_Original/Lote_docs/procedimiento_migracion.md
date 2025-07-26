# Procedimiento de Migración y Depuración

Este documento describe el flujo a seguir para continuar la reorganización del repositorio paso a paso.

## 1. Barrido de Legacy
1. Identificar todos los archivos que correspondan a README, instrucciones, roadmap, master plan, checklists, objetivos, reglas y versiones antiguas del glosario.
2. Registrar en `checklist_incongruencias.md` cualquier duplicado o discrepancia encontrada.

## 2. Clasificación y movimiento
1. Clasificar cada archivo según su tipo y utilidad real:
   - **Rules** → `docs/rules/`
   - **Plans/Roadmaps/Master Plan** → `docs/plans/`
   - **Checklists** → `docs/checklists/`
   - **Glosario** → `docs/glosario/`
2. Copiar las versiones válidas al nuevo directorio correspondiente.
3. Mover el archivo legacy original a `backup/` una vez confirmada la migración.

## 3. Actualización de `universal/`
1. Asegurar que las plantillas finales residan en `universal/templates/` (migradas desde `Legacy/RwB_Templates`).
2. Añadir guías de onboarding y ejemplos prácticos en `universal/onboarding/`.
3. Mantener `universal/knowledge/` como bitácora de aprendizajes.

## 4. Registro y trazabilidad
1. Documentar cada migración en `registro_trazabilidad_total.md` indicando ruta anterior y nueva.
   Puede usarse el script `scripts/mapping.py` para generar una tabla automática.
   Ejemplo:
   ```bash
   python scripts/mapping.py Legacy --output registro_trazabilidad_total.md
   ```
    - Ejecutar `scripts/generate_globalchecklist_main.py` para actualizar `Legacy_RwB_Cons/globalchecklist_main.md`.
2. Para detectar duplicados de una misma clase se puede emplear `scripts/class_scan.py`.
   Por ejemplo, para listar archivos con la clase `MTR` y sus repeticiones:
   ```bash
   python scripts/class_scan.py MTR --duplicates
   ```
3. Actualizar `changelog.md` con la fecha y descripción breve de cada cambio.

## 5. Iteración y cierre
1. Repetir el procedimiento por carpeta, integrando los archivos útiles y moviendo el resto a `backup/`.
2. Validar que `Legacy/` quede vacío salvo por respaldos que aún requieran revisión.
3. Al finalizar, revisar nuevamente el glosario y las reglas para asegurar consistencia en todo el repo.

Sigue este esquema para avanzar con el resto del repositorio y aprovechar al máximo la infraestructura RawBase con ChatGPT.
