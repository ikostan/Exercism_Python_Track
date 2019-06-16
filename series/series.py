def slices(series, length):
    return [series[start:length + start] for start in range(len(series))
            if len(series[start:length + start]) == length]
