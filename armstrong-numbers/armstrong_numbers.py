def is_armstrong_number(number):
    power = len(str(number))
    return number == eval(' + '.join([str((int(n) ** power)) for n in str(number)]))


