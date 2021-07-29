from append_comment import append_comment

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