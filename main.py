from to_do_functions import get_todos
from to_do_functions import write_todos


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