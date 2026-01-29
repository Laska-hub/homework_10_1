# tests/test_utils.py

from pathlib import Path

from src.utils import load_operations


def test_load_operations_success(tmp_path: Path) -> None:
    file = tmp_path / "ops.json"
    file.write_text('[{"a": 1}]', encoding="utf-8")

    result = load_operations(str(file))
    assert result == [{"a": 1}]


def test_load_operations_empty() -> None:
    # Файл не существует
    assert load_operations("not_existing.json") == []


def test_load_operations_not_a_list(tmp_path: Path) -> None:
    file = tmp_path / "ops.json"
    file.write_text('{"a": 1}', encoding="utf-8")  # JSON не является списком
    result = load_operations(str(file))
    assert result == []


def test_load_operations_invalid_json(tmp_path: Path) -> None:
    file = tmp_path / "ops.json"
    file.write_text("invalid json", encoding="utf-8")  # Некорректный JSON
    result = load_operations(str(file))
    assert result == []
