import re


def parse(markdown):
    # Split source string in to list by new line
    lines = markdown.split('\n')

    # Flags
    result = ''
    in_list = False
    in_list_append = False

    # Process the list line by line and replace
    # patterns into HTML tags
    for line in lines:

        line = replace_header(line)

        m = re.match(r'\* (.*)', line)
        if m:

            curr = m.group(1)

            if not in_list:
                in_list = True
                line = ''.join(('<ul><li>',
                                curr,
                                '</li>'))
            else:
                # List item
                line = ''.join(('<li>',
                                curr,
                                '</li>'))
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = '<p>' + line + '</p>'

        line = replace_strong(line)
        line = replace_em(line)

        if in_list_append:
            line = '</ul>' + line
            in_list_append = False

        result += line

    if in_list:
        result += '</ul>'

    return result


def replace_em(line: str) -> str:
    # Replace * with EM tag
    m = re.match('(.*)_(.*)_(.*)', line)
    if m:
        line = ''.join((m.group(1), '<em>',
                        m.group(2), '</em>',
                        m.group(3)))
    return line


def replace_strong(line: str) -> str:
    # Replace double underscore with STRONG tag
    m = re.match('(.*)__(.*)__(.*)', line)
    if m:
        line = ''.join((m.group(1), '<strong>',
                        m.group(2), '</strong>',
                        m.group(3)))
    return line


def replace_header(line: str) -> str:
    # Replace hash tag with appropriate header level
    if '#' in line[:7]:
        counter = line[:7].count('#')
        line = ''.join(('<h{}>'.format(counter),
                        line[counter + 1:],
                        '</h{}>'.format(counter)))
    return line
