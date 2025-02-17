def join(s1: str, s2: str) -> str:
    return f"{s1} {s2}"

# Do not change the below code
if __name__ == "__main__":
    a, b = "Jon", "Doe"

    assert join(a, b) == "Jon Doe"
    assert join(b, a) == "Doe Jon"
    assert join("aba", "baba") == "aba baba"
