def count_words(sentence: str):

    result = dict()
    words = filter_illegal_chars(sentence)

    for word in words:
        if word not in result:
            result[word] = words.count(word)

    return result


def filter_illegal_chars(sentence: str) -> list:

    replaceable = ",:!&@$%^._\n"
    sentence = ''.join(char if char not in replaceable else " " for char in sentence)

    words = [word.lower() for word in sentence.split()]

    for i, word in enumerate(words):
        if "'" in word and (word.index("'") == 0 or word.index("'") == -1):
            words[i] = word.replace("'", "")

    return words
