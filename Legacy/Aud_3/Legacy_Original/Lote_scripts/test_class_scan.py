from scripts.class_scan import find_class_files, group_by_name
from pathlib import Path


def test_find_class_files(tmp_path):
    (tmp_path / 'a_MTR_doc.md').write_text('x')
    sub = tmp_path / 'sub'
    sub.mkdir()
    (sub / 'b_MTR_other.md').write_text('y')
    files = find_class_files(tmp_path, 'MTR')
    names = {p.name for p in files}
    assert names == {'a_MTR_doc.md', 'b_MTR_other.md'}


def test_group_by_name_duplicates(tmp_path):
    p1 = tmp_path / 'dup_MTR.md'
    p2_dir = tmp_path / 'sub'
    p2_dir.mkdir()
    p2 = p2_dir / 'dup_MTR.md'
    p1.write_text('x')
    p2.write_text('y')
    groups = group_by_name([p1, p2])
    assert set(groups.keys()) == {'dup_MTR.md'}
    assert len(groups['dup_MTR.md']) == 2
