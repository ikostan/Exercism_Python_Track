def slices(series, length):
    if not series or series == '':
        raise ValueError('Empty series is invalid')
    elif length < 0:
        raise ValueError('Length can not be negative')
    elif length == 0:
        raise ValueError('Length can not be zero')
    elif length > len(series):
        raise ValueError('Length is too large')
    else:
        return [series[start:length + start] for start in range(len(series))
                if len(series[start:length + start]) == length]
