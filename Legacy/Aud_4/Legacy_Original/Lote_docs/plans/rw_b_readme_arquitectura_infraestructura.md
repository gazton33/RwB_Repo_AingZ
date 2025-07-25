# [RwB] Blueprint de Arquitectura & Infraestructura Universal (AingZ)

> Referencia técnica y visual de la estructura modular, flujos y áreas principales de la infraestructura RwB-RAWBASE. Todo upgrade, integración y migración debe respetar este diagrama y ciclo.

---

## 1. Visión de la arquitectura modular RwB
- Infraestructura dividida por contextos (`PR`, `CO`, `CL`), dominios, categorías y estados, con trayectorias claras de migración, staging (`purgatorio`), revisión y consolidación.

---

## 2. Diagrama estructural (lógico)

```plaintext
/
├── README_MAIN_RwB.md
├── RwB_Diccionario_Glosario.md
├── RwB_Arquitectura.md
├── universal/templates/
├── purgatorio/
│    └── [CTX]/[GRP]/[DOMINIO]/[CAT]/
├── PR/
│    └── projects/[Dominio]/[CAT]/
├── CO/
├── CL/
├── knowledge/
├── config/
├── onboarding/
├── universal/
├── docs/
```

- Flujos de migración: legacy/original → purgatorio → auditoría/revisión → integración final
- Naming, logs, checklist y mapping en cada fase
- Modularidad total para sumar nuevas áreas, features o integraciones
- El directorio `universal/` es el workspace común; sus legacies deben pasar por `purgatorio/universal/` antes de integrarse

---

## 3. Referencias clave
- Naming universal y glosario: `RwB_Diccionario_Glosario.md`
- Ciclo y macroplan de migración: `rw_b_macro_plan_migracion_v_2.md`
- Templates y prompts: `universal/templates/`, `RwB_CHECKPOINT_TEMPLATES.md`, `RwB_CHECKPOINT_INSTRUCTION_PROMPT.md`
- Changelogs y logs de migración en cada área

---

## 4. Buenas prácticas y reglas de oro (RawBase)
- Toda integración, migración o upgrade comienza por el `purgatorio`, nunca va directo a `PR/CO/CL`.
- Toda estructura, template o archivo fuera del blueprint debe ser justificado, documentado y versionado.
- Los logs, mapping y checklists deben mantenerse siempre versionados y auditables.

---

> Consulta siempre este blueprint antes de planificar una integración, migración o nuevo proyecto en la infraestructura RwB-RAWBASE. Versiona y actualiza cada vez que evolucione la arquitectura.

