def change_date(dataType):
    for value in dataType:
        index = dataType.index(value)
        date = value.replace('.', '')
        import datetime
        datetimeobject = datetime.datetime.strptime(date, '%d%m%Y')
        dataType[index] = datetimeobject.strftime('%Y%m%d')
    return dataType