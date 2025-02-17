from pathlib import Path

L10_PATH = Path(__file__).parent

# Функция для записи содержимого в файл
def write(path: Path, content: str):
    with open(path, 'w') as file:  # Открываем файл в режиме записи ('w')
        file.write(content)  # Записываем содержимое в файл

# Не изменяй код ниже
if __name__ == "__main__":
    text = "Hello World!"
    path = L10_PATH / "example.txt"

    assert path.exists() is False  # Проверка, что файла нет
    write(path, text)  # Записываем текст в файл
    assert path.exists() is True  # Проверка, что файл появился
    assert path.read_text() == text  # Проверяем, что содержимое файла соответствует тексту

    path.unlink(missing_ok=True)  # Удаляем файл после проверки
