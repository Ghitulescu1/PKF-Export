def remove_string(dataType):
    for value in dataType:
        index = dataType.index(value)
        dataType[index] = str(''.join(c for c in value if c.isdigit() or c == '.'))
    return dataType