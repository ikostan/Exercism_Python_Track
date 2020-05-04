def decode(string: str) -> str:

    if not string:
        return ""

    strings = list()
    for char in string:

        if char.isdigit():
            if len(strings) > 0 and strings[-1].isdigit():
                strings[-1] += char
            else:
                strings.append(char)
        else:
            strings.append(char)

    result = ''
    for i, string in enumerate(strings):
        if string.isdigit():
            result += (int(string) - 1) * strings[i + 1]
        else:
            result += string

    return result


def encode(string: str) -> str:

    if not string:
        return ""

    results = list()
    temp = string[0]
    counter = 0

    for i in range(0, len(string)):

        if string[i] == temp:
            counter += 1
        else:
            if counter > 1:
                results.append(str(counter))
            results.append(string[i - 1])
            counter = 1
            temp = string[i]

        if i == len(string) - 1:
            if counter > 1:
                results.append(str(counter))
            results.append(string[i])

    return ''.join(results)
