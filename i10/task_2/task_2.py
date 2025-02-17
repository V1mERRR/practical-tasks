from pathlib import Path

L10_PATH = Path(__file__).parent

# Используем Path и L10_PATH для создания директории с именем name
def create_directory(name: str):
    (L10_PATH / name).mkdir(parents=True, exist_ok=True)  # Создаёт директорию

# Не изменяй код ниже
if __name__ == "__main__":
    name = "tmp"
    path = L10_PATH / name
    assert path.exists() is False

    create_directory(name)
    assert path.exists() is True  # Проверяем, что директория создана
    path.rmdir()  # Удаляем директорию после проверки
