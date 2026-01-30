"""Модуль для работы с операциями из JSON-файлов."""

import json
from pathlib import Path
from typing import Any, List
import logging

# Настройка логера для модуля utils
LOG_DIR: Path = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
utils_logger: logging.Logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    LOG_DIR / "utils.log", mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter(
    fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def load_operations(path: str) -> List[dict[str, Any]]:
    """Загружает операции из JSON-файла."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            utils_logger.warning(
                f"{path} не содержит список операций"
            )
            return []

        utils_logger.debug(
            f"load_operations успешно загружено {len(data)} операций "
            f"из {path}"
        )
        return data

    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {path}")
        return []

    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON: {path}")
        return []


if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent
    ops_file = base_dir / "data" / "operations.json"

    ops = load_operations(str(ops_file))
    print(ops)
