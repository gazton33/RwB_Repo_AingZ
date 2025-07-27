# Auditoría de Consolidación de Legacy (Propuesta)

Esta propuesta se basa en el `audit_mapping.csv`, los `audit_insights.json` y la guía `readme_legacy_rw_b_v_1_20250725.md` junto al `rw_b_wf_auditoria_legacy_v_3_20250725.md`. El objetivo es consolidar el contenido de `Legacy_Original` y definir qué archivos se integrarán al stack vivo, cuáles pasan a backup y cuáles requieren división o reestructuración.

## Resumen de categorías de auditoría

| Categoría | Cantidad de auditorías |
|-----------|-----------------------|
| Gem_Dig | 11 |
| General | 26 |
| Inventarios | 9 |
| KNS | 11 |
| Tmpl | 3 |
| WF | 6 |
| mtx | 14 |

## Duplicados detectados en Legacy_Original

Los siguientes archivos aparecen en más de un lote:

- `README.md` en las rutas:
  - `AUDT/LOTE_2/Legacy_Original/README.md`
  - `AUDT/LOTE_1/Legacy_Original/Lote_1_2/README.md`
  - `AUDT/LOTE_1/Legacy_Original/Lote_1_1/README.md`
- `t_3_raw_gold_matriz_final.md` en las rutas:
  - `AUDT/LOTE_2/Legacy_Original/Lote_knowledge/t_3_raw_gold_matriz_final.md`
  - `AUDT/LOTE_2/Legacy_Original/Lote_matrices/t_3_raw_gold_matriz_final.md`
  - `AUDT/LOTE_1/Legacy_Original/Lote_1_2/t_3_raw_gold_matriz_final.md`

En el mapeo de auditorías existen versiones actualizadas de estos documentos. Por tanto se recomienda conservar una sola copia actualizada y enviar las demás a backup.

## Barrido literal de Legacy_Original

### LOTE_1

```text
AUDT/LOTE_1/Legacy_Original
├── Lote_1_1
│   ├── Legacy_MTX_features_prompts.md
│   ├── Legacy_MTX_instrucciones.md
│   ├── Legacy_MTX_jerarquia_instrucciones.md
│   ├── Legacy_MTXfaq_avanzada_gestion_de_adjuntos.md
│   ├── Legacy_onboarding_gz.md
│   └── README.md
└── Lote_1_2
    ├── README.md
    ├── aing_z_repo_legacy_barrido_raw.md
    ├── aing_z_repo_raw_gold_scaffold.md
    ├── faq_workflows_operativo_v_1_lote_1_20250724.md
    ├── jerarquia_precedencia_instrucciones_v_1_lote_1_20250724.md
    ├── matriz_features_prompts_v_1_lote_1_20250724.md
    ├── rawgold_scaffold_readme.md
    ├── readme_base_aingz_t_3_infra.md
    ├── readme_integracion_t_2_memorias_historiales.md
    ├── readme_master_plan.md
    ├── readme_matriz_memorias_historiales.md
    ├── readme_onbrd_v_1_lote_1_20250724.md
    ├── t_3_raw_gold_canvas_integrado_final_v_2.md
    └── t_3_raw_gold_matriz_final.md

3 directories, 20 files
```

### LOTE_2
```text
AUDT/LOTE_2/Legacy_Original
├── Lote_knowledge
│   ├── knowledge_base_aingz_t_3.md
│   ├── knowledge_base_matriz_precedencia_templates_universales_raw.md
│   ├── knowledge_gz_project_insights.md
│   ├── knowledge_memorias_feedback_reglas_oro.md
│   ├── mtx
│   ├── readme_knowledge.md
│   └── t_3_raw_gold_matriz_final.md
├── Lote_matrices
│   ├── checklist_testing_memorias_historiales.md
│   ├── control_cruce_matriz_raw_vs_extendida.md
│   ├── control_trazabilidad_fuentes_chatgpt_workflow.md
│   ├── ejemplo_integracion_memoria_feedback.md
│   ├── leccion_aprendida_upgrade_memorias.md
│   ├── matrices_readme.md
│   ├── matriz_memorias_historiales_chatgpt.md
│   ├── matriz_precedencia_instrucciones_full_custom_infraestructura.md
│   ├── plantilla_snapshot_memoria.md
│   ├── rw_b_matriz_triggers_contexto.md
│   ├── t_2_2_raw_gold_matriz_historiales.md
│   └── t_3_raw_gold_matriz_final.md
├── Lote_templates
│   ├── plantilla_prompt_custom_gpt.md
│   └── templates_casos_uso_precedencia_infraestructura_full_custom.md
├── Lote_workflows
│   ├── readme_workflows.md
│   ├── rw_b_macro_plan_migracion_v_2.md
│   ├── workflow_gpt_raw.md
│   ├── workflow_gpt_raw_v_1.md
│   └── workflow_gz_project_template.md
└── README.md

6 directories, 26 files
```

### LOTE_3
```text
AUDT/LOTE_3/Legacy_Original
├── Lote_Gem_Digitales
│   ├── Bloque 1.json
│   ├── Bloque 2.json
│   ├── Bloque 3.json
│   ├── Bloque 4.json
│   ├── Bloque 5.json
│   ├── Bloque 6.json
│   ├── Bloque 7.json
│   ├── Bloque 8.json
│   ├── Cv Gaston 2020.doc
│   ├── DR GZ Web 1.pdf
│   ├── gem_dig_gz_gpt_raw.md
│   └── gem_dig_gz_gpt_raw_v_1.md
└── Lote_Inventario
    ├── bike_electrical_knowledge_v_2.md
    ├── gz_e_bike_knowledge v2.md
    ├── gz_e_bike_knowledge.md
    ├── gz_n_56_vz_hw_info_script_full.py
    ├── gz_n_56_vz_tech.md
    ├── inventario_tecnico_prompt_y_template_raw.md
    ├── reporte_hw_gz_n56vz_2025-07-15_19-51.csv
    └── reporte_hw_gz_n56vz_2025-07-15_19-51.md

3 directories, 20 files
```

## Recomendaciones de consolidación

1. **Integrar** los archivos que no cuentan con una auditoría específica en `audit_mapping.csv`. Principalmente corresponden a datos de inventarios y gemelos digitales del Lote 3.
2. **Respaldar** (mover a carpeta `backup/`) los archivos que poseen versiones auditadas o duplicadas, tales como `t_3_raw_gold_matriz_final.md` y los `README.md` de Lotes 1 y 2.
3. **Dividir** algunos documentos extensos (p. ej. `knowledge_base_aingz_t_3.md` o `workflow_gpt_raw.md`) en módulos temáticos siguiendo la nueva infraestructura definida en el Master Plan, para integrarlos en las categorías de `Knowledge`, `WF` y `Templates`.
4. Utilizar el **workflow v3** para registrar cada movimiento y mantener trazabilidad. Los pasos de validación indicados en el README aseguran que no se pierda contexto de legacy antes de archivar o migrar información.

Esta propuesta inicial podrá refinarse iterativamente aplicando las matrices de dependencias y el seguimiento de insights por lote.

