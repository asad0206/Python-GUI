import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkTeal9')

Excel_File = 'Data_Entry.xlsx'
df = pd.read_excel(Excel_File)

layout = [
    [sg.Text('Fill in the following fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('City', size=(15,1)), sg.InputText(key='City')],
    [sg.Text('Favourite Color', size=(15,1)), sg.Combo(['Green', 'Blue', 'Red'], key='Favourite Color')],
    [sg.Text('Language', size=(15,1)),
                        sg.Checkbox('German', key='German'),
                        sg.Checkbox('French', key='French'),
                        sg.Checkbox('Spanish', key='Spanish')
    ],
    [sg.Text('No. of Children', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                       initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(Excel_File, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()