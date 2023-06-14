to_do_file = "C:\\Users\\mhmts\\PycharmProjects\\To_Do_List_App\\todo.txt"

def get_todos(filepath=to_do_file):
    # Reads text file and returns the list of to-do items
    with open(to_do_file, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos, filepath=to_do_file):
    # Writes to-do items list in the text file
    with open(to_do_file, "w") as file:
        file.writelines(todos)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            print(f"Todo {todo_to_remove} is completed and removed from the list..")

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid..")

print("Bye!")