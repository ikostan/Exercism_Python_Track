def is_leap(year:int):
    '''
    The tricky thing here is that a leap year occurs:
        on every year that is evenly divisible by 4
            except every year that is evenly divisible by 100
                except every year that is evenly divisible by 400
    :param year:
    :return:
    '''

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        if year % 100 != 0:
            return True

    return False

