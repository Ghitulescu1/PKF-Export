def append_comment(debit, credit, val_debit, val_credit):
    debit.append(val_debit)
    credit.append(val_credit)

def get_collumn(table):
    obj = []
    for i in table:
        obj.append(i)
    return obj

def remove_string(dataType):
    for value in dataType:
        index = dataType.index(value)
        dataType[index] = str(''.join(c for c in value if c.isdigit() or c == '.'))
    return dataType

def change_date(dataType):
    for value in dataType:
        index = dataType.index(value)
        date = value.replace('.', '')
        import datetime
        datetimeobject = datetime.datetime.strptime(date, '%d%m%Y')
        dataType[index] = datetimeobject.strftime('%Y%m%d')
    return dataType

def alpha_date(dataType):
    for value in dataType:
        index = dataType.index(value)
        date = value.replace(' ', '')
        import datetime
        datetimeobject = datetime.datetime.strptime(date, '%d%b%Y')
        dataType[index] = datetimeobject.strftime('%Y%m%d')
    return dataType
        
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

def comments(dataType, debit, credit):
    for value in dataType:
        val_comision = 627
        val_virament = 766
        val_atm_alimentare = 581
        val_pos_plata = 401
        val_standard = 5121
        val_incasare = 4111
        virament = "VIRAMENT DOBANDA"
        incasare, incasare2, incasare3 = "INCASARE INT", "INCASARE FACT", "INCASARE OP"
        alimentare = "ALIMENTARE CARDURI"
        transfer = "TRANSFER SOLD"
        retragere = "RETRAGERE NUMERAR"
        schimb = "SCHIMB"
        comision, comision2 = "COMISION", "COM."
        plata, plata2, plata3, plata4 = "PLATA", "VANZARE POS", "PLATI", "TRANZ. POS"
        atm = "UTILIZ. CARD LA ATM"
        
        if plata4 in value.upper():
            append_comment(debit, credit, val_pos_plata, val_standard)
        elif comision in value.upper():
            append_comment(debit, credit, val_comision, val_standard)
        elif comision2 in value.upper():
            append_comment(debit, credit, val_comision, val_standard)
        elif incasare in value.upper():
            append_comment(debit, credit, val_standard, val_incasare)
        elif incasare2 in value.upper():
            append_comment(debit, credit, val_standard, val_incasare)
        elif incasare3 in value.upper():
            append_comment(debit, credit, val_standard, val_incasare)
        elif plata in value.upper():
            append_comment(debit, credit, val_pos_plata, val_standard)
        elif plata2 in value.upper():
            append_comment(debit, credit, val_pos_plata, val_standard)
        elif plata3 in value.upper():
            append_comment(debit, credit, val_pos_plata, val_standard)
        elif atm in value.upper():
            append_comment(debit, credit, val_atm_alimentare, val_standard)
        elif alimentare in value.upper():
            append_comment(debit, credit, val_standard, val_atm_alimentare)
        elif transfer in value.upper():
            append_comment(debit, credit, val_atm_alimentare, val_standard)
        elif retragere in value.upper():
            append_comment(debit, credit, val_atm_alimentare, val_standard)
        elif schimb in value.upper():
            append_comment(debit, credit, val_atm_alimentare, val_standard)
        elif virament in value.upper():
            append_comment(debit, credit, val_standard, val_virament)
        else:
            append_comment(debit, credit, "", "")
        
