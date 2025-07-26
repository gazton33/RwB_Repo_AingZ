from pathlib import Path
import os
import re
import argparse

REPO_ROOT = Path(__file__).resolve().parents[1]

CLASSES = {
    'MTR': ['matriz', 'matrices', '_MTR_', 'MTR'],
    'SCR': ['scripts', '.py', '_SCR_'],
    'WF': ['workflows', 'workflow', '_WF_'],
    'LOG': ['logs', '.log', '_LOG_'],
    'DOC': ['docs', '.md', 'readme', '_DOC_'],
    'KNS': ['knowledge', '_KNS_'],
    'BK': ['backups', 'backup', '.zip', '.bak', '_BK_'],
    'NB': ['notebooks', '.ipynb', '_NB_'],
    'CFG': ['config', '.cfg', '.ini', '.yaml', '.yml', '.env', '.config', 'Dockerfile', '_CFG_'],
    'TMP': ['templates', '_TMP_'],
    'CHK': ['checklist', '_CHK_'],
    'IMG': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '_IMG_'],
    'PLN': ['plans', 'roadmap', '_PLN_'],
}


def classify(path: Path) -> str:
    p = path.as_posix().lower()
    name = path.name.lower()
    for cls, keywords in CLASSES.items():
        for kw in keywords:
            if kw.startswith('.'):
                if name.endswith(kw):
                    return cls
            elif kw.lower() in p:
                return cls
    return 'DOC' if path.suffix.lower() in {'.md', '.txt'} else 'OTR'


def scan_repo(base: Path = REPO_ROOT):
    files = []
    for root, dirs, filenames in os.walk(base):
        if '.git' in dirs:
            dirs.remove('.git')
        for fname in filenames:
            full = Path(root) / fname
            rel = full.relative_to(base)
            files.append(rel)
    return files


def determine_status(path: Path) -> str:
    return 'pendiente' if path.parts and path.parts[0].lower() == 'legacy' else 'migrado'


def readme_references():
    readmes = [REPO_ROOT / 'README.md', REPO_ROOT / 'readme_aing_z_rw_b_v_2025_07_22.md']
    refs = {}
    pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
    for rfile in readmes:
        if rfile.exists():
            text = rfile.read_text(encoding='utf-8', errors='ignore')
            for match in pattern.findall(text):
                if match.startswith('http'):
                    continue
                ref_path = (REPO_ROOT / match).resolve()
                try:
                    rel = ref_path.relative_to(REPO_ROOT)
                except ValueError:
                    rel = Path(match)
                refs[rel] = ref_path.exists()
    return refs


def generate_table(files, readme_refs):
    entries = []
    for rel in files:
        cls = classify(rel)
        status = determine_status(rel)
        obs = []
        if rel in readme_refs:
            obs.append('EN_README')
            del readme_refs[rel]
        entries.append((cls, rel.as_posix(), rel.name, status, ';'.join(obs), ''))

    # add missing references
    for ref, exists in list(readme_refs.items()):
        obs = 'LINK_MISSING' if not exists else 'EN_README'
        status = 'faltante' if not exists else determine_status(ref)
        entries.append((classify(ref), ref.as_posix(), ref.name, status, obs, ''))

    entries.sort(key=lambda x: (x[0], x[1]))
    lines = []
    current_class = None
    summary = {}
    for cls, path, name, status, obs, ref in entries:
        summary.setdefault(cls, {}).setdefault(status, 0)
        summary[cls][status] += 1
        if cls != current_class:
            if current_class is not None:
                lines.append('')
            lines.append(f'### {cls}')
            lines.append('| Archivo | Ruta Legacy | Clase | Status | Observaciones | Referencia Registro |')
            lines.append('| --- | --- | --- | --- | --- | --- |')
            current_class = cls
        lines.append(f'| {name} | {path} | {cls} | {status} | {obs} | {ref} |')

    lines.append('\n## Resumen')
    for cls, stats in summary.items():
        total = sum(stats.values())
        status_parts = ', '.join(f'{s}: {c}' for s, c in stats.items())
        lines.append(f'- {cls}: {total} ({status_parts})')

    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate global checklist main.')
    parser.add_argument('--output', default=REPO_ROOT / 'Legacy_RwB_Cons/globalchecklist_main.md', type=Path)
    args = parser.parse_args()

    files = scan_repo()
    refs = readme_references()
    content = generate_table(files, refs)
    args.output.write_text(content, encoding='utf-8')
    print(f'Checklist written to {args.output}')
