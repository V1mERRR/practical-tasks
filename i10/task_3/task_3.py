from pathlib import Path

L10_PATH = Path(__file__).parent

# Используем метод is_file() для проверки, является ли p файлом
def is_file(p: Path):
    return p.is_file()  # Возвращает True, если p — файл, иначе False

# Не изменяй код ниже
if __name__ == "__main__":
    path = L10_PATH / "example.txt"
    path.touch()  # Создаём пустой файл для теста

    assert is_file(path) is True  # Проверка, что это файл
    assert is_file(L10_PATH) is False  # Проверка, что директория — не файл

    path.unlink(missing_ok=True)  # Удаляем файл после проверки