def main(filePath, fileDest, fileType, valutaType):

    print("PDF: " + filePath)
    print("Dest: " + fileDest)
    print("Type: " + fileType)
    print("Currency Type: " + valutaType)

    obj = {"Nr. inreg.": "", "Tip inregistrare": "Banca", "Jurnal": "JB", "Data": [], "Data scadenta": [], "Numar Document": "Extras bancar 1", 
            "Cont debit simbol": [], "Cont debit titlu": "", "Cont credit simbol": [], "Cont credit titlu": "", "Explicatie": [], 
            "Valoare": [], "Partener CIF": "", "Partener Nume": "", "Partener Rezidenta": "", "Partener Judet": "", 
            "Partener Cont": "", "Angajat CNP": "", "Angajat Nume": "", "Angajat Cont": "", "Optiune TVA": "", "Cota TVA": "", 
            "Moneda": "", "Curs": "", "Valoare deviza": "", "Stornare-Nr. inreg.": "", "Incasari/Plati": "", "Diferente curs": "", 
            "TVA la incasare": "0", "Colectare/Deducere TVA": "", "Efect de incasat/platit": "", "Banca efect": "", "Centre de cost": "", 
            "Informatii export": "", "Punct de lucru": "", "Deductibilitate": "", "Reevaluare": "", "Factura simplificata": "", 
            "Borderou de achizitie": "", "Carnet prod. Agricole": ""}
    import  camelot
    tables = camelot.read_pdf(filePath, pages = 'all', line_scale=40, strip_text='\n')
    if fileType == "Intesa":
        for i in range(1, tables.n - 1):
            if tables.n < 4:
                if i == 1:
                    obj["Data"] += get_collumn(tables[i].df[0][2:len(tables[i].df[2]) - 1])
                    obj["Data scadenta"] += get_collumn(tables[i].df[0][2:len(tables[i].df[2]) - 1])
                    obj["Explicatie"] += get_collumn(tables[i].df[2][2:len(tables[i].df[2]) - 1])
                    obj["Valoare"] += get_collumn(tables[i].df[6][2:len(tables[i].df[6]) - 1])
            else:
                if i == 1:
                    obj["Data"] += get_collumn(tables[i].df[0][2:])
                    obj["Data scadenta"] += get_collumn(tables[i].df[0][2:])
                    obj["Explicatie"] += get_collumn(tables[i].df[2][2:])
                    obj["Valoare"] += get_collumn(tables[i].df[6][2:])
                elif i < (tables.n - 2):
                    obj["Data"] += get_collumn(tables[i].df[0][1:len(tables[i].df[2])])
                    obj["Data scadenta"] += get_collumn(tables[i].df[0][1:len(tables[i].df[2])])
                    obj["Explicatie"] += get_collumn(tables[i].df[2][1:len(tables[i].df[2])])
                    obj["Valoare"] += get_collumn(tables[i].df[6][1:len(tables[i].df[6])])
                elif i == (tables.n - 2):
                    obj["Data"] += get_collumn(tables[i].df[0][1:len(tables[i].df[2]) - 1])
                    obj["Data scadenta"] += get_collumn(tables[i].df[0][1:len(tables[i].df[2]) - 1])
                    obj["Explicatie"] += get_collumn(tables[i].df[2][1:len(tables[i].df[2]) - 1])
                    obj["Valoare"] += get_collumn(tables[i].df[6][1:len(tables[i].df[6]) - 1])
            if valutaType == "EURO":
                obj["Curs"] = []
                obj["Valoare deviza"] = []
                intesa_euro(obj["Valoare"], obj["Curs"], obj["Valoare deviza"], tables)
            else:
                remove_string(obj["Valoare"])   
        comments(obj["Explicatie"], obj["Cont debit simbol"], obj["Cont credit simbol"])
        change_date(obj["Data"])
        change_date(obj["Data scadenta"])
        
    elif fileType == "Otp":
        for i in range(0, tables.n):
            obj["Data"] += get_collumn(tables[i].df[0][1:])
            obj["Data scadenta"] += get_collumn(tables[i].df[0][1:])
            obj["Explicatie"] += get_collumn(tables[i].df[3][1:])
            obj["Valoare"] += get_collumn(tables[i].df[4][1:])
        remove_string(obj["Valoare"])
        comments(obj["Explicatie"], obj["Cont debit simbol"], obj["Cont credit simbol"])
        change_date(obj["Data"])
        change_date(obj["Data scadenta"])
    elif fileType == "Alpha":
        for i in range(0, tables.n):
            if i != 0:
                obj["Data"] += get_collumn(tables[i].df[1][0:])
                obj["Data scadenta"] += get_collumn(tables[i].df[1][0:])
                obj["Explicatie"] += get_collumn(tables[i].df[2][0:])
                obj["Valoare"] += get_collumn(tables[i].df[4][0:])
            else:
                obj["Data"] += get_collumn(tables[i].df[1][2:])
                obj["Data scadenta"] += get_collumn(tables[i].df[1][2:])
                obj["Explicatie"] += get_collumn(tables[i].df[2][2:])
                obj["Valoare"] += get_collumn(tables[i].df[4][2:])
        remove_string(obj["Valoare"])
        comments(obj["Explicatie"], obj["Cont debit simbol"], obj["Cont credit simbol"])
        alpha_date(obj["Data"])
        alpha_date(obj["Data scadenta"])

    import pandas as pd
    df = pd.DataFrame(data=obj)
    print (df)

    import csv
    df.to_csv(fileDest, mode = 'w', index = False)

