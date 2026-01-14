# src/decorators.py
import functools
import sys
from typing import Callable, Optional, Any


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования начала и конца выполнения функции.
    Логи можно писать в файл или в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise  # пробрасываем исключение дальше

        return wrapper

    return decorator
