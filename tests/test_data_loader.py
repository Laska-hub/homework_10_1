from unittest.mock import patch
from typing import List, Dict, Any
import pandas as pd

from src.data_loader import load_csv, load_excel


# ---------- Тестирование load_csv ----------

def test_load_csv_success(monkeypatch: Any) -> None:
    df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])

    with patch("pandas.read_csv", return_value=df):
        result: List[Dict[Any, Any]] = load_csv("dummy.csv")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["amount"] == 200


def test_load_csv_file_not_found() -> None:
    result = load_csv("nonexistent.csv")
    assert result == []


def test_load_csv_parser_error(monkeypatch: Any) -> None:
    def raise_parser_error(*args: Any, **kwargs: Any) -> None:
        raise pd.errors.ParserError("Invalid CSV")

    with patch("pandas.read_csv", side_effect=raise_parser_error):
        result = load_csv("invalid.csv")

    assert result == []


# ---------- Тестирование load_excel ----------

def test_load_excel_success(monkeypatch: Any) -> None:
    df = pd.DataFrame([{"id": 1, "amount": 300}, {"id": 2, "amount": 400}])

    with patch("pandas.read_excel", return_value=df):
        result: List[Dict[Any, Any]] = load_excel("dummy.xlsx")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == 300
    assert result[1]["id"] == 2


def test_load_excel_file_not_found() -> None:
    result = load_excel("nonexistent.xlsx")
    assert result == []


def test_load_excel_value_error(monkeypatch: Any) -> None:
    def raise_value_error(*args: Any, **kwargs: Any) -> None:
        raise ValueError("Bad Excel file")

    with patch("pandas.read_excel", side_effect=raise_value_error):
        result = load_excel("invalid.xlsx")

    assert result == []
