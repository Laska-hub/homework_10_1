import pytest
from src.decorators import log

def test_log_console(capsys: pytest.CaptureFixture[str]) -> None:
    @log()  # без filename, чтобы вывод шел в консоль
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(3, 5)
    assert result == 15

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out
