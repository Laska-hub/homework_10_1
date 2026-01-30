"""Модуль для маскировки номеров карт и счетов."""

from typing import List
import logging
from pathlib import Path

# Настройка логера для модуля masks
LOG_DIR: Path = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
masks_logger: logging.Logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    LOG_DIR / "masks.log", mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter(
    fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str:
    """
    Возвращает маску номера карты в формате XXXX XX** **** XXXX.
    Видны первые 6 и последние 4 цифры, остальные скрыты.
    """
    try:
        if not card_number.isdigit() or len(card_number) < 10:
            raise ValueError(
                "Номер карты должен содержать только цифры "
                "и иметь длину не менее 10 символов"
            )

        first_six = card_number[:6]
        last_four = card_number[-4:]
        hidden_part = card_number[6:-4]
        masked_middle = "*" * len(hidden_part)
        masked_number = f"{first_six}{masked_middle}{last_four}"

        # Разбиваем на блоки по 4 символа
        blocks: List[str] = [
            masked_number[i:i + 4] for i in range(0, len(masked_number), 4)
        ]
        result = " ".join(blocks)
        masks_logger.debug(
            f"mask_card_number успешно: {card_number} -> {result}"
        )
        return result

    except ValueError as e:
        masks_logger.error(f"mask_card_number ошибка: {e}")
        raise


def mask_account_number(account_number: str) -> str:
    """
    Возвращает маску банковского счёта в формате **XXXX.
    Видны только последние 4 цифры.
    """
    try:
        if not account_number.isdigit() or len(account_number) < 4:
            raise ValueError(
                "Номер счета должен содержать хотя бы 4 цифры"
            )

        result = f"**{account_number[-4:]}"
        masks_logger.debug(
            f"mask_account_number успешно: {account_number} -> {result}"
        )
        return result

    except ValueError as e:
        masks_logger.error(f"mask_account_number ошибка: {e}")
        raise


if __name__ == "__main__":
    print(mask_card_number("7000792289606361"))
    print(mask_account_number("73654108430135874305"))
