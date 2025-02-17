def count_chars(s: str) -> dict[str, int]:
    # Создаем пустой словарь для хранения подсчета символов
    char_count = {}
    
    # Проходим по каждому символу в строке
    for char in s:
        # Увеличиваем счетчик для символа
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count


# Do not change the below's code
if __name__ == "__main__":
    assert count_chars("aabc") == {"a": 2, "b": 1, "c": 1}
    assert count_chars("abc") == {"a": 1, "b": 1, "c": 1}
    assert count_chars("") == {}
