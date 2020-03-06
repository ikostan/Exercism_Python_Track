PATTERNS = {
    'p': ('<p>', '</p>'),
    '__': ('<strong>', '</strong>'),
    '_': ('<em>', '</em>'),
    '#': ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'),
    '*': ('<ul>', '</ul>', '<li>', '</li>')
}


def parse(markdown: str) -> str:
    lines = markdown.split('\n')
    result = ""

    for line in lines:

        # Add paragraph tag
        if line[0].isalpha():
            line = PATTERNS['p'][0] + line + PATTERNS['p'][1]

        # Replace double underscore at the beginning/end of the markdown with STRONG tag
        if line[0:2] == '__':
            line = PATTERNS['p'][0] + \
                   PATTERNS['__'][0] + \
                   line[2:len(line) - 2] + \
                   PATTERNS['__'][1] + \
                   PATTERNS['p'][1]

        # Replace double underscore with STRONG tag
        if '__' in line:
            line = replace_pattern(line, '__', PATTERNS['__'], 2)

        # Replace single underscore at the beginning/end of the markdown with italic and header
        if line[0] == '_' and line[0:2] != '__':
            line = PATTERNS['p'][0] + \
                   PATTERNS['_'][0] + \
                   line[1:len(line) - 1] + \
                   PATTERNS['_'][1] + \
                   PATTERNS['p'][1]

        # Replace single underscore with italic
        if '_' in line:
            line = replace_pattern(line, '_', PATTERNS['_'], 1)

        # Replace hash tag with appropriate header level
        if line[0] == '#':
            n = line.count('#', 0, 7)
            line = '<{}>'.format(PATTERNS['#'][n - 1]) + \
                   line[n + 1:] + \
                   '</{}>'.format(PATTERNS['#'][n - 1])

        # Replace * with list item
        if '*' in line:

            if ' * ' in line:
                line = line.replace(' * ', ' + ')

            while '*' in line:
                n = line.find('*')
                line = line[:n] + \
                       PATTERNS['*'][2] + \
                       line[n + 2:] + \
                       PATTERNS['*'][3]

            if ' + ' in line:
                line = line.replace(' + ', ' * ')

        result += line

    # Wrap list items
    if '<li>' in result:
        # Find index of first occurrence of a substring in a string
        n = result.find('<li>')
        result = result[:n] + \
                 PATTERNS['*'][0] + \
                 result[n:]

        # Find index of last occurrence of a substring in a string
        n = result.rfind('</li>')
        result = result[:n + 5] + \
                 PATTERNS['*'][1] + \
                 result[n + 5:]

    return result


def replace_pattern(line: str,
                    pattern: str,
                    new_pattern: tuple,
                    index: int) -> str:
    """
    Replace string pattern based on user criteria
    """
    i = 0
    while pattern in line:
        n = line.find(pattern)

        if i == 0:
            line = line[:n] + new_pattern[0] + line[n + index:]
            i = 1
        else:
            line = line[:n] + new_pattern[1] + line[n + index:]
            i = 0

    return line
