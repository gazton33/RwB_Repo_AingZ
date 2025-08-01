# AingZ_Platform · Matriz de Conectores Gratuitos (v1 ‑ jul‑2025)

[BARRIDO_LITERAL]

> **Propósito**: registrar los conectores/apps gratuitos que amplían la plataforma AingZ_Platform (repositorio RwB + IA) y estandarizar su nomenclatura para trazabilidad.

## 1 · Tabla comparativa “versus”

| # | Conector / App | Categoría | Función general | Aplicación AingZ_Platform | Punto de integración† | Naming sugerido |
|---|----------------|-----------|-----------------|---------------------------|-----------------------|-----------------|
| 1 | Draw.io GitHub App / VS Code ext. | Diagramas WYSIWYG | Editar `.drawio`, exportar SVG/PNG, diff visual PR | Versionado de diagramas de infraestructura, flujos | Carpeta `/diagrams` + PR | **CNX.DI.drawio** |
| 2 | Mermaid (nativo GitHub) | Diagramas como código | Render Markdown→SVG sin CI | Docs técnicas y specs | Cualquier `.md` | **CNX.DI.mermaid** |
| 3 | PlantUML Action | Diagramas UML texto | CI convierte `.puml`→SVG | Modelado UML de módulos | GitHub Action `render-plantuml` | **CNX.DI.plantuml** |
| 4 | D2 Action | DSL moderno de diagramas | CI `.d2`→SVG | Infra-as-code visual | Action `terrastruct/d2-action` | **CNX.DI.d2** |
| 5 | Obsidian‑Git | Sync notas ↔ Git | Push automático vault | Knowledge base sincronizada | Vault `obsidian/` rama `knowledge` | **CNX.SYNC.obs_git** |
| 6 | Obsidian‑GDrive‑Sync | Backup vault ↔ Drive | Redundancia & trabajo móvil | Copy off‑site | Google Drive folder | **CNX.SYNC.obs_gdrive** |
| 7 | Dropbox‑folder sync / Action | Backup artefactos | Copia fría de releases | Resguardo de SVG/PDF | `/backups/dropbox` + secret TOKEN | **CNX.SYNC.dropbox** |
| 8 | GDrive‑upload Action | Distribución builds | Sube datasets/release | Compartir externos | Action `gdrive-upload` | **CNX.SYNC.gdrive** |
| 9 | GitLens (VS Code) | IDE / Git UX | Blame, history, PR in‑editor | Auditoría y trazabilidad de código | Extensión VS Code | **CNX.IDE.gitlens** |
|10| Draw.io‑for‑Obsidian | Diagramas en notas | Edición `.drawio` in‑vault | Diagrama+texto juntos | Plugin Obsidian | **CNX.DI.obs_drawio** |
|11| Mermaid Preview (VS Code) | IDE render | Preview en vivo Mermaid | Refactor rápido | Extensión VS Code | **CNX.IDE.mermaid_preview** |
|12| tldraw (self‑host/SDK) | Pizarra colaborativa | Canvas realtime, export SVG | Ideación visual remota | GH Pages / React app | **CNX.CANVAS.tldraw** |

†*Punto de integración* = carpeta, acción o extensión exacta dentro de la plataforma.

---

## 2 · Nomenclatura estandarizada

```
<AingZ_Platform>.<LAYER>.<ROLE>.<tool>[.<qualifier>]
```

* **LAYER** → DI (diagramas), SYNC (sincronización/backup), IDE (extensiones IDE), CANVAS (pizarras).  
* **ROLE** → nombre de conector o acción (ej: `drawio`, `gdrive`).  
* **Qualifier** opcional para distinguir subplugins (ej: `preview`).

Ejemplo: `AingZ_Platform.DI.drawio` → Draw.io como conector de diagramas.

---

## 3 · Pasos de integración inmediata (short‑term)

1. **Instalar Draw.io GitHub App** y crear directorio `diagrams/` (naming `MOD_*`).
2. **Activar Obsidian‑Git** con PAT de bot `rw‑bot`. _Auto‑push_ = 15 min.
3. **Configurar PlantUML + D2 Actions** (`.github/workflows/diagrams.yml`).
4. **Agregar GitLens & Mermaid Preview** a `/.vscode/extensions.json` (recomendaciones).
5. **Implementar GDrive‑upload** para tag `v*` y **Dropbox backup** nightly.
6. Registrar cada conector en `rw_b_dir_arch_plan_v_4_20250729.md`.

---

## 4 · Checkpoint RwB (REVISION_PENDING)

- Validar tokens PAT y scopes mínimos.  
- Documentar secretos en `gh‑settings/secrets.md` (solo refs, sin valores).  
- Programar auditoría post‑integración + diffs.

---

> **Fin Matriz v1 – listo para revisión y merge en rama `infra/connectors`.**

