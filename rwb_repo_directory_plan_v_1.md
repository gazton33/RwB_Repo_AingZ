# RwB Repo — Propuesta de Estructura de Directorios (v1)

> Basado en los workflows de auditoría v2 y migración final v1, los drafts de roadmap de consolidación (Etapas 1‑2b) y el **Glosario CODE v0**.

---

## 1 Árbol raíz sugerido

*(prefijos ↔ códigos del glosario)*

```text
/                          # CTX raíz del repo (CTX)
├── LEGACY/                # Fuentes originales y backups (BK)
│   ├── ORIGINAL/          # ZIPs, dumps, datos «tal‑cual»
│   └── ARCHIVE/           # Copias aisladas tras cierre de migración
│
├── AUDT/                  # Auditorías (AUDT)
│   ├── LOTE_1/
│   ├── LOTE_2/
│   └── ...
│
├── CONSOLIDADO/           # Outputs finales por lote (FINAL) – ready 4 use
│   ├── LOTE_1/
│   ├── LOTE_2/
│   └── ...
│
├── MIG/                   # Artefactos de migración (MIG)
│   ├── WF/                # Workflows de migración (WF)
│   ├── LOG/               # Logs/bitácoras (LOG/BIT)
│   └── SCRIPTS/           # Scripts auxiliares (SCR/INTG)
│
├── KNS/                   # Knowledge base (KNS)
│   ├── GLOS/              # Glosarios y taxonomías (GLOS)
│   ├── MEM/               # Memorias/contexto activo (MEM)
│   ├── LEARN/             # Lessons learned (LEARN)
│   └── NOTE/              # Notas rápidas (NOTE)
│
├── DOC/                   # Documentación formal (DOC)
│   ├── RDM/               # READMEs human/AI (RDM_H / RDM_AI)
│   └── BLPR/              # Blueprints & master‑plans (BLPR/MPLN)
│
├── WF/                    # Workflows operativos (WF)
│   └── ...
│
├── SCR/                   # Scripts globales (SCR)
│   ├── PIPE/  INTG/  CMD/ …
│
├── LOG/                   # Logs globales, changelogs, audit‑logs (LOG/CHG/ADT)
│
└── PURGATORIO/            # Staging temporal previo a integración (STA=draft)
```

---

## 2 Mapeo macro ➜ destino

| Origen (patrón)            | Tipo `TYP` | Destino → Dir/CODE    | Notas                                     |
| -------------------------- | ---------- | --------------------- | ----------------------------------------- |
| `Legacy/**`                | BK         | `LEGACY/ORIGINAL/`    | Conservar ZIP, CSV, imágenes crudas       |
| `Legacy/Aud_*`             | AUDT       | `AUDT/LOTE_n/`        | Mantener árbol original + checklist       |
| `Legacy/**/Consolidados/*` | FINAL      | `CONSOLIDADO/LOTE_n/` | Copiar tras validación │                  |
| `workflow/*.md`            | WF         | `WF/`                 | Reubicar con prefijo `WF_` + versión      |
| `scripts/**`               | SCR        | `SCR/`                | Re‑clasificar a PIPE/INTG/… según función |
| `*_glosario*.md`           | GLOS       | `KNS/GLOS/`           | Naming `GLOS_<tema>_v#.md`                |
| `*_feedback*`              | FBCK       | `KNS/LEARN/`          | Snapshot tras cada ciclo                  |

> **Regla:** los archivos pasan primero por `PURGATORIO/` si requieren tuning manual; al integrarse reciben prefijo `RDM_`, `WF_`, etc., según glosario.

---

## 3 Pasos para "acomodar" el repo

1. **Snapshot & branch**  – `git checkout -b refactor/infra-v1`.
2. **Mover legacy**  – `git mv Legacy/ LEGACY/ORIGINAL/` (preserva historia).
3. **Crear estructura vacía**  – script:
   ```bash
   for d in AUDT CONSOLIDADO MIG/WF MIG/LOG MIG/SCRIPTS KNS/{GLOS,MEM,LEARN,NOTE} DOC/{RDM,BLPR} WF SCR/{PIPE,INTG,CMD} LOG/{CHG,ADT} PURGATORIO; do
       mkdir -p "$d" && git add "$d";
   done
   ```
