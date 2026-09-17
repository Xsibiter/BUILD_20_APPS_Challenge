from time import strftime
import functions
import FreeSimpleGUI as FSG
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as todos:
        pass

FSG.theme("GreenMono")
clock = FSG.Text("", key="clock")

label = FSG.Text("Type in a To-Do")
input_box = FSG.InputText(tooltip="Type in a To-Do", key="todo")

add_button = FSG.Button(mouseover_colors='green',
                        size=1, tooltip="add_todo",
                        image_source="add_button.png", key="Add")

list_box = FSG.Listbox(values = functions.get_todos(), enable_events=True,
                       tooltip="Here are the To-Do list", key='todos', size=[30,10])

edit_button = FSG.Button("Edit")
complete_button = FSG.Button("Complete")

exit_button = FSG.Button("Exit")

window = FSG.Window('My To-Do App',
                    layout=[[clock], [label],
                            [input_box,add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button],],
                    font=('Times New Roman', 30),
                    )

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=strftime("%d.%m.%y %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":

            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"

            todos.append(new_todo)
            functions.write_todos(todos)

            window["todos"].update(values=todos)

        case "Edit":

            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)

                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos"].update(values=todos)
            except IndexError:
                FSG.popup("Please, select an item first", title="Error", font=("Times New Roman", 30))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()

                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window["todos"].update(values=todos)
            except IndexError:
                FSG.popup("Please, select an item first", title="Error", font=("Times New Roman", 30))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case FSG.WINDOW_CLOSED | None:
            break

window.close()