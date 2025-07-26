# Repositorio AingZ — Infraestructura RwB

Este repositorio centraliza la reorganización de todos los archivos históricos bajo el estándar **RawBase (RwB)**. La carpeta `Legacy/` conserva el material original y `universal/` es el entorno activo para pruebas y workflows.

## Directorios principales
- `Legacy/` — Histórico completo pendiente de depuración.
- `universal/` — Entorno unificado para ejemplos, templates y conocimiento.
- `backup/` — Almacén temporal de archivos migrados desde `Legacy/`.
- `docs/` — Documentación central (reglas, planes, glosario y checklists).
  Revisa `docs/checklists/checklist_clases_archivos.md` para las categorías de
  archivos a migrar.

## Documentación clave
- [Glosario y naming universal](docs/glosario/RwB_Glosario_vFinal.md)
- [Reglas RawBase y trazabilidad](docs/rules/README_reglas_raw_base.md)
- [Registro de trazabilidad total](registro_trazabilidad_total.md)
- [Changelog de documentación](docs/changelog.md)
- [Roadmap y línea de base](docs/plans/baseline_roadmap.md)
- [Procedimiento de migración y depuración](docs/procedimiento_migracion.md)
- [Checklist de incongruencias](docs/checklists/checklist_incongruencias.md)
- Revisión histórica adicional en `Legacy/`

El objetivo de RwB es **recopilar sin interpretar**, garantizando la máxima calidad y confianza en el manejo de la información. Cada integración debe registrarse y evitar duplicidades para no generar ruido.

Consulta `docs/plans/baseline_roadmap.md` para el estado actual y los pasos planeados para completar la migración.

## Entorno conectado a OpenAI
El roadmap actualizado prioriza un repositorio dinámico integrado con la API de OpenAI.
Se incluye un `Dockerfile` que instala las dependencias necesarias y permite ejecutar los flujos en línea.

### Construcción
```bash
docker build -t rw-b-chatgpt .
```
La imagen descargará automáticamente las dependencias desde PyPI.

### Ejecución básica
```bash
docker run -it --rm -e OPENAI_API_KEY=tu_clave rw-b-chatgpt
```

La imagen contiene `gpt4all`, `llama-cpp-python` y `langchain`. Define `OPENAI_API_KEY` para habilitar la conexión con OpenAI.


## Ediciones automáticas con ChatGPT
El repositorio puede actualizarse de forma dinámica utilizando ChatGPT en modo Codex. Las sugerencias de cambio se generan como Pull Requests en GitHub para su revisión.


## Script de mapeo automático
`scripts/mapping.py` permite generar una tabla de correspondencia entre archivos
de `Legacy/` y su destino final. Ahora soporta argumentos para indicar la
carpeta a escanear y la ubicación del registro:

```bash
python scripts/mapping.py [carpeta] --output registro.md
```

Si no se pasan argumentos, utiliza `Legacy/` y `registro_trazabilidad_total.md`
por defecto.

## Generación de checklist global
Utiliza `scripts/generate_globalchecklist_main.py` para crear un listado completo de todos los archivos y su estado. El resultado se guarda en `Legacy_RwB_Cons/globalchecklist_main.md`.


## Licencia
Este proyecto se publica bajo la licencia [MIT](LICENSE).

