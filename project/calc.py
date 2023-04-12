import PySimpleGUI as sg

# colors, fonts, sizes
button_size = (4,2)
pop_up_size = (40, 40)
digits_color="blue"
operator_color="green"
clear_button_color="red"
global_font = ("Consolas", 14)

# elements of calculator
result_panel = sg.InputText(size=(20,1), key='input', disabled=True)
button_0 = sg.Button("0", size=button_size, button_color=digits_color)
button_1 = sg.Button("1", size=button_size, button_color=digits_color)
button_2 = sg.Button("2", size=button_size, button_color=digits_color)
button_3 = sg.Button("3", size=button_size, button_color=digits_color)
button_4 = sg.Button("4", size=button_size, button_color=digits_color)
button_5 = sg.Button("5", size=button_size, button_color=digits_color)
button_6 = sg.Button("6", size=button_size, button_color=digits_color)
button_7 = sg.Button("7", size=button_size, button_color=digits_color)
button_8 = sg.Button("8", size=button_size, button_color=digits_color)
button_9 = sg.Button("9", size=button_size, button_color=digits_color)
button_equals = sg.Button("=", size=button_size, button_color=operator_color)
button_plus = sg.Button("+", size=button_size, button_color=operator_color)
button_divide = sg.Button("/", size=button_size, button_color=operator_color)
button_multiply = sg.Button("*", size=button_size, button_color=operator_color)
button_minus = sg.Button("-", size=button_size, button_color=operator_color)
button_dot = sg.Button(".", size=button_size, button_color=operator_color)
button_clear = sg.Button("C", size=button_size, pad=(20), button_color=clear_button_color)

current_value = ""
calculation = ["", "", ""]

layout = [
    [result_panel, button_clear],
    [button_7, button_8, button_9, button_multiply],
    [button_4, button_5, button_6, button_divide],
    [button_1, button_2, button_3, button_plus],
    [button_0, button_dot, button_minus, button_equals]
]



window = sg.Window('Calculator', layout, font=global_font, background_color="gray", icon='E:\code\Python\personal_projects\py_simple_gui_calculator\project\imgs\gears.ico')


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    

    
    # handle digit inputs
    if str.isdigit(event):
        current_value += event
        
        
    # handle dot input
    if event == '.' and event not in current_value:
        current_value += '.'
    
    # handle C input
    if event == "C":
        current_value = ""
        calculation = ["", "", ""]
    
    # handle operator input
    if event in "/+-*":
        calculation[0] = current_value
        calculation[1] = event
        current_value = ""
        window["input"].update(current_value)
    
    try:
        # handle = input
        if event == "=":
            calculation[2] = current_value
            c = ""
            for i in range(len(calculation)):
                c += calculation[i]
            current_value = str(eval(c))    
            calculation = [current_value, "", ""]
    except ZeroDivisionError:
        sg.popup("You can not divide by zero", title="Error", font=global_font)
    except SyntaxError:
        sg.popup("You made an error, reseting calculator", title="Error", font=global_font)
        current_value = ""
        calculation = ["", "", ""]
        
    # update display
    window["input"].update(current_value)
    
    #print(f"EVENT: {event}\nVALUES: {values}")

window.close()
