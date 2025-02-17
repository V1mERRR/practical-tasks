from pathlib import Path

L10_PATH = Path(__file__).parent  # Определяем родительскую директорию текущего файла

# Функция для проверки существования пути
def path_exists(path: str) -> bool:
    return (L10_PATH / path).exists()  # Используем / для объединения путей и проверяем, существует ли путь

# Не изменяй код ниже
if __name__ == "__main__":
    assert path_exists(".") is True  # Проверяем текущую директорию
    assert path_exists("../__init__.py") is True  # Проверяем файл, который находится на уровень выше
    assert path_exists("../task1.py") is True  # Проверяем файл, который находится на уровень выше
    assert path_exists("../wrong.txt") is False  # Проверяем несуществующий файл
    assert path_exists("/wrong/path") is False  # Проверяем несуществующий путь
