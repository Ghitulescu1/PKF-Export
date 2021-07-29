from get_column import get_collumn

def intesa_euro(valoare, curs, valoare_deviza, tables):
    for i in range(1, tables.n - 1):
            if tables.n < 4:
                if i == 1:
                    curs += get_collumn(tables[i].df[3][2:len(tables[i].df[3]) - 1])
                    valoare_deviza += get_collumn(tables[i].df[6][2:len(tables[i].df[6]) - 1])
            else:
                if i == 1:
                    curs += get_collumn(tables[i].df[3][2:])
                    valoare_deviza += get_collumn(tables[i].df[6][2:])
                elif i == (tables.n - 2):
                    curs += get_collumn(tables[i].df[3][1:len(tables[i].df[3]) - 1])
                    valoare_deviza += get_collumn(tables[i].df[6][1:len(tables[i].df[6]) - 1])
    for value in valoare_deviza:
        index = valoare_deviza.index(value)
        valoare_deviza[index] = value.replace(',', '')
    for value in curs:
        index = curs.index(value)
        curs[index] = value.replace(',', '.')
        numarCurs = float(curs[index])
        numarDeviza = float(valoare_deviza[index])
        valoare[index] = float(numarCurs * numarDeviza)