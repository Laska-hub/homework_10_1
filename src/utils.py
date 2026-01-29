import json
from pathlib import Path
from typing import Any, List


def load_operations(path: str) -> List[dict[str, Any]]:
    """Загружает операции из JSON-файла."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        return []


if __name__ == "__main__":
    # Автоматически ищем data/operations.json относительно этого скрипта
    base_dir = Path(__file__).parent.parent
    ops_file = base_dir / "data" / "operations.json"

    ops = load_operations(str(ops_file))
    print(ops)
