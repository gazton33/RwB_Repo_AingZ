from pathlib import Path

LEGACY_DIR = Path('Legacy')

# Keywords per class
CLASSES = {
    'MTR': ['matriz', 'matrices', '_MTR_', 'MTR'],
    'SCR': ['scripts', '.py', '_SCR_'],
    'WF': ['workflows', 'workflow', '_WF_'],
    'LOG': ['logs', '.log', '_LOG_'],
    'DOC': ['docs', '_DOC_'],
    'KNS': ['knowledge', '_KNS_'],
    'BK': ['backups', 'backup', '.zip', '.bak', '_BK_'],
    'NB': ['notebooks', '.ipynb', '_NB_'],
    'CFG': ['config', '.cfg', '.ini', '.yaml', '.yml', '.env', '.config', 'Dockerfile', '_CFG_'],
    'TMP': ['templates', '_TMP_', 'prompt'],
    'CHK': ['checklist', '_CHK_'],
    'IMG': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '_IMG_'],
    'PLN': ['plans', 'roadmap', '_PLN_', 'plan'],
}

# Additional keywords for DOC content to reclassify
DOC_CONTENT_MAP = {
    'checklist': 'CHK',
    'matriz': 'MTR',
    'roadmap': 'PLN',
    'master plan': 'PLN',
    'plan': 'PLN',
    'knowledge': 'KNS',
    'prompt': 'TMP',
    'template': 'TMP',
}


def scan_files(base: Path = LEGACY_DIR):
    return [p for p in base.rglob('*') if p.is_file()]


def classify(path: Path) -> str:
    p_low = path.as_posix().lower()
    name_low = path.name.lower()
    for cls, kws in CLASSES.items():
        for kw in kws:
            if kw.startswith('.'):
                if name_low.endswith(kw):
                    return cls
            elif kw in p_low:
                return cls
    if name_low.endswith(('.md', '.txt', '.doc', '.docx')):
        try:
            text = path.read_text(encoding='utf-8', errors='ignore').lower()
        except Exception:
            text = ''
        for kw, cls in DOC_CONTENT_MAP.items():
            if kw in name_low or kw in text:
                return cls
        return 'DOC'
    return 'OTR'


def generate_checklist(files):
    groups = {}
    for f in files:
        cls = classify(f)
        groups.setdefault(cls, []).append(f)

    lines = []
    for cls in sorted(groups.keys()):
        lines.append(f"### {cls}")
        for p in sorted(groups[cls]):
            rel = p.as_posix()
            lines.append(f"- {rel}")
        lines.append('')
    return "\n".join(lines)


def main():
    files = scan_files()
    checklist = generate_checklist(files)
    header = Path('docs/checklists/checklist_clases_archivos.md').read_text(encoding='utf-8').split('## Pendientes')[0].rstrip()
    out = f"{header}\n\n## Pendientes en `Legacy/` (2025-07-22)\n\n" + checklist
    Path('docs/checklists/checklist_clases_archivos.md').write_text(out, encoding='utf-8')

if __name__ == '__main__':
    main()
