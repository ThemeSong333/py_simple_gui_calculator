import PySimpleGUI as sg
result_panel = sg.InputText(key='input')
button_0 = sg.Button("0")
button_1 = sg.Button("1")
button_2 = sg.Button("2")
button_3 = sg.Button("3")
button_4 = sg.Button("4")
button_5 = sg.Button("5")
button_6 = sg.Button("6")
button_7 = sg.Button("7")
button_8 = sg.Button("8")
button_9 = sg.Button("9")
button_equals = sg.Button("=")
button_plus = sg.Button("+")
button_divide = sg.Button("/")
button_multiply = sg.Button("*")
button_minus = sg.Button("-")
button_dot = sg.Button(".")
button_clear = sg.Button("C")

current_value = "0"
total = 0
operator = ""

layout = [
    [result_panel, button_clear],
    [button_7, button_8, button_9, button_multiply],
    [button_4, button_5, button_6, button_divide],
    [button_1, button_2, button_3, button_plus],
    [button_0, button_dot, button_minus, button_equals]
]



window = sg.Window('Calculator', layout)



while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    
    # next step handle digit inputs
            
            
    
    
    # update display
    window["input"].update(current_value)
    
    print(f"EVENT: {event}\nVALUES: {values}")

window.close()