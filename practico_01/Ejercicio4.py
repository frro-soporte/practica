def vocal(c):
    if (c == "a") or (c == "e") or (c == "i") or (c == "o") or (c == "u"):
        return True
    else:
        return False


assert vocal("a")
assert vocal("b") is False