shoud_be_open = True
while shoud_be_open:
    list = ['Alpha', 'Intesa', 'Otp']
    valuta_list = ['RON', 'EURO']
    import PySimpleGUIQt as sg
    layout = [
        [sg.Text(' Selecteaza fisierul')],
        [sg.Input(key = 'input_file'), sg.FileBrowse('Cauta', size = (70, 35), file_types=(("Fisiere PDF", "*.pdf"),))],
        [sg.Text(' Selecteaza tipul bancii       '), sg.Text('Selecteaza valuta')],
        [sg.Stretch(), sg.Listbox(list, size=(20,3), enable_events = True, key='_LIST_'), 
        sg.Listbox(valuta_list, size=(20,3), default_values=['RON'], enable_events = True, key='_VALUTA_LIST_'), sg.Stretch()],
        [sg.Text(' Selecteaza directorul de salvare')],
        [sg.Input(key = 'folder'), sg.FolderBrowse('Cauta folder', size = (115, 35))],
        [sg.Stretch(), sg.Button('Export', size = (75, 35)), sg.Exit('Inchide', size = (75, 35)), sg.Stretch()]
    ]

    error_layout =  [
        [sg.Text('Nu ati selectat corect datele', justification = 'c')],
        [sg.Stretch(), sg.Exit('Inchide', size = (80, 35)), sg.Stretch()]
    ]

    check_file_layout =  [
        [sg.Text('Exista deja un fisier cu acest nume', justification = 'c')],
        [sg.Stretch(), sg.Exit('Inchide', size = (80, 35)), sg.Stretch()]
    ]

    window = sg.Window('PKF Export', layout, size=(400, 380))
    error_window = sg.Window('Eroare!', error_layout, size=(265, 80), finalize=True)
    check_file_window = sg.Window('Eroare!', check_file_layout, size=(265, 80), finalize=True)
    error_window.Hide()
    check_file_window.Hide()
    
    inputFile = None
    inputType = None
    folderPath = None
    valutaType = None

    while True:
        event, values = window.read()
        if event == 'Export':
            inputFile = str(values['input_file'])
            inputType = values['_LIST_']
            valutaType = values['_VALUTA_LIST_']
            folderPath = str(values['folder'])
            if inputFile and inputType and folderPath and valutaType:
                import os
                base = os.path.basename(inputFile)
                fileName = os.path.splitext(base)[0]
                filePath = os.path.join(folderPath, fileName + ".csv")
                check = os.path.isfile(filePath)
                if check == False:
                    try:
                        main(inputFile, filePath, inputType[0], valutaType[0])
                    except Exception as inst:
                        print(inst)
                    window.close()
                    break
                else:
                    check_file_window.UnHide()
                    while True:
                        event, values = check_file_window.read()
                        if event in (None, 'Inchide'):
                            break
                    check_file_window.Hide()
            else:
                error_window.UnHide()
                while True:
                    event, values = error_window.read()
                    if event in (None, 'Inchide'):
                        break
                error_window.Hide()
        elif event == sg.WIN_CLOSED or event == "Inchide":
            shoud_be_open = False
            break