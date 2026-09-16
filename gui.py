import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a To-Do")
input_box = FSG.InputText(tooltip="Type in a To-Do")
add_button = FSG.Button("ADD")

window = FSG.Window('My To-Do App', layout=[[label],[input_box,add_button]])

window.read()
window.close()