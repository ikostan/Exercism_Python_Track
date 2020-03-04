import re


def parse(markdown: str) -> str:
    lines = markdown.split('\n')
    result = ""

    for line in lines:

        # Add paragraph tag
        if line[0].isalpha():
            line = '<p>' + line + '</p>'

        # Replace double underscore at the beginning/end of the markdown with STRONG tag
        if line[0:2] == '__':
            line = '<p><strong>' + line[2:len(line) - 2] + '</strong></p>'

        # Replace double underscore with STRONG tag
        if '__' in line:
            i = 0
            while '__' in line:
                n = line.find('__')

                if i == 0:
                    line = line[:n] + '<strong>' + line[n + 2:]
                    i = 1
                else:
                    line = line[:n] + '</strong>' + line[n + 2:]
                    i = 0

        # Replace single underscore at the beginning/end of the markdown with italic and header
        if line[0] == '_' and line[0:2] != '__':
            line = '<p><em>' + line[1:len(line) - 1] + '</em></p>'

        # Replace single underscore with italic
        if '_' in line:
            i = 0
            while '_' in line:
                n = line.find('_')

                if i == 0:
                    line = line[:n] + '<em>' + line[n + 1:]
                    i = 1
                else:
                    line = line[:n] + '</em>' + line[n + 1:]
                    i = 0

        # Replace hash tag with appropriate header level
        if line[0] == '#':
            n = line.count('#', 0, 7)
            line = '<h{}>'.format(n) + line[n + 1:] + '</h{}>'.format(n)

        # Replace * with list item
        if '*' in line:

            if ' * ' in line:
                line = line.replace(' * ', ' + ')

            while '*' in line:
                n = line.find('*')
                line = line[:n] + '<li>' + line[n + 2:] + '</li>'

            if ' + ' in line:
                line = line.replace(' + ', ' * ')

        result += line

    # Wrap list items
    if '<li>' in result:
        # Find index of first occurrence of a substring in a string
        n = result.find('<li>')
        result = result[:n] + '<ul>' + result[n:]

        # Find index of last occurrence of a substring in a string
        n = result.rfind('</li>')
        result = result[:n + 5] + '</ul>' + result[n + 5:]

    return result
