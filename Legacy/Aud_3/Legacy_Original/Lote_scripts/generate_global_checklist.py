from pathlib import Path
import os
import re
import argparse
import csv

# Directory to scan - repo root
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
    for root, _, filenames in os.walk(base):
        for fname in filenames:
            full = Path(root) / fname
            rel = full.relative_to(base)
            files.append(rel)
    return files


def determine_status(path: Path) -> str:
    # Simple heuristic: files under Legacy are pending, others are migrated
    parts = path.parts
    if parts and parts[0].lower() == 'legacy':
        return 'pendiente'
    else:
        return 'migrado'


def generate_table(files):
    # Group by class
    entries = []
    for rel in files:
        cls = classify(rel)
        status = determine_status(rel)
        entries.append((cls, rel.as_posix(), rel.name, status))
    entries.sort(key=lambda x: (x[0], x[1]))
    lines = []
    current_class = None
    for cls, path, name, status in entries:
        if cls != current_class:
            if current_class is not None:
                lines.append('\n')
            lines.append(f"### {cls}")
            lines.append('| Archivo | Ruta Legacy | Clase | Status | Observaciones | Referencia Registro |')
            lines.append('| --- | --- | --- | --- | --- | --- |')
            current_class = cls
        lines.append(f"| {name} | {path} | {cls} | {status} | | |")
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate global checklist.')
    parser.add_argument('--output', default=REPO_ROOT / 'Legacy_RwB_Cons/global_checklist.md', type=Path)
    args = parser.parse_args()

    files = scan_repo()
    content = generate_table(files)
    args.output.write_text(content, encoding='utf-8')
    print(f'Checklist written to {args.output}')
