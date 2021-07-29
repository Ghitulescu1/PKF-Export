from main import main

shoud_be_open = True
while shoud_be_open:
    list = ['Alpha', 'Intesa', 'Otp', 'Intesa SanPaolo']
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