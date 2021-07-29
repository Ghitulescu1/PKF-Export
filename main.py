from numpy import row_stack
from get_column import get_collumn
from change_date import change_date
from intesa_euro import intesa_euro
from remove_string import remove_string
from comments import comments

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
    tables = camelot.read_pdf(filePath, pages = 'all', line_scale=40, strip_text='\n', process_background=True)
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
    elif fileType == "Intesa SanPaolo":
        import pandas as pd
        for i in range(0, tables.n):
            print(tables[i].df["1"])
            #print(tables[i].df[0], df.Name.str.split(expand=True))
            print("///////////////////////")
            print(i)
            print("///////////////////////")

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
        from alpha_date import alpha_date
        alpha_date(obj["Data"])
        alpha_date(obj["Data scadenta"])

    import pandas as pd
    df = pd.DataFrame(data=obj)
    print (df)

    import csv
    #df.to_csv(fileDest, mode = 'w', index = False)