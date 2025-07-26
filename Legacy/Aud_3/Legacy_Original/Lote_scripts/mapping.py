import argparse
import datetime
from pathlib import Path

LEGACY_DIR = Path('Legacy')
REGISTRY_FILE = Path('registro_trazabilidad_total.md')


def scan_legacy(directory: Path = LEGACY_DIR, exclude=None):
    """Return a list of legacy files relative to repository root.

    Parameters
    ----------
    directory : Path, optional
        Base directory to scan. Defaults to ``LEGACY_DIR``.
    exclude : list[str] | None
        List of directories to omit from the scan. Each path can be absolute or
        relative to ``directory``.
    """

    exclude_paths = []
    if exclude:
        for ex in exclude:
            ex_path = Path(ex)
            if not ex_path.is_absolute():
                ex_path = directory / ex_path
            exclude_paths.append(ex_path.resolve())

    files = []
    for path in directory.rglob("*"):
        if exclude_paths and any(ep in path.resolve().parents for ep in exclude_paths):
            continue
        if path.is_file():
            files.append(path.as_posix())
    return files


def append_mapping(
    files,
    registry: Path = REGISTRY_FILE,
    destination: str = "PENDIENTE",
    add_header: bool = True,
):
    """Append mapping information to the registry file if not already present.

    Parameters
    ----------
    files : list[str]
        List of source paths to append.
    registry : Path, optional
        Path to the registry file. Defaults to ``REGISTRY_FILE``.
    destination : str, optional
        Default value for the destination column. Defaults to ``"PENDIENTE"``.
    """
    existing = set()
    content = ""
    if registry.exists():
        with registry.open("r", encoding="utf-8") as fh:
            content = fh.read()
        for line in content.splitlines():
            if line.startswith("|") and "|" in line[1:]:
                path = line.split("|")[1].strip()
                existing.add(path)

    new_entries = [f for f in files if f not in existing]
    if not new_entries:
        return

    date_str = datetime.date.today().isoformat()
    header_line = f"## Mapeo automático ({date_str})"
    table_header = "| Ruta Legacy | Destino propuesto |\n| --- | --- |\n"

    lines = []
    if add_header:
        if header_line not in content:
            lines.append(f"\n{header_line}\n")
            lines.append(table_header)
    for src in sorted(new_entries):
        lines.append(f"| {src} | {destination} |\n")

    with registry.open('a', encoding='utf-8') as fh:
        fh.writelines(lines)


def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Generar tabla de mapeo legacy→RwB")
    parser.add_argument(
        "directory",
        nargs="?",
        default=str(LEGACY_DIR),
        help="Carpeta a escanear (por defecto 'Legacy/')",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=str(REGISTRY_FILE),
        help="Archivo de registro (por defecto 'registro_trazabilidad_total.md')",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Directorio a excluir (se puede usar varias veces)",
    )
    parser.add_argument(
        "-d",
        "--destination",
        default="PENDIENTE",
        help="Valor por defecto para la columna destino",
    )
    parser.add_argument(
        "--no-header",
        action="store_true",
        help="No agregar el encabezado con la fecha actual",
    )
    return parser.parse_args(args)


def main():
    args = parse_args()
    directory = Path(args.directory)
    registry = Path(args.output)
    files = scan_legacy(directory, exclude=args.exclude)
    append_mapping(
        files,
        registry,
        destination=args.destination,
        add_header=not args.no_header,
    )


if __name__ == "__main__":
    main()

