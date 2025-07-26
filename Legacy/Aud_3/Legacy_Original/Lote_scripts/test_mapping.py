import re
from scripts.mapping import scan_legacy, append_mapping, parse_args

def test_scan_legacy(tmp_path):
    # create nested files and a directory to exclude
    file_a = tmp_path / "dir" / "a.txt"
    file_a.parent.mkdir(parents=True)
    file_a.write_text("example")
    excluded_dir = tmp_path / "backup"
    file_b = excluded_dir / "b.log"
    excluded_dir.mkdir()
    file_b.write_text("data")

    # without exclude all files are returned
    result = scan_legacy(tmp_path)
    assert set(result) == {file_a.as_posix(), file_b.as_posix()}

    # using exclude should skip the backup dir
    result_exclude = scan_legacy(tmp_path, exclude=["backup"])
    assert set(result_exclude) == {file_a.as_posix()}

def test_append_mapping(tmp_path):
    registry = tmp_path / "registry.md"
    files = ["Legacy/a.txt", "Legacy/b.log"]
    append_mapping(files, registry, destination="target")
    content = registry.read_text()
    # check header and table lines
    assert "## Mapeo automático" in content
    for f in files:
        assert f"| {f} | target |" in content
    # ensure table header exists
    assert re.search(r"\| Ruta Legacy \| Destino propuesto \|", content)


def test_append_mapping_existing_header(tmp_path):
    registry = tmp_path / "registry.md"
    first = ["Legacy/a.txt"]
    second = ["Legacy/b.log"]
    append_mapping(first, registry)
    append_mapping(second, registry)
    content = registry.read_text()
    # header must appear only once
    assert content.count("## Mapeo automático") == 1
    assert content.count("| Ruta Legacy | Destino propuesto |") == 1
    # both entries should be present
    for f in first + second:
        assert f"| {f} | PENDIENTE |" in content


def test_no_header_option(tmp_path):
    registry = tmp_path / "registry.md"
    files = ["Legacy/a.txt"]
    append_mapping(files, registry, add_header=False)
    content = registry.read_text()
    assert "## Mapeo automático" not in content
    assert "| Legacy/a.txt | PENDIENTE |" in content

    args = parse_args(["--no-header"])
    assert args.no_header
