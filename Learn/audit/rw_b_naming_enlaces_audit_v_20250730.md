# RwB Naming & Link Audit — 2025-07-30

> Revisión de cumplimiento del naming ruleset y enlaces a glosario.

## Carpetas auditadas
- `workflow/`
- `knowledges/`
- `Learn/`
- `template/`
- `doc/`

## Excepciones detectadas
- `Learn/Relev ideas` contiene espacio y debería renombrarse a `relev_ideas/`.
- `doc/bliblioteca_Refencia/` tiene errores tipográficos; se propone `biblioteca_referencia/`.
- `doc/bliblioteca_Refencia/openai/Docs OpenAi` y `doc/bliblioteca_Refencia/openai/Help OpenAi` deberían renombrarse a `docs_openai/` y `help_openai/`.
- Las carpetas raíz `Learn/` y `doc/` no siguen el prefijo `rw_b_`, mantener por compatibilidad pero documentar.

## Enlaces revisados
Todos los README principales enlazan correctamente al glosario en `knowledges/glossary/`. Se añadieron referencias faltantes en la memoria viva.

### Próximas acciones
- Aplicar los renombres propuestos en el próximo ciclo.
- Revisar scripts de CI/CD para reflejar las rutas actualizadas.

