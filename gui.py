import to_do_functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass


sg.theme("DarkTeal10")

time_label = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10, mouseover_colors="gray",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=to_do_functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete", size=10, mouseover_colors="gray",
                       tooltip="Complete Todo", key="Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My App",
                   layout=[[time_label],
                            [label],
                           [input_box,add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Arial", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = to_do_functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            to_do_functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
            sg.popup("New todo has been added in your list.", font=("Arial", 10))

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = to_do_functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                to_do_functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Arial", 10))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = to_do_functions.get_todos()
                todos.remove(todo_to_complete)
                to_do_functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
                sg.popup("Congrats! You've completed a task!", font=("Arial", 10))

            except IndexError:
                sg.popup("Please select an item first", font=("Arial", 10))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()