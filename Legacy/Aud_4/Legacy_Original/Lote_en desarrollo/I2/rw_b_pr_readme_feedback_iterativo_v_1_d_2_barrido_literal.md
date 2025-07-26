# [RwB] README — FEEDBACK ITERATIVO Y ANÁLISIS POST-BARRIDO LITERAL (v1d2 WIP)

---

## 1. Propósito y alcance

- Definir el procedimiento, triggers y reglas para la etapa de feedback iterativo posterior al barrido literal/auditoría bajo el estándar RwB.
- Garantizar que todo output marcado como `BARRIDO_LITERAL` sea analizado, revisado y refinado SIN omisión ni eliminación de datos, salvo autorización expresa.
- Marcar, priorizar y referenciar todos los outputs con tag `REVISION_PENDING` para que reciban análisis profundo, refactor o integración en futuros ciclos.

---

## 2. Flujo operativo de feedback iterativo post-barrido

1. **Revisión secuencial de outputs**: Procesar cada archivo, ciclo o hilo generado por el barrido literal, siguiendo la tabla de mapping y referencias cruzadas.
2. **Identificación y priorización de `REVISION_PENDING`**: Listar explícitamente todos los outputs/ciclos marcados en la etapa anterior para revisión profunda.
3. **Análisis, refactor y clasificación**: Ejecutar análisis detallado, proponer refactor, y decidir integración, archivo o depuración de cada output (solo tras registro y autorización del responsable).
4. **Documentación literal y changelogs**: Registrar cambios, aprendizajes y decisiones en logs y changelogs versionados. No eliminar nada sin trazabilidad.
5. **Feedback y aprendizaje global**: Extraer lecciones, feedback y reglas para evolucionar glosario, triggers, templates y workflows.

---

## 3. Triggers y tags clave del ciclo

| Trigger           | Uso/fase               | Acción obligatoria                |
|-------------------|------------------------|-----------------------------------|
| BARRIDO_LITERAL   | Entrada a feedback     | No modificar/omitir outputs       |
| REVISION_PENDING  | Foco de análisis       | Documentar motivo y referencia    |
| REF (Refactor)    | Análisis profundo      | Proponer y registrar cambios      |
| FIN               | Cierre/integración     | Solo tras registro y aprobación   |

---

## 4. Ejemplo de procedimiento de feedback

1. **Input**: Archivo/ciclo generado por barrido literal (con tags y mapping)
2. **Paso 1**: Leer tabla mapping y detectar filas con tag `REVISION_PENDING`
3. **Paso 2**: Para cada output/tag:
   - Leer y documentar motivo, referencia, prioridad
   - Ejecutar análisis/refactor si corresponde
   - Registrar decisión y actualizar logs
4. **Paso 3**: Tras revisar todo, proponer integración/cierre (tag `FIN`), solo tras aprobación

---

## 5. Reglas y advertencias

- Nunca eliminar ni resumir outputs hasta finalizar feedback iterativo, registro y aprobación
- Toda excepción debe dejarse registrada y referenciada en mapping y changelog
- Los triggers y tags usados deben actualizarse en el glosario y templates
- Feedback y aprendizaje deben alimentar el knowledge base y la evolución de la infraestructura

---

> Esta guía y README deben acompañar cualquier ciclo de feedback post-barrido. Usa siempre naming y triggers RwB, y mantén el registro literal de decisiones hasta la integración final.

