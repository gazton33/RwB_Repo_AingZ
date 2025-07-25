# [RwB] Propuesta de Infraestructura "Repo Full" — v1

Este documento consolida la línea de base observada en el repositorio y propone la estructura final de archivos y directorios para aprovechar al máximo las capacidades de ChatGPT y la arquitectura RwB.

## 1. Línea de base actual
- Documentación principal en `README.md` y archivos de reglas, glosario y blueprint (`rw_b_readme_*.md`).
- Carpeta `universal/templates/` con prompts y plantillas universales.
- Ejemplos de proyectos bajo `PR/projects/` y material legacy pendiente en `purgatorio/`.
- Carpetas de trabajo en `en desarrollo/` con planes, glosarios WIP y propuestas.

## 2. Objetivo de la infraestructura final
Organizar la información, workflows y templates para habilitar:
- Personalización completa de instrucciones y proyectos en ChatGPT.
- Manejo de subproyectos y threads con naming extendido.
- Versionado de knowledge base, logs y mappings de migración.
- Integración de agentes, evaluaciones y workflows automatizados.

## 3. Estructura de directorios propuesta
```plaintext
/
├── README.md                      # Visión y referencias globales
├── RwB_Glosario_vFinal.md         # Naming extendido y siglas oficiales
├── rw_b_readme_arquitectura_infraestructura.md
├── docs/rules/README_reglas_raw_base.md
├── rw_b_readme_templates.md
├── universal/templates/                     # Plantillas y prompts oficiales
│   └── ...
├── purgatorio/                    # Staging y auditoría
│   └── [CTX]/[GRP]/[Dominio]/[Proyecto]/[Thread]/[CAT]/
├── PR/                            # Entorno privado
│   ├── README.md
│   ├── changelog.md
│   ├── knowledge/
│   ├── templates/
│   ├── onboarding/
│   ├── feedback/
│   └── projects/
│       └── [Dominio]/[Proyecto]/[Thread]/[CAT]/
├── CO/                            # Collaborators (estructura espejo)
├── CL/                            # Clients (estructura espejo)
├── knowledge/                     # Knowledge base global
├── config/                        # Configuración y ejemplos
├── onboarding/                    # Guías y checklists
├── docs/                          # Documentación extendida
└── scripts_global/                # Scripts de migración y automatización
```

## 4. Roadmap de implementación
1. **Consolidar glosario final**
   - Unificar versiones de `en desarrollo/` y publicar `RwB_Glosario_vFinal.md` en la raíz.
2. **Crear READMEs contextuales**
   - `PR/README.md`, `CO/README.md` y `CL/README.md` describiendo subproyectos y reglas.
3. **Soportar subproyectos y threads**
   - Actualizar scripts y plantillas para naming `RwB_[CTX][_GRP]_PRJ_[PROJECT]_[THREAD]_CAT_VER_STA_TAG.ext`.
4. **Migrar material legacy**
   - Usar los prompts de checkpoint para mapear y mover archivos de `purgatorio/` a su destino definitivo.
5. **Integrar capacidades de ChatGPT**
   - Documentar templates para personalización global, proyectos y GPTs/asistentes.
   - Registrar workflows de evaluación y agentes en `docs/` y `workflows/`.
6. **Automatizar y versionar**
   - Mantener `universal/templates/rw_b_templates_index.md` actualizado y usar scripts en `scripts_global/`.
7. **Feedback y conocimiento**
   - Seguir el procedimiento de feedback iterativo y registrar aprendizajes en `knowledge/`.
8. **Validación final**
   - Verificar cumplimiento de reglas RawBase y publicar el repositorio final listo para explotación completa de ChatGPT.

---
Esta propuesta se basa en los documentos de `en desarrollo/` y consolida la infraestructura necesaria para el "repo full".
