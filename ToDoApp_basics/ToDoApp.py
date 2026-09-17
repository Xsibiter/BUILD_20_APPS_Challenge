#from functions import get_todos, write_todos
import functions as func
import time

now = time.strftime("%Y-%m-%d %H:%M:%S")
print(now)

while True:
    user_action = input("Type add or show,edit or exit, complete:").strip().lower()

    if  user_action.startswith("add") or user_action.startswith("new"):

        todo = user_action[4:].capitalize().strip() + '\n'
        todos = func.get_todos()
        todos.append(todo)

        func.write_todos(todos)

    elif  user_action.startswith("show") or user_action.startswith("display"):

        todos = func.get_todos()

        #new_todos = [item.strip('\n') for item in todos]

        for index, activity in enumerate(todos, start=1):
            activity = activity.capitalize().strip()
            print(f"{index}) {activity}")

    elif user_action.startswith("edit") or user_action.startswith("change"):
        try:
            todos = func.get_todos()

            num_change = int(user_action[5:].strip())
            new_todo = input("Enter new todo: ")
            todos[num_change - 1] = new_todo + '\n'

            func.write_todos( todos_arg= todos)

        except ValueError:
            print("The command is not valid")
            continue
        except IndexError:
            print("There are less todos")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = func.get_todos()

            num_comp = int(user_action[9:].strip())
            todo_removed = todos[num_comp - 1]
            todos.pop(num_comp - 1)

            func.write_todos( todo_removed)

            print(f'{todo_removed.strip().capitalize()} was removed')
        except IndexError:
            print("There are less todos")
            continue

    elif user_action.startswith("exit") or user_action.startswith("leave"):
        break
    else:
        print("Invalid input")

print('Bye!')