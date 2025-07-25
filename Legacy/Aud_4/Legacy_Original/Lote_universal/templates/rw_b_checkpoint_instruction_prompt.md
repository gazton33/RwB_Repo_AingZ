# [RwB] CHECKPOINT INSTRUCTION PROMPT — Auditoría/Migración/Actualización Automatizada

> **Instrucciones y prompt para auditar, migrar o cerrar hilos/chats/proyectos de cualquier tipo usando archivos legacy adjuntos.**

---

## 1. Instrucciones generales

- Adjunta aquí todos los archivos a relevar (outputs de chat/ciclo/hilo, docs, scripts, logs, matrices, knowledge, templates, etc), en cualquier formato compatible.
- Al iniciar este prompt, **se preguntará** si el objetivo es:
    1. Auditoría inicial
    2. Actualización/Incremental
    3. Cierre total de ciclo/hilo/proyecto
- Según la opción, se realizará el barrido y análisis correspondiente, generando **TODOS los archivos/outputs necesarios** en el canvas, agrupados y listos para migración a `/purgatorio/` o integración final.

---

## 2. Qué ejecuta el prompt

- **Analiza y clasifica** cada archivo según contexto, dominio, tipo y naming universal RAWBASE.
- **Genera automáticamente:**
    - El/los `CHECKPOINT_TEMPLATES` requeridos (cierre, inventario, mapping, revisión, changelog).
    - Mapping completo legacy→RwB para cada archivo, listo para actualización de referencias cruzadas.
    - Logs, changelogs, listas de pendientes, duplicados y feedback.
- **Incluye y referencia:**
    - Aprendizajes, feedback, reglas de oro y coverage del ciclo/hilo.
    - Glosario, macroplan, matrices y cualquier estándar vigente.

---

## 3. Flujo de interacción (paso a paso)
1. Adjunta archivos o indica carpeta/ciclo a auditar.
2. El prompt preguntará qué tipo de auditoría quieres realizar:
    - Auditoría inicial (barrido y checklist básico, sin cierre)
    - Actualización/Incremental (agrega outputs a una auditoría/cierre anterior)
    - Cierre total (genera todo el output de cierre y mapping definitivo)
3. El sistema:
    - Analiza y clasifica 100% de los archivos.
    - Genera y muestra en el canvas TODOS los templates, logs y outputs requeridos para esa acción, agrupados pero separados según corresponda (inventario, mapping, changelog, revisión, README/archivo de cierre, feedback, etc).
    - Deja cada archivo listo para ser migrado/integrado.
    - Si encuentra errores, duplicados o información cruzada, los marca para revisión manual.
4. Indica instrucciones para el siguiente paso: migrar, integrar o seguir iterando la auditoría.

---

## 4. Notas de uso

- Puedes usar este prompt en cualquier chat, API o ciclo con archivos legacy/históricos.
- Asegúrate de mantener los logs y mapping resultantes para actualización cruzada en la infraestructura.
- No elimines nada del legado original hasta validar el mapping y cobertura final.
- Si un archivo contiene información de varios proyectos/contextos, documentarlo y marcarlo para análisis posterior.

---

> Usa siempre los templates y reglas RwB-RAWBASE. Si tienes dudas sobre el flujo, consulta el glosario y macroplan antes de marcar el ciclo/hilo como cerrado.

