to_do_file = "C:\\Users\\mhmts\\PycharmProjects\\To_Do_List_App\\todo.txt"

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        with open(to_do_file, "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open(to_do_file, "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open(to_do_file, "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open(to_do_file, "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open(to_do_file, "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open(to_do_file, "r") as file:
                todos = file.readlines()
            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open(to_do_file, "w") as file:
                file.writelines(todos)

            print(f"Todo {todo_to_remove} is completed and removed from the list..")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid..")

print("Bye!")