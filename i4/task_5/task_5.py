def has_char(s: str, c: str) -> bool:
    for char in s:
        if char == c:
            return True
    return False


# Do not change the below's code
if __name__ == "__main__":
    assert has_char("lfhyt", "f") == True
    assert has_char("abbaabba", "c") == False