4. **Reubicar auditorías**  – `git mv LEGACY/ORIGINAL/Aud_* AUDT/LOTE_#/` según lote.
5. **Reclasificar scripts**  – identificar por nombre ⇒ mover a `SCR/PIPE` (ETL), `SCR/INTG` (CI), `SCR/CMD` (bash utilitarios).
6. **Migrar documentos**  – Workflows a `WF/`, blueprints a `DOC/BLPR/`, READMEs raíz a `DOC/RDM/`.
7. **Actualizar enlaces**  – buscar y reemplazar rutas antiguas en Markdown (`sed -i 's|Legacy/[^)]*|...|g' *.md`).
8. **Commit & PR**  – `git commit -m "infra v1: reorganización según glosario RwB"`.
9. **Revisión cruzada**  – usar checklist de auditoría v2 antes de merge.

---

## 4 Scripts auxiliares mínimos

```bash
# mover_por_tipo.sh — ejemplo rápido
find . -type f -name "*_checklist*" -exec git mv {} KNS/LEARN/ \;
find . -type f -name "*_glosario*" -exec git mv {} KNS/GLOS/ \;
# ... añadir reglas por patrón
```

---

## 5 Próximos pasos

- **Validación** con `WF_AUDITORIA_LEGACY_v2` ✓
- **Ejecución migración** con `WF_Migracion_Final_Legacy_RwB_v1` ✓
- **Purgatorio**: eliminar `LEGACY/ORIGINAL/` solo tras `VALD` y firma.

---

*Draft infra‑v1 listo para revisión.*

---

## 6 Playbook **Codex** — Ejecución paso a paso

> **Objetivo**: reestructurar el repo local clon (o Codespace) siguiendo la propuesta. Ejecutar en una shell Bash (o directamente vía Codex) en la rama `refactor/infra‑v1`.

### 0 Prereqs

| Requisito               | Comando de verificación |
| ----------------------- | ----------------------- |
| Git ≥ 2.30              | `git --version`         |
| Bash ≥ 4                | `bash --version`        |
| jq (opcional para JSON) | `jq --version`          |

### 1 Snapshot de seguridad

```bash
# fuera del repo ➜ copia por si acaso
cp -R RwB_Repo RwB_Repo.bak.$(date +%F-%H%M)
cd RwB_Repo
```

### 2 Crear branch de trabajo

```bash
main_branch=$(git symbolic-ref --short HEAD)
git checkout -b refactor/infra-v1
```

### 3 Mover **legacy** completo

```bash
git mv Legacy LEGACY/ORIGINAL
```

### 4 Generar estructura vacía

```bash
read -r -d '' DIRS <<'EOF'
AUDT CONSOLIDADO MIG/WF MIG/LOG MIG/SCRIPTS KNS/GLOS KNS/MEM KNS/LEARN KNS/NOTE \
DOC/RDM DOC/BLPR WF SCR/PIPE SCR/INTG SCR/CMD LOG/CHG LOG/ADT PURGATORIO
EOF
for d in $DIRS; do
  mkdir -p "$d" && git add "$d"
done
```

### 5 Reubicar auditorías (lote detectado vía nombre de carpeta)

```bash
for lote in $(ls LEGACY/ORIGINAL | grep -E "Aud_?"); do
  num=$(echo "$lote" | grep -oE "[0-9]+")
  git mv "LEGACY/ORIGINAL/$lote" "AUDT/LOTE_${num}/"
done
```

### 6 Re‑clasificar scripts

```bash
# ejemplo básico — ajustar patrones según naming real
find LEGACY/ORIGINAL -type f -name "*extract*\.py" -exec git mv {} SCR/PIPE/ \;
find LEGACY/ORIGINAL -type f -name "*deploy*\.sh"  -exec git mv {} SCR/INTG/ \;
```

### 7 Workflows y blueprints

```bash
git mv workflow/*.md WF/
git mv docs/*blueprint*.md DOC/BLPR/
```

### 8 Actualizar rutas en Markdown

```bash
# remplaza rutas Legacy ➜ nuevas — probar en dry‑run primero
grep -Rl "Legacy/" --exclude-dir=.git --include=*.md \
  | xargs sed -i.bak -E 's|Legacy/[^)]*|LEGACY/ORIGINAL/|g'
rm -f *.bak
```

### 9 Commit

```bash
git add .
git commit -m "infra v1: reorganización según glosario RwB (playbook Codex)"
```

### 10 Checklist antes de push

-

### 11 Push + Pull Request

```bash
git push -u origin refactor/infra-v1
```

Crear PR, asignar reviewers y enlazar con issue "Infra v1".

---

> **Tip Codex** : puedes empaquetar cada bloque Bash como *snippet* y ejecutarlo secuencialmente. Ante dudas añade `set -euxo pipefail` para modo debug.

