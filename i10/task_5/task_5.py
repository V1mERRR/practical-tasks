from pathlib import Path

L10_PATH = Path(__file__).parent

# Функция для чтения содержимого файла с использованием open
def read(path: Path) -> str:
    with open(path, 'r') as file:  # Открываем файл для чтения
        return file.read()  # Читаем все содержимое и возвращаем как строку

# Не изменяй код ниже
if __name__ == "__main__":
    text = "Hello World!"
    path = L10_PATH / "example.txt"
    path.write_text(text)  # Записываем текст в файл

    assert read(path) == text  # Проверяем, что прочитанный текст совпадает с ожидаемым

    path.unlink(missing_ok=True)  # Удаляем файл после проверки
