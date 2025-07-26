import os
import shutil
from pathlib import Path
import re

REGISTRY = Path('registro_trazabilidad_total.md')
LEGACY_ROOT = Path('Legacy')
UNIVERSAL_ROOT = Path('universal/projects')
BACKUP_ROOT = Path('backup/PR/projects')


def parse_registry():
    entries = []
    pattern = re.compile(r"^\|\s*(Legacy\/[^|]+)\s*\|\s*PENDIENTE\s*\|")
    with REGISTRY.open('r', encoding='utf-8') as fh:
        for line in fh:
            m = pattern.match(line)
            if m:
                entries.append(m.group(1))
    return entries


def migrate_project_files(paths):
    REG_LINES = REGISTRY.read_text().splitlines()
    new_lines = []
    for line in REG_LINES:
        m = re.match(r"^(\|\s*(Legacy\/[^|]+)\s*\|)\s*PENDIENTE(\s*\|)", line)
        if m:
            legacy_path = m.group(2)
            if legacy_path.startswith('Legacy/PR/projects/'):
                rel = Path(legacy_path).relative_to('Legacy/PR/projects')
                dest_path = UNIVERSAL_ROOT / rel
                backup_path = BACKUP_ROOT / rel
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                src = Path(legacy_path)
                if src.exists():
                    shutil.copy2(src, dest_path)
                    shutil.move(src, backup_path)
                line = f"| {legacy_path} | {dest_path.as_posix()} |"
        new_lines.append(line)
    REGISTRY.write_text('\n'.join(new_lines), encoding='utf-8')


if __name__ == '__main__':
    paths = parse_registry()
    migrate_project_files(paths)
