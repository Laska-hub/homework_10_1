import pytest
from pathlib import Path

from src.decorators import log


def test_log_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    """Успешный вызов без filename — лог в консоль"""

    @log()
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(3, 5)
    assert result == 15

    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_success_to_file(tmp_path: Path) -> None:
    """Успешный вызов с filename — лог в файл"""

    log_file = tmp_path / "success.log"

    @log(filename=str(log_file))
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    assert result == 5

    content = log_file.read_text()
    assert "add ok" in content


def test_log_error_to_file(tmp_path: Path) -> None:
    """Ошибка с filename — лог ошибки в файл"""

    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    content = log_file.read_text()
    assert "divide error" in content
    assert "ZeroDivisionError" in content


def test_log_error_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Ошибка без filename — лог ошибки в консоль"""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "ZeroDivisionError" in captured.out

