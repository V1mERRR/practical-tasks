from pathlib import Path

L10_PATH = Path(__file__).parent

# Функция для подсчета количества строк в файле
def count_lines(path: Path) -> int:
    with open(path, 'r') as file:  # Открываем файл для чтения
        return len(file.readlines())  # Читаем все строки и возвращаем их количество

# Не изменяй код ниже
if __name__ == "__main__":
    text = "line\nline\nline\nline"
    path = L10_PATH / "example.txt"

    path.write_text(text)  # Записываем текст в файл
    assert count_lines(path) == 4  # Проверяем, что количество строк правильно подсчитано
    path.unlink(missing_ok=True)  # Удаляем файл после проверки
