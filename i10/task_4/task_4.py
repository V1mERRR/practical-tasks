from pathlib import Path

L10_PATH = Path(__file__).parent

# Функция для чтения содержимого файла и возврата его как строки
def read(path: Path) -> str:
    return path.read_text()  # Читает текстовый файл и возвращает его содержимое как строку

# Не изменяй код ниже
if __name__ == "__main__":
    text = "Hello World!"
    path = L10_PATH / "example.txt"
    path.write_text(text)  # Записываем текст в файл

    assert read(path) == text  # Проверяем, что прочитанный текст соответствует ожидаемому

    path.unlink(missing_ok=True)  # Удаляем файл после проверки
