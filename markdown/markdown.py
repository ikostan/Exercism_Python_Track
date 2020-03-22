import re


def parse(markdown):
    # Split source string in to list by new line
    lines = markdown.split('\n')

    # Flags
    res = ''
    in_list = False
    in_list_append = False

    # Process the list line by line and replace
    # patterns into HTML tags
    for i in lines:

        # Replace hash tag with appropriate header level
        if '#' in i[:7]:
            counter = i[:7].count('#')
            i = '<h{}>'.format(counter) + \
                i[counter + 1:] + \
                '</h{}>'.format(counter)

        m = re.match(r'\* (.*)', i)
        if m:

            curr = m.group(1)

            # Replace double underscore with STRONG tag
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            if m1:
                curr = m1.group(1) + '<strong>' + \
                       m1.group(2) + '</strong>' + \
                       m1.group(3)

            # Replace single underscore with italic
            m1 = re.match('(.*)_(.*)_(.*)', curr)
            if m1:
                curr = m1.group(1) + '<em>' + \
                       m1.group(2) + \
                       '</em>' + \
                       m1.group(3)

            if not in_list:
                in_list = True
                i = '<ul><li>' + curr + '</li>'
            else:
                # List item
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'

        # Replace double underscore with STRONG tag
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + \
                '<strong>' + \
                m.group(2) + \
                '</strong>' + \
                m.group(3)

        # Replace * with EM tag
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + \
                m.group(2) + '</em>' + \
                m.group(3)

        if in_list_append:
            i = '</ul>' + i
            in_list_append = False

        res += i

    if in_list:
        res += '</ul>'

    return res
