"""Модуль для считывания финансовых операций из CSV и Excel файлов."""

import logging
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

# ---------------------- Настройка логирования ---------------------- #
LOG_DIR: Path = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
data_logger: logging.Logger = logging.getLogger("data_loader")
data_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_DIR / "data_loader.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
data_logger.addHandler(file_handler)

# ---------------------- Функции для чтения ---------------------- #


def load_csv(path: str) -> List[Dict[Any, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    :param path: путь к CSV-файлу
    :return: список словарей с транзакциями
    """
    try:
        df = pd.read_csv(path)
        data: List[Dict[Any, Any]] = df.to_dict(orient="records")
        data_logger.debug(f"CSV успешно загружен: {path}, " f"записей: {len(data)}")
        return data
    except FileNotFoundError:
        data_logger.error(f"CSV файл не найден: {path}")
        return []
    except pd.errors.ParserError as e:
        data_logger.error(f"Ошибка парсинга CSV: {path}, {e}")
        return []


def load_excel(path: str) -> List[Dict[Any, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    :param path: путь к Excel-файлу
    :return: список словарей с транзакциями
    """
    try:
        df = pd.read_excel(path)
        data: List[Dict[Any, Any]] = df.to_dict(orient="records")
        data_logger.debug(f"Excel успешно загружен: {path}, " f"записей: {len(data)}")
        return data
    except FileNotFoundError:
        data_logger.error(f"Excel файл не найден: {path}")
        return []
    except ValueError as e:
        data_logger.error(f"Ошибка чтения Excel: {path}, {e}")
        return []


# ---------------------- Блок проверки ---------------------- #


if __name__ == "__main__":
    csv_path = "data/transactions.csv"
    excel_path = "data/transactions_excel.xlsx"

    csv_data = load_csv(csv_path)
    print("CSV данные:")
    print(csv_data)

    excel_data = load_excel(excel_path)
    print("\nExcel данные:")
    print(excel_data)
