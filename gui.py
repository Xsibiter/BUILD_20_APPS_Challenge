import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a To-Do")
input_box = FSG.InputText(tooltip="Type in a To-Do", key="todo")
add_button = FSG.Button("ADD")

window = FSG.Window('My To-Do App',
                    layout=[[label],[input_box,add_button]],
                    font=('Helvetica', 20),
                    )

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case FSG.WINDOW_CLOSED:
            break


window.close()