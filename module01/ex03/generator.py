import random

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yields the substrings."""
    if not isinstance(text, str) or not isinstance(sep, str):
        yield "ERROR"
        return

    if option not in (None, "shuffle", "unique", "ordered"):
        yield "ERROR"
        return

    words = text.split(sep)

    if option == "shuffle":
        for i in range(len(words) - 1, 0, -1):
            j = random.randint(0, i)
            words[i], words[j] = words[j], words[i]
    elif option == "unique":
        words = list(dict.fromkeys(words))
    elif option == "ordered":
        words.sort()

    for word in words:
        yield word
    return