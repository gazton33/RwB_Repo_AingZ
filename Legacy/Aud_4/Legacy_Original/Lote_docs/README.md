# Documentación Central

El directorio `docs/` agrupa los archivos principales de referencia para la infraestructura RwB.

- `plans/` — Roadmaps y planes de implementación.
- `rules/` — Reglas de operación y trazabilidad.
- `checklists/` — Listados de control para auditoría y migración.
- `glosario/` — Diccionarios y naming universal.

Consulta `procedimiento_migracion.md` para seguir el flujo de depuración y migración.

## Ejecución de pruebas

Instala `pytest` y lanza las pruebas desde la raíz del repositorio:

```bash
pip install pytest
pytest
```

Esto valida el script `scripts/mapping.py` y cualquier futura automatización.
