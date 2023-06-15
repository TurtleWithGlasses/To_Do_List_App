import to_do_functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My App",
                   layout=[[label],[input_box,add_button]],
                   font=("Arial", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = to_do_functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            to_do_functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()