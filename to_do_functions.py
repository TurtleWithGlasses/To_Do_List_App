to_do_file = "todo.txt"

def get_todos(filepath=to_do_file):
    # Reads text file and returns the list of to-do items
    with open(to_do_file, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos, filepath=to_do_file):
    # Writes to-do items list in the text file
    with open(to_do_file, "w") as file:
        file.writelines(todos)